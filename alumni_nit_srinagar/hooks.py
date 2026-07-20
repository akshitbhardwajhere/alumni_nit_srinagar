app_name = "alumni_nit_srinagar"
app_title = "Alumni NIT Srinagar"
app_publisher = "Akshit Bhardwaj"
app_description = "The Official Alumni Website of NIT Srinagar connects alumni with the institute and one another, fostering lifelong relationships through networking, events, mentorship, and opportunities to give back to the NIT Srinagar community."
app_email = "akshitbhardwaj257448@gmail.com"
app_license = "agpl-3.0"

# Send non-GET requests for this app's endpoints as native `application/json`
# bodies instead of form-encoded, per-key JSON-stringified values.
use_json_request_body = True

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "alumni_nit_srinagar",
# 		"logo": "/assets/alumni_nit_srinagar/logo.png",
# 		"title": "Alumni NIT Srinagar",
# 		"route": "/alumni_nit_srinagar",
# 		"has_permission": "alumni_nit_srinagar.api.permission.has_app_permission",
# 	}
# ]

# Companion apps that extend a host app (instead of taking their own apps-screen icon) can pin
# their workspaces into the host app's workspace dock (rail) with this hook.
# add_app_to_rail = [
# 	{
# 		"app": "erpnext",
# 		"workspace": "My Workspace",
# 		"has_permission": "alumni_nit_srinagar.api.permission.has_app_permission",
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/alumni_nit_srinagar/css/alumni_nit_srinagar.css"
# app_include_js = "/assets/alumni_nit_srinagar/js/alumni_nit_srinagar.js"

# include js, css files in header of web template
# web_include_css = "/assets/alumni_nit_srinagar/css/alumni_nit_srinagar.css"
# web_include_js = "/assets/alumni_nit_srinagar/js/alumni_nit_srinagar.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "alumni_nit_srinagar/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "alumni_nit_srinagar/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "alumni_nit_srinagar.utils.jinja_methods",
# 	"filters": "alumni_nit_srinagar.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "alumni_nit_srinagar.install.before_install"
# after_install = "alumni_nit_srinagar.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "alumni_nit_srinagar.uninstall.before_uninstall"
# after_uninstall = "alumni_nit_srinagar.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "alumni_nit_srinagar.utils.before_app_install"
# after_app_install = "alumni_nit_srinagar.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "alumni_nit_srinagar.utils.before_app_uninstall"
# after_app_uninstall = "alumni_nit_srinagar.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "alumni_nit_srinagar.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alumni_nit_srinagar.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"alumni_nit_srinagar.tasks.all"
# 	],
# 	"daily": [
# 		"alumni_nit_srinagar.tasks.daily"
# 	],
# 	"hourly": [
# 		"alumni_nit_srinagar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"alumni_nit_srinagar.tasks.weekly"
# 	],
# 	"monthly": [
# 		"alumni_nit_srinagar.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "alumni_nit_srinagar.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "alumni_nit_srinagar.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "alumni_nit_srinagar.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "alumni_nit_srinagar.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["alumni_nit_srinagar.utils.before_request"]
# after_request = ["alumni_nit_srinagar.utils.after_request"]

# Job Events
# ----------
# before_job = ["alumni_nit_srinagar.utils.before_job"]
# after_job = ["alumni_nit_srinagar.utils.after_job"]

# after_file_upload = ["alumni_nit_srinagar.utils.after_file_upload"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"alumni_nit_srinagar.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

