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
							Global Network
						</div>
						<h1 class="text-3xl sm:text-4xl lg:text-5xl font-exo-2 font-bold tracking-tight text-white">
							Alumni Directory
						</h1>
						<p class="mt-3 text-base sm:text-lg text-gray-200 max-w-2xl leading-relaxed">
							Connect and engage with our distinguished alumni network around the world across batches and departments.
						</p>
					</div>
					<div class="flex-shrink-0">
						<router-link
							:to="{ name: 'RegisterAlumni' }"
							class="inline-flex items-center gap-2 px-6 py-3 bg-[#F2B633] hover:bg-[#D5A33D] text-gray-950 font-bold rounded-lg shadow-lg transition-all transform hover:-translate-y-0.5 text-sm"
						>
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
							</svg>
							Register as Alumni
						</router-link>
					</div>
				</div>
			</div>
		</section>

		<!-- Main Content Area -->
		<section class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-grow">
			<!-- Breadcrumbs -->
			<div class="mb-6">
				<Breadcrumbs
					:items="[
						{ label: 'Home', route: '/' },
						{ label: 'Alumni Directory' }
					]"
				/>
			</div>

			<!-- Top Controls: Tabs & View Toggle -->
			<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
				<!-- Category Tabs -->
				<div class="flex flex-wrap items-center gap-2">
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

				<!-- View Mode Toggle (List vs Grid) -->
				<div class="flex items-center gap-1 bg-white p-1 rounded-lg border border-gray-200 shadow-2xs self-start sm:self-auto">
					<button
						type="button"
						@click="viewMode = 'list'"
						:class="[
							'px-3 py-1.5 rounded-md text-xs font-bold flex items-center gap-1.5 transition-all',
							viewMode === 'list' ? 'bg-[#17345F] text-white shadow-xs' : 'text-gray-600 hover:text-gray-900'
						]"
						title="Structured List View"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
						</svg>
						<span>Directory List</span>
					</button>
					<button
						type="button"
						@click="viewMode = 'grid'"
						:class="[
							'px-3 py-1.5 rounded-md text-xs font-bold flex items-center gap-1.5 transition-all',
							viewMode === 'grid' ? 'bg-[#17345F] text-white shadow-xs' : 'text-gray-600 hover:text-gray-900'
						]"
						title="Grid View"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
						</svg>
						<span>Grid Cards</span>
					</button>
				</div>
			</div>

			<!-- Filter & Search Controls Bar -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 sm:p-5 mb-8">
				<!-- Mobile Controls Layout (Visible on < md) -->
				<div class="flex md:hidden items-center gap-2">
					<!-- Search Bar on Left -->
					<div class="flex-1">
						<TextInput
							id="alumni-search-mobile"
							v-model="searchQuery"
							placeholder="Search by name, branch, batch..."
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
							placeholder="Search by name, branch, batch..."
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
							class="w-full justify-center py-2 font-bold text-xs"
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
			<div v-if="alumniResource.loading" class="space-y-3">
				<div v-for="i in 6" :key="i" class="bg-white rounded-xl p-4 border border-gray-200 shadow-2xs animate-pulse flex items-center gap-4">
					<div class="rounded-full bg-gray-200 h-12 w-12 flex-shrink-0"></div>
					<div class="flex-1 space-y-2">
						<div class="h-4 bg-gray-200 rounded w-1/3"></div>
						<div class="h-3 bg-gray-200 rounded w-1/4"></div>
					</div>
				</div>
			</div>

			<!-- Alumni Directory List View (Default - Space Saving & Professional) -->
			<div v-else-if="filteredAlumniList.length > 0">
				<!-- List Mode -->
				<div v-if="viewMode === 'list'" class="bg-white rounded-xl border border-gray-200/90 shadow-sm overflow-hidden">
					<!-- Desktop Table View (>= lg) -->
					<div class="hidden lg:block overflow-x-auto">
						<table class="w-full text-left border-collapse">
							<thead>
								<tr class="bg-[#17345F] text-white text-xs font-bold font-exo-2 uppercase tracking-wider">
									<th scope="col" class="py-3.5 px-6">Alumni Member</th>
									<th scope="col" class="py-3.5 px-6">Department / Branch</th>
									<th scope="col" class="py-3.5 px-6">Batch</th>
									<th scope="col" class="py-3.5 px-6">Contact Details</th>
									<th scope="col" class="py-3.5 px-6 text-right">Action</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-gray-100 text-sm">
								<tr
									v-for="alumni in filteredAlumniList"
									:key="alumni.name || alumni.email_address"
									class="hover:bg-blue-50/40 transition-colors group cursor-pointer"
									@click="selectedAlumni = alumni"
								>
									<!-- Member Profile -->
									<td class="py-4 px-6">
										<div class="flex items-center gap-3.5">
											<img
												v-if="alumni.image && !imageErrors[alumni.name]"
												:src="alumni.image"
												:alt="alumni.full_name"
												class="w-11 h-11 rounded-full object-cover border-2 border-white shadow-2xs flex-shrink-0"
												@error="imageErrors[alumni.name] = true"
											/>
											<div
												v-else
												class="w-11 h-11 rounded-full bg-gradient-to-br from-[#17345F] to-[#255294] text-white flex items-center justify-center font-bold text-sm flex-shrink-0"
											>
												{{ getInitials(alumni.full_name) }}
											</div>
											<div class="min-w-0">
												<div class="flex items-center gap-2">
													<span class="font-bold text-gray-900 group-hover:text-[#17345F] font-exo-2 text-base truncate">
														{{ alumni.full_name }}
													</span>
													<span v-if="alumni.featured" class="text-[10px] font-bold bg-amber-100 text-amber-900 border border-amber-300 px-1.5 py-0.2 rounded-full">
														★ Featured
													</span>
												</div>
												<p v-if="alumni.designation || alumni.company_organization" class="text-xs text-gray-500 truncate mt-0.5">
													{{ alumni.designation }} <span v-if="alumni.designation && alumni.company_organization" class="text-gray-400">at</span> {{ alumni.company_organization }}
												</p>
											</div>
										</div>
									</td>

									<!-- Department -->
									<td class="py-4 px-6">
										<span class="inline-block px-2.5 py-1 bg-slate-100 text-[#17345F] rounded-md text-xs font-semibold border border-slate-200">
											{{ alumni.branchdepartment }}
										</span>
									</td>

									<!-- Batch -->
									<td class="py-4 px-6">
										<span class="font-bold text-xs text-[#B8841D]">
											{{ alumni.batchyear || 'N/A' }}
										</span>
									</td>

									<!-- Contact -->
									<td class="py-4 px-6 text-xs text-gray-600 space-y-0.5">
										<div class="font-medium text-gray-700 truncate">{{ alumni.email_address }}</div>
										<div v-if="alumni.phone_number" class="text-gray-500 font-mono text-[11px]">{{ alumni.phone_number }}</div>
									</td>

									<!-- Action Button -->
									<td class="py-4 px-6 text-right">
										<button
											type="button"
											class="px-3.5 py-1.5 rounded-md text-xs font-bold uppercase tracking-wider text-[#17345F] hover:bg-[#17345F] hover:text-white border border-gray-200 transition-all shadow-2xs inline-flex items-center gap-1"
											@click.stop="selectedAlumni = alumni"
										>
											<span>View</span>
											<svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
												<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
											</svg>
										</button>
									</td>
								</tr>
							</tbody>
						</table>
					</div>

					<!-- Mobile Dense Compact Rows (< lg - Takes minimal vertical height!) -->
					<div class="lg:hidden divide-y divide-gray-100">
						<div
							v-for="alumni in filteredAlumniList"
							:key="alumni.name || alumni.email_address"
							@click="selectedAlumni = alumni"
							class="p-3.5 hover:bg-blue-50/40 active:bg-blue-100/50 transition-colors flex items-center justify-between gap-3 cursor-pointer"
						>
							<div class="flex items-center gap-3 min-w-0">
								<!-- Compact Avatar -->
								<img
									v-if="alumni.image && !imageErrors[alumni.name]"
									:src="alumni.image"
									:alt="alumni.full_name"
									class="w-11 h-11 rounded-full object-cover border border-gray-200 flex-shrink-0"
									@error="imageErrors[alumni.name] = true"
								/>
								<div
									v-else
									class="w-11 h-11 rounded-full bg-[#17345F] text-white flex items-center justify-center font-bold text-xs flex-shrink-0"
								>
									{{ getInitials(alumni.full_name) }}
								</div>

								<!-- Info -->
								<div class="min-w-0">
									<div class="flex items-center gap-1.5 truncate">
										<h4 class="font-bold font-exo-2 text-sm text-gray-900 truncate">{{ alumni.full_name }}</h4>
										<span v-if="alumni.featured" class="text-[9px] font-bold bg-amber-100 text-amber-900 border border-amber-300 px-1 rounded flex-shrink-0">★</span>
									</div>
									<p class="text-xs text-[#17345F] font-semibold truncate mt-0.5">
										{{ alumni.branchdepartment }}
									</p>
									<div class="flex items-center gap-2 text-[11px] text-gray-500 mt-0.5">
										<span class="font-bold text-[#B8841D]">Batch: {{ alumni.batchyear }}</span>
										<span v-if="alumni.designation" class="truncate">• {{ alumni.designation }}</span>
									</div>
								</div>
							</div>

							<!-- Arrow Action -->
							<div class="flex-shrink-0 text-gray-400">
								<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
								</svg>
							</div>
						</div>
					</div>
				</div>

				<!-- Grid Mode -->
				<div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
					<AlumniCard
						v-for="alumni in filteredAlumniList"
						:key="alumni.name || alumni.email_address"
						:alumni="alumni"
						@select="selectedAlumni = $event"
					/>
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

		<!-- Mobile Branch Filter Selection Modal Component -->
		<BranchFilterModal
			:isOpen="isBranchModalOpen"
			:selectedBranch="selectedBranch"
			:branches="branches"
			@close="isBranchModalOpen = false"
			@select="onModalSelectBranch"
		/>

		<!-- Alumni Profile Detail Modal -->
		<AlumniProfileModal
			:alumni="selectedAlumni"
			@close="selectedAlumni = null"
		/>

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup>
import {
	Breadcrumbs,
	Button,
	Select,
	TextInput,
	createListResource,
} from "frappe-ui"
import { computed, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import AlumniCard from "../components/AlumniCard.vue"
import AlumniProfileModal from "../components/AlumniProfileModal.vue"
import BranchFilterModal from "../components/BranchFilterModal.vue"
import Footer from "../components/Footer.vue"
import { DEPARTMENT_BRANCHES, formatErrorMessage, getInitials } from "../utils"

const route = useRoute()
const router = useRouter()

const searchQuery = ref("")
const selectedBranch = ref("")
const selectedAlumni = ref(null)
const activeTab = ref("all") // "all" or "featured"
const viewMode = ref("list") // "list" or "grid"
const isBranchModalOpen = ref(false)
const imageErrors = ref({})

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
	url: "alumni_nit_srinagar.api.get_alumni_list",
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

const filteredAlumniList = computed(() => {
	const q = searchQuery.value.trim().toLowerCase()
	const branch = selectedBranch.value

	return allAlumni.value.filter((alumni) => {
		// Filter by Tab
		if (activeTab.value === "featured" && !alumni.featured) {
			return false
		}

		// Filter by Branch
		if (branch && alumni.branchdepartment !== branch) {
			return false
		}

		// Search Query filter (matches Name, Batch, Designation, Company, or Email)
		if (q) {
			const nameMatch = alumni.full_name?.toLowerCase().includes(q)
			const batchMatch = alumni.batchyear?.toLowerCase().includes(q)
			const branchMatch = alumni.branchdepartment?.toLowerCase().includes(q)
			const designationMatch = alumni.designation?.toLowerCase().includes(q)
			const companyMatch = alumni.company_organization?.toLowerCase().includes(q)
			const emailMatch = alumni.email_address?.toLowerCase().includes(q)

			if (
				!nameMatch &&
				!batchMatch &&
				!branchMatch &&
				!designationMatch &&
				!companyMatch &&
				!emailMatch
			) {
				return false
			}
		}

		return true
	})
})

const isFiltered = computed(() => {
	return !!searchQuery.value || !!selectedBranch.value || activeTab.value !== "all"
})

const resetFilters = () => {
	searchQuery.value = ""
	selectedBranch.value = ""
	activeTab.value = "all"
	router.replace({ query: {} })
}

const onModalSelectBranch = (branch) => {
	selectedBranch.value = branch
}
</script>
