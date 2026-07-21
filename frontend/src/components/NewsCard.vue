<template>
  <div class="bg-white rounded-xl overflow-hidden shadow-md border border-gray-100 hover:shadow-lg transition-all duration-300 flex flex-col h-full">
    <div class="h-48 bg-[#17345F]/5 flex items-center justify-center p-6 border-b border-gray-100">
      <span class="text-lg font-bold text-[#17345F]/40 font-serif">{{ categoryTitle }}</span>
    </div>
    <div class="p-6 flex-grow flex flex-col">
      <span class="text-xs font-semibold text-[#D5A33D] uppercase tracking-wider">{{ tag }}</span>
      <h3 class="text-lg font-bold text-gray-900 mt-2 leading-snug">
        {{ title }}
      </h3>
      <p class="text-sm text-gray-600 mt-3 flex-grow leading-relaxed">
        {{ description }}
      </p>
      <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between text-xs text-gray-500">
        <span>{{ date }}</span>
        <a :href="linkUrl" class="font-bold text-[#17345F] hover:underline cursor-pointer">
          {{ linkText }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
	categoryTitle: {
		type: String,
		required: true,
	},
	tag: {
		type: String,
		required: true,
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
		required: true,
	},
	linkText: {
		type: String,
		default: "Details",
	},
	linkUrl: {
		type: String,
		default: "#",
	},
})
</script>
