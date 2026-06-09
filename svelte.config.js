import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// adapter-static configures the project as a fully static site
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: '404.html', // Allows SPA-style client routing on page refresh
			precompress: false,
			strict: true
		}),
		paths: {
			// In production, prepend the GitHub repository name.
			// In development, keep it empty ('') so it runs at localhost:5173/
			base: process.env.NODE_ENV === 'production' ? '/scca-website' : ''
		}
	}
};

export default config;