# Shipley's Choice Community Association (SCCA) Website

Welcome to the official repository for the SCCA website. This project is a modern, responsive, serverless web application developed for the SCCA Board to serve residents, prospective homeowners, and realtors with transparent, high-fidelity information about the Shipley's Choice community.

---

## 🏛️ Webmaster Mission & SCCA Philosophy

The SCCA website runs on a **$0/month serverless architecture** optimized for extreme speed, search engine optimization (SEO), and low maintenance. Rather than operating a costly and vulnerable database server, the entire application is driven by a **SvelteKit static compile pipeline**.

### Core Tenets for Webmasters

1. **Board-Driven Consensus**: Updates, news, and financial postings must align with official board communications, bylaws, and community-wide consensus.
2. **Neutral & Objective Tone**: All content should remain non-partisan, objective, professional, and accessible.
3. **Data Privacy**: No personal emails, physical addresses, or phone numbers of residents should ever be stored or hardcoded in public repository files.
4. **Accessibility (a11y)**: All images, charts, and interactive elements should maintain high contrast, have proper ARIA labels, and avoid redundant screenreader announcements.

---

## 🛠️ Technology Stack

- **Framework**: [SvelteKit](https://kit.svelte.dev/) (using Svelte 5 with reactivity runes like `$state`, `$derived`, and `$props`)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Charts & Data Viz**: [D3.js](https://d3js.org/) for highly-customizable SVGs (Expense Donuts, Comparison Bars, and Spark Lines)
- **Hosting & Analytics**: Vercel Integration (configured via `@sveltejs/adapter-auto` with Vercel Web Analytics and Speed Insights)

---

## 📁 Key File Directory Structure

```text
├── scripts/
│   └── prepare-news.js         # Interactive CLI script for news generation
├── src/
│   ├── app.html                # SvelteKit page entry shell
│   ├── components/
│   │   ├── charts/             # D3.js interactive financial visualizations
│   │   └── news/               # YYYY/MM/DD structure for physical news .htm files
│   ├── data/                   # The "JSON Database" of the website
│   │   ├── financials.json     # Line-item financial datasets for graphs
│   │   ├── financialStats.json # High-level summary text and key stats
│   │   ├── meetingNotes.json   # Board meeting notes and minutes index
│   │   ├── newsItems.json      # Metadata index for community announcements
│   │   └── scbdChartData.json  # D3 datasets for Special Community Benefit District
│   └── routes/                 # SvelteKit routing pages
└── static/
    └── data/                   # Official PDFs, images, and section plats
        ├── docs/               # SCCA Covenants, Bylaws, and ARC Forms
        └── plats/              # High-resolution JPEG Section Plats
```

---

## ✍️ Content Maintenance Workflows

### 📰 1. Community News & Announcements

To optimize performance and simplify HTML writing, news post bodies are decoupled from the metadata index:

- **Metadata Index**: `src/data/newsItems.json` stores basic properties like `id`, `title`, `date`, `tags`, and `contentPath`.
- **News Content**: Discrete `.htm` files containing rich text/HTML reside under `src/components/news/YYYY/MM/DD/id.htm`.

#### 🤖 Automated Generation Command

Instead of manually editing files and risking malformed JSON, use the interactive generator:

```bash
npm run prepare-news
```

This CLI script will:

1. Prompt you for the news Title, Tags, and post Date (defaults to today's date).
2. Auto-generate a clean URL slug `id`.
3. Create the physical directory and `.htm` file pre-populated with SCCA-standard HTML markup.
4. Insert a new index entry at the **very top** of `src/data/newsItems.json`.

#### ⚡ How Svelte Loads the HTML File

The website uses Vite's **eager raw glob imports** to statically compile and embed the HTML files without causing layout shifts or runtime network requests:

```svelte
<script>
  // Dynamically import all news HTML contents raw at build time
  const newsContents = import.meta.glob('/src/components/news/**/*.htm', {
    query: '?raw',
    import: 'default',
    eager: true
  });
</script>
```

---

### 📝 2. Posting Board Meeting Notes & Minutes

When the Board approves new meeting minutes:

1. Open `src/data/meetingNotes.json`.
2. Add a new entry to the array at the **top** (newest first).
3. The schema includes:

```json
{
  "id": "2026-09-13-minutes",
  "date": "September 13, 2026",
  "type": "Regular Meeting",
  "attendees": [
    "John Doe (Pres)",
    "Jane Smith (Treas)",
    "Robert Johnson (Sec)"
  ],
  "summary": "Key highlights of what was discussed, such as SCBD updates or maintenance.",
  "decisions": [
    "Approved common ground landscape repair bids.",
    "Confirmed annual membership meeting date and location."
  ],
  "pdfUrl": "/data/docs/meeting-notes/2026-09-13-approved.pdf"
}
```

4. If a companion PDF is provided, upload it to `static/data/docs/meeting-notes/` and link it in `pdfUrl`.

---

### 📊 3. Updating Financials & Budget Visualizations

The SCCA financials page uses dynamic D3 charts driven entirely by JSON.

- **`src/data/financials.json`**: Controls the SCCA actual expenditures vs. budget totals. Adding/removing items here updates the visual bars automatically.
- **`src/data/financialStats.json`**: Hosts key highlighted strings, reserve totals, and audit certification text displayed in callouts.
- **`src/data/scbdChartData.json`**: Populates comparison visualizations between standard SCCA dues structures and proposed SCBD assessment models.

---

### 📂 4. Uploading Official Legal & Static Documents

Large static resources must never be committed to the Svelte components directory. They must be uploaded to the `static/` directory to bypass compilation:

- **Legal Covenants**: Must be placed in `static/data/docs/` (e.g., `scca_section_1_covenants.pdf`).
- **Section Plats**: High-resolution maps must go to `static/data/plats/` as JPEGs.
- **Filing Forms**: Editable documents (e.g., Architectural Request `.docx` files) go to `static/data/docs/`.

_Recommendation: Always compress PDFs and optimize images before uploading to maintain the site's high Google Lighthouse scores._

---

## 💻 Local Development Setup

To run the application locally on your computer for updates and previewing:

### Prerequisites

Make sure you have [Node.js](https://nodejs.org/) (v18 or newer) and `npm` installed.

### Installation

Clone the repository and install all node modules:

```bash
npm install
```

### Run Dev Server

Launch the local Vite development server with hot-module replacement (HMR):

```bash
npm run dev
```

Open your browser to `http://localhost:5173` to view the live app.

### Quality Assurance & Build Checks

Before committing any changes to the main branch, always verify the production compilation:

```bash
# Build SvelteKit static and server pages
npm run build

# Preview the built production assets locally
npm run preview
```

---

## 🚀 Deployment

The site is configured for automatic, zero-touch deployments:

- **Production**: Connecting your GitHub repository to Vercel will trigger a production build automatically on every push to the `main` branch.
- **Secondary Mirror**: The workspace includes a GitHub Actions CI/CD configuration under `.github/workflows/deploy.yml` that builds and deploys static artifacts to GitHub Pages on pushes to the `gh-deploy` branch.

---

_Thank you for serving the Shipley's Choice Community. Feel free to contact the SCCA Board of Directors for policy or communication approvals regarding website releases._
