<template>
	<footer class="mt-auto bg-[#17345F] text-gray-300 border-t-8 border-[#D5A33D] font-sans">
		<div class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
				<!-- Brand & Institution Info -->
				<div class="space-y-4">
					<div class="flex items-center gap-3.5">
						<div class="h-16 w-16 rounded-full border-2 border-[#D5A33D] bg-white p-0.5 shadow-md overflow-hidden flex-shrink-0">
							<img src="../assets/nits.jpeg" alt="NIT Srinagar Logo" class="w-full h-full object-cover" />
						</div>
						<div>
							<h3 class="text-2xl font-exo-2 font-bold text-white tracking-wide leading-tight">
								Dean Alumni &amp;
							</h3>
							<p class="text-base font-semibold text-[#F2B633] mt-0.5">International Affairs</p>
						</div>
					</div>

					<p class="text-sm text-gray-200 leading-relaxed font-normal">
						National Institute of Technology Srinagar (NIT Srinagar), Hazratbal, Srinagar, Jammu &amp; Kashmir — 190006.
					</p>

					<div class="flex items-center gap-3 pt-1">
						<a
							href="https://nitsri.ac.in"
							target="_blank"
							rel="noopener noreferrer"
							class="text-sm font-semibold text-white hover:text-[#F2B633] underline transition-colors"
						>
							nitsri.ac.in →
						</a>
					</div>
				</div>

				<!-- Quick Links -->
				<div>
					<span class="text-sm font-bold uppercase tracking-wider text-[#F2B633]">Quick Links</span>
					<ul class="mt-4 space-y-2.5 text-sm font-medium">
						<li>
							<router-link to="/" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Home
							</router-link>
						</li>
						<li>
							<router-link :to="{ name: 'Alumni' }" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Our Alumni Directory
							</router-link>
						</li>
						<li>
							<router-link :to="{ name: 'NewsSpotlight' }" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> News &amp; Spotlight
							</router-link>
						</li>
						<li>
							<router-link :to="{ name: 'RegisterAlumni' }" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Register as Alumni
							</router-link>
						</li>
						<li>
							<a href="https://nitsri.ac.in/Pages/AboutUs.aspx" target="_blank" rel="noopener noreferrer" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> About Institute
							</a>
						</li>
					</ul>
				</div>

				<!-- Initiatives & Programs -->
				<div>
					<span class="text-sm font-bold uppercase tracking-wider text-[#F2B633]">Alumni Initiatives</span>
					<ul class="mt-4 space-y-2.5 text-sm font-medium">
						<li>
							<router-link :to="{ name: 'NewsSpotlight' }" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Annual SANGAM Meet
							</router-link>
						</li>
						<li>
							<a href="#" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Global Chapters
							</a>
						</li>
						<li>
							<a href="#" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Student Mentorship
							</a>
						</li>
						<li>
							<a href="#" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Giving Back &amp; Aid
							</a>
						</li>
						<li>
							<a href="#" class="hover:text-white transition-colors flex items-center gap-1.5">
								<span class="text-[#D5A33D]">›</span> Alumni Innovation Center
							</a>
						</li>
					</ul>
				</div>

				<!-- Official Contact Information -->
				<div>
					<span class="text-sm font-bold uppercase tracking-wider text-[#F2B633]">Contact Office</span>
					<ul class="mt-4 space-y-4 text-sm sm:text-base leading-relaxed font-medium">
						<li class="flex items-start gap-3">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#D5A33D] flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
							</svg>
							<span class="text-gray-200">Hazratbal, Srinagar, J&amp;K - 190006, India</span>
						</li>
						<li class="flex items-center gap-3">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#D5A33D] flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
							</svg>
							<a href="mailto:alumni@nitsri.ac.in" class="hover:underline text-white font-semibold">alumni@nitsri.ac.in</a>
						</li>
						<li class="flex items-center gap-3">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#D5A33D] flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
							</svg>
							<span class="text-white font-semibold">+91 (194) 242-2032</span>
						</li>
					</ul>
				</div>
			</div>

			<!-- Bottom Copyright Bar -->
			<div class="mt-12 pt-8 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-400">
				<div>
					&copy; 2026 National Institute of Technology Srinagar. All rights reserved.
				</div>
				<div>
					Designed &amp; Developed by
					<a
						target="_blank"
						rel="noopener noreferrer"
						href="https://foss.nitsri.ac.in/"
						class="font-bold text-[#F2B633] hover:underline"
					>
						FOSS Club, NIT Srinagar
					</a>
				</div>
			</div>
		</div>
	</footer>
</template>

<script setup>
</script>
