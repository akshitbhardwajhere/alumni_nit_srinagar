<template>
	<div
		v-if="isOpen"
		class="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/60 backdrop-blur-xs transition-opacity"
		@click.self="$emit('close')"
	>
		<div class="bg-white rounded-t-2xl sm:rounded-2xl max-w-md w-full overflow-hidden shadow-2xl border border-gray-100 transform transition-all text-left flex flex-col max-h-[85vh]">
			<!-- Modal Header -->
			<div class="bg-[#17345F] p-4 text-white flex items-center justify-between flex-shrink-0">
				<div>
					<h3 class="text-lg font-bold font-exo-2 text-white">Select Department</h3>
					<p class="text-xs text-gray-300">Filter alumni directory by department</p>
				</div>
				<button
					type="button"
					@click="$emit('close')"
					class="text-gray-300 hover:text-white p-1 rounded-full hover:bg-white/10 transition-colors"
					aria-label="Close modal"
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</button>
			</div>

			<!-- Options List -->
			<div class="p-4 overflow-y-auto divide-y divide-gray-100 flex-grow space-y-1">
				<button
					type="button"
					@click="selectBranch('')"
					:class="[
						'w-full text-left py-3 px-3 rounded-lg flex items-center justify-between text-sm font-semibold transition-colors',
						selectedBranch === '' ? 'bg-blue-50 text-[#17345F] border border-blue-200' : 'hover:bg-gray-50 text-gray-700'
					]"
				>
					<span>All Departments</span>
					<svg v-if="selectedBranch === ''" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#17345F]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
					</svg>
				</button>

				<button
					v-for="b in branches"
					:key="b"
					type="button"
					@click="selectBranch(b)"
					:class="[
						'w-full text-left py-3 px-3 rounded-lg flex items-center justify-between text-sm font-semibold transition-colors',
						selectedBranch === b ? 'bg-blue-50 text-[#17345F] border border-blue-200' : 'hover:bg-gray-50 text-gray-700'
					]"
				>
					<span>{{ b }}</span>
					<svg v-if="selectedBranch === b" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#17345F]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
					</svg>
				</button>
			</div>

			<!-- Modal Footer Buttons -->
			<div class="p-4 bg-gray-50 border-t border-gray-100 flex gap-2 flex-shrink-0">
				<Button
					variant="subtle"
					theme="gray"
					size="md"
					class="flex-1 justify-center"
					@click="selectBranch('')"
				>
					Clear Filter
				</Button>
				<Button
					variant="solid"
					theme="blue"
					size="md"
					class="flex-1 justify-center bg-[#17345F]"
					@click="$emit('close')"
				>
					Done
				</Button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { Button } from "frappe-ui"

defineProps({
	isOpen: {
		type: Boolean,
		default: false,
	},
	selectedBranch: {
		type: String,
		default: "",
	},
	branches: {
		type: Array,
		default: () => [],
	},
})

const emit = defineEmits(["select", "close"])

const selectBranch = (branch) => {
	emit("select", branch)
	emit("close")
}
</script>
