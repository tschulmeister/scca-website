# Shipley's Choice Community Association (SCCA) Website

Welcome to the SCCA website codebase. This project is a modern, responsive SvelteKit web application operated by the SCCA Board. The website serves two primary audiences:
1. **Residents**: To stay informed about community news, board meeting notes, association finances, architectural request guidelines, and upcoming events.
2. **Potential Residents & Realtors**: To research the neighborhood, its history, local covenants, section plats, FAQs, and registration requirements.

---

## Tech Stack

- **Framework**: [SvelteKit](https://kit.svelte.dev/) (using Svelte 5)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Data Visualization**: [D3.js](https://d3js.org/) (for interactive financial and expense charts)
- **Bundler & Dev Server**: Vite
- **Analytics & Speed Insights**: Vercel Integration

---

## Directory Structure

Key folders and files include:
*   `src/routes/` - SvelteKit pages and layouts (organized by page context: `documents/`, `faq/`, `board/`, `meeting-notes/`, `why-scbd/`, etc.).
*   `src/components/` - Shared and reusable components, notably `./charts/` for D3-powered financial visualization.
*   `src/data/` - JSON-based datasets (e.g., `financials.json`, `meetingNotes.json`, `newsItems.json`) that power the site's dynamic content without requiring a database backend.
*   `static/data/` - Static assets, housing official community files:
    *   `docs/` - Covenants, by-laws, fence standards, and architectural request forms.
    *   `plats/` - High-resolution plats for Section 1 and Section 2.
    *   `newsletter/` - Monthly community newsletter PDFs.

---

## Guidelines & Best Practices

### 1. Code Style & Architecture
- **Svelte 5 Runes**: Use Svelte 5 syntax and runes (`$state`, `$derived`, `$props`) for state management and reactivity.
- **Component Design**: Keep UI components modular, accessible, and responsive.
- **Tailwind CSS**: Follow existing tailwind styling patterns. Maintain a professional, clean, and community-friendly look (soft blues, greens, and neutral tones).

### 2. Static Content Management
- For content that changes regularly (news, meeting notes, financial statistics), prefer updating the structured JSON files in `src/data/` rather than hardcoding values into pages.
- Large documents (PDFs, Plats) must be placed in `static/data/...` under their respective folders.

### 3. Git Conventions
- Maintain a clean git history.
- Never commit credentials, API keys, or private personal data to the repository.
