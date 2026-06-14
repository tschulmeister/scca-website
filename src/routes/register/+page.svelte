<script>
  let formData = {
    email: "",
    name: "",
    phone: "",
    address: "",
  };

  // Dynamically generate the mailto link with structured subject and body text
  $: {
    const emailTo = "shipleyschoice.scca@gmail.com";
    const subject = encodeURIComponent(
      `SCCA Registration Request: ${formData.name || "New Resident"}`,
    );

    const bodyText = `Dear SCCA Board,

Please register me to receive future email newsletters, announcements, and community updates for Shipley's Choice.

Here is my contact information:

Name: ${formData.name}
Email: ${formData.email}
Phone: ${formData.phone || "Not provided"}
Address: ${formData.address || "Not provided"}

Thank you!`;

    const body = encodeURIComponent(bodyText);

    // Combine everything into a single structural mailto link
    mailtoUrl = `mailto:${emailTo}?subject=${subject}&body=${body}`;
  }

  let mailtoUrl = "";
</script>

<svelte:head>
  <title>Register | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Register</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
      Sign up for updates
    </h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Share your contact information with the board to receive the annual
      newsletter and pertinent community news. 
    </p>
  </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-12">
  <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    <h2 class="text-2xl font-bold text-slate-900 mb-6">Contact registration</h2>

    <form class="space-y-6">
      <div class="grid gap-6 md:grid-cols-2">
        <label class="block">
          <span class="text-slate-700">Name *</span>
          <input
            bind:value={formData.name}
            type="text"
            required
            class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none"
          />
        </label>
        <label class="block">
          <span class="text-slate-700">Email *</span>
          <input
            bind:value={formData.email}
            type="email"
            required
            class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none"
          />
        </label>
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <label class="block md:col-span-1">
          <span class="text-slate-700"
            >Phone Number <span class="text-sm text-slate-400 font-normal"
              >(Optional)</span
            ></span
          >
          <input
            bind:value={formData.phone}
            type="tel"
            class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none"
          />
        </label>
        <label class="block md:col-span-2">
          <span class="text-slate-700">Street Address *</span>
          <input
            bind:value={formData.address}
            type="text"
            required
            placeholder="e.g., 123 Main St"
            class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 focus:border-blue-500 focus:outline-none"
          />
        </label>
      </div>

      <div class="pt-2">
        <a
          href={mailtoUrl}
          class="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 text-white font-semibold shadow-sm hover:bg-blue-700 transition-colors no-underline"
        >
          Generate Registration Email
        </a>
      </div>
    </form>
  </div>
</section>
