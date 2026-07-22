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
				<div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8 pt-8 border-t border-white/10 text-center">
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
				</div>
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
						All Published ({{ allAlumni.length }})
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

				<div class="text-xs text-gray-500 font-medium italic">
					Managed via Admin Dashboard (Frappe Desk)
				</div>
			</div>

			<!-- Filter & Search Controls Bar -->
			<div class="bg-white rounded-xl shadow-md border border-gray-200 p-4 sm:p-6 mb-8">
				<div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
					<!-- Search Input using frappe-ui TextInput -->
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

					<!-- Branch Filter using frappe-ui Select -->
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

					<!-- Reset Filters Button using frappe-ui Button -->
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

			<!-- Alumni Grid -->
			<div v-else-if="filteredAlumniList.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
				<div
					v-for="alumni in filteredAlumniList"
					:key="alumni.name || alumni.email_address"
					class="bg-white rounded-xl border border-gray-200 shadow-sm hover:shadow-lg hover:border-gray-300 transition-all duration-300 flex flex-col overflow-hidden group relative"
				>
					<!-- Card Header Banner -->
					<div
						:class="[
							'h-2',
							alumni.featured
								? 'bg-gradient-to-r from-[#D5A33D] via-amber-400 to-amber-600'
								: 'bg-gradient-to-r from-[#17345F] to-[#D5A33D]'
						]"
					></div>

					<div class="p-6 flex flex-col flex-grow">
						<!-- Featured Badge if Admin marked as Hotshot -->
						<div v-if="alumni.featured" class="absolute top-4 right-4">
							<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-300 shadow-xs">
								★ Featured
							</span>
						</div>

						<div class="flex items-start gap-4">
							<!-- Profile Image or Initial Avatar -->
							<div class="relative flex-shrink-0">
								<img
									v-if="alumni.image"
									:src="alumni.image"
									:alt="alumni.full_name"
									class="w-16 h-16 rounded-full object-cover border-2 border-white shadow-md group-hover:scale-105 transition-transform"
									@error="handleImageError(alumni)"
								/>
								<div
									v-else
									class="w-16 h-16 rounded-full bg-gradient-to-br from-[#17345F] to-[#255294] text-white flex items-center justify-center font-bold text-xl border-2 border-white shadow-md"
								>
									{{ getInitials(alumni.full_name) }}
								</div>
							</div>

							<!-- Name & Info -->
							<div class="flex-1 min-w-0 pr-12">
								<h2 class="text-lg font-bold text-gray-900 group-hover:text-[#17345F] transition-colors truncate">
									{{ alumni.full_name }}
								</h2>
								<!-- Role / Designation if available -->
								<div v-if="alumni.designation || alumni.company_organization" class="text-xs font-medium text-gray-600 mt-0.5 truncate">
									{{ alumni.designation }} <span v-if="alumni.designation && alumni.company_organization">at</span> {{ alumni.company_organization }}
								</div>
								<div class="flex items-center gap-1.5 mt-1 text-xs font-semibold text-[#D5A33D]">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
									</svg>
									Batch: {{ alumni.batchyear || 'N/A' }}
								</div>
							</div>
						</div>

						<!-- Branch Tag -->
						<div class="mt-4">
							<span class="inline-block px-3 py-1 bg-blue-50 text-[#17345F] rounded-md text-xs font-medium border border-blue-100 max-w-full truncate">
								{{ alumni.branchdepartment }}
							</span>
						</div>

						<!-- Contact Details -->
						<div class="mt-4 pt-4 border-t border-gray-100 space-y-2 text-xs text-gray-600 flex-grow">
							<div class="flex items-center gap-2 truncate">
								<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
								</svg>
								<a :href="`mailto:${alumni.email_address}`" class="hover:underline text-gray-700 hover:text-[#17345F] truncate">
									{{ alumni.email_address }}
								</a>
							</div>
							<div v-if="alumni.phone_number" class="flex items-center gap-2 truncate">
								<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
								</svg>
								<span class="text-gray-700">{{ alumni.phone_number }}</span>
							</div>
						</div>

						<!-- Card Footer Button using frappe-ui Button -->
						<div class="mt-5 pt-3">
							<Button
								variant="outline"
								theme="gray"
								size="sm"
								class="w-full justify-center font-semibold"
								@click="openModal(alumni)"
							>
								View Full Profile
								<template #suffix>
									<svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
									</svg>
								</template>
							</Button>
						</div>
					</div>
				</div>
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

		<!-- Profile Detail Modal -->
		<div
			v-if="selectedAlumni"
			class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs transition-opacity"
			@click.self="selectedAlumni = null"
		>
			<div class="bg-white rounded-2xl max-w-lg w-full overflow-hidden shadow-2xl border border-gray-100 transform transition-all">
				<!-- Modal Header -->
				<div class="bg-[#17345F] p-6 text-white relative">
					<button
						@click="selectedAlumni = null"
						class="absolute top-4 right-4 text-gray-300 hover:text-white p-1 rounded-full hover:bg-white/10 transition-colors"
						aria-label="Close modal"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
						</svg>
					</button>

					<div class="flex items-center gap-4">
						<img
							v-if="selectedAlumni.image"
							:src="selectedAlumni.image"
							:alt="selectedAlumni.full_name"
							class="w-20 h-20 rounded-full object-cover border-4 border-[#D5A33D] shadow-md"
						/>
						<div
							v-else
							class="w-20 h-20 rounded-full bg-[#D5A33D] text-[#17345F] flex items-center justify-center font-bold text-2xl border-4 border-white shadow-md"
						>
							{{ getInitials(selectedAlumni.full_name) }}
						</div>
						<div>
							<div class="flex items-center gap-2">
								<span class="text-xs font-semibold text-[#F2B633] uppercase tracking-wider">NIT Srinagar Alumni Profile</span>
								<span v-if="selectedAlumni.featured" class="text-[10px] bg-amber-400 text-gray-950 font-bold px-2 py-0.5 rounded-full">★ Hotshot</span>
							</div>
							<h3 class="text-2xl font-bold font-exo-2 text-white">{{ selectedAlumni.full_name }}</h3>
							<p v-if="selectedAlumni.designation || selectedAlumni.company_organization" class="text-xs text-gray-200 mt-0.5 font-medium">
								{{ selectedAlumni.designation }} <span v-if="selectedAlumni.designation && selectedAlumni.company_organization">at</span> {{ selectedAlumni.company_organization }}
							</p>
							<p class="text-xs text-gray-300 mt-0.5">Batch of {{ selectedAlumni.batchyear }}</p>
						</div>
					</div>
				</div>

				<!-- Modal Body -->
				<div class="p-6 space-y-4">
					<div class="bg-gray-50 rounded-xl p-4 border border-gray-100 space-y-3">
						<div>
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Department / Branch</span>
							<span class="text-sm font-semibold text-gray-800">{{ selectedAlumni.branchdepartment }}</span>
						</div>
						<div class="pt-2 border-t border-gray-200/60">
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Graduation Batch</span>
							<span class="text-sm font-semibold text-gray-800">{{ selectedAlumni.batchyear }}</span>
						</div>
						<div v-if="selectedAlumni.designation" class="pt-2 border-t border-gray-200/60">
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Designation / Role</span>
							<span class="text-sm font-semibold text-gray-800">{{ selectedAlumni.designation }}</span>
						</div>
						<div v-if="selectedAlumni.company_organization" class="pt-2 border-t border-gray-200/60">
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Company / Organization</span>
							<span class="text-sm font-semibold text-gray-800">{{ selectedAlumni.company_organization }}</span>
						</div>
						<div class="pt-2 border-t border-gray-200/60">
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Email Address</span>
							<a :href="`mailto:${selectedAlumni.email_address}`" class="text-sm font-semibold text-blue-600 hover:underline">
								{{ selectedAlumni.email_address }}
							</a>
						</div>
						<div v-if="selectedAlumni.phone_number" class="pt-2 border-t border-gray-200/60">
							<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Phone Number</span>
							<span class="text-sm font-semibold text-gray-800">{{ selectedAlumni.phone_number }}</span>
						</div>
					</div>

					<div class="pt-2 flex gap-3">
						<a
							:href="`mailto:${selectedAlumni.email_address}`"
							class="flex-1"
						>
							<Button
								variant="solid"
								theme="blue"
								size="md"
								class="w-full bg-[#17345F] hover:bg-[#12284c] text-white font-bold py-2.5 justify-center"
							>
								<template #prefix>
									<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
									</svg>
								</template>
								Send Email
							</Button>
						</a>
						<Button
							variant="subtle"
							theme="gray"
							size="md"
							@click="selectedAlumni = null"
						>
							Close
						</Button>
					</div>
				</div>
			</div>
		</div>

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup>
import { Button, Select, TextInput, createListResource } from "frappe-ui"
import { computed, ref } from "vue"
import Footer from "../components/Footer.vue"

const searchQuery = ref("")
const selectedBranch = ref("")
const selectedAlumni = ref(null)
const activeTab = ref("all") // "all" or "featured"

const branches = [
	"Computer Science & Engineering (CSE)",
	"Information Technology (IT)",
	"Electrical Engineering",
	"Electronics & Communication Engineering (ECE)",
	"Mechanical Engineering",
	"Civil Engineering",
	"Chemical Engineering",
	"Metallurgical & Materials Engineering",
	"Mathematics",
	"Physics",
	"Chemistry",
	"Humanities, Social Sciences & Management (HSS&M)",
]

const branchOptions = computed(() => [
	{ label: "All Departments", value: "" },
	...branches.map((b) => ({ label: b, value: b })),
])

// Frappe UI list resource to query backend database
// Filters for published = 1 so admins control exactly who appears on the website
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
}

const getInitials = (name) => {
	if (!name) return "AN"
	const cleanName = name.replace(/^(Er\.|Dr\.|Prof\.|Mr\.|Ms\.)\s+/i, "")
	const parts = cleanName.trim().split(" ")
	if (parts.length >= 2) {
		return `${parts[0][0]}${parts[parts.length - 1][0]}`.toUpperCase()
	}
	return name.substring(0, 2).toUpperCase()
}

const handleImageError = (alumni) => {
	alumni.image = ""
}

const openModal = (alumni) => {
	selectedAlumni.value = alumni
}
</script>
