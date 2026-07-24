import { userResource } from "@/data/user"
import {
	createRouter,
	createWebHashHistory,
	createWebHistory,
} from "vue-router"
import { session } from "./data/session"

const routes = [
	{
		path: "/",
		name: "HomePage",
		component: () => import("@/pages/LandingPage.vue"),
	},
	// {
	// 	path: "/home",
	// 	name: "LandingPage",
	// 	component: () => import("@/pages/LandingPage.vue"),
	// 	meta: {
	// 		requiresLogin: false,
	// 	},
	// },
	{
		path: "/register-alumni",
		name: "RegisterAlumni",
		component: () => import("@/pages/RegisterAlumni.vue"),
		meta: {
			requiresLogin: false,
		},
	},
	{
		path: "/alumni",
		name: "Alumni",
		component: () => import("@/pages/Alumni.vue"),
		meta: {
			requiresLogin: false,
		},
	},
	{
		path: "/news",
		name: "NewsSpotlight",
		component: () => import("@/pages/NewsSpotlight.vue"),
		meta: {
			requiresLogin: false,
		},
	},
	{
		path: "/executive-committee",
		name: "ExecutiveCommittee",
		component: () => import("@/pages/ExecutiveCommittee.vue"),
		meta: {
			requiresLogin: false,
		},
	},
]

const router = createRouter({
	history: createWebHashHistory(),
	routes,
	scrollBehavior(to, from, savedPosition) {
		if (savedPosition) {
			return savedPosition
		}
		return { top: 0, left: 0 }
	},
})

router.beforeEach(async (to, from, next) => {
	let isLoggedIn = session.isLoggedIn
	try {
		await userResource.promise
	} catch (error) {
		isLoggedIn = false
	}

	if (to.meta.requiresLogin && !isLoggedIn) {
		// If the route requires login and the user is not logged in, redirect to the Login page
		window.location.href = "/login?redirect-to=/"
	}
	next()
})

export default router
