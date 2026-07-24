from typing import Any, Dict, List, Optional, Union
import frappe


@frappe.whitelist(allow_guest=True)
def register_alumni(doc: Optional[Union[Dict[str, Any], str]] = None) -> Dict[str, Any]:
	"""
	Whitelisted endpoint allowing Guest users to submit Alumni registration.
	"""
	if doc is None:
		doc = dict(frappe.form_dict)

	if isinstance(doc, str):
		doc = frappe.parse_json(doc)

	if not isinstance(doc, dict):
		frappe.throw("Invalid registration payload provided.")

	full_name = doc.get("full_name")
	branchdepartment = doc.get("branchdepartment")
	batchyear = doc.get("batchyear")
	email_address = doc.get("email_address")
	enrollment_number = doc.get("enrollment_number")

	if not full_name or not branchdepartment or not batchyear or not email_address or not enrollment_number:
		frappe.throw("Missing required fields for Alumni registration.")

	email_clean = str(email_address).strip()
	if frappe.db.exists("Alumni", {"email_address": email_clean}):
		frappe.throw(f"An alumni record with email address '{email_clean}' already exists.")

	new_doc = frappe.get_doc({
		"doctype": "Alumni",
		"full_name": str(full_name).strip(),
		"branchdepartment": branchdepartment,
		"batchyear": str(batchyear).strip(),
		"email_address": email_clean,
		"enrollment_number": str(enrollment_number).strip(),
		"phone_number": doc.get("phone_number"),
		"image": doc.get("image"),
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
	"""
	if "file" not in frappe.request.files:
		frappe.throw("No file attached in request.")

	file_obj = frappe.request.files["file"]
	file_doc = frappe.get_doc({
		"doctype": "File",
		"file_name": file_obj.filename,
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
