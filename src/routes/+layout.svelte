<script>
  import { onMount } from "svelte";
  import "../app.css";
  import { page } from "$app/stores";
  import communitySign from "../data/community-sign.jpg";

  import { dev } from "$app/environment";
  import { injectAnalytics } from "@vercel/analytics/sveltekit";
  import { injectSpeedInsights } from "@vercel/speed-insights/sveltekit";

  injectAnalytics({ mode: dev ? "development" : "production" });
  injectSpeedInsights();

  let navOpen = false;
  let moreOpen = false;
  let openDropdown = null;
  let activeNavParent = null; // Track explicit selection
  let navWrapper;
  let brandWrapper;
  let measureContainer;
  let moreButton;
  let measureRefs = {};
  let visibleLinks = [];
  let overflowLinks = [];

  // Tracks the inner bounding container width reactively
  let containerWidth = 0;

  function trackMeasure(el, link) {
    const key = link.path ?? link.name;
    measureRefs[key] = el;
    return {
      destroy() {
        if (measureRefs[key] === el) {
          delete measureRefs[key];
        }
      },
    };
  }

  const navLinks = [
    { name: "Home", path: "/" },
    { name: "News & Records", path: "/news-records" },
    { name: "SCBD", path: "/why-scbd" },
    {
      name: "Resources",
      children: [
        { name: "Information", path: "/information" },
        { name: "Documents", path: "/documents" },
        { name: "Architecture Requests", path: "/architecture-requests" }
      ]
    },
    {
      name: "FAQ & Guide",
      children: [
        { name: "Information", path: "/information" },
        { name: "Documents", path: "/documents" },
        { name: "FAQ", path: "/faq" }
      ]
    },
    {
      name: "Board & Meetings",
      children: [
        { name: "Board Responsibilities", path: "/board" },
        { name: "Meeting Notes", path: "/meeting-notes" },
        { name: "Register", path: "/register" },
        { name: "Contact", path: "/contact" }
      ]
    }
  ];

  function toggleDropdown(name, event) {
    if (event) event.stopPropagation();
    if (openDropdown === name) {
      openDropdown = null;
    } else {
      openDropdown = name;
      if (name !== 'more_btn') activeNavParent = name;
    }
  }

  function updateNav() {
    if (!navWrapper || !measureContainer || !moreButton) return;

    // Get the exact width of the parent flex row
    const parentRow = navWrapper.parentElement;
    if (!parentRow) return;

    const parentAvailable = parentRow.clientWidth;
    const brandWidth = brandWrapper ? brandWrapper.offsetWidth : 0;

    // Remaining horizontal space for desktop layout
    const available = parentAvailable - brandWidth - 64; // Increased safety margin for desktop spacing

    const moreWidth = moreButton.offsetWidth;
    let used = 0;
    const visible = [];
    const overflow = [];

    for (const link of navLinks) {
      const key = link.path ?? link.name;
      const width = measureRefs[key]?.offsetWidth ?? 0;
      const needsMore = overflow.length > 0;
      const reserve = needsMore ? moreWidth : 0;

      if (used + width + reserve <= available) {
        visible.push(link);
        used += width;
      } else {
        overflow.push(link);
      }
    }

    if (overflow.length > 0 && used + moreWidth > available) {
      while (visible.length > 0 && used + moreWidth > available) {
        const last = visible.pop();
        overflow.unshift(last);
        const lastKey = last.path ?? last.name;
        used -= measureRefs[lastKey]?.offsetWidth ?? 0;
      }
    }

    visibleLinks = visible.length ? visible : navLinks;
    overflowLinks = overflow;
  }

  // Svelte reactivity: Re-run calculations immediately whenever the container dimension updates
  $: if (containerWidth || navWrapper || brandWrapper) {
    updateNav();
  }

  onMount(() => {
    visibleLinks = navLinks;
    updateNav();

    const ro = new ResizeObserver(() => updateNav());
    ro.observe(navWrapper);
    window.addEventListener("resize", updateNav);

    const closeAll = () => {
      openDropdown = null;
      moreOpen = false;
    };
    window.addEventListener("click", closeAll);

    return () => {
      ro.disconnect();
      window.removeEventListener("resize", updateNav);
      window.removeEventListener("click", closeAll);
    };
  });

  $: if (navWrapper) updateNav();
</script>

<div
  class="min-h-screen bg-slate-50 flex flex-col"
  style="--page-header-bg: url({communitySign});"
>
  <!-- Navigation Header -->
  <header
    class="relative z-30 bg-slate-900/95 text-white shadow-lg shadow-slate-900/10 backdrop-blur-sm border-b border-slate-800"
  >
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
      bind:clientWidth={containerWidth}
    >
      <div class="flex flex-row items-center justify-between py-4 gap-4">
        <div bind:this={brandWrapper} class="flex items-center gap-3 shrink-0">
          <img
            src="/shipleys-logo.png"
            style="height: 40px; width: 40px;"
            alt="Shipley's Choice Logo"
            class="object-contain shrink-0"
          />
          <div class="flex flex-col select-none shrink-0">
            <span
              class="text-xl font-bold tracking-tight leading-tight whitespace-nowrap"
            >
              Shipley's Choice
            </span>
            <p class="text-sm text-slate-300 whitespace-nowrap">
              Community Association
            </p>
          </div>
        </div>

        <div class="flex items-center md:hidden shrink-0">
          <button
            type="button"
            on:click={() => (navOpen = !navOpen)}
            aria-expanded={navOpen}
            aria-label="Toggle navigation"
            class="inline-flex h-10 w-10 items-center justify-center rounded-full border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {#if navOpen}
              <svg
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            {:else}
              <svg
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            {/if}
          </button>
        </div>

        <nav
          bind:this={navWrapper}
          class="hidden flex-nowrap items-center gap-2 md:flex md:justify-end min-w-0 md:overflow-visible"
          aria-label="Primary navigation"
        >
          {#each visibleLinks as link}
            {#if link.children}
              <div class="relative shrink-0">
                <button
                  type="button"
                  on:click={(e) => toggleDropdown(link.name, e)}
                  class="inline-flex items-center gap-1 px-3 py-2 text-sm transition-colors duration-150 shrink-0 whitespace-nowrap {activeNavParent === link.name ? 'border-b-2 border-blue-400 text-white font-semibold' : 'border-b-2 border-transparent text-slate-200 hover:text-white hover:border-slate-500'}"
                >
                  {link.name}
                  <svg
                    class="h-4 w-4 transition-transform duration-150 {openDropdown === link.name ? 'rotate-180' : ''}"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>

                {#if openDropdown === link.name}
                  <div
                    class="absolute left-0 z-50 mt-2 w-56 overflow-hidden rounded-2xl border border-slate-700 bg-slate-900/95 shadow-lg shadow-slate-900/30 backdrop-blur-sm"
                  >
                    {#each link.children as child}
                      <a
                        href={child.path}
                        on:click={() => (openDropdown = null)}
                        class="block px-4 py-2 text-sm transition-colors duration-150 {$page.url.pathname === child.path ? 'bg-blue-600 text-white font-semibold' : 'text-slate-200 hover:bg-slate-800 hover:text-white'}"
                      >
                        {child.name}
                      </a>
                    {/each}
                  </div>
                {/if}
              </div>
            {:else}
              <a
                href={link.path}
                class="inline-flex items-center px-3 py-2 text-sm transition-colors duration-150 shrink-0 whitespace-nowrap {$page
                  .url.pathname === link.path
                  ? 'border-b-2 border-blue-400 text-white font-semibold'
                  : 'border-b-2 border-transparent text-slate-200 hover:text-white hover:border-slate-500'}"
              >
                {link.name}
              </a>
            {/if}
          {/each}

          {#if overflowLinks.length}
            <div class="relative shrink-0">
              <button
                type="button"
                on:click={(e) => toggleDropdown('more_btn', e)}
                class="inline-flex items-center gap-1 rounded-full border px-3 py-2 text-sm font-medium border-slate-700/70 text-slate-200 hover:bg-slate-700 hover:text-white transition-colors whitespace-nowrap"
              >
                More..
                <svg
                  class="h-4 w-4"
                  viewBox="0 0 20 20"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M6 8l4 4 4-4" />
                </svg>
              </button>

              {#if openDropdown === 'more_btn'}
                <div
                  class="absolute right-0 z-50 mt-2 w-56 overflow-hidden rounded-2xl border border-slate-700 bg-slate-900/95 shadow-lg shadow-slate-900/30 backdrop-blur-sm"
                >
                  {#each overflowLinks as link}
                    {#if link.children}
                      <div class="px-4 py-1.5 text-xs font-bold text-slate-400 uppercase tracking-wider bg-slate-950/40 border-y border-slate-800">
                        {link.name}
                      </div>
                      {#each link.children as child}
                        <a
                          href={child.path}
                          on:click={() => (openDropdown = null)}
                          class="block pl-6 pr-4 py-2 text-sm transition-colors duration-150 {$page.url.pathname === child.path ? 'bg-blue-600/30 text-white font-semibold' : 'text-slate-200 hover:bg-slate-800 hover:text-white'}"
                        >
                          {child.name}
                        </a>
                      {/each}
                    {:else}
                      <a
                        href={link.path}
                        on:click={() => (openDropdown = null)}
                        class="block px-4 py-2 text-sm text-slate-200 hover:bg-slate-800 hover:text-white transition-colors duration-150"
                      >
                        {link.name}
                      </a>
                    {/if}
                  {/each}
                </div>
              {/if}
            </div>
          {/if}
        </nav>
      </div>

      {#if navOpen}
        <nav class="md:hidden grid gap-2 border-t border-slate-700 pt-4 pb-4 max-h-[80vh] overflow-y-auto">
          {#each navLinks as link}
            {#if link.children}
              <div>
                <button
                  type="button"
                  on:click={(e) => toggleDropdown(link.name + '_mobile', e)}
                  class="flex w-full items-center justify-between px-4 py-3 text-sm font-medium text-slate-200 hover:text-white transition-colors"
                >
                  {link.name}
                  <svg
                    class="h-4 w-4 transition-transform duration-150 {openDropdown === link.name + '_mobile' ? 'rotate-180' : ''}"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>
                {#if openDropdown === link.name + '_mobile'}
                  <div class="bg-slate-950/30 pl-4 py-1 border-l-2 border-blue-500/50">
                    {#each link.children as child}
                      <a
                        href={child.path}
                        on:click={() => (navOpen = false)}
                        class="block px-4 py-2.5 text-sm font-medium transition-colors {$page.url.pathname === child.path ? 'text-blue-400 font-semibold' : 'text-slate-300 hover:text-white'}"
                      >
                        {child.name}
                      </a>
                    {/each}
                  </div>
                {/if}
              </div>
            {:else}
              <a
                href={link.path}
                on:click={() => (navOpen = false)}
                class="block px-4 py-3 text-sm font-medium transition-colors {$page.url.pathname === link.path ? 'text-blue-400 font-semibold' : 'text-slate-200 hover:text-white'}"
              >
                {link.name}
              </a>
            {/if}
          {/each}
        </nav>
      {/if}
    </div>
  </header>

  <div
    bind:this={measureContainer}
    class="pointer-events-none absolute left-[-9999px] top-[-9999px] opacity-0"
    aria-hidden="true"
  >
    {#each navLinks as link}
      <span
        use:trackMeasure={link}
        class="inline-flex items-center px-3 py-2 text-sm font-medium"
      >
        {link.name}
      </span>
    {/each}
    <span
      bind:this={moreButton}
      class="inline-flex items-center px-3 py-2 text-sm font-medium"
    >
      More..
    </span>
  </div>

  <!-- Page Content -->
  <main class="flex-grow">
    <slot />
  </main>

  <footer
    class="bg-white border-t border-slate-200 p-8 text-center text-slate-500 text-sm"
  >
    &copy; {new Date().getFullYear()} Shipley's Choice Community Association. All
    rights reserved.
  </footer>
</div>
