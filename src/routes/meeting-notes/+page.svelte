<script>
  import { onMount, onDestroy } from 'svelte';
  import meetingNotes from '$data/meetingNotes.json';

  let activeId = '';
  let observer;

  onMount(() => {
    // Set the first item as active on initial load
    if (meetingNotes.length > 0) {
      activeId = meetingNotes[0].id;
    }

    const sections = meetingNotes.map((item) => document.getElementById(item.id));

    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -60% 0px',
      threshold: 0
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
  <title>Meeting Notes | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Meeting notes</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">SCCA Board Meeting Minutes</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">Select a meeting date to view the official minutes for Shipley's Choice Community Association board meetings.</p>
  </div>
</section>

<section class="max-w-7xl mx-auto px-4 py-12">
  <div class="lg:grid lg:grid-cols-12 lg:gap-12">
    <aside class="hidden lg:block lg:col-span-3">
      <nav class="sticky top-24">
        <h3 class="font-semibold text-slate-900">Meeting Dates</h3>
        <ul class="mt-4 space-y-1 border-l-2 border-slate-100">
          {#each meetingNotes as item}
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
                {item.dateLabel}
              </a>
            </li>
          {/each}
        </ul>
      </nav>
    </aside>

    <div class="lg:col-span-9">
      <article class="rounded-2xl border border-slate-200/80 bg-white p-6 md:p-8 shadow-sm">
        <div class="divide-y divide-slate-100">
          {#each meetingNotes as meeting}
            <div id={meeting.id} class="py-8 first:pt-0 last:pb-0 group scroll-mt-20">
              <div class="space-y-5">
                <div>
                  <h2 class="text-2xl font-bold text-slate-900">{meeting.dateLabel}</h2>
                  <p class="mt-3 text-sm text-slate-500"><span class="font-semibold text-slate-700">Attendees:</span> {meeting.participants}</p>
                </div>

                <div class="space-y-6 text-slate-700 leading-7">
                  {#each meeting.content.split('\n\n') as paragraph}
                    <p>{paragraph}</p>
                  {/each}
                </div>
              </div>
            </div>
          {/each}
        </div>
      </article>
    </div>
  </div>
</section>
