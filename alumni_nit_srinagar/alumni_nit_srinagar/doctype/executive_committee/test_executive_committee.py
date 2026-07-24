# Copyright (c) 2026, Akshit Bhardwaj and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


class TestExecutiveCommittee(IntegrationTestCase):
	"""
	Integration & Unit tests for Executive Committee DocType.
	"""

	def setUp(self):
		"""
		Clean up test executive committee records before each test.
		"""
		frappe.db.delete(
			"Executive Committee",
			{
				"full_name": [
					"in",
					[
						"Test President",
						"Test Vice President",
						"Test Member No Batch",
					],
				]
			},
		)
		frappe.db.commit()

	def tearDown(self):
		"""
		Clean up test executive committee records after each test.
		"""
		frappe.db.delete(
			"Executive Committee",
			{
				"full_name": [
					"in",
					[
						"Test President",
						"Test Vice President",
						"Test Member No Batch",
					],
				]
			},
		)
		frappe.db.commit()

	def test_create_executive_committee_member(self):
		"""Test successful creation of Executive Committee member with batch."""
		doc = frappe.get_doc({
			"doctype": "Executive Committee",
			"title": "Dr.",
			"full_name": "Test President",
			"position": "President",
			"branchdepartment": "Computer Science & Engineering (CSE)",
			"degree": "PhD",
			"batch": "1994",
		}).insert(ignore_permissions=True)

		self.assertTrue(doc.name)
		self.assertEqual(doc.title, "Dr.")
		self.assertEqual(doc.full_name, "Test President")
		self.assertEqual(doc.position, "President")
		self.assertEqual(doc.branchdepartment, "Computer Science & Engineering (CSE)")
		self.assertEqual(doc.degree, "PhD")
		self.assertEqual(doc.batch, "1994")

	def test_executive_committee_member_optional_batch(self):
		"""Test member creation without batch (batch = None/empty)."""
		doc = frappe.get_doc({
			"doctype": "Executive Committee",
			"title": "Er.",
			"full_name": "Test Member No Batch",
			"position": "General Secretary",
			"branchdepartment": "Electrical Engineering",
			"degree": "B.Tech",
			"batch": None,
		}).insert(ignore_permissions=True)

		self.assertTrue(doc.name)
		self.assertIsNone(doc.batch)

	def test_mandatory_executive_committee_fields(self):
		"""Test that missing mandatory Data field full_name raises MandatoryError."""
		doc = frappe.get_doc({
			"doctype": "Executive Committee",
			"title": "Dr.",
			"position": "President",
			"branchdepartment": "Computer Science & Engineering (CSE)",
			"degree": "PhD",
			# Missing mandatory full_name (Data field, reqd: 1)
		})

		self.assertRaises(frappe.MandatoryError, doc.insert, ignore_permissions=True)

	def test_update_and_delete_executive_committee_member(self):
		"""Test updating position and deleting an Executive Committee record."""
		doc = frappe.get_doc({
			"doctype": "Executive Committee",
			"title": "Dr.",
			"full_name": "Test Vice President",
			"position": "Vice President",
			"branchdepartment": "Information Technology (IT)",
			"degree": "M.Tech",
			"batch": "2005",
		}).insert(ignore_permissions=True)

		# Update position
		doc.position = "President"
		doc.save(ignore_permissions=True)

		updated = frappe.get_doc("Executive Committee", doc.name)
		self.assertEqual(updated.position, "President")

		# Delete record
		doc_name = doc.name
		doc.delete(ignore_permissions=True)
		self.assertFalse(frappe.db.exists("Executive Committee", doc_name))
