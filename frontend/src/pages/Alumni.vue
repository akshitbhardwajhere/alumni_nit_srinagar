<template>
	<div class="min-h-screen bg-gray-50 font-sans text-gray-900 flex flex-col">
		<!-- Hero Section -->
		<section class="bg-[#17345F] text-white relative overflow-hidden py-12 lg:py-16">
			<div class="absolute inset-0 opacity-10 bg-[radial-gradient(#D5A33D_1px,transparent_1px)] [background-size:16px_16px]"></div>
			<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
				<div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
					<div>
						<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D5A33D]/20 border border-[#D5A33D]/40 text-[#F2B633] text-xs sm:text-sm font-medium tracking-wide mb-3">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
							</svg>
							NIT Srinagar Alumni Network
						</div>
						<h1 class="text-3xl sm:text-4xl lg:text-5xl font-exo-2 font-bold tracking-tight text-white">
							Our Alumni Directory
						</h1>
						<p class="mt-3 text-base sm:text-lg text-gray-200 max-w-2xl leading-relaxed">
							Featuring distinguished graduates approved by the Institute Administration. Discover leaders, innovators, and achievers from NIT Srinagar across the globe.
						</p>
					</div>
					<div class="flex-shrink-0">
						<router-link :to="{ name: 'RegisterAlumni' }">
							<Button
								variant="solid"
								theme="yellow"
								size="lg"
								class="bg-[#F2B633] hover:bg-[#D5A33D] text-gray-950 font-bold shadow-md hover:shadow-xl transition-all"
							>
								<template #prefix>
									<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
									</svg>
								</template>
								Register as Alumni
							</Button>
						</router-link>
					</div>
				</div>

				<!-- Stats Bar -->
				<!-- <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8 pt-8 border-t border-white/10 text-center">
					<div class="bg-white/5 rounded-lg p-3 backdrop-blur-sm">
						<div class="text-2xl font-bold text-[#F2B633]">{{ filteredAlumniList.length }}</div>
						<div class="text-xs text-gray-300">Published Alumni</div>
					</div>
					<div class="bg-white/5 rounded-lg p-3 backdrop-blur-sm">
						<div class="text-2xl font-bold text-[#F2B633]">{{ featuredCount }}</div>
						<div class="text-xs text-gray-300">Featured Hotshots</div>
					</div>
					<div class="bg-white/5 rounded-lg p-3 backdrop-blur-sm">
						<div class="text-2xl font-bold text-[#F2B633]">{{ branches.length }}</div>
						<div class="text-xs text-gray-300">Departments</div>
					</div>
					<div class="bg-white/5 rounded-lg p-3 backdrop-blur-sm">
						<div class="text-2xl font-bold text-[#F2B633]">Verified</div>
						<div class="text-xs text-gray-300">Desk Managed</div>
					</div>
				</div> -->
			</div>
		</section>

		<!-- Main Content Section -->
		<section class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-grow">
			<!-- View Mode & Featured Filter Tabs -->
			<div class="flex flex-wrap items-center justify-between gap-4 mb-6 border-b border-gray-200 pb-4">
				<div class="flex items-center gap-2">
					<button
						@click="activeTab = 'all'"
						:class="[
							'px-4 py-2 text-sm font-bold rounded-lg transition-all',
							activeTab === 'all'
								? 'bg-[#17345F] text-white shadow-sm'
								: 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
						]"
					>
						All Alumni ({{ allAlumni.length }})
					</button>
					<button
						@click="activeTab = 'featured'"
						:class="[
							'px-4 py-2 text-sm font-bold rounded-lg transition-all flex items-center gap-1.5',
							activeTab === 'featured'
								? 'bg-[#D5A33D] text-gray-950 shadow-sm'
								: 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
						]"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-amber-600" fill="currentColor" viewBox="0 0 24 24">
							<path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
						</svg>
						Featured Hotshots ({{ featuredCount }})
					</button>
				</div>
			</div>

			<!-- Filter & Search Controls Bar -->
			<div class="bg-white rounded-xl shadow-md border border-gray-200 p-4 sm:p-6 mb-8">
				<!-- Mobile Controls Layout (Visible on < md) -->
				<div class="flex md:hidden items-center gap-2">
					<!-- Search Bar on Left -->
					<div class="flex-1">
						<TextInput
							id="alumni-search-mobile"
							v-model="searchQuery"
							placeholder="Search by name, role, batch..."
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

					<!-- Branch Filter Icon Button on Right -->
					<button
						type="button"
						@click="isBranchModalOpen = true"
						:class="[
							'h-10 px-3.5 rounded-lg border flex items-center justify-center gap-1.5 font-bold text-xs relative flex-shrink-0 transition-colors',
							selectedBranch
								? 'bg-[#17345F] text-white border-[#17345F] shadow-sm'
								: 'bg-gray-50 text-gray-700 border-gray-300 hover:bg-gray-100'
						]"
						aria-label="Filter Department"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
						</svg>
						<span class="hidden sm:inline">Filter</span>
						<span v-if="selectedBranch" class="w-2 h-2 rounded-full bg-[#F2B633]"></span>
					</button>
				</div>

				<!-- Desktop Controls Layout (Visible on >= md) -->
				<div class="hidden md:grid md:grid-cols-12 gap-4 items-center">
					<!-- Search Input -->
					<div class="md:col-span-6">
						<label for="alumni-search" class="block text-xs font-semibold text-gray-500 mb-1 uppercase tracking-wider">Search</label>
						<TextInput
							id="alumni-search"
							v-model="searchQuery"
							placeholder="Search by name, role, company, batch..."
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

					<!-- Branch Filter Select -->
					<div class="md:col-span-4">
						<label for="branch-filter" class="block text-xs font-semibold text-gray-500 mb-1 uppercase tracking-wider">Department / Branch</label>
						<Select
							id="branch-filter"
							v-model="selectedBranch"
							:options="branchOptions"
							placeholder="Select Department"
							size="md"
							variant="outline"
							class="w-full"
						/>
					</div>

					<!-- Reset Filters Button -->
					<div class="md:col-span-2 flex items-end h-full pt-5">
						<Button
							variant="subtle"
							theme="gray"
							size="md"
							class="w-full justify-center py-2"
							:disabled="!isFiltered"
							@click="resetFilters"
						>
							<template #prefix>
								<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
								</svg>
							</template>
							Reset
						</Button>
					</div>
				</div>
			</div>

			<!-- Error Alert State -->
			<div
				v-if="alumniResource.error"
				class="p-4 bg-red-50 border-l-4 border-red-500 rounded-r-lg text-red-700 text-sm mb-6"
			>
				{{ formatErrorMessage(alumniResource.error, "Unable to load alumni records at this time. Please try again later.") }}
			</div>

			<!-- Loading State -->
			<div v-if="alumniResource.loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
				<div v-for="i in 6" :key="i" class="bg-white rounded-xl p-6 border border-gray-100 shadow-sm animate-pulse space-y-4">
					<div class="flex items-center space-x-4">
						<div class="rounded-full bg-gray-200 h-16 w-16"></div>
						<div class="flex-1 space-y-2">
							<div class="h-4 bg-gray-200 rounded w-3/4"></div>
							<div class="h-3 bg-gray-200 rounded w-1/2"></div>
						</div>
					</div>
					<div class="h-3 bg-gray-200 rounded w-full"></div>
					<div class="h-3 bg-gray-200 rounded w-2/3"></div>
				</div>
			</div>

			<!-- Alumni Grid with AlumniCard Component -->
			<div v-else-if="filteredAlumniList.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
				<AlumniCard
					v-for="alumni in filteredAlumniList"
					:key="alumni.name || alumni.email_address"
					:alumni="alumni"
					@select="selectedAlumni = $event"
				/>
			</div>

			<!-- Empty State -->
			<div v-else class="bg-white rounded-2xl p-12 text-center border border-gray-200 max-w-xl mx-auto my-8">
				<div class="w-16 h-16 bg-blue-50 text-[#17345F] rounded-full flex items-center justify-center mx-auto mb-4">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
					</svg>
				</div>
				<h3 class="text-xl font-bold text-gray-900">No Alumni Displayed Yet</h3>
				<p class="text-gray-500 mt-2 text-sm leading-relaxed">
					No alumni match your search or have been published by the Institute Admin yet. In Frappe Desk, admins can toggle <strong>"Publish on Website"</strong> to display selected alumni on this page.
				</p>
				<div class="mt-6 flex flex-wrap gap-3 justify-center">
					<Button
						variant="solid"
						theme="blue"
						size="md"
						class="bg-[#17345F] hover:bg-[#12284c]"
						@click="resetFilters"
					>
						Clear Filters
					</Button>
					<router-link :to="{ name: 'RegisterAlumni' }">
						<Button
							variant="subtle"
							theme="gray"
							size="md"
						>
							Register New Alumni
						</Button>
					</router-link>
				</div>
			</div>
		</section>

		<!-- Mobile Branch Filter Selection Modal Component -->
		<BranchFilterModal
			:isOpen="isBranchModalOpen"
			:selectedBranch="selectedBranch"
			:branches="branches"
			@select="selectedBranch = $event"
			@close="isBranchModalOpen = false"
		/>

		<!-- Profile Detail Modal Component -->
		<AlumniProfileModal
			:alumni="selectedAlumni"
			@close="selectedAlumni = null"
		/>

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup>
import { Button, Select, TextInput, createListResource } from "frappe-ui"
import { computed, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import AlumniCard from "../components/AlumniCard.vue"
import AlumniProfileModal from "../components/AlumniProfileModal.vue"
import BranchFilterModal from "../components/BranchFilterModal.vue"
import Footer from "../components/Footer.vue"
import { DEPARTMENT_BRANCHES, formatErrorMessage } from "../utils"

const route = useRoute()
const router = useRouter()

const searchQuery = ref("")
const selectedBranch = ref("")
const selectedAlumni = ref(null)
const activeTab = ref("all") // "all" or "featured"
const isBranchModalOpen = ref(false)

watch(
	() => route.query.search,
	(newSearch) => {
		searchQuery.value = (newSearch || "").toString()
	},
	{ immediate: true },
)

const branches = DEPARTMENT_BRANCHES

const branchOptions = computed(() => [
	{ label: "All Departments", value: "" },
	...branches.map((b) => ({ label: b, value: b })),
])

// Frappe UI list resource to query backend database
const alumniResource = createListResource({
	doctype: "Alumni",
	fields: [
		"name",
		"full_name",
		"branchdepartment",
		"batchyear",
		"email_address",
		"phone_number",
		"image",
		"designation",
		"company_organization",
		"published",
		"featured",
	],
	filters: [["published", "=", 1]],
	auto: true,
	pageLength: 100,
})

const allAlumni = computed(() => {
	return alumniResource.data || []
})

watch(
	[allAlumni, () => route.query.profile],
	([alumniList, profileId]) => {
		if (profileId && alumniList?.length) {
			const found = alumniList.find(
				(a) =>
					a.name === profileId ||
					a.full_name?.toLowerCase() === profileId.toLowerCase(),
			)
			if (found) {
				selectedAlumni.value = found
			}
		}
	},
	{ immediate: true },
)

const featuredCount = computed(() => {
	return allAlumni.value.filter((a) => a.featured).length
})

const isFiltered = computed(() => {
	return (
		searchQuery.value.trim() !== "" ||
		selectedBranch.value !== "" ||
		activeTab.value !== "all"
	)
})

const filteredAlumniList = computed(() => {
	return allAlumni.value.filter((alumni) => {
		const matchesSearch =
			!searchQuery.value ||
			alumni.full_name
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase()) ||
			alumni.email_address
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase()) ||
			alumni.batchyear
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase()) ||
			alumni.branchdepartment
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase()) ||
			alumni.designation
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase()) ||
			alumni.company_organization
				?.toLowerCase()
				.includes(searchQuery.value.toLowerCase())

		const matchesBranch =
			!selectedBranch.value || alumni.branchdepartment === selectedBranch.value

		const matchesTab =
			activeTab.value === "all" ||
			(activeTab.value === "featured" && alumni.featured)

		return matchesSearch && matchesBranch && matchesTab
	})
})

const uniqueBatches = computed(() => {
	const set = new Set()
	for (const a of allAlumni.value) {
		if (a.batchyear) set.add(a.batchyear)
	}
	return Array.from(set)
})

const resetFilters = () => {
	searchQuery.value = ""
	selectedBranch.value = ""
	activeTab.value = "all"
	if (route.query.search) {
		router.replace({ name: "Alumni" })
	}
}
</script>
