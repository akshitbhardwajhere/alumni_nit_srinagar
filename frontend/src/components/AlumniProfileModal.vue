<template>
	<div
		v-if="alumni"
		class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs transition-opacity"
		@click.self="$emit('close')"
	>
		<div class="bg-white rounded-2xl max-w-lg w-full overflow-hidden shadow-2xl border border-gray-100 transform transition-all text-left">
			<!-- Modal Header -->
			<div class="bg-[#17345F] p-6 text-white relative">
				<button
					@click="$emit('close')"
					class="absolute top-4 right-4 text-gray-300 hover:text-white p-1 rounded-full hover:bg-white/10 transition-colors"
					aria-label="Close modal"
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</button>

				<div class="flex items-center gap-4">
					<img
						v-if="alumni.image && !hasImageError"
						:src="alumni.image"
						:alt="alumni.full_name"
						class="w-20 h-20 rounded-full object-cover border-4 border-[#D5A33D] shadow-md"
						@error="hasImageError = true"
					/>
					<div
						v-else
						class="w-20 h-20 rounded-full bg-[#D5A33D] text-[#17345F] flex items-center justify-center font-bold text-2xl border-4 border-white shadow-md"
					>
						{{ getInitials(alumni.full_name) }}
					</div>
					<div>
						<div class="flex items-center gap-2">
							<span class="text-xs font-semibold text-[#F2B633] uppercase tracking-wider">NIT Srinagar Alumni Profile</span>
							<span v-if="alumni.featured" class="text-[10px] bg-amber-400 text-gray-950 font-bold px-2 py-0.5 rounded-full">★ Hotshot</span>
						</div>
						<h3 class="text-2xl font-bold font-exo-2 text-white">{{ alumni.full_name }}</h3>
						<p v-if="alumni.designation || alumni.company_organization" class="text-xs text-gray-200 mt-0.5 font-medium">
							{{ alumni.designation }} <span v-if="alumni.designation && alumni.company_organization">at</span> {{ alumni.company_organization }}
						</p>
						<p class="text-xs text-gray-300 mt-0.5">Batch of {{ alumni.batchyear }}</p>
					</div>
				</div>
			</div>

			<!-- Modal Body -->
			<div class="p-6 space-y-4">
				<div class="bg-gray-50 rounded-xl p-4 border border-gray-100 space-y-3">
					<div>
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Department / Branch</span>
						<span class="text-sm font-semibold text-gray-800">{{ alumni.branchdepartment }}</span>
					</div>
					<div class="pt-2 border-t border-gray-200/60">
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Graduation Batch</span>
						<span class="text-sm font-semibold text-gray-800">{{ alumni.batchyear }}</span>
					</div>
					<div v-if="alumni.designation" class="pt-2 border-t border-gray-200/60">
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Designation / Role</span>
						<span class="text-sm font-semibold text-gray-800">{{ alumni.designation }}</span>
					</div>
					<div v-if="alumni.company_organization" class="pt-2 border-t border-gray-200/60">
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Company / Organization</span>
						<span class="text-sm font-semibold text-gray-800">{{ alumni.company_organization }}</span>
					</div>
					<div class="pt-2 border-t border-gray-200/60">
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Email Address</span>
						<a :href="`mailto:${alumni.email_address}`" class="text-sm font-semibold text-blue-600 hover:underline">
							{{ alumni.email_address }}
						</a>
					</div>
					<div v-if="alumni.phone_number" class="pt-2 border-t border-gray-200/60">
						<span class="text-xs text-gray-400 font-semibold uppercase tracking-wider block">Phone Number</span>
						<span class="text-sm font-semibold text-gray-800">{{ alumni.phone_number }}</span>
					</div>
				</div>

				<div class="pt-2 flex gap-3">
					<a :href="`mailto:${alumni.email_address}`" class="flex-1">
						<Button
							variant="solid"
							theme="blue"
							size="md"
							class="w-full bg-[#17345F] hover:bg-[#12284c] text-white font-bold py-2.5 justify-center"
						>
							<template #prefix>
								<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
								</svg>
							</template>
							Send Email
						</Button>
					</a>
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
	</div>
</template>

<script setup>
import { Button } from "frappe-ui"
import { ref } from "vue"
import { getInitials } from "../utils"

defineProps({
	alumni: {
		type: Object,
		default: null,
	},
})

defineEmits(["close"])

const hasImageError = ref(false)
</script>
