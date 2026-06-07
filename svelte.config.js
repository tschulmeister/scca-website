import adapter from '@sveltejs/adapter-auto';
import preprocess from 'svelte-preprocess';

const config = {
  preprocess: preprocess(),
  kit: {
    adapter: adapter(),
    files: {
      routes: '.',
      appTemplate: 'app.html'
    }
  }
};

export default config;
