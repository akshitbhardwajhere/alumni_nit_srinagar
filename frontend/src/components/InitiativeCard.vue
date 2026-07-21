<template>
  <div class="bg-white rounded-xl shadow-md border border-gray-100 p-8 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col h-full">
    <div class="w-12 h-12 rounded-lg bg-[#17345F]/10 flex items-center justify-center text-[#17345F] mb-6">
      <slot name="icon"></slot>
    </div>
    <h3 class="text-xl font-bold text-[#17345F]">{{ title }}</h3>
    <p class="text-gray-600 mt-4 leading-relaxed flex-grow">
      {{ description }}
    </p>
    <a :href="linkUrl" class="inline-flex items-center gap-1.5 text-sm font-bold text-[#17345F] hover:text-[#D5A33D] transition-colors mt-6">
      {{ linkText }} →
    </a>
  </div>
</template>

<script setup>
defineProps({
	title: {
		type: String,
		required: true,
	},
	description: {
		type: String,
		required: true,
	},
	linkText: {
		type: String,
		default: "Learn More",
	},
	linkUrl: {
		type: String,
		default: "#",
	},
})
</script>
