# Alumni NIT Srinagar — SANGAM

The Official Alumni Web Application of **National Institute of Technology Srinagar (NIT Srinagar)**, maintained by the **Office of Dean Alumni & International Affairs**.

---

## 🌟 Features

- **Alumni Directory**: Comprehensive directory of NIT Srinagar graduates with live search, department filtering, and detailed profile views.
- **News & Spotlight**: Updates, achievements, spotlights, and events regarding alumni and the institute.
- **Alumni Registration**: Online portal for NIT Srinagar graduates to register their profiles.
- **Responsive Interface**: Designed for desktop and mobile devices with fast navigation and modern typography.

---

## 🛠️ Technology Stack

- **Backend**: [Frappe Framework](https://frappeframework.com)
- **Frontend**: Vue 3, Vite, [Frappe UI](https://frappeui.com), Tailwind CSS

---

## ⚙️ Installation

```bash
# Navigate to your bench directory
cd $PATH_TO_YOUR_BENCH

# Fetch and install the app
bench get-app alumni_nit_srinagar --branch develop
bench --site [site-name] install-app alumni_nit_srinagar
bench --site [site-name] migrate
```

### Development Setup

```bash
cd apps/alumni_nit_srinagar/frontend

# Install dependencies
yarn

# Start development server
yarn dev

# Build production bundle
yarn build
```

---

## 📜 License & Credits

- **Maintained By**: Office of Dean Alumni & International Affairs, NIT Srinagar
- **Designed & Developed By**: [FOSS Club, NIT Srinagar](https://foss.nitsri.ac.in/)
- **License**: AGPL-3.0
