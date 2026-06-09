import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: '404.html', // Allows SPA-style routing for un-prerendered pages
			precompress: false,
			strict: true
		}),
		paths: {
			// Only use the repo base path in production, keep root for local development
			base: process.env.NODE_ENV === 'production' ? '/scca-website' : ''
		}
	}
};

export default config;