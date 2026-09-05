import adapter from "@sveltejs/adapter-auto";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    // adapter-auto will seamlessly optimize the build specifically for Vercel
    adapter: adapter(),
    alias: {
      $data: "src/data",
      $components: "src/components",
    },
  },
};

export default config;
