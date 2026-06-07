<script>
  import meetingNotes from '../data/meetingNotes.json';

  let selectedId = meetingNotes?.[0]?.id;
  $: selectedMeeting = meetingNotes.find((meeting) => meeting.id === selectedId);
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

<section class="max-w-7xl mx-auto px-4 py-12 grid gap-8 lg:grid-cols-[300px_1fr]">
  <aside class="space-y-4">
    <div class="rounded-3xl border border-slate-200 bg-white shadow-sm overflow-hidden">
      <div class="bg-slate-50 px-5 py-4 border-b border-slate-200 text-slate-700 font-semibold">Meeting Dates</div>
      <div class="divide-y divide-slate-100">
        {#each meetingNotes as meeting}
          <button
            type="button"
            on:click={() => selectedId = meeting.id}
            class="w-full text-left px-5 py-4 transition-colors duration-150 focus:outline-none {selectedId === meeting.id ? 'bg-blue-600 text-white' : 'bg-white text-slate-700 hover:bg-slate-50'}"
          >
            {meeting.dateLabel}
          </button>
        {/each}
      </div>
    </div>
  </aside>

  <article class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    {#if selectedMeeting}
      <div class="space-y-5">
        <div>
          <p class="text-sm uppercase tracking-[0.24em] text-blue-600">Selected meeting</p>
          <h2 class="mt-2 text-3xl font-bold text-slate-900">{selectedMeeting.dateLabel}</h2>
          <p class="mt-3 text-sm text-slate-500"><span class="font-semibold text-slate-700">Attendees:</span> {selectedMeeting.participants}</p>
        </div>

        <div class="space-y-6 text-slate-700 leading-7">
          {#each selectedMeeting.content.split('\n\n') as paragraph}
            <p>{paragraph}</p>
          {/each}
        </div>
      </div>
    {:else}
      <div class="text-slate-600">No meeting selected yet.</div>
    {/if}
  </article>
</section>
