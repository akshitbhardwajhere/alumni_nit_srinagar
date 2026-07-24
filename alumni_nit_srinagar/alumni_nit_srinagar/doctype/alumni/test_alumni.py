# Copyright (c) 2026, Akshit Bhardwaj and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


class TestAlumni(IntegrationTestCase):
	"""
	Integration & Unit tests for Alumni DocType.
	"""

	def setUp(self):
		"""
		Clean up test alumni records before each test.
		"""
		frappe.db.delete(
			"Alumni",
			{
				"email_address": [
					"in",
					[
						"test.alumni@nitsri.ac.in",
						"duplicate.alumni@nitsri.ac.in",
						"featured.alumni@nitsri.ac.in",
						"unpublished.alumni@nitsri.ac.in",
						"verify.alumni@nitsri.ac.in",
					],
				]
			},
		)
		frappe.db.commit()

	def tearDown(self):
		"""
		Clean up test alumni records after each test.
		"""
		frappe.db.delete(
			"Alumni",
			{
				"email_address": [
					"in",
					[
						"test.alumni@nitsri.ac.in",
						"duplicate.alumni@nitsri.ac.in",
						"featured.alumni@nitsri.ac.in",
						"unpublished.alumni@nitsri.ac.in",
						"verify.alumni@nitsri.ac.in",
					],
				]
			},
		)
		frappe.db.commit()

	def test_create_alumni(self):
		"""Test successful creation of a valid Alumni document."""
		doc = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Test Engineer",
			"email_address": "test.alumni@nitsri.ac.in",
			"enrollment_number": "2020CSE045",
			"branchdepartment": "Computer Science & Engineering (CSE)",
			"batchyear": "2020",
			"phone_number": "+91-9876543210",
			"designation": "Software Engineer",
			"company_organization": "Tech Corp",
			"verification": 0,
			"published": 0,
			"featured": 0,
		}).insert(ignore_permissions=True)

		self.assertTrue(doc.name)
		self.assertEqual(doc.full_name, "Test Engineer")
		self.assertEqual(doc.email_address, "test.alumni@nitsri.ac.in")
		self.assertEqual(doc.enrollment_number, "2020CSE045")
		self.assertEqual(doc.branchdepartment, "Computer Science & Engineering (CSE)")
		self.assertEqual(doc.batchyear, "2020")
		self.assertEqual(doc.verification, 0)
		self.assertEqual(doc.published, 0)

	def test_admin_verification_auto_publishes(self):
		"""Test that marking verification = 1 automatically sets published = 1."""
		doc = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Verification Test Alumni",
			"email_address": "verify.alumni@nitsri.ac.in",
			"enrollment_number": "2021ECE012",
			"branchdepartment": "Electronics & Communication Engineering (ECE)",
			"batchyear": "2021",
			"verification": 0,
			"published": 0,
		}).insert(ignore_permissions=True)

		self.assertEqual(doc.verification, 0)
		self.assertEqual(doc.published, 0)

		# Admin verifies the record
		doc.verification = 1
		doc.save(ignore_permissions=True)

		# Check that published is automatically set to 1 by validate()
		updated_doc = frappe.get_doc("Alumni", doc.name)
		self.assertEqual(updated_doc.verification, 1)
		self.assertEqual(updated_doc.published, 1)

	def test_duplicate_email_prevention(self):
		"""Test that creating an alumni with a duplicate email address raises an error."""
		doc1 = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Original Alumni",
			"email_address": "duplicate.alumni@nitsri.ac.in",
			"enrollment_number": "2018IT001",
			"branchdepartment": "Information Technology (IT)",
			"batchyear": "2018",
			"verification": 1,
			"published": 1,
		}).insert(ignore_permissions=True)

		self.assertTrue(doc1.name)

		# Attempting to create a second document with the same unique email should fail
		doc2 = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Duplicate Alumni",
			"email_address": "duplicate.alumni@nitsri.ac.in",
			"enrollment_number": "2019CIV002",
			"branchdepartment": "Civil Engineering",
			"batchyear": "2019",
			"verification": 1,
			"published": 1,
		})

		self.assertRaises(
			(frappe.UniqueValidationError, frappe.DuplicateEntryError),
			doc2.insert,
			ignore_permissions=True,
		)

	def test_mandatory_fields_validation(self):
		"""Test that missing mandatory fields raise MandatoryError."""
		doc = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Incomplete Alumni",
			# Missing email_address, enrollment_number, branchdepartment, batchyear
		})

		self.assertRaises(frappe.MandatoryError, doc.insert, ignore_permissions=True)

	def test_published_and_featured_flags(self):
		"""Test querying published and featured alumni records."""
		doc_pub = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Featured Alumni",
			"email_address": "featured.alumni@nitsri.ac.in",
			"enrollment_number": "2015ELE099",
			"branchdepartment": "Electrical Engineering",
			"batchyear": "2015",
			"verification": 1,
			"published": 1,
			"featured": 1,
		}).insert(ignore_permissions=True)

		doc_unpub = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Unpublished Alumni",
			"email_address": "unpublished.alumni@nitsri.ac.in",
			"enrollment_number": "2021MEC033",
			"branchdepartment": "Mechanical Engineering",
			"batchyear": "2021",
			"verification": 0,
			"published": 0,
			"featured": 0,
		}).insert(ignore_permissions=True)

		published_alumni = frappe.get_all(
			"Alumni", filters={"published": 1}, fields=["email_address"]
		)
		published_emails = [a.email_address for a in published_alumni]

		self.assertIn("featured.alumni@nitsri.ac.in", published_emails)
		self.assertNotIn("unpublished.alumni@nitsri.ac.in", published_emails)

		featured_alumni = frappe.get_all(
			"Alumni", filters={"featured": 1}, fields=["email_address"]
		)
		featured_emails = [a.email_address for a in featured_alumni]
		self.assertIn("featured.alumni@nitsri.ac.in", featured_emails)

	def test_update_and_delete_alumni(self):
		"""Test updating and deleting an Alumni document."""
		doc = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Update Test Alumni",
			"email_address": "test.alumni@nitsri.ac.in",
			"enrollment_number": "2017PHY007",
			"branchdepartment": "Physics",
			"batchyear": "2017",
			"verification": 1,
			"published": 1,
		}).insert(ignore_permissions=True)

		# Update fields
		doc.designation = "Lead Scientist"
		doc.company_organization = "ISRO"
		doc.save(ignore_permissions=True)

		updated_doc = frappe.get_doc("Alumni", doc.name)
		self.assertEqual(updated_doc.designation, "Lead Scientist")
		self.assertEqual(updated_doc.company_organization, "ISRO")

		# Delete document
		doc_name = doc.name
		doc.delete(ignore_permissions=True)
		self.assertFalse(frappe.db.exists("Alumni", doc_name))
