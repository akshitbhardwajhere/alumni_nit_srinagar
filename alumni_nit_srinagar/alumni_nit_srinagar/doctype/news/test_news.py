# Copyright (c) 2026, Akshit Bhardwaj and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import today


class TestNews(IntegrationTestCase):
	"""
	Integration & Unit tests for News DocType.
	"""

	def setUp(self):
		"""
		Clean up test news and alumni records before each test.
		"""
		frappe.db.delete("News", {"title": ["like", "Test News%"]})
		frappe.db.delete("Alumni", {"email_address": "news.author@nitsri.ac.in"})
		frappe.db.commit()

	def tearDown(self):
		"""
		Clean up test news and alumni records after each test.
		"""
		frappe.db.delete("News", {"title": ["like", "Test News%"]})
		frappe.db.delete("Alumni", {"email_address": "news.author@nitsri.ac.in"})
		frappe.db.commit()

	def test_create_news(self):
		"""Test successful creation of a News article document."""
		doc = frappe.get_doc({
			"doctype": "News",
			"title": "Test News Story Title",
			"category": "Spotlight",
			"published_date": today(),
			"is_hot_news": 1,
			"published": 1,
			"summary": "This is a test news summary highlighting an alumnus achievement.",
			"content": "<p>Full content of the test news story goes here.</p>"
		}).insert(ignore_permissions=True)

		self.assertTrue(doc.name)
		self.assertEqual(doc.title, "Test News Story Title")
		self.assertEqual(doc.category, "Spotlight")
		self.assertEqual(doc.is_hot_news, 1)
		self.assertEqual(doc.published, 1)

	def test_mandatory_news_fields(self):
		"""Test that title is mandatory for News document."""
		doc = frappe.get_doc({
			"doctype": "News",
			"category": "Event",
			"published": 1
			# Missing title
		})

		self.assertRaises(frappe.MandatoryError, doc.insert, ignore_permissions=True)

	def test_is_hot_news_query(self):
		"""Test querying Top 3 Hot News for homepage spotlight."""
		# Create hot news item
		hot_news = frappe.get_doc({
			"doctype": "News",
			"title": "Test News Hot Item",
			"category": "Achievement",
			"published_date": today(),
			"is_hot_news": 1,
			"published": 1,
			"summary": "Hot news summary item."
		}).insert(ignore_permissions=True)

		# Create regular news item
		regular_news = frappe.get_doc({
			"doctype": "News",
			"title": "Test News Regular Item",
			"category": "News",
			"published_date": today(),
			"is_hot_news": 0,
			"published": 1,
			"summary": "Regular news summary item."
		}).insert(ignore_permissions=True)

		hot_items = frappe.get_all(
			"News",
			filters={"published": 1, "is_hot_news": 1},
			fields=["title"]
		)
		hot_titles = [n.title for n in hot_items]

		self.assertIn("Test News Hot Item", hot_titles)
		self.assertNotIn("Test News Regular Item", hot_titles)

	def test_author_alumni_link(self):
		"""Test linking a News article to an Alumni document."""
		alumni = frappe.get_doc({
			"doctype": "Alumni",
			"full_name": "Author Alumnus",
			"email_address": "news.author@nitsri.ac.in",
			"branchdepartment": "Computer Science & Engineering (CSE)",
			"batchyear": "2016",
			"published": 1
		}).insert(ignore_permissions=True)

		news = frappe.get_doc({
			"doctype": "News",
			"title": "Test News Linked to Author",
			"category": "Spotlight",
			"published_date": today(),
			"published": 1,
			"author_alumni": alumni.name,
			"summary": "Spotlight story about author alumnus."
		}).insert(ignore_permissions=True)

		self.assertEqual(news.author_alumni, alumni.name)

	def test_update_and_delete_news(self):
		"""Test updating and deleting a News article document."""
		doc = frappe.get_doc({
			"doctype": "News",
			"title": "Test News To Be Deleted",
			"category": "Event",
			"summary": "Test event summary description.",
			"published": 1
		}).insert(ignore_permissions=True)

		doc.title = "Test News Title Updated"
		doc.save(ignore_permissions=True)

		updated = frappe.get_doc("News", doc.name)
		self.assertEqual(updated.title, "Test News Title Updated")

		doc_name = doc.name
		doc.delete(ignore_permissions=True)
		self.assertFalse(frappe.db.exists("News", doc_name))
