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

			<!-- Search & View Toggle Controls Bar -->
			<div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
				<div>
					<h2 class="text-xl font-bold text-gray-900 font-exo-2">
						Committee Office Bearers ({{ filteredMembers.length }})
					</h2>
					<p class="text-xs text-gray-500 mt-0.5">Governing officers of the global NIT Srinagar alumni network</p>
				</div>

				<div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
					<!-- Search Input -->
					<div class="w-full sm:w-72">
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

					<!-- View Mode Toggle (List vs Grid) -->
					<div class="flex items-center gap-1 bg-white p-1 rounded-lg border border-gray-200 shadow-2xs">
						<button
							type="button"
							@click="viewMode = 'list'"
							:class="[
								'px-3 py-1.5 rounded-md text-xs font-bold flex items-center gap-1.5 transition-all',
								viewMode === 'list' ? 'bg-[#17345F] text-white shadow-xs' : 'text-gray-600 hover:text-gray-900'
							]"
							title="Structured Table View"
						>
							<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
							</svg>
							<span>Table View</span>
						</button>
						<button
							type="button"
							@click="viewMode = 'grid'"
							:class="[
								'px-3 py-1.5 rounded-md text-xs font-bold flex items-center gap-1.5 transition-all',
								viewMode === 'grid' ? 'bg-[#17345F] text-white shadow-xs' : 'text-gray-600 hover:text-gray-900'
							]"
							title="Grid Card View"
						>
							<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
							</svg>
							<span>Grid View</span>
						</button>
					</div>
				</div>
			</div>

			<!-- Loading Skeleton -->
			<div v-if="committeeResource.loading" class="space-y-3">
				<div v-for="i in 6" :key="i" class="bg-white rounded-xl p-4 border border-gray-200 shadow-2xs animate-pulse flex items-center gap-4">
					<div class="rounded-full bg-gray-200 h-12 w-12 flex-shrink-0"></div>
					<div class="flex-1 space-y-2">
						<div class="h-4 bg-gray-200 rounded w-1/3"></div>
						<div class="h-3 bg-gray-200 rounded w-1/4"></div>
					</div>
				</div>
			</div>

			<!-- Executive Committee Content -->
			<div v-else-if="filteredMembers.length > 0">
				<!-- Table / List View (Default - Space Saving & Prestigious) -->
				<div v-if="viewMode === 'list'" class="bg-white rounded-xl border border-gray-200/90 shadow-sm overflow-hidden">
					<!-- Desktop Institutional Table (>= lg) -->
					<div class="hidden lg:block overflow-x-auto">
						<table class="w-full text-left border-collapse">
							<thead>
								<tr class="bg-[#17345F] text-white text-xs font-bold font-exo-2 uppercase tracking-wider">
									<th scope="col" class="py-3.5 px-6">Executive Officer</th>
									<th scope="col" class="py-3.5 px-6">Position</th>
									<th scope="col" class="py-3.5 px-6">Department / Branch</th>
									<th scope="col" class="py-3.5 px-6">Degree</th>
									<th scope="col" class="py-3.5 px-6 text-right">Batch</th>
								</tr>
							</thead>
							<tbody class="divide-y divide-gray-100 text-sm">
								<tr
									v-for="member in filteredMembers"
									:key="member.name"
									class="hover:bg-blue-50/40 transition-colors group"
								>
									<!-- Officer Avatar & Name -->
									<td class="py-4 px-6">
										<div class="flex items-center gap-3.5">
											<img
												v-if="member.photo && !imageErrors[member.name]"
												:src="member.photo"
												:alt="member.full_name"
												class="w-11 h-11 rounded-full object-cover border-2 border-white shadow-2xs flex-shrink-0"
												@error="imageErrors[member.name] = true"
											/>
											<div
												v-else
												class="w-11 h-11 rounded-full bg-gradient-to-br from-[#17345F] to-[#255294] text-white flex items-center justify-center font-bold text-sm flex-shrink-0"
											>
												{{ getInitials(member.full_name) }}
											</div>
											<div>
												<span class="font-bold text-gray-900 font-exo-2 text-base block group-hover:text-[#17345F] transition-colors">
													{{ (member.title ? member.title + ' ' : '') + member.full_name }}
												</span>
											</div>
										</div>
									</td>

									<!-- Position Badge -->
									<td class="py-4 px-6">
										<span class="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-bold bg-[#17345F] text-white shadow-2xs">
											<svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-[#F2B633]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
												<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
											</svg>
											{{ member.position }}
										</span>
									</td>

									<!-- Branch / Department -->
									<td class="py-4 px-6">
										<span class="inline-block px-2.5 py-1 bg-slate-100 text-[#17345F] rounded-md text-xs font-semibold border border-slate-200">
											{{ member.branchdepartment }}
										</span>
									</td>

									<!-- Degree -->
									<td class="py-4 px-6">
										<span v-if="member.degree" class="text-xs font-semibold text-gray-700 bg-gray-100 px-2 py-0.5 rounded border border-gray-200">
											{{ member.degree }}
										</span>
										<span v-else class="text-gray-300">-</span>
									</td>

									<!-- Batch (ONLY if present) -->
									<td class="py-4 px-6 text-right">
										<span v-if="member.batch && String(member.batch).trim()" class="font-bold text-xs text-[#B8841D]">
											Batch: {{ member.batch }}
										</span>
										<span v-else class="text-gray-300">-</span>
									</td>
								</tr>
							</tbody>
						</table>
					</div>

					<!-- Mobile Dense Compact Rows (< lg - Takes minimal vertical height!) -->
					<div class="lg:hidden divide-y divide-gray-100">
						<div
							v-for="member in filteredMembers"
							:key="member.name"
							class="p-3.5 hover:bg-blue-50/40 transition-colors flex items-center justify-between gap-3"
						>
							<div class="flex items-center gap-3 min-w-0">
								<!-- Avatar -->
								<img
									v-if="member.photo && !imageErrors[member.name]"
									:src="member.photo"
									:alt="member.full_name"
									class="w-11 h-11 rounded-full object-cover border border-gray-200 flex-shrink-0"
									@error="imageErrors[member.name] = true"
								/>
								<div
									v-else
									class="w-11 h-11 rounded-full bg-[#17345F] text-white flex items-center justify-center font-bold text-xs flex-shrink-0"
								>
									{{ getInitials(member.full_name) }}
								</div>

								<!-- Member Info -->
								<div class="min-w-0">
									<div class="flex items-center gap-1.5 truncate">
										<h4 class="font-bold font-exo-2 text-sm text-gray-900 truncate">
											{{ (member.title ? member.title + ' ' : '') + member.full_name }}
										</h4>
									</div>
									<div class="flex items-center gap-1.5 mt-0.5">
										<span class="text-[10px] font-bold bg-[#17345F] text-white px-2 py-0.2 rounded-full truncate">
											{{ member.position }}
										</span>
										<span v-if="member.batch && String(member.batch).trim()" class="text-[11px] font-bold text-[#B8841D] truncate">
											• Batch: {{ member.batch }}
										</span>
									</div>
									<p class="text-xs text-gray-500 truncate mt-0.5">
										{{ member.branchdepartment }} <span v-if="member.degree">({{ member.degree }})</span>
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Grid Mode -->
				<div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
					<ExecutiveCommitteeCard
						v-for="member in filteredMembers"
						:key="member.name"
						:member="member"
					/>
				</div>
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
import { getInitials } from "../utils"

const searchQuery = ref("")
const viewMode = ref("list") // "list" (Table View) or "grid"
const imageErrors = ref({})

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
