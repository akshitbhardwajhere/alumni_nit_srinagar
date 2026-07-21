<template>
	<div class="flex-grow bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 flex items-center justify-center">
		<div
			class="max-w-2xl w-full bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden"
		>
			<!-- Form Header -->
			<div class="bg-[#17345F] px-8 py-8 text-white relative">
				<div class="absolute right-8 top-8 opacity-10">
					<svg class="w-24 h-24 text-white" fill="currentColor" viewBox="0 0 24 24">
						<path
							d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"
						/>
					</svg>
				</div>
				<span class="text-xs font-semibold text-[#D5A33D] uppercase tracking-wider"
					>Office of Dean Alumni &amp; International Affairs</span
				>
				<h2 class="text-3xl font-exo-2 font-bold mt-2">Alumni Registration</h2>
				<p class="text-gray-200 mt-2 text-sm">
					Please fill out the form below to register your profile in the official Alumni
					Directory.
				</p>
			</div>

			<!-- Success State -->
			<div v-if="isSuccess" class="p-8 sm:p-12 text-center flex flex-col items-center">
				<div
					class="w-16 h-16 bg-green-50 text-green-600 rounded-full flex items-center justify-center mb-6"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-10 w-10"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2.5"
							d="M5 13l4 4L19 7"
						/>
					</svg>
				</div>
				<h3 class="text-2xl font-bold text-gray-900">Registration Successful!</h3>
				<p class="text-gray-600 mt-4 max-w-md leading-relaxed">
					Thank you, <strong>{{ form.full_name }}</strong
					>. Your profile has been successfully registered under the
					<strong>{{ form.branchdepartment }}</strong> department.
				</p>
				<Button
					variant="solid"
					theme="blue"
					size="lg"
					class="mt-8 px-8 bg-[#17345F] hover:bg-[#12284c] text-white font-bold"
					@click="goBack"
				>
					Go back to Home Page
				</Button>
			</div>

			<!-- Form State -->
			<form v-else @submit.prevent="submitForm" class="p-8 sm:p-10 space-y-6">
				<!-- Error Alert -->
				<div
					v-if="errorMsg"
					class="p-4 bg-red-50 border-l-4 border-red-500 rounded-r-lg text-red-700 text-sm"
				>
					{{ errorMsg }}
				</div>

				<div
					class="flex flex-col items-center justify-center border-b border-gray-100 pb-6"
				>
					<!-- Profile Image Upload -->
					<div class="relative group">
						<div
							class="w-24 h-24 rounded-full overflow-hidden border-2 border-gray-200 bg-gray-50 flex items-center justify-center relative shadow-inner"
						>
							<img
								v-if="form.image"
								:src="form.image"
								alt="Profile Preview"
								class="w-full h-full object-cover"
							/>
							<svg
								v-else
								class="w-12 h-12 text-gray-300"
								fill="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z"
								/>
							</svg>

							<!-- Uploading Spinner -->
							<div
								v-if="uploading"
								class="absolute inset-0 bg-black/50 flex items-center justify-center"
							>
								<svg
									class="animate-spin h-6 w-6 text-white"
									fill="none"
									viewBox="0 0 24 24"
								>
									<circle
										class="opacity-25"
										cx="12"
										cy="12"
										r="10"
										stroke="currentColor"
										stroke-width="4"
									></circle>
									<path
										class="opacity-75"
										fill="currentColor"
										d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
									></path>
								</svg>
							</div>
						</div>

						<!-- Floating Upload Trigger -->
						<label
							for="image-upload"
							class="absolute bottom-0 right-0 w-8 h-8 rounded-full bg-[#17345F] hover:bg-[#12284c] text-white flex items-center justify-center cursor-pointer shadow-lg border border-white transition-colors"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-4 w-4"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"
								/>
							</svg>
						</label>
						<input
							type="file"
							id="image-upload"
							accept="image/*"
							class="hidden"
							@change="handleImageUpload"
						/>
					</div>

					<div class="mt-3 text-center">
						<span
							class="text-xs font-bold text-gray-500 uppercase tracking-wider block"
							>Profile Photo</span
						>
						<button
							v-if="form.image"
							type="button"
							@click="removeImage"
							class="text-xs text-red-600 hover:text-red-800 font-semibold mt-1"
						>
							Remove Photo
						</button>
					</div>
				</div>

				<div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
					<!-- Full Name -->
					<div class="sm:col-span-2">
						<label class="block text-sm font-bold text-gray-700"
							>Full Name <span class="text-red-500">*</span></label
						>
						<TextInput
							v-model="form.full_name"
							placeholder="Enter your full name"
							size="md"
							variant="outline"
							required
							class="mt-1.5"
						/>
					</div>

					<!-- Branch/Department -->
					<div class="sm:col-span-2">
						<label class="block text-sm font-bold text-gray-700 mb-1.5"
							>Branch / Department <span class="text-red-500">*</span></label
						>
						<Select
							v-model="form.branchdepartment"
							:options="branches"
							placeholder="Select your branch / department"
							size="md"
							variant="outline"
							class="w-full"
						/>
					</div>

					<!-- Batch/Year -->
					<div>
						<label class="block text-sm font-bold text-gray-700"
							>Batch / Year <span class="text-red-500">*</span></label
						>
						<TextInput
							v-model="form.batchyear"
							placeholder="e.g. 2023-2027"
							size="md"
							variant="outline"
							required
							class="mt-1.5"
						/>
					</div>

					<!-- Phone Number -->
					<div>
						<label class="block text-sm font-bold text-gray-700 mb-1.5"
							>Phone Number (Optional)</label
						>
						<div class="flex items-center gap-2">
							<Select
								v-model="countryCode"
								:options="countryOptions"
								placeholder="ISD"
								size="md"
								variant="outline"
								class="w-21 shrink-0"
							/>
							<TextInput
								type="tel"
								v-model="phoneNumberVal"
								placeholder="Enter your phone number"
								variant="outline"
								size="md"
								class="flex-2"
							/>
						</div>
					</div>

					<!-- Email Address -->
					<div class="sm:col-span-2">
						<label class="block text-sm font-bold text-gray-700"
							>Email Address <span class="text-red-500">*</span></label
						>
						<TextInput
							type="email"
							v-model="form.email_address"
							placeholder="Enter your email address"
							size="md"
							variant="outline"
							required
							class="mt-1.5"
						/>
					</div>
				</div>

				<div class="pt-4 border-t border-gray-100 flex items-center justify-end gap-3">
					<Button type="button" variant="outline" size="md" @click="goBack">
						Cancel
					</Button>
					<Button
						type="submit"
						variant="solid"
						theme="blue"
						size="md"
						class="bg-[#17345F] hover:bg-[#12284c] text-white"
						:loading="loading || uploading"
					>
						Register
					</Button>
				</div>
			</form>
		</div>
	</div>
  <Footer />
</template>

<script setup>
import { Select, createResource } from "frappe-ui";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import Footer from "../components/Footer.vue"

const router = useRouter();

const form = reactive({
	full_name: "",
	branchdepartment: "",
	batchyear: "",
	email_address: "",
	image: "",
});

const countryCode = ref("+91");
const phoneNumberVal = ref("");

const loading = ref(false);
const uploading = ref(false);
const isSuccess = ref(false);
const errorMsg = ref("");

const branches = [
	"Computer Science & Engineering (CSE)",
	"Information Technology (IT)",
	"Electrical Engineering",
	"Electronics & Communication Engineering (ECE)",
	"Mechanical Engineering",
	"Civil Engineering",
	"Chemical Engineering",
	"Metallurgical & Materials Engineering",
	"Mathematics",
	"Physics",
	"Chemistry",
	"Humanities, Social Sciences & Management (HSS&M)",
];

const countryOptions = [
	{ label: "🇮🇳 +91", value: "+91" },
	{ label: "🇺🇸 +1", value: "+1" },
	{ label: "🇬🇧 +44", value: "+44" },
	{ label: "🇦🇪 +971", value: "+971" },
	{ label: "🇸🇦 +966", value: "+966" },
	{ label: "🇦🇺 +61", value: "+61" },
	{ label: "🇩🇪 +49", value: "+49" },
	{ label: "🇸🇬 +65", value: "+65" },
];

const handleImageUpload = async (event) => {
	const file = event.target.files[0];
	if (!file) return;

	// Validate file size (2MB limit)
	if (file.size > 2 * 1024 * 1024) {
		errorMsg.value = "Image size should be less than 2MB.";
		return;
	}

	uploading.value = true;
	errorMsg.value = "";

	const formData = new FormData();
	formData.append("file", file);
	formData.append("is_private", 0);
	formData.append("folder", "Home/Attachments");

	try {
		const headers = {
			Accept: "application/json",
			"X-Frappe-Site-Name": window.location.hostname,
		};
		if (window.csrf_token && window.csrf_token !== "{{ csrf_token }}") {
			headers["X-Frappe-CSRF-Token"] = window.csrf_token;
		}

		const response = await fetch("/api/method/upload_file", {
			method: "POST",
			headers,
			body: formData,
		});

		if (!response.ok) {
			const errData = await response.json();
			throw new Error(errData._error_message || "Failed to upload image.");
		}

		const data = await response.json();
		form.image = data.message.file_url;
	} catch (err) {
		errorMsg.value = err.message || "Failed to upload image. Please try again.";
	} finally {
		uploading.value = false;
	}
};

const removeImage = () => {
	form.image = "";
};

const alumniResource = createResource({
	url: "frappe.client.insert",
	onSuccess(data) {
		loading.value = false;
		isSuccess.value = true;
	},
	onError(err) {
		loading.value = false;
		errorMsg.value =
			err.message ||
			"An error occurred while submitting your registration. Please try again.";
	},
});

const submitForm = () => {
	loading.value = true;
	errorMsg.value = "";

	if (!form.branchdepartment) {
		errorMsg.value = "Please select your branch / department.";
		loading.value = false;
		return;
	}

	// Format details before submission.
	// Frappe's Phone control expects the value formatted as [Country Code]-[Phone Number]
	// to successfully parse it and render the number on the Desk detail view.
	let finalPhoneNumber = undefined;
	if (phoneNumberVal.value?.trim()) {
		finalPhoneNumber = `${countryCode.value}-${phoneNumberVal.value.trim()}`;
	}

	const doc = {
		doctype: "Alumni",
		full_name: form.full_name,
		branchdepartment: form.branchdepartment,
		batchyear: form.batchyear,
		email_address: form.email_address,
		phone_number: finalPhoneNumber,
		image: form.image || undefined,
	};

	alumniResource.submit({ doc });
};

const goBack = () => {
	router.push({ name: "LandingPage" });
};
</script>
