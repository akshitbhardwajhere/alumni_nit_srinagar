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
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
							</svg>
							Updates &amp; Achievers
						</div>
						<h1 class="text-3xl sm:text-4xl lg:text-5xl font-exo-2 font-bold tracking-tight text-white">
							News &amp; Alumni Spotlight
						</h1>
						<p class="mt-3 text-base sm:text-lg text-gray-200 max-w-2xl leading-relaxed">
							Stay updated with the latest institutional announcements, alumni achievements, research milestones, and upcoming global reunion events.
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
						{ label: 'News & Spotlight' }
					]"
				/>
			</div>
			<!-- Controls Bar: Tabs & Search -->
			<div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
				<!-- Category Tabs -->
				<div class="flex flex-wrap items-center gap-2">
					<button
						v-for="cat in categories"
						:key="cat.value"
						@click="selectedCategory = cat.value"
						:class="[
							'px-4 py-2 text-sm font-bold rounded-lg transition-all',
							selectedCategory === cat.value
								? 'bg-[#17345F] text-white shadow-sm'
								: 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
						]"
					>
						{{ cat.label }}
					</button>
				</div>

				<!-- Search Bar -->
				<div class="w-full md:w-72">
					<TextInput
						v-model="searchQuery"
						placeholder="Search news & spotlights..."
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

			<!-- Error Alert State -->
			<div
				v-if="newsResource.error"
				class="p-4 bg-red-50 border-l-4 border-red-500 rounded-r-lg text-red-700 text-sm mb-6 flex items-center justify-between"
			>
				<span>{{ formatErrorMessage(newsResource.error, "Unable to load news & spotlight stories at this time. Please try again later.") }}</span>
				<Button size="sm" variant="subtle" theme="gray" @click="newsResource.reload()">Retry</Button>
			</div>

			<!-- Loading State -->
			<div v-if="newsResource.loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
				<div v-for="i in 6" :key="i" class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm animate-pulse space-y-4">
					<div class="h-48 bg-gray-200 rounded-lg w-full"></div>
					<div class="h-4 bg-gray-200 rounded w-3/4"></div>
					<div class="h-3 bg-gray-200 rounded w-full"></div>
					<div class="h-3 bg-gray-200 rounded w-2/3"></div>
				</div>
			</div>

			<!-- News Grid -->
			<div v-else-if="filteredNews.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
				<NewsCard
					v-for="item in filteredNews"
					:key="item.name"
					:newsItem="item"
					:category="item.category"
					:tag="item.category || 'News'"
					:title="item.title"
					:description="item.summary"
					:date="item.published_date"
					:coverImage="item.cover_image"
					:isHotNews="!!item.is_hot_news"
					@read="selectedNews = $event"
				/>
			</div>

			<!-- Empty State -->
			<div v-else class="bg-white rounded-2xl p-12 text-center border border-gray-200 max-w-xl mx-auto my-8">
				<div class="w-16 h-16 bg-blue-50 text-[#17345F] rounded-full flex items-center justify-center mx-auto mb-4">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 01-2-2h10a2 2 0 01-2 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
					</svg>
				</div>
				<h3 class="text-xl font-bold text-gray-900">No News or Spotlight Found</h3>
				<p class="text-gray-500 mt-2 text-sm leading-relaxed">
					No published articles match your selected filter or search terms. Admins can publish news from the Frappe Desk dashboard.
				</p>
				<div class="mt-6 flex justify-center">
					<Button variant="solid" theme="blue" size="md" class="bg-[#17345F]" @click="resetFilters">
						Reset Filters
					</Button>
				</div>
			</div>
		</section>

		<!-- Detail Modal -->
		<NewsDetailModal :news="selectedNews" @close="selectedNews = null" />

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup>
import { Breadcrumbs, Button, TextInput, createListResource } from "frappe-ui"
import { computed, onMounted, ref } from "vue"
import Footer from "../components/Footer.vue"
import NewsCard from "../components/NewsCard.vue"
import NewsDetailModal from "../components/NewsDetailModal.vue"
import { NEWS_CATEGORIES, formatErrorMessage } from "../utils"

const searchQuery = ref("")
const selectedCategory = ref("all")
const selectedNews = ref(null)

onMounted(() => {
	window.scrollTo(0, 0)
})

const categories = NEWS_CATEGORIES

// Query backend News doctype where published = 1
const newsResource = createListResource({
	doctype: "News",
	url: "alumni_nit_srinagar.api.get_news_list",
	fields: [
		"name",
		"title",
		"category",
		"published_date",
		"is_hot_news",
		"published",
		"cover_image",
		"summary",
		"content",
	],
	filters: [["published", "=", 1]],
	orderBy: "published_date desc",
	auto: true,
	pageLength: 100,
})

const allNews = computed(() => newsResource.data || [])

const filteredNews = computed(() => {
	const q = searchQuery.value.trim().toLowerCase()
	return allNews.value.filter((item) => {
		const matchesSearch =
			!q ||
			item.title?.toLowerCase().includes(q) ||
			item.summary?.toLowerCase().includes(q) ||
			item.category?.toLowerCase().includes(q)

		const matchesCategory =
			selectedCategory.value === "all"
				? true
				: selectedCategory.value === "hot"
					? item.is_hot_news === 1
					: item.category === selectedCategory.value

		return matchesSearch && matchesCategory
	})
})

const resetFilters = () => {
	searchQuery.value = ""
	selectedCategory.value = "all"
}
</script>
