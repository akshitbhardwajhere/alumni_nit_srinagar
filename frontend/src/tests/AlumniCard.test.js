import { describe, expect, it } from "vitest"
import { getInitials } from "../utils"

describe("Alumni Directory Rules Unit Tests", () => {
	const isFeatured = (alumni) => {
		return Boolean(alumni && (alumni.featured === 1 || alumni.featured === true))
	}

	const formatDesignationAndCompany = (alumni) => {
		if (!alumni.designation && !alumni.company_organization) return ""
		if (alumni.designation && alumni.company_organization) {
			return `${alumni.designation} at ${alumni.company_organization}`
		}
		return alumni.designation || alumni.company_organization
	}

	it("evaluates isFeatured correctly for featured alumni", () => {
		expect(isFeatured({ featured: 1 })).toBe(true)
		expect(isFeatured({ featured: true })).toBe(true)
		expect(isFeatured({ featured: 0 })).toBe(false)
		expect(isFeatured({ featured: false })).toBe(false)
		expect(isFeatured({})).toBe(false)
	})

	it("formats designation and company text cleanly", () => {
		expect(
			formatDesignationAndCompany({
				designation: "Senior Lead Architect",
				company_organization: "Google",
			}),
		).toBe("Senior Lead Architect at Google")

		expect(
			formatDesignationAndCompany({
				designation: "Software Engineer",
				company_organization: "",
			}),
		).toBe("Software Engineer")

		expect(
			formatDesignationAndCompany({
				designation: "",
				company_organization: "ISRO",
			}),
		).toBe("ISRO")
	})

	it("computes initials correctly for alumni cards without images", () => {
		expect(getInitials("Rahul Sharma")).toBe("RS")
		expect(getInitials("Er. Priya Verma")).toBe("PV")
		expect(getInitials("Amit Patel")).toBe("AP")
	})
})
