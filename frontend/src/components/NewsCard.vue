<template>
	<div class="bg-white rounded-xl overflow-hidden shadow-md border border-gray-200 hover:shadow-xl transition-all duration-300 flex flex-col h-full group relative">
		<!-- Cover Image or Category Fallback Header -->
		<div class="h-48 bg-[#17345F] relative overflow-hidden flex items-center justify-center">
			<img
				v-if="coverImage"
				:src="coverImage"
				:alt="title"
				class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
			/>
			<div v-else class="w-full h-full bg-gradient-to-br from-[#17345F] to-[#244c85] p-6 flex flex-col items-center justify-center text-center">
				<span class="text-xs font-semibold text-[#F2B633] uppercase tracking-widest mb-1">{{ category || tag }}</span>
				<span class="text-xl font-bold font-exo-2 text-white/90 leading-tight truncate max-w-full px-2">{{ title }}</span>
			</div>

			<!-- Hot News Badge -->
			<div v-if="isHotNews" class="absolute top-3 right-3">
				<span class="px-2.5 py-1 text-[11px] font-extrabold rounded-full bg-amber-400 text-gray-950 shadow-md border border-amber-300 flex items-center gap-1">
					★ Hot News
				</span>
			</div>
		</div>

		<!-- Body -->
		<div class="p-6 flex-grow flex flex-col">
			<div class="flex items-center justify-between gap-2 mb-2">
				<span class="text-xs font-bold text-[#D5A33D] uppercase tracking-wider">{{ category || tag }}</span>
				<span v-if="date" class="text-xs font-medium text-gray-400">{{ date }}</span>
			</div>

			<h3 class="text-lg font-bold text-gray-900 group-hover:text-[#17345F] transition-colors leading-snug line-clamp-2">
				{{ title }}
			</h3>

			<p class="text-sm text-gray-600 mt-3 flex-grow leading-relaxed line-clamp-3">
				{{ description }}
			</p>

			<div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
				<button
					type="button"
					@click="$emit('read', newsItem)"
					class="text-xs font-bold text-[#17345F] hover:text-[#D5A33D] flex items-center gap-1 transition-colors group-hover:translate-x-0.5"
				>
					<span>Read Story</span>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
					</svg>
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
defineProps({
	newsItem: {
		type: Object,
		default: () => ({}),
	},
	category: {
		type: String,
		default: "News",
	},
	tag: {
		type: String,
		default: "Spotlight",
	},
	title: {
		type: String,
		required: true,
	},
	description: {
		type: String,
		required: true,
	},
	date: {
		type: String,
		default: "",
	},
	coverImage: {
		type: String,
		default: "",
	},
	isHotNews: {
		type: Boolean,
		default: false,
	},
})

defineEmits(["read"])
</script>
