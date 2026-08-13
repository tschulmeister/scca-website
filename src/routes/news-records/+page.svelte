<script>
  import { onMount, onDestroy } from "svelte";
  import newsItems from "$data/newsItems.json";

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

        <div class="divide-y divide-slate-100">
          {#each newsItems as item}
            <div
              id={item.id}
              class="py-6 first:pt-0 last:pb-0 group scroll-mt-20"
            >
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
          {/each}
        </div>
      </article>
    </div>
  </div>
</section>
