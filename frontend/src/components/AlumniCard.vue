<template>
	<div
		class="bg-white rounded-xl border border-gray-200 shadow-sm hover:shadow-lg hover:border-gray-300 transition-all duration-300 flex flex-col overflow-hidden group relative"
	>
		<!-- Card Header Banner -->
		<div
			:class="[
				'h-2',
				alumni.featured
					? 'bg-gradient-to-r from-[#D5A33D] via-amber-400 to-amber-600'
					: 'bg-gradient-to-r from-[#17345F] to-[#D5A33D]',
			]"
		></div>

		<div class="p-6 flex flex-col flex-grow">
			<!-- Featured Badge -->
			<div v-if="alumni.featured" class="absolute top-4 right-4">
				<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-300 shadow-xs">
					★ Featured
				</span>
			</div>

			<div class="flex items-start gap-4">
				<!-- Profile Image or Initial Avatar -->
				<div class="relative flex-shrink-0">
					<img
						v-if="alumni.image && !hasImageError"
						:src="alumni.image"
						:alt="alumni.full_name"
						class="w-16 h-16 rounded-full object-cover border-2 border-white shadow-md group-hover:scale-105 transition-transform"
						@error="hasImageError = true"
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

			<!-- Card Footer Button -->
			<div class="mt-5 pt-3">
				<Button
					variant="outline"
					theme="gray"
					size="sm"
					class="w-full justify-center font-semibold"
					@click="$emit('select', alumni)"
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
</template>

<script setup>
import { Button } from "frappe-ui"
import { ref } from "vue"
import { getInitials } from "../utils"

defineProps({
	alumni: {
		type: Object,
		required: true,
	},
})

defineEmits(["select"])

const hasImageError = ref(false)
</script>
