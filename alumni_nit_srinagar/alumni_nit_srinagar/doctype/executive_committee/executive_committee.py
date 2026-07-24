# Copyright (c) 2026, Akshit Bhardwaj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExecutiveCommittee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		batch: DF.Data | None
		branchdepartment: DF.Literal["Computer Science & Engineering (CSE)", "Information Technology (IT)", "Electrical Engineering", "Electronics & Communication Engineering (ECE)", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Metallurgical & Materials Engineering", "Mathematics", "Physics", "Chemistry", "Humanities, Social Sciences & Management (HSS&M)"]
		degree: DF.Literal["B.Tech", "M.Tech", "PhD"]
		full_name: DF.Data
		photo: DF.AttachImage | None
		position: DF.Literal["President", "Vice President", "General Secretary", "Secretary", "Additional Secretary - I", "Additional Secretary - II", "Additional Secretary - III", "Joint Secretary - I", "Joint Secretary - II", "Joint Secretary - III", "Treasurer/Cashier"]
		title: DF.Literal["Er.", "Dr."]
	# end: auto-generated types

	_DOCTYPE_NAME = "Executive Committee"
