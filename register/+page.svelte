<script>
  let submitted = false;
  let formData = {
    email: '',
    name: '',
    address1: '',
    address2: '',
    city: '',
    state: '',
    zip: '',
    country: ''
  };

  function handleSubmit() {
    submitted = true;
  }
</script>

<svelte:head>
  <title>Register | Shipley's Choice</title>
</svelte:head>

<section class="bg-slate-900 text-white py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Register</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">Sign up for updates</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">Register your contact information to receive future email newsletters, announcements, and community updates.</p>
  </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-12">
  {#if submitted}
    <div class="rounded-3xl border border-green-200 bg-green-50 p-8 text-green-900 shadow-sm">
      <h2 class="text-2xl font-bold mb-4">Thank you!</h2>
      <p>Your registration information has been recorded on this page demo. Please contact the Board to finalize your subscription.</p>
    </div>
  {:else}
    <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
      <h2 class="text-2xl font-bold text-slate-900 mb-6">Contact registration</h2>
      <form on:submit|preventDefault={handleSubmit} class="space-y-6">
        <div class="grid gap-6 md:grid-cols-2">
          <label class="block">
            <span class="text-slate-700">Email *</span>
            <input bind:value={formData.email} type="email" required class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
          <label class="block">
            <span class="text-slate-700">Name *</span>
            <input bind:value={formData.name} type="text" required class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
        </div>

        <div>
          <label class="block">
            <span class="text-slate-700">Address Line 1</span>
            <input bind:value={formData.address1} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
        </div>

        <div>
          <label class="block">
            <span class="text-slate-700">Address Line 2</span>
            <input bind:value={formData.address2} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
        </div>

        <div class="grid gap-6 md:grid-cols-3">
          <label class="block">
            <span class="text-slate-700">City</span>
            <input bind:value={formData.city} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
          <label class="block">
            <span class="text-slate-700">State</span>
            <input bind:value={formData.state} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
          <label class="block">
            <span class="text-slate-700">Zip Code</span>
            <input bind:value={formData.zip} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
          </label>
        </div>

        <label class="block">
          <span class="text-slate-700">Country</span>
          <input bind:value={formData.country} type="text" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none" />
        </label>

        <button type="submit" class="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 text-white font-semibold shadow-sm hover:bg-blue-700 transition-colors">Submit registration</button>
      </form>
    </div>
  {/if}

  <div class="mt-10 rounded-3xl border border-slate-200 bg-slate-50 p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">Alternative contact</h2>
    <p class="text-slate-700">If you prefer, send your name and contact details to the Board email address listed on the Contact page so you can receive future newsletters and announcements.</p>
  </div>
</section>
