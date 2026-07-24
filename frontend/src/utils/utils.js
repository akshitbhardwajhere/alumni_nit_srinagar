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

/**
 * Formats position string to display Arabic or plain Roman numerals as hyphenated Roman numerals
 * for Additional Secretary and Joint Secretary positions (e.g. Additional Secretary - I, Joint Secretary - II).
 */
export function formatPosition(pos) {
	if (!pos) return ""
	return pos
		.replace(/\bAdditional Secretary\s*[-–—]?\s*1\b/gi, "Additional Secretary - I")
		.replace(/\bAdditional Secretary\s*[-–—]?\s*2\b/gi, "Additional Secretary - II")
		.replace(/\bAdditional Secretary\s*[-–—]?\s*3\b/gi, "Additional Secretary - III")
		.replace(/\bJoint Secretary\s*[-–—]?\s*1\b/gi, "Joint Secretary - I")
		.replace(/\bJoint Secretary\s*[-–—]?\s*2\b/gi, "Joint Secretary - II")
		.replace(/\bJoint Secretary\s*[-–—]?\s*3\b/gi, "Joint Secretary - III")
		.replace(/\bAdditional Secretary\s+I\b/gi, "Additional Secretary - I")
		.replace(/\bAdditional Secretary\s+II\b/gi, "Additional Secretary - II")
		.replace(/\bAdditional Secretary\s+III\b/gi, "Additional Secretary - III")
		.replace(/\bJoint Secretary\s+I\b/gi, "Joint Secretary - I")
		.replace(/\bJoint Secretary\s+II\b/gi, "Joint Secretary - II")
		.replace(/\bJoint Secretary\s+III\b/gi, "Joint Secretary - III")
}

export { formatErrorMessage }

