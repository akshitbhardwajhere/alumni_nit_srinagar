<template>
	<div
		class="bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-xl hover:border-blue-200 transition-all duration-300 flex flex-col overflow-hidden group relative"
	>
		<!-- Card Top Accent Banner -->
		<div class="h-2.5 bg-gradient-to-r from-[#17345F] via-[#255294] to-[#D5A33D]"></div>

		<div class="p-6 flex flex-col flex-grow items-center text-center">
			<!-- Position Tag -->
			<div class="mb-4">
				<span
					class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-[#17345F]/10 text-[#17345F] border border-[#17345F]/20 uppercase tracking-wider shadow-2xs"
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-[#D5A33D]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
					</svg>
					{{ member.position || 'Committee Member' }}
				</span>
			</div>

			<!-- Image Container / Placeholder Image -->
			<div class="relative mb-5 flex-shrink-0">
				<img
					v-if="member.photo && !hasImageError"
					:src="member.photo"
					:alt="fullNameWithTitle"
					class="w-28 h-28 rounded-full object-cover border-4 border-white shadow-lg group-hover:scale-105 transition-transform duration-300"
					@error="hasImageError = true"
				/>
				<!-- Placeholder Graphic for members with no image -->
				<div
					v-else
					class="w-28 h-28 rounded-full bg-gradient-to-br from-slate-100 via-gray-200 to-slate-300 text-[#17345F] flex flex-col items-center justify-center border-4 border-white shadow-lg relative overflow-hidden group-hover:scale-105 transition-transform duration-300"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="w-16 h-16 text-gray-400 mt-2"
						fill="currentColor"
						viewBox="0 0 24 24"
					>
						<path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
					</svg>
					<span v-if="initials" class="absolute bottom-2 text-xs font-bold bg-[#17345F] text-white px-2 py-0.5 rounded-full shadow-xs">
						{{ initials }}
					</span>
				</div>
			</div>

			<!-- Member Name -->
			<h3 class="text-xl font-bold text-gray-900 group-hover:text-[#17345F] transition-colors leading-tight">
				{{ fullNameWithTitle }}
			</h3>

			<!-- Branch & Department -->
			<p v-if="member.branchdepartment" class="text-xs font-medium text-gray-600 mt-2 line-clamp-2">
				{{ member.branchdepartment }}
			</p>

			<!-- Degree Badge -->
			<div v-if="member.degree" class="mt-2.5">
				<span class="inline-block px-2.5 py-0.5 bg-gray-100 text-gray-700 text-xs font-medium rounded-md border border-gray-200">
					{{ member.degree }}
				</span>
			</div>

			<!-- Batch Mention (ONLY if batch exists and is non-empty) -->
			<div
				v-if="hasBatch"
				class="mt-4 pt-3 border-t border-gray-100 w-full flex items-center justify-center gap-1.5 text-xs font-bold text-[#D5A33D]"
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
				</svg>
				<span>Batch: {{ member.batch }}</span>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, ref, watch } from "vue"
import { getInitials } from "../utils"

const props = defineProps({
	member: {
		type: Object,
		required: true,
	},
})

const hasImageError = ref(false)

// Reset image error state when photo property changes
watch(
	() => props.member.photo,
	() => {
		hasImageError.value = false
	},
)

const fullNameWithTitle = computed(() => {
	const title = props.member.title ? `${props.member.title.trim()} ` : ""
	const name = props.member.full_name || ""
	return `${title}${name}`.trim()
})

const initials = computed(() => {
	return getInitials(props.member.full_name)
})

// Check if member has a valid, non-empty batch string
const hasBatch = computed(() => {
	return Boolean(
		props.member.batch && String(props.member.batch).trim().length > 0,
	)
})
</script>
