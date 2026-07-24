import { describe, expect, it } from "vitest"
import { getInitials } from "../utils"

describe("Executive Committee Member Rules Unit Tests", () => {
	// Helper logic mimicking ExecutiveCommitteeCard computed properties
	const getFullNameWithTitle = (member) => {
		const title = member.title ? `${member.title.trim()} ` : ""
		const name = member.full_name || ""
		return `${title}${name}`.trim()
	}

	const hasBatch = (member) => {
		return Boolean(member.batch && String(member.batch).trim().length > 0)
	}

	it("formats full name with title correctly", () => {
		expect(
			getFullNameWithTitle({ title: "Dr.", full_name: "Malay Kumar" }),
		).toBe("Dr. Malay Kumar")
		expect(
			getFullNameWithTitle({ title: "", full_name: "Irfan Ahmad" }),
		).toBe("Irfan Ahmad")
		expect(getFullNameWithTitle({ full_name: "Sunil Dutt" })).toBe(
			"Sunil Dutt",
		)
	})

	it("evaluates hasBatch to true ONLY when member has non-empty batch string", () => {
		expect(hasBatch({ batch: "1994" })).toBe(true)
		expect(hasBatch({ batch: " 2005 " })).toBe(true)
		expect(hasBatch({ batch: "" })).toBe(false)
		expect(hasBatch({ batch: "   " })).toBe(false)
		expect(hasBatch({ batch: null })).toBe(false)
		expect(hasBatch({})).toBe(false)
	})

	it("computes initials fallback for executive committee members without photos", () => {
		expect(getInitials("Malay Kumar")).toBe("MK")
		expect(getInitials("Dr. Irfan Ahmad")).toBe("IA")
		expect(getInitials("Prof. Sunil Dutt")).toBe("SD")
	})
})
