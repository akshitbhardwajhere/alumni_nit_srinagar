/**
 * Utility to parse raw Frappe server errors, backend exceptions, and API error objects
 * into clean, user-friendly natural language error messages.
 */
export function formatErrorMessage(
	err,
	defaultMsg = "An unexpected error occurred. Please try again.",
) {
	if (!err) return defaultMsg

	// 1. If err is a direct string
	if (typeof err === "string") {
		return cleanErrorMessage(err, defaultMsg)
	}

	// 2. Check for Frappe _server_messages (JSON string array from backend)
	if (err._server_messages) {
		try {
			const messages =
				typeof err._server_messages === "string"
					? JSON.parse(err._server_messages)
					: err._server_messages

			if (Array.isArray(messages) && messages.length > 0) {
				const parsed =
					typeof messages[0] === "string"
						? JSON.parse(messages[0])
						: messages[0]
				const msg = parsed?.message || parsed?.text || parsed
				if (msg) return cleanErrorMessage(msg, defaultMsg)
			}
		} catch (e) {
			// Ignore JSON parse error and fallback
		}
	}

	// 3. Check for err.messages array
	if (Array.isArray(err.messages) && err.messages.length > 0) {
		return cleanErrorMessage(err.messages[0], defaultMsg)
	}

	// 4. Check for err.message, err._error_message, err.exception, or err.exc
	const rawMsg = err.message || err._error_message || err.exception || err.exc
	if (rawMsg) {
		return cleanErrorMessage(rawMsg, defaultMsg)
	}

	return defaultMsg
}

function cleanErrorMessage(raw, defaultMsg) {
	if (typeof raw !== "string") return defaultMsg

	let str = raw.trim()

	// Remove JSON string wrappers if present
	if (str.startsWith("{") && str.endsWith("}")) {
		try {
			const obj = JSON.parse(str)
			str = obj.message || obj.text || str
		} catch (e) {
			// ignore
		}
	}

	// Strip raw API endpoint prefix (e.g. "/api/method/frappe.client.insert ")
	str = str.replace(/^\/api\/method\/[^\s]+\s*/i, "")

	// Map known Frappe Exception Types & Errors to friendly natural language messages
	if (
		str.includes("InvalidPhoneNumberError") ||
		str.includes("Invalid Phone Number") ||
		str.includes("Phone")
	) {
		return "Invalid phone number provided. Please enter a valid phone number."
	}

	if (
		str.includes("DuplicateEntryError") ||
		str.includes("already exists") ||
		str.includes("Duplicate")
	) {
		return "An alumni profile with this email address is already registered."
	}

	if (str.includes("MandatoryError") || str.includes("ValueMissing")) {
		return "Please fill out all required fields marked with an asterisk (*)."
	}

	if (str.includes("PermissionError") || str.includes("DoesNotExistError")) {
		return "You do not have permission or the requested record was not found."
	}

	// Remove Tracebacks / Python Exception class prefixes
	str = str.replace(/^[a-zA-Z0-9_.]*Error:\s*/i, "")
	str = str.replace(/^frappe\.exceptions\.[a-zA-Z0-9_]+:\s*/i, "")

	// Strip HTML tags if any (e.g. <script> or <b>)
	str = str.replace(/<\/?[^>]+(>|$)/g, "").trim()

	if (!str) return defaultMsg

	// Capitalize first letter and ensure ending period
	str = str.charAt(0).toUpperCase() + str.slice(1)
	if (!/[.!?]$/.test(str)) {
		str += "."
	}

	return str
}
