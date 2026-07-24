import { describe, expect, it } from "vitest"
import {
	cleanPhoneNumber,
	formatErrorMessage,
	getInitials,
	isValidEmail,
} from "../utils"

describe("Utility Functions Unit Tests", () => {
	describe("getInitials", () => {
		it("should extract correct 2-letter initials for normal full names", () => {
			expect(getInitials("Akshit Bhardwaj")).toBe("AB")
			expect(getInitials("John Doe")).toBe("JD")
			expect(getInitials("Rahul Kumar Sharma")).toBe("RS")
		})

		it("should strip academic and professional titles before computing initials", () => {
			expect(getInitials("Dr. Jane Doe")).toBe("JD")
			expect(getInitials("Er. Ramesh Kumar")).toBe("RK")
			expect(getInitials("Prof. Sunil Dutt")).toBe("SD")
			expect(getInitials("Mr. Alex Smith")).toBe("AS")
		})

		it("should handle single name or fallback gracefully", () => {
			expect(getInitials("Srinagar")).toBe("SR")
			expect(getInitials("")).toBe("AN")
			expect(getInitials(null)).toBe("AN")
		})
	})

	describe("isValidEmail", () => {
		it("should validate correct email addresses", () => {
			expect(isValidEmail("alumni@nitsri.ac.in")).toBe(true)
			expect(isValidEmail("test.user@domain.com")).toBe(true)
		})

		it("should reject invalid email addresses", () => {
			expect(isValidEmail("plainaddress")).toBe(false)
			expect(isValidEmail("@missingusername.com")).toBe(false)
			expect(isValidEmail("missingdomain@")).toBe(false)
			expect(isValidEmail("")).toBe(false)
			expect(isValidEmail(null)).toBe(false)
		})
	})

	describe("cleanPhoneNumber", () => {
		it("should strip non-digit characters from phone numbers", () => {
			expect(cleanPhoneNumber("+91-9876543210")).toBe("919876543210")
			expect(cleanPhoneNumber("(0194) 242-2032")).toBe("01942422032")
			expect(cleanPhoneNumber("987 654 3210")).toBe("9876543210")
		})

		it("should return empty string for null or empty inputs", () => {
			expect(cleanPhoneNumber("")).toBe("")
			expect(cleanPhoneNumber(null)).toBe("")
		})
	})

	describe("formatErrorMessage", () => {
		it("should extract string error messages and capitalize with ending period", () => {
			expect(formatErrorMessage("direct error message", "Default msg")).toBe(
				"Direct error message.",
			)
		})

		it("should extract error from object structure", () => {
			const errObj = { message: "Server connection failed" }
			expect(formatErrorMessage(errObj, "Fallback")).toBe(
				"Server connection failed.",
			)
		})

		it("should return friendly text for duplicate email errors", () => {
			const dupErr = "DuplicateEntryError: Alumni duplicate.alumni@nitsri.ac.in already exists"
			expect(formatErrorMessage(dupErr, "Fallback")).toBe(
				"An alumni profile with this email address is already registered.",
			)
		})

		it("should return fallback message for empty error", () => {
			expect(formatErrorMessage(null, "Fallback message")).toBe(
				"Fallback message",
			)
		})
	})
})
