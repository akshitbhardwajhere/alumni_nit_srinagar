# Copyright (c) 2026, Akshit Bhardwaj and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase
from alumni_nit_srinagar.api import (
	get_alumni_list,
	get_executive_committee,
	get_news_list,
	register_alumni,
)


class TestWhitelistedAPIs(IntegrationTestCase):
	"""
	Unit & Integration tests for whitelisted APIs in alumni_nit_srinagar.api
	"""

	def setUp(self):
		"""
		Clean up test records before each test.
		"""
		frappe.db.delete("Alumni", {"email_address": ["like", "api.test%@nitsri.ac.in"]})
		frappe.db.delete("Executive Committee", {"full_name": "API Committee Test"})
		frappe.db.delete("News", {"title": "API News Test"})
		frappe.db.commit()

	def tearDown(self):
		"""
		Clean up test records after each test.
		"""
		frappe.db.delete("Alumni", {"email_address": ["like", "api.test%@nitsri.ac.in"]})
		frappe.db.delete("Executive Committee", {"full_name": "API Committee Test"})
		frappe.db.delete("News", {"title": "API News Test"})
		frappe.db.commit()

	def test_register_alumni_api(self):
		"""Test registering alumni via register_alumni API sets published=0 and verification=0."""
		payload = {
			"full_name": "API Test Alumni",
			"branchdepartment": "Computer Science & Engineering (CSE)",
			"batchyear": "2022",
			"email_address": "api.test1@nitsri.ac.in",
			"enrollment_number": "2022CSE100",
			"phone_number": "+91-9988776655",
		}

		res = register_alumni(doc=payload)

		self.assertTrue(res.get("name"))
		self.assertEqual(res.get("full_name"), "API Test Alumni")
		self.assertEqual(res.get("enrollment_number"), "2022CSE100")
		self.assertEqual(res.get("published"), 0)
		self.assertEqual(res.get("verification"), 0)

	def test_register_alumni_missing_fields_throws(self):
		"""Test that missing enrollment_number or mandatory fields in register_alumni throws error."""
		payload = {
			"full_name": "Incomplete Payload",
			"branchdepartment": "Information Technology (IT)",
			"email_address": "api.test2@nitsri.ac.in",
			# Missing batchyear and enrollment_number
		}

		with self.assertRaises(frappe.ValidationError):
			register_alumni(doc=payload)

	def test_register_alumni_duplicate_email_throws(self):
		"""Test registering an alumni with an existing email raises exception."""
		payload = {
			"full_name": "First Alumni",
			"branchdepartment": "Civil Engineering",
			"batchyear": "2020",
			"email_address": "api.test3@nitsri.ac.in",
			"enrollment_number": "2020CIV050",
		}
		register_alumni(doc=payload)

		duplicate_payload = {
			"full_name": "Duplicate Alumni",
			"branchdepartment": "Civil Engineering",
			"batchyear": "2020",
			"email_address": "api.test3@nitsri.ac.in",
			"enrollment_number": "2020CIV051",
		}

		with self.assertRaises(frappe.ValidationError):
			register_alumni(doc=duplicate_payload)

	def test_get_alumni_list_api_excludes_private_fields(self):
		"""Test that get_alumni_list API returns only published records and excludes enrollment_number."""
		# Create an unpublished record
		register_alumni(doc={
			"full_name": "API Test Unpublished",
			"branchdepartment": "Physics",
			"batchyear": "2021",
			"email_address": "api.test4@nitsri.ac.in",
			"enrollment_number": "PRIVATE123",
		})

		# Create a published record directly
		pub = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "API Test Published",
			"email_address": "api.test5@nitsri.ac.in",
			"enrollment_number": "PRIVATE456",
			"branchdepartment": "Mathematics",
			"batchyear": "2019",
			"verification": 1,
			"published": 1,
		}).insert(ignore_permissions=True)

		alumni_list = get_alumni_list()
		emails = [a.get("email_address") for a in alumni_list]

		self.assertIn("api.test5@nitsri.ac.in", emails)
		self.assertNotIn("api.test4@nitsri.ac.in", emails)

		# Crucial Security Check: Ensure enrollment_number is NEVER exposed in the public list API
		for item in alumni_list:
			self.assertNotIn("enrollment_number", item)

	def test_get_executive_committee_api(self):
		"""Test get_executive_committee API returns executive members."""
		member = frappe.get_doc({
			"doctype": "Executive Committee",
			"title": "Er.",
			"full_name": "API Committee Test",
			"position": "Joint Secretary 1",
			"branchdepartment": "Mechanical Engineering",
			"degree": "B.Tech",
			"batch": "2010",
		}).insert(ignore_permissions=True)

		committee_list = get_executive_committee()
		names = [m.get("full_name") for m in committee_list]

		self.assertIn("API Committee Test", names)

	def test_get_news_list_api(self):
		"""Test get_news_list API returns published news."""
		news = frappe.get_doc({
			"doctype": "News",
			"title": "API News Test",
			"category": "Event",
			"published_date": "2026-07-24",
			"summary": "API news test summary.",
			"published": 1,
		}).insert(ignore_permissions=True)

		news_list = get_news_list()
		titles = [n.get("title") for n in news_list]

		self.assertIn("API News Test", titles)
