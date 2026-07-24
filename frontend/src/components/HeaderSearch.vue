<template>
	<div class="relative w-full">
		<form @submit.prevent="performSearch" class="flex shadow-sm">
			<input
				type="text"
				v-model="searchQuery"
				@focus="handleFocus"
				@blur="handleBlur"
				@input="isDropdownOpen = true"
				:placeholder="placeholder || 'Search Alumni'"
				:class="inputClass || 'w-72 px-4 py-2.5 text-[15px] rounded-l bg-white outline-none text-gray-800 focus:ring-2 focus:ring-[#D5A33D] transition-all'"
			/>
			<button
				type="submit"
				class="bg-[#F2B633] px-5 rounded-r hover:bg-[#D5A33D] text-gray-900 font-bold transition-colors flex items-center justify-center"
				aria-label="Search"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-5 w-5"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2.5"
						d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
					/>
				</svg>
			</button>
		</form>

		<!-- Live Search Results Dropdown -->
		<div
			v-if="isDropdownOpen && searchQuery.trim().length > 0"
			class="absolute top-full left-0 right-0 mt-1 bg-white rounded-lg shadow-2xl border border-gray-200 overflow-hidden z-50 divide-y divide-gray-100 max-h-80 overflow-y-auto text-left"
		>
			<div v-if="searchResults.length === 0" class="p-4 text-center text-xs text-gray-500">
				No alumni found matching "{{ searchQuery }}"
			</div>
			<div
				v-for="alumni in searchResults"
				:key="alumni.name || alumni.email_address"
				@mousedown.prevent="selectAlumni(alumni)"
				class="p-3 hover:bg-blue-50 cursor-pointer transition-colors flex items-center gap-3"
			>
				<img
					v-if="alumni.image"
					:src="alumni.image"
					:alt="alumni.full_name"
					class="w-10 h-10 rounded-full object-cover border border-gray-200 flex-shrink-0"
				/>
				<div
					v-else
					class="w-10 h-10 rounded-full bg-[#17345F] text-white flex items-center justify-center font-bold text-xs flex-shrink-0"
				>
					{{ getInitials(alumni.full_name) }}
				</div>
				<div class="flex-1 min-w-0">
					<div class="flex items-center justify-between gap-1">
						<span class="font-bold text-sm text-gray-900 truncate">{{ alumni.full_name }}</span>
						<span v-if="alumni.featured" class="text-[9px] bg-amber-100 text-amber-900 font-bold px-1.5 py-0.5 rounded border border-amber-300 flex-shrink-0">★ Hotshot</span>
					</div>
					<div class="text-xs text-gray-500 truncate mt-0.5">
						<span v-if="alumni.designation" class="font-medium text-gray-700">{{ alumni.designation }} • </span>
						<span>{{ alumni.branchdepartment }} ({{ alumni.batchyear }})</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { createListResource } from "frappe-ui"
import { computed, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import { getInitials } from "../utils"

defineProps({
	inputClass: {
		type: String,
		default: "",
	},
	placeholder: {
		type: String,
		default: "Search by name and batch...",
	},
})

const emit = defineEmits(["selectAlumni"])

const searchQuery = ref("")
const isDropdownOpen = ref(false)
const router = useRouter()
const route = useRoute()

// Query backend published alumni for live header search
const alumniSearchResource = createListResource({
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

const searchResults = computed(() => {
	const q = searchQuery.value.trim().toLowerCase()
	if (!q) return []
	const data = alumniSearchResource.data || []
	return data
		.filter((alumni) => {
			return (
				alumni.full_name?.toLowerCase().includes(q) ||
				alumni.batchyear?.toLowerCase().includes(q)
			)
		})
		.slice(0, 6)
})

watch(
	() => route.query.search,
	(newSearch) => {
		searchQuery.value = (newSearch || "").toString()
	},
	{ immediate: true },
)

const handleFocus = () => {
	isDropdownOpen.value = true
}

const handleBlur = () => {
	setTimeout(() => {
		isDropdownOpen.value = false
	}, 200)
}

const selectAlumni = (alumni) => {
	isDropdownOpen.value = false
	emit("selectAlumni", alumni)
	router.push({
		name: "Alumni",
		query: {
			search: alumni.full_name,
			profile: alumni.name,
		},
	})
}

const performSearch = () => {
	isDropdownOpen.value = false
	const q = searchQuery.value.trim()
	if (q) {
		router.push({ name: "Alumni", query: { search: q } })
	} else {
		router.push({ name: "Alumni" })
	}
}
</script>
