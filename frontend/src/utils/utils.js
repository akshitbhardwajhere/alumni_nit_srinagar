import { formatErrorMessage } from "./errorMessage"

/**
 * Generates clean 2-letter initials for avatar fallbacks.
 * Handles titles/prefixes such as Er., Dr., Prof., Mr., Ms.
 */
export function getInitials(name) {
	if (!name) return "AN"
	const cleanName = name.replace(/^(Er\.|Dr\.|Prof\.|Mr\.|Ms\.)\s+/i, "")
	const parts = cleanName.trim().split(" ")
	if (parts.length >= 2 && parts[0] && parts[parts.length - 1]) {
		return `${parts[0][0]}${parts[parts.length - 1][0]}`.toUpperCase()
	}
	return name.substring(0, 2).toUpperCase()
}

/**
 * Simple email address format validator
 */
export function isValidEmail(email) {
	if (!email) return false
	return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim())
}

/**
 * Cleans phone number string to keep only digits
 */
export function cleanPhoneNumber(phone) {
	if (!phone) return ""
	return phone.trim().replace(/\D/g, "")
}

export { formatErrorMessage }
