# Brevo Integration Components

This directory manages official Brevo web forms embedded natively within the Shipley's Choice Community Association (SCCA) website. 

To ensure modularity and scalability, each Brevo form has its own self-contained subdirectory containing the raw form export and its Svelte wrapper component.

---

## Directory Structure

```
src/components/brevo/
├── README.md                          # This master planning guide
└── email-registration/                # Resident Email & Newsletter Registration
    ├── brevoEmailSignup.htm           # Raw HTML export from Brevo (source of truth)
    └── BrevoEmailSignup.svelte       # Svelte component wrapping and sanitizing the HTML
```

---

## Technical Integration Strategy

Brevo forms typically consist of extensive HTML containing standard input fields, CSS styling, translation maps, and form-handling scripts. 

To embed these forms cleanly and natively without resorting to iframes, we employ the following architecture:

1. **Vite Raw Loader**: The `.htm` file is imported directly inside the Svelte component as a raw string using Vite's `?raw` suffix:
   ```javascript
   import brevoHtml from './brevoEmailSignup.htm?raw';
   ```
2. **Script Sanitization**: Because Svelte's `{@html}` block does not execute static `<script>` tags, we strip raw script tags out at build/runtime using a simple regular expression:
   ```javascript
   const cleanedHtml = brevoHtml.replace(/<script[\s\S]*?<\/script>/gi, '');
   ```
3. **Safe Client-Side Mount**: The variables and form scripts are safely initialized inside the Svelte `onMount` hook, declaring expected translation properties on the client-side `window` object, injecting Brevo's standard form-validation runtime (`https://sibforms.com/forms/end-form/build/main.js`), and cleaning up on destruction.
4. **Style Overrides**: Scoped CSS overrides are defined within each wrapper component to match the main site's cards, layout, and colors, providing a completely integrated aesthetic.

---

## How to Add a New Brevo Form

If the SCCA Board requests a new form in the future (e.g., for surveys, event RSVPs, or volunteer recruitment):

1. **Create a New Subdirectory**: Under `src/components/brevo/`, create a new descriptive folder:
   ```bash
   mkdir -p src/components/brevo/new-form-name
   ```
2. **Export HTML from Brevo**: Design the form inside the Brevo dashboard, navigate to **Share / Embed**, and copy the **HTML code** (NOT the iframe snippet).
3. **Save raw HTML**: Paste the raw HTML into a file named `rawForm.htm` (or similar) inside the new folder.
4. **Create the Svelte Wrapper**: Duplicate `BrevoEmailSignup.svelte` into your new directory, naming it `NewFormName.svelte`.
5. **Adjust Styles and Configuration**:
   - Update the import path of the raw HTML: `import formHtml from './rawForm.htm?raw';`
   - Adjust any CSS override targets if Brevo containers differ.
6. **Import and Render**: Import your new Svelte component into the desired page under `src/routes/`.
