<script>
  const faqItems = [
    {
      question: 'Are there design requirements as to what changes we can make to our house?',
      answer: 'Yes, there are requirements in the applicable Section Covenants, authorized by the By-Laws and specified in your deed. Examples include fences, outside structures, and other exterior changes. Please read the covenants carefully before submitting an Architectural Change Request.'
    },
    {
      question: 'Is it true that there are appearance requirements for our property in the SCCA By-Laws?',
      answer: 'Yes. The SCCA By-Laws and the Covenants contain appearance requirements. The Board of Directors, elected by homeowners, is required by the By-Laws to ensure these requirements are met in order to preserve the appearance and property values of the community.'
    },
    {
      question: 'When do I have to submit an Architectural Change Request (ACR) to the Architectural Review Committee?',
      answer: 'Any time you make any change to the outside of your house, including color changes, landscaping changes, additions, decks, fences, garage doors, or any other change that costs $500 or more. ACR forms can be found in the Documents section and can be completed, scanned, and emailed.'
    },
    {
      question: 'When and how often does the SCCA meet?',
      answer: 'General membership meetings are held annually in the fall and whenever needed. The date, time, and place are published in advance, usually with the Annual Election Notice & Ballot. Board of Directors meetings are held as needed.'
    },
    {
      question: 'How do I become a Shipley’s Choice Pool member?',
      answer: 'Please see the Shipleys Pool Registration site for details: https://www.shipleyspool.com/'
    },
    {
      question: 'What are covenants?',
      answer: 'Covenants are legally binding obligations that you assumed when you purchased your home in Shipley\'s Choice. The Declaration of Covenants is recorded in the Anne Arundel County land records and governs restrictions such as front yard fences, structure placement, and exterior appearance. It also obligates homeowners to submit plans for outside structures for review before construction begins.'
    },
    {
      question: 'Do the Section 1 Covenants ever expire?',
      answer: 'The Declaration of Covenants must periodically be renewed or extended. The current expiration date is December 31, 2047. The most recent extension occurred in 2017 and the required legal documents are recorded in the Anne Arundel County Land Records.'
    },
    {
      question: 'How can I determine whether my home is in Section 1?',
      answer: 'Section 1 consists of the first 166 lots developed by Monumental Properties and includes streets northeast of Benfield Boulevard such as Arbor Oaks Ct., Rustling Oaks Drive (numbers 1018–1067), Braeburn Glen Ct., Songwood Ct., Briarwick Ct., Tanglewood Ct., Candlewood Ct., Windfern Ct., Galena Ct., Wood Shadows Ct., Lazywood Ct., and others. The section number is also recorded in your deed as part of the property description.'
    },
    {
      question: 'Who currently holds the rights and powers granted by the covenants?',
      answer: 'The developer permanently transferred all rights and powers to the Shipley\'s Choice Community Association (SCCA) in 1980. That transfer was recorded in Anne Arundel County Land Records.'
    },
    {
      question: 'Am I subject to the covenants if I was never given a copy?',
      answer: 'Yes. Because the covenants are recorded in the public land records, they are legally an extension of your deed and part of the property transfer to you. Even if a copy was not provided at settlement, the property remains subject to the covenants.'
    },
    {
      question: 'Am I subject to the covenants if I don’t join the association?',
      answer: 'Yes. All Section 1 residents are subject to the covenants whether or not they choose to join the association. Membership in the Shipley\'s Choice Community Association is not mandatory and does not change the fact that your property remains subject to covenant provisions.'
    }
  ];
</script>

<svelte:head>
  <title>FAQ | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">FAQ</p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">Frequently Asked Questions</h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">Find answers to common questions about covenants, architectural review, meetings, and community membership.</p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12 space-y-6">
  {#each faqItems as item}
    <details class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
      <summary class="cursor-pointer text-lg font-semibold text-slate-900">{item.question}</summary>
      <p class="mt-4 text-slate-700 leading-7">{item.answer}</p>
    </details>
  {/each}
</section>
