<script>
  import "./app.css";
  let navOpen = false;

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Information', path: '/information' },
    { name: 'Meeting Notes', path: '/meeting-notes' },
    { name: 'Documents', path: '/documents' },
    { name: 'News & Records', path: '/news-records' },
    { name: 'Register', path: '/register' },
    { name: 'Architecture Requests', path: '/architecture-requests' },
    { name: 'FAQ', path: '/faq' },
    { name: 'Contact', path: '/contact' },
    { name: 'Board', path: '/board' }
  ];
</script>

<div class="min-h-screen bg-slate-50 flex flex-col">
  <!-- Navigation Header -->
  <header class="bg-slate-800 text-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        <div class="flex-shrink-0 flex items-center">
          <span class="text-xl font-bold tracking-tight">Shipley's Choice Community</span>
        </div>
        
        <!-- Desktop Nav -->
        <nav class="hidden md:flex space-x-8">
          {#each navLinks as link}
            <a href={link.path} class="text-slate-300 hover:text-white transition-colors text-sm font-medium">
              {link.name}
            </a>
          {/each}
        </nav>

        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            on:click={() => navOpen = !navOpen}
            aria-label="Toggle navigation"
            class="p-2 text-slate-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-blue-400 rounded-md"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
        </div>
      </div>
      {#if navOpen}
        <nav class="md:hidden px-4 pb-4 space-y-2 border-t border-slate-700 bg-slate-800">
          {#each navLinks as link}
            <a href={link.path} on:click={() => navOpen = false} class="block rounded-lg px-3 py-2 text-sm font-medium text-slate-200 hover:bg-slate-700 hover:text-white transition-colors">
              {link.name}
            </a>
          {/each}
        </nav>
      {/if}
    </div>
  </header>

  <!-- Page Content -->
  <main class="flex-grow">
    <slot />
  </main>

  <footer class="bg-white border-t border-slate-200 p-8 text-center text-slate-500 text-sm">
    &copy; {new Date().getFullYear()} Shipley's Choice Community Association. All rights reserved.
  </footer>
</div>