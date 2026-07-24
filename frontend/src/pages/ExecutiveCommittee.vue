<template>
	<div class="min-h-screen bg-gray-50 font-sans text-gray-900 flex flex-col">
		<!-- Hero Banner -->
		<section class="bg-[#17345F] text-white relative overflow-hidden py-12 lg:py-16">
			<div class="absolute inset-0 opacity-10 bg-[radial-gradient(#D5A33D_1px,transparent_1px)] [background-size:16px_16px]"></div>
			<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
				<div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
					<div>
						<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D5A33D]/20 border border-[#D5A33D]/40 text-[#F2B633] text-xs sm:text-sm font-medium tracking-wide mb-3">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
							</svg>
							Alumni Leadership
						</div>
						<h1 class="text-3xl sm:text-4xl lg:text-5xl font-exo-2 font-bold tracking-tight text-white">
							Executive Committee
						</h1>
						<p class="mt-3 text-base sm:text-lg text-gray-200 max-w-2xl leading-relaxed">
							Meet the dedicated office bearers and committee members governing the National Institute of Technology Srinagar Alumni Association.
						</p>
					</div>
				</div>
			</div>
		</section>

		<!-- Main Content Section -->
		<section class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-grow">
			<!-- Breadcrumbs -->
			<div class="mb-6">
				<Breadcrumbs
					:items="[
						{ label: 'Home', route: '/' },
						{ label: 'Executive Committee' }
					]"
				/>
			</div>

			<!-- Search & Control Bar -->
			<div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
				<div>
					<h2 class="text-xl font-bold text-gray-900 font-exo-2">
						Committee Members ({{ filteredMembers.length }})
					</h2>
					<p class="text-xs text-gray-500 mt-0.5">Office bearers guiding the global NIT Srinagar alumni network</p>
				</div>

				<!-- Search Input -->
				<div class="w-full md:w-80">
					<TextInput
						v-model="searchQuery"
						placeholder="Search by name, position, branch..."
						size="md"
						variant="outline"
						class="w-full"
					>
						<template #prefix>
							<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
							</svg>
						</template>
					</TextInput>
				</div>
			</div>

			<!-- Loading Skeleton -->
			<div v-if="committeeResource.loading" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
				<div v-for="i in 8" :key="i" class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm animate-pulse flex flex-col items-center text-center space-y-4">
					<div class="h-4 bg-gray-200 rounded w-1/2"></div>
					<div class="w-24 h-24 rounded-full bg-gray-200"></div>
					<div class="h-5 bg-gray-200 rounded w-3/4"></div>
					<div class="h-3 bg-gray-200 rounded w-2/3"></div>
					<div class="h-3 bg-gray-200 rounded w-1/3"></div>
				</div>
			</div>

			<!-- Committee Members Grid -->
			<div v-else-if="filteredMembers.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
				<ExecutiveCommitteeCard
					v-for="member in filteredMembers"
					:key="member.name"
					:member="member"
				/>
			</div>

			<!-- Empty State -->
			<div v-else class="bg-white rounded-2xl p-12 text-center border border-gray-200 max-w-xl mx-auto my-8">
				<div class="w-16 h-16 bg-blue-50 text-[#17345F] rounded-full flex items-center justify-center mx-auto mb-4">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
					</svg>
				</div>
				<h3 class="text-xl font-bold text-gray-900">No Committee Members Found</h3>
				<p class="text-gray-500 mt-2 text-sm leading-relaxed">
					{{ searchQuery ? 'No committee members match your search criteria.' : 'No executive committee records are currently published in Frappe.' }}
				</p>
				<div v-if="searchQuery" class="mt-6 flex justify-center">
					<Button variant="solid" theme="blue" size="md" class="bg-[#17345F]" @click="searchQuery = ''">
						Clear Search
					</Button>
				</div>
			</div>
		</section>

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup>
import { Breadcrumbs, Button, TextInput, createListResource } from "frappe-ui"
import { computed, onMounted, ref } from "vue"
import ExecutiveCommitteeCard from "../components/ExecutiveCommitteeCard.vue"
import Footer from "../components/Footer.vue"

const searchQuery = ref("")

onMounted(() => {
	window.scrollTo(0, 0)
})

// Query Executive Committee DocType
const committeeResource = createListResource({
	doctype: "Executive Committee",
	url: "alumni_nit_srinagar.api.get_executive_committee",
	fields: [
		"name",
		"title",
		"full_name",
		"position",
		"branchdepartment",
		"degree",
		"batch",
		"photo",
	],
	orderBy: "creation asc",
	auto: true,
	pageLength: 100,
})

const POSITION_HIERARCHY = [
	"President",
	"Vice President",
	"General Secretary",
	"Secretary",
	"Additional Secretary 1",
	"Additional Secretary 2",
	"Additional Secretary 3",
	"Joint Secretary 1",
	"Joint Secretary 2",
	"Joint Secretary 3",
	"Treasurer/Cashier",
]

const getPositionRank = (position) => {
	if (!position) return 999
	const index = POSITION_HIERARCHY.indexOf(position)
	return index !== -1 ? index : 900
}

const allMembers = computed(() => {
	const members = committeeResource.data || []
	return [...members].sort(
		(a, b) => getPositionRank(a.position) - getPositionRank(b.position),
	)
})

const filteredMembers = computed(() => {
	const q = searchQuery.value.trim().toLowerCase()
	if (!q) return allMembers.value

	return allMembers.value.filter((m) => {
		const nameMatch = m.full_name?.toLowerCase().includes(q)
		const posMatch = m.position?.toLowerCase().includes(q)
		const branchMatch = m.branchdepartment?.toLowerCase().includes(q)
		const batchMatch = m.batch?.toLowerCase().includes(q)
		const degreeMatch = m.degree?.toLowerCase().includes(q)
		return nameMatch || posMatch || branchMatch || batchMatch || degreeMatch
	})
})
</script>
