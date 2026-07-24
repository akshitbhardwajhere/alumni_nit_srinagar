import os
from typing import Any, Dict, List, Optional, Union
import frappe
from frappe.utils import validate_email_address

ALLOWED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}


@frappe.whitelist(allow_guest=True)
def register_alumni(doc: Optional[Union[Dict[str, Any], str]] = None) -> Dict[str, Any]:
	"""
	Whitelisted public endpoint allowing Guest users to submit Alumni registration.
	Enforces backend validation, input sanitization, and sets initial verification state.
	"""
	if doc is None:
		doc = dict(frappe.form_dict)

	if isinstance(doc, str):
		doc = frappe.parse_json(doc)

	if not isinstance(doc, dict):
		frappe.throw("Invalid registration payload provided.")

	full_name = str(doc.get("full_name") or "").strip()
	branchdepartment = str(doc.get("branchdepartment") or "").strip()
	batchyear = str(doc.get("batchyear") or "").strip()
	email_address = str(doc.get("email_address") or "").strip()
	enrollment_number = str(doc.get("enrollment_number") or "").strip()
	phone_number = str(doc.get("phone_number") or "").strip() if doc.get("phone_number") else None
	image = str(doc.get("image") or "").strip() if doc.get("image") else None

	# Validate mandatory fields
	if not full_name or not branchdepartment or not batchyear or not email_address or not enrollment_number:
		frappe.throw("Missing required fields for Alumni registration.")

	# Validate email address format
	validate_email_address(email_address, throw=True)

	# Check for duplicate email address
	if frappe.db.exists("Alumni", {"email_address": email_address}):
		frappe.throw(f"An alumni record with email address already exists.")

	# Create new Alumni record (unverified and unpublished by default)
	new_doc = frappe.get_doc({
		"doctype": "Alumni",
		"full_name": full_name,
		"branchdepartment": branchdepartment,
		"batchyear": batchyear,
		"email_address": email_address,
		"enrollment_number": enrollment_number,
		"phone_number": phone_number,
		"image": image,
		"verification": 0,
		"published": 0,
	})

	new_doc.insert(ignore_permissions=True)
	frappe.db.commit()

	return new_doc.as_dict()


@frappe.whitelist(allow_guest=True)
def upload_alumni_image() -> Dict[str, str]:
	"""
	Whitelisted endpoint for Guest image uploads during Alumni registration.
	Enforces strict extension and security validation to prevent arbitrary file uploads.
	"""
	if "file" not in frappe.request.files:
		frappe.throw("No file attached in request.")

	file_obj = frappe.request.files["file"]
	filename = file_obj.filename or "upload.jpg"
	_, ext = os.path.splitext(filename.lower())

	if ext not in ALLOWED_IMAGE_EXTENSIONS:
		frappe.throw("Only image files (PNG, JPEG, JPG, WEBP) are allowed for upload.")

	file_doc = frappe.get_doc({
		"doctype": "File",
		"file_name": filename,
		"is_private": 0,
		"content": file_obj.read(),
	})
	file_doc.insert(ignore_permissions=True)
	frappe.db.commit()

	return {"file_url": file_doc.file_url}


@frappe.whitelist(allow_guest=True)
def get_executive_committee() -> List[Dict[str, Any]]:
	"""
	Public whitelisted endpoint to fetch Executive Committee members.
	"""
	return frappe.get_all(
		"Executive Committee",
		fields=[
			"name",
			"title",
			"full_name",
			"position",
			"branchdepartment",
			"degree",
			"batch",
			"photo",
		],
		order_by="creation asc",
		limit_page_length=200,
	)


@frappe.whitelist(allow_guest=True)
def get_alumni_list() -> List[Dict[str, Any]]:
	"""
	Public whitelisted endpoint to fetch published Alumni directory.
	Strictly excludes private fields like enrollment_number.
	"""
	return frappe.get_all(
		"Alumni",
		fields=[
			"name",
			"full_name",
			"branchdepartment",
			"batchyear",
			"email_address",
			"phone_number",
			"image",
			"designation",
			"company_organization",
			"published",
			"featured",
		],
		filters={"published": 1},
		order_by="creation desc",
		limit_page_length=500,
	)


@frappe.whitelist(allow_guest=True)
def get_news_list() -> List[Dict[str, Any]]:
	"""
	Public whitelisted endpoint to fetch published News items.
	"""
	return frappe.get_all(
		"News",
		fields=[
			"name",
			"title",
			"category",
			"published_date",
			"is_hot_news",
			"published",
			"cover_image",
			"summary",
			"content",
		],
		filters={"published": 1},
		order_by="published_date desc",
		limit_page_length=500,
	)
