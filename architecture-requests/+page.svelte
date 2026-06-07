<script>
  const requests = [
    { date: '2016-07-20', address: '310 Braeburn Ct.', project: 'Fence', section: 'One' },
    { date: '2016-03-29', address: '1049 Rustling Oaks', project: 'Front House Upgrade', section: 'One' },
    { date: '2016-04-12', address: '303 Galena Ct.', project: 'Fence', section: 'One' },
    { date: '2016-08-13', address: '314 Songwood Ct.', project: 'Fence', section: 'One' },
    { date: '2016-09-29', address: '308 Wood Shadows Ct.', project: 'Fence', section: 'One' },
    { date: '2017-11-21', address: '306 Windfern Ct.', project: 'Portico & Walkway', section: 'One' },
    { date: '2018-06-14', address: '1054 Rustling Oaks', project: 'Siding', section: 'One' },
    { date: '2018-07-01', address: '318 Lazywood Ct.', project: 'Roof', section: 'One' },
    { date: '1998-09-28', address: '375 Broadleaf Ct.', project: 'Pool, fence, landscaping', section: 'Two' },
    { date: '2000-05-06', address: '381 Broadleaf Ct.', project: 'Fence', section: 'Two' }
  ];
</script>

<svelte:head>
  <title>Architecture Requests | Shipley's Choice</title>
</svelte:head>

<section class="bg-slate-900 text-white py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Architecture requests</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">Architectural Change Requests</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">Submit your ACR form and review current requirements for home improvements, fences, and exterior modifications.</p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12 space-y-8">
  <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">Submit an architectural request</h2>
    <p class="text-slate-700 mb-6">Please email completed Architectural Change Request forms to the SCCA architectural chairman.</p>
    <p class="text-slate-700"><span class="font-semibold">Email:</span> [email protected]</p>
    <div class="mt-6 grid gap-6 md:grid-cols-2">
      <a href="https://www.shipleyschoice.org/uploads/1/4/6/6/146632212/scca_architectural_request_form.docx" target="_blank" rel="noreferrer" class="rounded-3xl border border-slate-200 bg-slate-50 p-6 text-slate-800 hover:bg-slate-100 transition-colors">
        <h3 class="font-semibold mb-2">ACR form</h3>
        <p>Download the Architectural Change Request form.</p>
      </a>
      <a href="https://www.shipleyschoice.org/uploads/1/4/6/6/146632212/scca_fence_standards_v4%5B389%5D.pdf" target="_blank" rel="noreferrer" class="rounded-3xl border border-slate-200 bg-slate-50 p-6 text-slate-800 hover:bg-slate-100 transition-colors">
        <h3 class="font-semibold mb-2">Fence standards</h3>
        <p>Download the current fence standards and guidelines.</p>
      </a>
    </div>
  </div>

  <div class="rounded-3xl border border-slate-200 bg-slate-50 p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">Recent requests</h2>
    <p class="text-slate-700 mb-6">These examples were published by the community review committee.</p>
    <div class="overflow-x-auto rounded-3xl border border-slate-200 bg-white">
      <table class="min-w-full text-left text-sm text-slate-700">
        <thead class="bg-slate-100 text-slate-900">
          <tr>
            <th class="px-4 py-3 font-semibold">Date</th>
            <th class="px-4 py-3 font-semibold">Address</th>
            <th class="px-4 py-3 font-semibold">Project</th>
            <th class="px-4 py-3 font-semibold">Section</th>
          </tr>
        </thead>
        <tbody>
          {#each requests as item}
            <tr class="border-t border-slate-200">
              <td class="px-4 py-3">{item.date}</td>
              <td class="px-4 py-3">{item.address}</td>
              <td class="px-4 py-3">{item.project}</td>
              <td class="px-4 py-3">{item.section}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</section>
