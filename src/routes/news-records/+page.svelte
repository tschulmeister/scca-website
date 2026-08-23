<script>
  import { onMount, onDestroy } from "svelte";
  import { ShieldAlert, DollarSign, Lightbulb, Wrench, Megaphone, Sparkles } from "@lucide/svelte";
  import newsItems from "$data/newsItems.json";

  // The `newsItems` are now imported directly.

  let activeId = "";
  let observer;

  onMount(() => {
    const sections = newsItems.map((item) => document.getElementById(item.id));

    const observerOptions = {
      root: null,
      rootMargin: "0px 0px -60% 0px",
      threshold: 0,
    };

    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeId = entry.target.id;
        }
      });
    }, observerOptions);

    sections.forEach((section) => {
      if (section) observer.observe(section);
    });
  });

  onDestroy(() => {
    if (observer) observer.disconnect();
  });

  function getItemCategory(item) {
    const title = item.title.toLowerCase();
    const id = item.id.toLowerCase();
    const tags = (item.tags || []).map((t) => t.toLowerCase());

    if (
      tags.includes("idea") ||
      title.includes("idea")
    ) {
      return "idea";
    }
    if (
      tags.includes("safety") ||
      tags.includes("community safety") ||
      title.includes("safety")
    ) {
      return "safety";
    }
    if (
      tags.includes("financials") ||
      title.includes("dues") ||
      title.includes("scbd") ||
      id.includes("scbd") ||
      title.includes("finance")
    ) {
      return "finance";
    }
    if (title.includes("light") || title.includes("upgrade")) {
      return "improvement";
    }
    if (
      title.includes("maintenance") ||
      title.includes("ground") ||
      title.includes("common")
    ) {
      return "maintenance";
    }
    return "announcement";
  }

  function getCategoryStyles(category) {
    switch (category) {
      case "idea":
        return {
          bg: "bg-white border-yellow-200 text-yellow-500",
          hoverBg: "group-hover:bg-yellow-50 group-hover:border-yellow-300",
        };
      case "safety":
        return {
          bg: "bg-rose-50 border-rose-200 text-rose-600",
          hoverBg: "group-hover:bg-rose-100 group-hover:border-rose-300",
        };
      case "finance":
        return {
          bg: "bg-emerald-50 border-emerald-200 text-emerald-600",
          hoverBg: "group-hover:bg-emerald-100 group-hover:border-emerald-300",
        };
      case "improvement":
        return {
          bg: "bg-amber-50 border-amber-200 text-amber-600",
          hoverBg: "group-hover:bg-amber-100 group-hover:border-amber-300",
        };
      case "maintenance":
        return {
          bg: "bg-green-50 border-green-200 text-green-600",
          hoverBg: "group-hover:bg-green-100 group-hover:border-green-300",
        };
      default:
        return {
          bg: "bg-blue-50 border-blue-200 text-blue-600",
          hoverBg: "group-hover:bg-blue-100 group-hover:border-blue-300",
        };
    }
  }
</script>

<svelte:head>
  <title>News & Records | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
      News &amp; records
    </p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
      News, newsletters, and meeting minutes
    </h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Download the latest community newsletter and browse community news items
      shared by the board
    </p>
    <div
      class="mt-8 flex flex-col items-center gap-4 sm:flex-row sm:justify-center"
    >
      <a
        href="/data/newsletter/2025-10.pdf"
        target="_blank"
        rel="noreferrer"
        class="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 text-white font-semibold shadow-sm hover:bg-blue-700 transition-colors"
      >
        Latest newsletter (PDF)
      </a>
    </div>
  </div>
</section>

<section class="max-w-7xl mx-auto px-4 py-12">
  <div class="lg:grid lg:grid-cols-12 lg:gap-12">
    <aside class="hidden lg:block lg:col-span-3">
      <nav class="sticky top-24">
        <h3 class="font-semibold text-slate-900">On this page</h3>
        <ul class="mt-4 space-y-1 border-l-2 border-slate-100">
          {#each newsItems as item}
            <li>
              <a
                href="#{item.id}"
                class="block w-full pl-3.5 pr-2 py-1.5 -ml-px border-l-2 text-sm transition-colors"
                class:border-blue-500={activeId === item.id}
                class:text-blue-600={activeId === item.id}
                class:font-semibold={activeId === item.id}
                class:border-transparent={activeId !== item.id}
                class:text-slate-500={activeId !== item.id}
                class:hover:border-slate-300={activeId !== item.id}
                class:hover:text-slate-700={activeId !== item.id}
              >
                {item.title}
              </a>
            </li>
          {/each}
        </ul>
      </nav>
    </aside>

    <div class="lg:col-span-9">
      <article
        class="rounded-2xl border border-slate-200/80 bg-white p-6 md:p-8 shadow-sm"
      >
        <h2
          class="text-2xl font-bold tracking-tight text-slate-900 border-b border-slate-100 pb-4 mb-6"
        >
          Community News & Announcements
        </h2>

        <div class="mt-6 space-y-8">
          {#each newsItems as item, i}
            {@const category = getItemCategory(item)}
            {@const styles = getCategoryStyles(category)}
            <div
              id={item.id}
              class="relative flex gap-4 sm:gap-6 group scroll-mt-24"
            >
              <!-- Timeline Left Column -->
              <div class="flex flex-col items-center flex-shrink-0">
                <div
                  class="w-10 h-10 rounded-full flex items-center justify-center border-2 shadow-sm {styles.bg} {styles.hoverBg} transition-all duration-300 transform group-hover:scale-105"
                >
                  {#if category === 'safety'}
                    <!-- Shield Alert Icon -->
                    <ShieldAlert size={20} />
                  {:else if category === 'finance'}
                    <!-- Dollar / SCBD / Finance Icon -->
                    <DollarSign size={20} />
                  {:else if category === 'idea'}
                    <!-- Idea Icon: Glowing Yellow Lightbulb -->
                    <Lightbulb size={20} fill="currentColor" fill-opacity={0.2} />
                  {:else if category === 'improvement'}
                    <!-- Sparkles Icon -->
                    <Sparkles size={20} />
                  {:else if category === 'maintenance'}
                    <!-- Wrench Icon -->
                    <Wrench size={20} />
                  {:else}
                    <!-- Megaphone / Announcement Icon -->
                    <Megaphone size={20} />
                  {/if}
                </div>
                <!-- Vertical timeline connector -->
                {#if i < newsItems.length - 1}
                  <div class="w-[2px] grow bg-slate-100 my-2"></div>
                {/if}
              </div>

              <!-- Content Right Column -->
              <div class="flex-1 pb-8 group-last:pb-2">
                <div
                  class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-2 mb-3"
                >
                  <h3
                    class="text-lg font-bold text-slate-900 leading-snug group-hover:text-blue-600 transition-colors"
                  >
                    {item.title}
                  </h3>
                  <time
                    class="text-xs font-semibold uppercase tracking-wider text-slate-400 whitespace-nowrap sm:shrink-0"
                  >
                    {item.date}
                  </time>
                </div>

                <div
                  class="space-y-3 text-slate-600 text-sm sm:text-base leading-relaxed"
                >
                  {@html item.content}
                </div>

                {#if item.tags.length}
                  <div class="mt-4 flex flex-wrap gap-2">
                    {#each item.tags as tag}
                      <span
                        class="inline-flex items-center rounded-md bg-slate-100 px-2.5 py-1 text-xs font-medium text-slate-600"
                      >
                        {tag}
                      </span>
                    {/each}
                  </div>
                {/if}
              </div>
            </div>
          {/each}
        </div>
      </article>
    </div>
  </div>
</section>
