<svelte:head>
  <title>Shipley's Choice Community Association</title>
</svelte:head>

<section class="relative bg-slate-900 text-white py-24 px-6 text-center">
  <div class="max-w-3xl mx-auto">
    <h1 class="text-5xl font-extrabold tracking-tight mb-4">Welcome to Shipley's Choice</h1>
    <p class="text-xl text-slate-300 leading-relaxed">
      A vibrant community in Anne Arundel County, Maryland. Stay informed on board activities, local news, and community documents.
    </p>
    <div class="mt-8 flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
      <a href="/meeting-notes" class="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold shadow-lg transition-colors">
        View Meeting Minutes
      </a>
      <a href="/documents" class="px-6 py-3 bg-slate-700 hover:bg-slate-600 rounded-lg font-semibold transition-colors">
        Community Documents
      </a>
    </div>
  </div>
</section>

<section class="max-w-7xl mx-auto py-16 px-4 grid md:grid-cols-2 gap-12">
  <div>
    <h2 class="text-2xl font-bold text-slate-800 mb-4 border-b-2 border-blue-500 inline-block pb-1">Community Overview</h2>
    <p class="text-slate-600 mb-4">Shipley's Choice is known for its beautiful common areas, active community participation, and excellent school district. Our board works to ensure the neighborhood remains a great place to live.</p>
    <p class="text-slate-600">The SCCA (Shipley's Choice Community Association) manages common property maintenance, architectural review, and community events.</p>
  </div>
</section>

<section class="bg-slate-50 border-t border-slate-200 py-16">
  <div class="max-w-7xl mx-auto px-4 grid gap-6 lg:grid-cols-3">
    <article class="rounded-3xl bg-white p-8 shadow-sm border border-slate-200">
      <h3 class="text-xl font-semibold text-slate-900 mb-3">Meeting Minutes</h3>
      <p class="text-slate-600 mb-4">Browse the latest board meeting notes and archives to stay up to date with community decisions.</p>
      <a href="/meeting-notes" class="inline-flex items-center gap-2 font-semibold text-blue-600 hover:text-blue-700">Open archive →</a>
    </article>

    <article class="rounded-3xl bg-white p-8 shadow-sm border border-slate-200">
      <h3 class="text-xl font-semibold text-slate-900 mb-3">Documents</h3>
      <p class="text-slate-600 mb-4">Find community documents, guidelines, and resources for Shipley’s Choice residents.</p>
      <a href="/documents" class="inline-flex items-center gap-2 font-semibold text-blue-600 hover:text-blue-700">View documents →</a>
    </article>

    <article class="rounded-3xl bg-white p-8 shadow-sm border border-slate-200">
      <h3 class="text-xl font-semibold text-slate-900 mb-3">Board & News</h3>
      <p class="text-slate-600 mb-4">Learn about the Board, upcoming meetings, and the latest community newsletter updates.</p>
      <div class="flex flex-col gap-3 sm:flex-row sm:flex-wrap">
        <a href="/board" class="inline-flex items-center gap-2 font-semibold text-blue-600 hover:text-blue-700">Board →</a>
        <a href="/newsletters" class="inline-flex items-center gap-2 font-semibold text-blue-600 hover:text-blue-700">Newsletters →</a>
      </div>
    </article>
  </div>
</section>