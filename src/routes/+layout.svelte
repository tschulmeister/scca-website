<script>
  import { onMount } from "svelte";
  import "../app.css";
  import { page } from "$app/stores";
  import communitySign from "../data/community-sign.jpg";

  let navOpen = false;
  let moreOpen = false;
  let navWrapper;
  let measureContainer;
  let moreButton;
  let measureRefs = {};
  let visibleLinks = [];
  let overflowLinks = [];

  function trackMeasure(el, link) {
    measureRefs[link.path] = el;

    return {
      destroy() {
        if (measureRefs[link.path] === el) {
          delete measureRefs[link.path];
        }
      },
    };
  }

  const navLinks = [
    { name: "Home", path: "/" },
    { name: "Information", path: "/information" },
    { name: "Documents", path: "/documents" },
    { name: "News & Records", path: "/news-records" },
    { name: "Meeting Notes", path: "/meeting-notes" },
    { name: "Register", path: "/register" },
    { name: "Architecture Requests", path: "/architecture-requests" },
    { name: "FAQ", path: "/faq" },
    { name: "Contact", path: "/contact" },
    { name: "Board", path: "/board" },
  ];

  function updateNav() {
    if (!navWrapper || !measureContainer || !moreButton) return;

    const available = navWrapper.clientWidth - 12;
    const moreWidth = moreButton.offsetWidth;
    let used = 0;
    const visible = [];
    const overflow = [];

    for (const link of navLinks) {
      const width = measureRefs[link.path]?.offsetWidth ?? 0;
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
        used -= measureRefs[last.path]?.offsetWidth ?? 0;
      }
    }

    visibleLinks = visible.length ? visible : navLinks;
    overflowLinks = overflow;
  }

  onMount(() => {
    visibleLinks = navLinks;
    updateNav();

    const ro = new ResizeObserver(() => updateNav());
    ro.observe(navWrapper);
    window.addEventListener("resize", updateNav);

    return () => {
      ro.disconnect();
      window.removeEventListener("resize", updateNav);
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
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div
        class="flex flex-col gap-4 py-4 md:flex-row md:items-center md:justify-between"
      >
        <div class="flex items-center justify-between gap-4">
          <div class="flex items-center gap-3">
            <img
              src="/shipleys-logo.png"
              style="height: 40px; width: 40px;"
              alt="Shipley's Choice Logo"
            />

            <div class="flex flex-col">
              <span class="text-xl font-bold tracking-tight leading-tight"
                >Shipley's Choice</span
              >
              <p class="text-sm text-slate-300">
                Community Association
              </p>
            </div>
          </div>
          <div class="md:hidden">
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
        </div>

        <nav
          bind:this={navWrapper}
          class="hidden flex-wrap items-center gap-2 md:flex md:justify-end"
          aria-label="Primary navigation"
        >
          {#each visibleLinks as link}
            <a
              href={link.path}
              class="inline-flex items-center px-3 py-2 text-sm transition-colors duration-150 {$page
                .url.pathname === link.path
                ? 'border-b-2 border-blue-400 text-white font-semibold'
                : 'border-b-2 border-transparent text-slate-200 hover:text-white hover:border-slate-500'}"
            >
              {link.name}
            </a>
          {/each}

          {#if overflowLinks.length}
            <div class="relative">
              <button
                type="button"
                on:click={() => (moreOpen = !moreOpen)}
                class="inline-flex items-center gap-1 rounded-full border px-3 py-2 text-sm font-medium border-slate-700/70 text-slate-200 hover:bg-slate-700 hover:text-white transition-colors"
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

              {#if moreOpen}
                <div
                  class="absolute right-0 z-50 mt-2 w-48 overflow-hidden rounded-2xl border border-slate-700 bg-slate-900/95 shadow-lg shadow-slate-900/30 backdrop-blur-sm"
                >
                  {#each overflowLinks as link}
                    <a
                      href={link.path}
                      on:click={() => (moreOpen = false)}
                      class="block px-4 py-2 text-sm text-slate-200 hover:bg-slate-800 hover:text-white"
                    >
                      {link.name}
                    </a>
                  {/each}
                </div>
              {/if}
            </div>
          {/if}
        </nav>
      </div>

      {#if navOpen}
        <nav class="md:hidden grid gap-2 border-t border-slate-700 pt-4 pb-4">
          {#each navLinks as link}
            <a
              href={link.path}
              on:click={() => (navOpen = false)}
              class="block px-4 py-3 text-sm font-medium text-slate-200 hover:text-white transition-colors"
            >
              {link.name}
            </a>
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
