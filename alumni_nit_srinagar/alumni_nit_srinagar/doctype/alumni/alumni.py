# Copyright (c) 2026, Akshit Bhardwaj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Alumni(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		batchyear: DF.Data
		branchdepartment: DF.Literal["Computer Science & Engineering (CSE)", "Information Technology (IT)", "Electrical Engineering", "Electronics & Communication Engineering (ECE)", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Metallurgical & Materials Engineering", "Mathematics", "Physics", "Chemistry", "Humanities, Social Sciences & Management (HSS&M)"]
		company_organization: DF.Data | None
		designation: DF.Data | None
		email_address: DF.Data
		enrollment_number: DF.Data
		featured: DF.Check
		full_name: DF.Data
		image: DF.AttachImage | None
		phone_number: DF.Phone | None
		published: DF.Check
		verification: DF.Check
	# end: auto-generated types

	_DOCTYPE_NAME = "Alumni"

	def validate(self):
		if self.verification:
			self.published = 1
