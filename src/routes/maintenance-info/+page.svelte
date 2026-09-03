<script>
  // Svelte 5 state rune for tracking active tab
  let activeTab = $state('protection');
</script>

<svelte:head>
  <title>Maintenance Information | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
      Community Maintenance & Rules
    </p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
      Maintenance & Common Area Guidelines
    </h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Important regulations and responsibilities regarding SCCA common properties,
      community aesthetics, utility clearance, and resident-association stewardship.
    </p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12 space-y-12">
  <!-- Interactive Warning Banner -->
  <div class="rounded-3xl border border-amber-200 bg-amber-50/40 p-6 md:p-8 shadow-sm flex flex-col md:flex-row gap-6 items-start">
    <div class="p-3 bg-amber-100 text-amber-800 rounded-2xl flex-shrink-0">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m0-10.036A11.959 11.959 0 0 1 3.598 6 11.99 11.99 0 0 0 3 9.75c0 5.592 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.57-.598-3.75h-.152c-3.196 0-6.1-1.249-8.25-3.286Zm0 13.036h.008v.008H12v-.008Z" />
      </svg>
    </div>
    <div class="space-y-3">
      <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
        Critical Property Encroachment Notice
      </h3>
      <p class="text-slate-700 text-sm md:text-base leading-relaxed">
        SCCA common areas, woodlands, and buffers are collective community assets. 
        <strong>Unauthorized clearing, altering, tree removal, or heavy machinery operation</strong> on SCCA-owned property 
        is strictly prohibited. Under SCCA Bylaws, the Board maintains sole executive power over all corporate property 
        to ensure safety, preserve environmental health, and protect SCCA's general liability insurance policy.
      </p>
      <div class="flex flex-wrap gap-x-6 gap-y-1 text-xs font-semibold text-amber-800">
        <span class="flex items-center gap-1">
          <svg class="w-4.5 h-4.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
          No Heavy Equipment on Roots
        </span>
        <span class="flex items-center gap-1">
          <svg class="w-4.5 h-4.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
          Miss Utility (811) Required
        </span>
        <span class="flex items-center gap-1">
          <svg class="w-4.5 h-4.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
          Full Personal Liability for Violations
        </span>
      </div>
    </div>
  </div>

  <!-- Interactive Tabs Interface -->
  <div class="space-y-6">
    <!-- Tabs Navigation Header -->
    <div class="flex flex-wrap gap-2 border-b border-slate-200 pb-2">
      <button 
        onclick={() => activeTab = 'protection'}
        class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'protection' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 0 1-1.043 3.296 3.745 3.745 0 0 1-3.296 1.043A3.745 3.745 0 0 1 12 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 0 1-3.296-1.043 3.745 3.745 0 0 1-1.043-3.296A3.745 3.745 0 0 1 3 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 0 1 1.043-3.296 3.746 3.746 0 0 1 3.296-1.043A3.746 3.746 0 0 1 12 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 0 1 3.296 1.043 3.746 3.746 0 0 1 1.043 3.296A3.745 3.745 0 0 1 21 12Z" />
        </svg>
        Property & Soil Protection
      </button>

      <button 
        onclick={() => activeTab = 'usage'}
        class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'usage' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m.94 3.198.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0 1 12 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 0 1 6 18.719m12 0a5.971 5.971 0 0 0-.941-3.197m0 0A5.995 5.995 0 0 0 12 12.75a5.995 5.995 0 0 0-5.058 2.772m0 0a3 3 0 0 0-4.681 2.72 8.986 8.986 0 0 0 3.74.477m.94-3.197a5.971 5.971 0 0 0-.94 3.197M15 6.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Zm-13.5 0a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z" />
        </svg>
        Common Area Usage
      </button>

      <button 
        onclick={() => activeTab = 'utility'}
        class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'utility' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 3h.01M12 6.5h.01M12 10h.01M12 13.5h.01M12 17h.01M12 20.5h.01M5 12h.01M8.5 12h.01M12 12h.01M15.5 12h.01M19 12h.01M3 12a9 9 0 1 1 18 0 9 9 0 0 1-18 0Z" stroke-dasharray="2 2" />
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v18M3 12h18" />
        </svg>
        Utility & 811 Clearance
      </button>

      <button 
        onclick={() => activeTab = 'beautification'}
        class="flex items-center gap-2 px-5 py-3 rounded-t-2xl font-semibold transition-all duration-200 text-sm md:text-base border-b-2 -mb-[10px] {activeTab === 'beautification' ? 'border-blue-600 text-blue-600 bg-blue-50/40 shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-50'}"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 10.5v1.375m0-1.375a3.375 3.375 0 1 0-3.375-3.375H12M12 10.5a3.375 3.375 0 1 1 3.375-3.375H12m0 3.875v7.5m0-7.5H4.875a1.125 1.125 0 0 1-.75-1.961l5.441-4.76A1.125 1.125 0 0 1 10.313 3h3.374a1.125 1.125 0 0 1 .748 1.965l5.44 4.76a1.125 1.125 0 0 1-.749 1.961H12Z" />
        </svg>
        Beautification & Stewardship
      </button>
    </div>

    <!-- Tab Content Area -->
    <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm min-h-[350px]">
      {#if activeTab === 'protection'}
        <div class="space-y-6">
          <div class="border-b border-slate-100 pb-4">
            <h2 class="text-2xl font-extrabold text-slate-900">Property & Soil Protection Policy</h2>
            <p class="text-slate-500 text-sm mt-1">Preserving community tree life, soil structure, and managing common area boundary integrity.</p>
          </div>

          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-red-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                Soil Compaction & Mature Trees
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Operating heavy machinery or parking vehicles over root zones compresses the soil, cutting off critical water and oxygen pathways. 
                Mature tree roots are incredibly sensitive; compaction causes rapid root decay, leading to hazardous dead trees that cost the association thousands of dollars to safely remove. 
                SCCA strictly prohibits unauthorized machinery in common wooded areas.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-slate-800 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                Board Executive Stewardship
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Under <strong>Article VIII, Section 1</strong>, SCCA's Officers and Directors are charged with executive authority over all corporate assets, properties, and committees. 
                Permitting individual residents to unilaterally clear or claim parts of SCCA common lands undermines collective governance and creates harmful legal precedents of unapproved encroachment.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-amber-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                Insurance Exclusion & Personal Risk
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Our general liability insurance covers approved actions by the Board or appointed committees to protect the community. 
                If an unauthorized homeowner or their contractor performs unapproved landscaping or heavy clearing on SCCA land, the carrier may exclude coverage. 
                The initiating homeowner then bears 100% of the financial and civil liability for any property damages, utility breaks, or personal injuries.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-emerald-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                Encroachment Restrictions
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Property lines are strictly defined in community plat maps (available under <a href="/documents" class="text-blue-600 hover:underline font-semibold">Documents</a>). 
                Dumping yard waste, compost, leaves, or erecting private structures (such as playsets, sheds, fences, or stone boundaries) beyond private lines into SCCA common land is considered encroachment and must be rectified immediately.
              </p>
            </div>
          </div>
        </div>
      {:else if activeTab === 'usage'}
        <div class="space-y-6">
          <div class="border-b border-slate-100 pb-4">
            <h2 class="text-2xl font-extrabold text-slate-900">Common Area Usage & Privileges</h2>
            <p class="text-slate-500 text-sm mt-1">Established by Article IV of the Shipley's Choice Community Association Bylaws.</p>
          </div>

          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-blue-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                Ordinary Use & Good Standing
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Under <strong>Article IV, Section 1</strong>, membership in good standing (meaning dues are current) entitles members 
                and their guests to the ordinary use of all SCCA facilities and common areas, subject to rules established by the Board and appropriate committees.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-blue-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                Accompanied Guest Rules
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Homeowners enjoy hosting guests on common properties. However, under <strong>Article IV, Section 2</strong>, 
                any guest must be accompanied by an SCCA member. Crucially, **no resident of Shipley's Choice may qualify as a guest** 
                of another member. Local residents must belong to a household in good standing to enjoy community assets.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-blue-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                Use At Own Risk
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                According to <strong>Article IV, Section 3</strong>, all persons who use Association facilities do so at their own risk. 
                Be mindful of local wildlife, natural trail unevenness, and woodland hazards when exploring the common properties.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-blue-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                Exclusivity of Facilities
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Per <strong>Article IV, Section 4</strong>, any facilities erected, purchased, or improved by SCCA shall only be enjoyed 
                by members of the Association in good standing and their guests. Active participation and dues support the upkeep and safety of these shared structures.
              </p>
            </div>
          </div>
        </div>
      {:else if activeTab === 'utility'}
        <div class="space-y-6">
          <div class="border-b border-slate-100 pb-4">
            <h2 class="text-2xl font-extrabold text-slate-900">Maryland Utility Clearance & Safe Excavation</h2>
            <p class="text-slate-500 text-sm mt-1">Understanding legal mandates for digging and protecting underground community infrastructure.</p>
          </div>

          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-amber-800 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                Maryland "Miss Utility" State Law
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Maryland law (<strong>Public Utilities Article §§ 12-101 – 135</strong>) strictly mandates that anyone planning to perform 
                excavation, grading, or operation of heavy digging machinery must notify Miss Utility by dialing <strong>811</strong> 
                at least three business days prior to commencing any work. This is a legally binding safety regulation.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-slate-800 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Common Area Infrastructure
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Shared community open spaces and wooded buffers contain essential underground public utility systems, sewer mains, stormwater drainage pipes, 
                and electrical conduits. Under <strong>Article II, Section 1</strong>, the Association has care and jurisdiction over the appearance and integrity of these open spaces. Unclear digging poses massive safety risks.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200 md:col-span-2">
              <div class="flex items-center gap-2 text-blue-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                What to do if doing boundary work
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                If you are hiring a contractor to perform grading, install a fence, or construct adjacent structures near common areas:
              </p>
              <ul class="list-disc list-inside space-y-1.5 pl-4 text-slate-700 text-sm font-medium">
                <li>Submit an <a href="/architecture-requests" class="text-blue-600 hover:underline">Architectural Change Request</a> to the committee.</li>
                <li>Ensure your contractor explicitly calls <strong>811 (Miss Utility)</strong> to mark out all public easements and lines.</li>
                <li>Confirm exact property boundaries on official plats to avoid accidentally digging or grading inside SCCA-owned woodlands.</li>
              </ul>
            </div>
          </div>
        </div>
      {:else if activeTab === 'beautification'}
        <div class="space-y-6">
          <div class="border-b border-slate-100 pb-4">
            <h2 class="text-2xl font-extrabold text-slate-900">Beautification & Environmental Stewardship</h2>
            <p class="text-slate-500 text-sm mt-1">How the Association and residents cooperate under Article IX to preserve Shipley's Choice aesthetics.</p>
          </div>

          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-emerald-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707-.707M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                The Beautification Committee
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Under <strong>Article IX, Section 2(d)</strong>, the SCCA Beautification Committee is responsible for keeping Shipley's Choice clean and beautiful. 
                They oversee the landscaping of all community entrance properties, schedule regular maintenance, and coordinate cleanliness and beautification campaigns.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200">
              <div class="flex items-center gap-2 text-emerald-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                Private Lot Appearance Standards
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                The SCCA Beautification Committee actively encourages all residents to maintain high visual standards in the landscaping and exterior care of their individual lots. 
                Keeping private yards well-groomed, weeding, and promptly removing dead private trees directly supports community aesthetics and sustains home values.
              </p>
            </div>

            <div class="space-y-3 p-5 rounded-2xl bg-slate-50 border border-slate-200 md:col-span-2">
              <div class="flex items-center gap-2 text-emerald-700 font-bold">
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.003 9.003 0 008.354-5.646 9.003 9.003 0 00-11.758-11.758A9.003 9.003 0 0012 21z"/></svg>
                County Environmental Compliance
              </div>
              <p class="text-slate-700 text-sm leading-relaxed">
                Our SCCA common grounds fall under strict <strong>Anne Arundel County Environmental and Land-Use Regulations</strong> governing open spaces and tree canopy preservation. 
                SCCA is legally obliged to keep these common wooded buffers wild and undeveloped, ensuring proper soil containment, stormwater filtering, and environmental stewardship for local watersheds.
              </p>
            </div>
          </div>
        </div>
      {/if}
    </div>
  </div>

  <!-- Help & Resources Dashboard -->
  <div class="space-y-6">
    <h3 class="text-2xl font-bold text-slate-900 text-center">Maintenance Resources & Rapid Response</h3>
    <div class="grid gap-6 md:grid-cols-3">
      <!-- Card 1 -->
      <article class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm flex flex-col justify-between hover:border-slate-300 transition-all duration-200">
        <div class="space-y-3">
          <div class="p-3 bg-red-50 text-red-700 rounded-2xl w-fit">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
            </svg>
          </div>
          <h4 class="text-lg font-bold text-slate-900">Hazardous Trees</h4>
          <p class="text-slate-600 text-sm leading-relaxed">
            Spotted a dead or dangerously leaning tree on SCCA common property? Report it immediately for expert inspection and removal.
          </p>
        </div>
        <a href="/trees" class="mt-6 inline-flex items-center justify-center px-4 py-2 bg-slate-900 text-white rounded-xl text-sm font-semibold hover:bg-slate-800 transition-colors">
          Report Common Tree
        </a>
      </article>

      <!-- Card 2 -->
      <article class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm flex flex-col justify-between hover:border-slate-300 transition-all duration-200">
        <div class="space-y-3">
          <div class="p-3 bg-blue-50 text-blue-700 rounded-2xl w-fit">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
            </svg>
          </div>
          <h4 class="text-lg font-bold text-slate-900">Architectural Requests</h4>
          <p class="text-slate-600 text-sm leading-relaxed">
            Planning changes on your lot that cost over $500 or alter exterior colors? Submit an Architectural Change Request (ACR).
          </p>
        </div>
        <a href="/architecture-requests" class="mt-6 inline-flex items-center justify-center px-4 py-2 bg-slate-900 text-white rounded-xl text-sm font-semibold hover:bg-slate-800 transition-colors">
          Submit ACR Form
        </a>
      </article>

      <!-- Card 3 -->
      <article class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm flex flex-col justify-between hover:border-slate-300 transition-all duration-200">
        <div class="space-y-3">
          <div class="p-3 bg-emerald-50 text-emerald-700 rounded-2xl w-fit">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 11.082 1.25l-.04.02a.75.75 0 01-.083-1.25zM12 21a9 9 0 110-18 9 9 0 010 18zm0-15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 11.25a.75.75 0 100-1.5.75.75 0 000 1.5z" />
            </svg>
          </div>
          <h4 class="text-lg font-bold text-slate-900">Official SCCA Documents</h4>
          <p class="text-slate-600 text-sm leading-relaxed">
            Need to download the full, officially recorded SCCA Bylaws, Section Covenants, plat maps, or fence standards?
          </p>
        </div>
        <a href="/documents" class="mt-6 inline-flex items-center justify-center px-4 py-2 bg-slate-900 text-white rounded-xl text-sm font-semibold hover:bg-slate-800 transition-colors">
          Browse Documents
        </a>
      </article>
    </div>
  </div>
</section>
