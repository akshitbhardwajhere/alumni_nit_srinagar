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
					<a href="/" class="flex items-center gap-3 sm:gap-5">
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
								Dean Alumni &
							</p>
							<h1
								class="text-sm sm:text-xl lg:text-3xl font-exo-2 tracking-wide mt-0.5 sm:mt-1"
							>
								International Affairs
							</h1>
						</div>
					</a>

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
						<!-- <a href="#" class="hover:underline">Our Offices</a>
            <span class="opacity-40">|</span> -->
						<a href="#" class="hover:underline">Find Help</a>
						<span class="opacity-40">|</span>
						<a href="#" class="hover:underline">Contact Us</a>
					</div>

					<!-- Search -->
					<div class="flex shadow-sm">
						<input
							type="text"
							placeholder="Search"
							class="w-72 px-4 py-2.5 text-[15px] rounded-l bg-white outline-none text-gray-800 focus:ring-2 focus:ring-[#D5A33D] transition-all"
						/>
						<button
							class="bg-[#F2B633] px-5 rounded-r hover:bg-[#D5A33D] text-gray-900 font-bold transition-colors flex items-center justify-center"
							aria-label="Search"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2.5"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								/>
							</svg>
						</button>
					</div>
				</div>

				<!-- Mobile Search Bar (Only visible on < lg, inline under title block) -->
				<div class="lg:hidden w-full mt-2">
					<div class="flex shadow-sm">
						<input
							type="text"
							placeholder="Search"
							class="w-full px-4 py-2.5 text-base rounded-l bg-white outline-none text-gray-800 focus:ring-2 focus:ring-[#D5A33D]"
						/>
						<button
							class="bg-[#F2B633] px-5 rounded-r hover:bg-[#D5A33D] text-gray-900 font-bold flex items-center justify-center"
							aria-label="Search"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2.5"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								/>
							</svg>
						</button>
					</div>
				</div>
			</div>
		</div>

		<!-- Bottom Navigation Bar (Desktop version only) -->
		<nav class="hidden lg:block bg-[#2C2A26] text-white">
			<div
				class="mx-auto max-w-7xl flex items-center justify-center gap-10 py-4 text-base font-semibold tracking-wide"
			>
				<a
					href="/"
					class="hover:text-[#F2B633] flex items-center gap-1 transition-colors"
				>
					Home
				</a>
				<a href="https://nitsri.ac.in/Pages/AboutUs.aspx" class="hover:text-[#F2B633] flex items-center gap-1 transition-colors">
					About Us
				</a>

				<!-- <a href="#" class="hover:text-[#F2B633] transition-colors">
          Our Work
        </a> -->

				<a href="https://nitsri.ac.in/Pages/DisplayPages.aspx?page=caaqq&ItemID=eaeqa" class="hover:text-[#F2B633] flex items-center gap-1 transition-colors">
					Our Alumni
				</a>

				<!-- <a href="#" class="hover:text-[#F2B633] flex items-center gap-1 transition-colors">
          Resources
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
          </svg>
        </a> -->

				<!-- <a href="#" class="hover:text-[#F2B633] transition-colors">
          Grants
        </a> -->

				<!-- <a href="#" class="hover:text-[#F2B633] flex items-center gap-1 transition-colors">
          Employment
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
          </svg>
        </a> -->
			</div>
		</nav>

		<!-- Mobile Navigation Menu Drawer (Only visible on < lg and when menu open) -->
		<nav
			v-show="isMobileMenuOpen"
			class="lg:hidden bg-[#2C2A26] text-white border-t border-[#D5A33D]/20 divide-y divide-[#3D3A35]"
		>
			<!-- Main Links -->
			<a
				href="#"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
			>
				<span class="font-semibold text-base">About</span>
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
			</a>

			<!-- <a href="#" class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors">
        <span class="font-semibold text-base">Our Work</span>
      </a> -->

			<a
				href="#"
				class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors"
			>
				<span class="font-semibold text-base">News</span>
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
			</a>

			<!-- <a href="#" class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors">
        <span class="font-semibold text-base">Resources</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
        </svg>
      </a> -->

			<!-- <a href="#" class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors">
        <span class="font-semibold text-base">Grants</span>
      </a> -->

			<!-- <a href="#" class="flex items-center justify-between px-5 py-3.5 hover:bg-[#3D3A35] transition-colors">
        <span class="font-semibold text-base">Employment</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
        </svg>
      </a> -->

			<!-- Utility Links appended to the bottom -->
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
	</header>
</template>

<script setup>
import { ref } from "vue"

const isMobileMenuOpen = ref(false)
</script>
