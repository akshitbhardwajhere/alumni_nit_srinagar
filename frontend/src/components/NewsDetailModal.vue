<template>
	<div
		v-if="news"
		class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs transition-opacity"
		@click.self="$emit('close')"
	>
		<div class="bg-white rounded-2xl max-w-2xl w-full overflow-hidden shadow-2xl border border-gray-100 transform transition-all text-left max-h-[90vh] flex flex-col">
			<!-- Modal Header Banner -->
			<div class="bg-[#17345F] p-6 text-white relative flex-shrink-0">
				<button
					@click="$emit('close')"
					class="absolute top-4 right-4 text-gray-300 hover:text-white p-1 rounded-full hover:bg-white/10 transition-colors"
					aria-label="Close modal"
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</button>

				<div class="flex items-center gap-2 mb-2">
					<span class="text-xs font-bold text-[#F2B633] uppercase tracking-wider">{{ news.category || 'News' }}</span>
					<span v-if="news.is_hot_news" class="text-[10px] bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded-full">★ Hot News</span>
				</div>
				<h2 class="text-2xl font-bold font-exo-2 text-white leading-tight">{{ news.title }}</h2>
				<p v-if="news.published_date" class="text-xs text-gray-300 mt-1">Published on {{ news.published_date }}</p>
			</div>

			<!-- Cover Image if present -->
			<div v-if="news.cover_image" class="h-64 w-full bg-gray-900 overflow-hidden flex-shrink-0">
				<img :src="news.cover_image" :alt="news.title" class="w-full h-full object-cover" />
			</div>

			<!-- Modal Body (Scrollable) -->
			<div class="p-6 overflow-y-auto space-y-4 flex-grow">
				<div class="bg-amber-50/70 border-l-4 border-[#D5A33D] p-4 rounded-r-lg">
					<p class="text-sm font-medium text-gray-800 leading-relaxed italic">
						{{ news.summary }}
					</p>
				</div>

				<div v-if="news.content" class="prose max-w-none text-gray-700 text-sm leading-relaxed space-y-3 pt-2" v-html="news.content"></div>
				<div v-else class="text-sm text-gray-600 leading-relaxed pt-2">
					{{ news.summary }}
				</div>
			</div>

			<!-- Modal Footer -->
			<div class="p-4 bg-gray-50 border-t border-gray-100 flex justify-end flex-shrink-0">
				<Button
					variant="subtle"
					theme="gray"
					size="md"
					@click="$emit('close')"
				>
					Close
				</Button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { Button } from "frappe-ui"

defineProps({
	news: {
		type: Object,
		default: null,
	},
})

defineEmits(["close"])
</script>
