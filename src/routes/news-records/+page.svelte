<script>
  import meetingNotes from '../../data/meetingNotes.json';
  const latestMeetingNotes = meetingNotes.slice(0, 5);
</script>

<svelte:head>
  <title>News & Records | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">News &amp; records</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">News, newsletters, and meeting minutes</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">Download the latest community newsletter, browse archived records, and view recent meeting minutes.</p>
  </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-12 space-y-8">
  <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">Latest newsletter</h2>
    <p class="text-slate-700 mb-6">The most recent community newsletter from the legacy site is available as a PDF. If your browser does not support previewing it, download the file directly.</p>
    <a href="https://www.shipleyschoice.org/uploads/1/4/6/6/146632212/newsletter_2025.pdf" target="_blank" rel="noreferrer" class="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 text-white font-semibold shadow-sm hover:bg-blue-700 transition-colors">
      Download latest newsletter (PDF)
    </a>
  </div>
  
  <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">Recent meeting minutes</h2>
    <p class="text-slate-700 mb-6">This section includes recent meeting notes from the Shipley's Choice Community Association board.</p>
    <div class="space-y-3">
      {#each latestMeetingNotes as meeting}
        <div class="rounded-2xl border border-slate-200 bg-slate-50 p-4">
          <p class="font-semibold text-slate-900">{meeting.dateLabel}</p>
          <p class="text-sm text-slate-600">{meeting.participants}</p>
        </div>
      {/each}
    </div>
    <p class="mt-6 text-slate-700">To browse the full archive, visit <a href="/meeting-notes" class="text-blue-600 hover:text-blue-700 underline">Meeting Notes</a>.</p>
  </div>
</section>
