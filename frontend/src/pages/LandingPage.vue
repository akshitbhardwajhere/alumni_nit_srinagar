<template>
  <div class="min-h-screen bg-gray-55 font-sans text-gray-900 flex flex-col">

    <!-- Hero Section -->
    <section class="relative w-full min-h-[580px] lg:min-h-[700px] flex items-center justify-center overflow-hidden">
      <!-- Background Image -->
      <div class="absolute inset-0">
        <img
          src="../assets/nit_srinagar_hero.png"
          alt="NIT Srinagar Campus"
          class="w-full h-full object-cover transform scale-105"
        />
        <!-- Deep Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-r from-[#0d203b]/95 via-[#17345f]/85 to-transparent"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-[#17345f]/90 via-transparent to-transparent"></div>
      </div>

      <!-- Hero Content -->
      <div class="relative max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24 z-10 flex flex-col justify-center">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#D5A33D]/25 border border-[#D5A33D]/40 text-[#F2B633] text-xs sm:text-sm font-semibold tracking-wider uppercase mb-6 animate-pulse">
            <span class="w-2 h-2 rounded-full bg-[#F2B633]"></span>
            Official Alumni Portal of NIT Srinagar
          </div>
          
          <h1 class="text-4xl sm:text-5xl lg:text-7xl font-exo-2 font-bold tracking-tight text-white leading-tight">
            SANGAM
          </h1>
          <p class="text-xl sm:text-2xl lg:text-3xl font-geomini font-semibold text-[#F2B633] tracking-wide mt-2">
            Reconnecting the Legacy of NIT Srinagar
          </p>
          
          <p class="mt-6 text-base sm:text-lg text-gray-200 leading-relaxed font-normal max-w-2xl">
            Fostering collaboration, mentorship, and professional growth across generations of graduates. Join the global network and contribute to the alma mater.
          </p>

          <div class="mt-8 flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
            <router-link
              :to="{ name: 'RegisterAlumni' }"
              class="px-8 py-4 bg-[#F2B633] hover:bg-[#D5A33D] text-gray-950 font-bold rounded shadow-lg transition-all duration-300 transform hover:-translate-y-0.5 text-center text-base"
            >
              Register as Alumni
            </router-link>
            <a
              href="#"
              class="px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-bold rounded border border-white/30 backdrop-blur-sm transition-all duration-300 transform hover:-translate-y-0.5 text-center text-base"
            >
              Explore Chapters
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Statistics Section -->
    <section class="relative -mt-16 z-20 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-xl shadow-xl border border-gray-100 p-6 sm:p-10 grid grid-cols-2 lg:grid-cols-4 gap-8 divide-y-2 lg:divide-y-0 lg:divide-x-2 divide-gray-100">
        <div class="flex flex-col items-center justify-center text-center p-2">
          <span class="text-3xl sm:text-5xl font-exo-2 font-extrabold text-[#17345F]">15k+</span>
          <span class="text-xs sm:text-sm font-semibold text-gray-500 uppercase tracking-wider mt-2">Registered Alumni</span>
        </div>
        <div class="flex flex-col items-center justify-center text-center p-2 pt-6 lg:pt-2">
          <span class="text-3xl sm:text-5xl font-exo-2 font-extrabold text-[#17345F]">25+</span>
          <span class="text-xs sm:text-sm font-semibold text-gray-500 uppercase tracking-wider mt-2">Global Chapters</span>
        </div>
        <div class="flex flex-col items-center justify-center text-center p-2 pt-6 lg:pt-2">
          <span class="text-3xl sm:text-5xl font-exo-2 font-extrabold text-[#17345F]">500+</span>
          <span class="text-xs sm:text-sm font-semibold text-gray-500 uppercase tracking-wider mt-2">Student Mentors</span>
        </div>
        <div class="flex flex-col items-center justify-center text-center p-2 pt-6 lg:pt-2">
          <span class="text-3xl sm:text-5xl font-exo-2 font-extrabold text-[#17345F]">12+</span>
          <span class="text-xs sm:text-sm font-semibold text-gray-500 uppercase tracking-wider mt-2">Active Scholarships</span>
        </div>
      </div>
    </section>

    <!-- Core Initiatives -->
    <section class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-exo-2 font-bold text-[#17345F] tracking-tight">
          Our Initiatives
        </h2>
        <div class="w-24 h-1 bg-[#D5A33D] mx-auto mt-4 rounded-full"></div>
        <p class="text-lg text-gray-600 mt-5">
          Empowering our community through structured engagement and support platforms.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Card 1: Directory -->
        <InitiativeCard
          title="Alumni Directory"
          description="Search and reconnect with classmates and alumni globally. Filter by branch, year, location, or industry."
          linkText="Access Directory"
          linkUrl="/alumni"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </template>
        </InitiativeCard>

        <!-- Card 2: Mentorship -->
        <InitiativeCard
          title="Mentorship Program"
          description="Bridge the gap between academia and industry. Share career advice, resume tips, and guide current students."
          linkText="Become a Mentor"
          linkUrl="#"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </template>
        </InitiativeCard>

        <!-- Card 3: Giving Back -->
        <InitiativeCard
          title="Giving Back"
          description="Support scholarships, research projects, and campus expansion plans to enable future students to succeed."
          linkText="Contribute Now"
          linkUrl="#"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </template>
        </InitiativeCard>
      </div>
    </section>

    <!-- News & Spotlight -->
    <section class="bg-gray-100 py-16 sm:py-24">
      <div class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
          <div>
            <h2 class="text-3xl sm:text-4xl font-exo-2 font-bold text-[#17345F] tracking-tight">
              News &amp; Spotlights
            </h2>
            <div class="w-20 h-1 bg-[#D5A33D] mt-4 rounded-full"></div>
          </div>
          <a href="#" class="text-sm font-bold text-[#17345F] hover:text-[#D5A33D] transition-colors mt-4 md:mt-0 flex items-center gap-1">
            View All Updates →
          </a>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <NewsCard
            categoryTitle="SANGAM 2026 Meet"
            tag="Upcoming Event"
            title="Annual Global Alumni Meet 'SANGAM 2026'"
            description="Join us back on campus for three days of reunions, panels, and networking opportunities. Registrations open this Friday."
            date="March 12, 2026"
            linkText="Details"
            linkUrl="#"
          />

          <NewsCard
            categoryTitle="Distinguished Alumnus"
            tag="Spotlight"
            title="Bhat Named CEO of TechCorp Global"
            description="We celebrate our alumnus from the batch of 1998, who has been appointed Chief Executive Officer of TechCorp."
            date="February 28, 2026"
            linkText="Read Interview"
            linkUrl="#"
          />

          <NewsCard
            categoryTitle="Innovation Center"
            tag="Infrastructure"
            title="Inauguration of the Alumni Innovation Center"
            description="The new innovation workspace, fully funded by alumni contributions, is now open for students to brainstorm and build projects."
            date="January 15, 2026"
            linkText="View Gallery"
            linkUrl="#"
          />
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer />

  </div>
</template>

<script setup>
import Footer from "../components/Footer.vue"
import InitiativeCard from "../components/InitiativeCard.vue"
import NewsCard from "../components/NewsCard.vue"
</script>