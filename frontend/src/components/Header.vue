<template>
	<header class="w-full font-sans">
		<div class="bg-white border-b text-[11px] sm:text-[13px] text-gray-700">
			<div
				class="mx-auto max-w-7xl flex flex-wrap items-center justify-center gap-2 py-1.5 px-4 text-center"
			>
				<img src="/nits.jpeg" alt="NITS Logo" class="h-4 sm:h-4.5" />

				<span>An official Alumni portal of NIT Srinagar</span>

				<a
					href="https://nitsri.ac.in/"
					class="text-blue-700 hover:underline flex items-center gap-1 font-medium"
				>
					Here's how you know
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-3 w-3"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2.5"
							d="M19 9l-7 7-7-7"
						/>
					</svg>
				</a>
			</div>
		</div>

		<!-- Main Blue Header -->
		<div class="bg-[#17345F] border-b-4 border-[#D5A33D] py-4 lg:py-5">
			<div
				class="mx-auto max-w-7xl flex flex-col lg:flex-row lg:items-center lg:justify-between px-4 sm:px-6 gap-4 lg:gap-0"
			>
				<!-- Top Row on Mobile: Logo/Title + Hamburger Button -->
				<div class="flex items-center justify-between w-full lg:w-auto">
					<!-- Logo & Title -->
					<router-link to="/" class="flex items-center gap-3 sm:gap-5">
						<!-- Seal -->
						<div
							class="h-14 w-14 sm:h-20 sm:w-20 lg:h-24 lg:w-24 rounded-full border-2 border-[#D5A33D] bg-white flex items-center justify-center flex-shrink-0 shadow-sm overflow-hidden"
						>
							<img
								src="../assets/nits.jpeg"
								alt="NIT Srinagar Seal"
								class="h-full w-full object-cover"
							/>
						</div>

						<!-- Title -->
						<div class="text-white leading-none">
							<p
								class="text-2xl sm:text-4xl lg:text-[40px] font-exo-2 font-bold tracking-wide text-gray-200"
							>
								Dean Alumni &amp;
							</p>
							<h1
								class="text-sm sm:text-xl lg:text-3xl font-exo-2 tracking-wide mt-0.5 sm:mt-1"
							>
								International Affairs
							</h1>
						</div>
					</router-link>

					<!-- Mobile Menu Button (Only visible on < lg) -->
					<button
						@click="isMobileMenuOpen = !isMobileMenuOpen"
						class="lg:hidden flex flex-col items-center justify-center focus:outline-none p-1.5 rounded hover:bg-white/10 transition-colors"
						aria-label="Toggle menu"
					>
						<template v-if="!isMobileMenuOpen">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-8 w-8 text-[#F2B633]"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2.5"
									d="M4 6h16M4 12h16M4 18h16"
								/>
							</svg>
							<span
								class="text-[10px] text-white font-bold uppercase tracking-wider mt-0.5"
								>Menu</span
							>
						</template>
						<template v-else>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-8 w-8 text-[#F2B633]"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2.5"
									d="M6 18L18 6M6 6l12 12"
								/>
							</svg>
							<span
								class="text-[10px] text-white font-bold uppercase tracking-wider mt-0.5"
								>Close</span
							>
						</template>
					</button>
				</div>

				<!-- Desktop Right: Utility Links & Search Bar (Only visible on lg) -->
				<div class="hidden lg:flex flex-col items-end gap-4">
					<!-- Top Links -->
					<div class="flex items-center gap-4 text-white text-[15px] font-medium">
						<a href="#" class="hover:underline">Find Help</a>
						<span class="opacity-40">|</span>
						<a href="#" class="hover:underline">Contact Us</a>
					</div>

					<!-- Header Live Search Component (Desktop) -->
					<HeaderSearch
						inputClass="w-72 px-4 py-2.5 text-[15px] rounded-l bg-white outline-none text-gray-800 focus:ring-2 focus:ring-[#D5A33D] transition-all"
						placeholder="Search by name and batch..."
						@selectAlumni="onSelectAlumni"
					/>
				</div>

				<!-- Header Live Search Component (Mobile, visible on < lg) -->
				<div class="lg:hidden w-full mt-2">
					<HeaderSearch
						inputClass="w-full px-4 py-2.5 text-base rounded-l bg-white outline-none text-gray-800 focus:ring-2 focus:ring-[#D5A33D]"
						placeholder="Search by name and batch..."
						@selectAlumni="onSelectAlumni"
					/>
				</div>
			</div>
		</div>

		<!-- Bottom Navigation Bar (Desktop version only) -->
		<nav class="hidden lg:block bg-[#2C2A26] text-white">
			<div
				class="mx-auto max-w-7xl flex items-center justify-center gap-10 py-4 text-base font-semibold tracking-wide"
			>
				<router-link
					to="/"
					class="hover:text-[#F2B633] flex items-center gap-1 transition-colors"
				>
					Home
				</router-link>
				<a
					href="https://nitsri.ac.in/Pages/AboutUs.aspx"
					target="_blank"
					rel="noopener noreferrer"
					class="hover:text-[#F2B633] flex items-center gap-1 transition-colors"
				>
					About Us
				</a>

				<router-link
					:to="{ name: 'Alumni' }"
					class="hover:text-[#F2B633] flex items-center gap-1 transition-colors"
				>
					Our Alumni
				</router-link>

				<router-link
					:to="{ name: 'NewsSpotlight' }"
					class="hover:text-[#F2B633] flex items-center gap-1 transition-colors"
				>
					News &amp; Spotlight
				</router-link>
			</div>
		</nav>

		<!-- Mobile Navigation Menu Drawer -->
		<nav
			v-show="isMobileMenuOpen"
			class="lg:hidden bg-[#2C2A26] text-white border-t border-[#D5A33D]/20 divide-y divide-[#3D3A35]"
		>
			<router-link
				to="/"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
				@click="isMobileMenuOpen = false"
			>
				<span class="font-semibold text-base">Home</span>
			</router-link>

			<a
				href="https://nitsri.ac.in/Pages/AboutUs.aspx"
				target="_blank"
				rel="noopener noreferrer"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
			>
				<span class="font-semibold text-base">About Us</span>
			</a>

			<router-link
				:to="{ name: 'Alumni' }"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
				@click="isMobileMenuOpen = false"
			>
				<span class="font-semibold text-base">Our Alumni</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-4 w-4 text-gray-400"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2.5"
						d="M9 5l7 7-7 7"
					/>
				</svg>
			</router-link>

			<router-link
				:to="{ name: 'NewsSpotlight' }"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
				@click="isMobileMenuOpen = false"
			>
				<span class="font-semibold text-base">News &amp; Spotlight</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-4 w-4 text-gray-400"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2.5"
						d="M9 5l7 7-7 7"
					/>
				</svg>
			</router-link>

			<!-- <router-link
				:to="{ name: 'RegisterAlumni' }"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
				@click="isMobileMenuOpen = false"
			>
				<span class="font-semibold text-base">Register Alumni</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-4 w-4 text-gray-400"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2.5"
						d="M9 5l7 7-7 7"
					/>
				</svg>
			</router-link> -->

			<a
				href="#"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors bg-[#23211F]"
			>
				<span class="text-base text-gray-200">Find Help</span>
			</a>

			<a
				href="#"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors bg-[#23211F]"
			>
				<span class="text-base text-gray-200">Contact Us</span>
			</a>
		</nav>

		<!-- Alumni Profile Modal Component -->
		<AlumniProfileModal
			:alumni="selectedAlumni"
			@close="selectedAlumni = null"
		/>
	</header>
</template>

<script setup>
import { ref } from "vue"
import AlumniProfileModal from "./AlumniProfileModal.vue"
import HeaderSearch from "./HeaderSearch.vue"

const isMobileMenuOpen = ref(false)
const selectedAlumni = ref(null)

const onSelectAlumni = (alumni) => {
	selectedAlumni.value = alumni
}
</script>
