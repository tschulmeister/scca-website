<script>
  import newsItems from "$data/newsItems.json";
  import Newspaper from "@lucide/svelte/icons/newspaper";
  import ClipboardList from "@lucide/svelte/icons/clipboard-list";
  import Users from "@lucide/svelte/icons/users";
  import ShieldAlert from "@lucide/svelte/icons/shield-alert";
  import ArrowRight from "@lucide/svelte/icons/arrow-right";
  import HelpCircle from "@lucide/svelte/icons/help-circle";
  import History from "@lucide/svelte/icons/history";
  import Mail from "@lucide/svelte/icons/mail";

  // The `newsItems` are now imported directly.
  $: latestNews = newsItems?.[0];
  $: latestThreeNews = newsItems?.slice(0, 3) ?? [];
</script>

<svelte:head>
  <title>Shipley's Choice Community Association</title>
</svelte:head>

<section class="page-header py-12 sm:py-24 px-4 sm:px-6 text-center">
  <div class="max-w-3xl mx-auto">
    <!-- Active SCBD Banner with fine animations -->
    <div
      class="mb-10 p-6 sm:p-8 bg-slate-900/95 border border-blue-500/30 rounded-3xl shadow-2xl backdrop-blur-md max-w-2xl mx-auto text-center animate-fadeIn"
    >
      <div
        class="inline-flex items-center gap-2 px-5 py-1.5 bg-blue-500/20 text-blue-300 border border-blue-400/20 text-xs font-bold rounded-2xl mb-4"
      >
        <span class="relative flex h-2.5 w-2.5">
          <span
            class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"
          ></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-500"
          ></span>
        </span>
        SCBD Petition & Information Drive Active
      </div>

      <h2 class="text-xl sm:text-2xl font-black text-white mb-3 tracking-tight">
        Help Secure our Community's Future
      </h2>

      <p class="text-sm text-slate-300 mb-6 leading-relaxed max-w-lg mx-auto font-medium">
        We are currently conducting an educational outreach and petition effort
        to establish a Special Community Benefits District (SCBD) in Shipley's
        Choice. Explore how this transition protects our community and find
        answers to common questions.
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a
          href="/why-scbd"
          class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-md hover:shadow-lg transition-all text-sm animate-button"
        >
          Why SCBD?
          <ArrowRight class="w-4 h-4" />
        </a>
        <a
          href="/why-scbd-faq"
          class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 bg-slate-800 text-blue-300 border border-slate-700 hover:bg-slate-700 hover:text-white transition-all text-sm font-bold"
        >
          SCBD FAQ
          <HelpCircle class="w-4 h-4" />
        </a>
      </div>
    </div>

    <h1 class="text-5xl md:text-6xl font-black tracking-tight mb-4 text-white">
      Welcome to Shipley's Choice
    </h1>
    <p class="text-xs text-blue-200 tracking-widest uppercase font-bold bg-blue-500/10 w-fit mx-auto px-5 py-1.5 rounded-2xl border border-blue-400/20 mb-6 leading-relaxed">
      Mailbox: 315 Arbor Oaks Ct, Millersville, MD 21108
    </p>
    <p class="text-xl text-slate-300 leading-relaxed max-w-2xl mx-auto font-medium">
      A vibrant community in Anne Arundel County, Maryland. Stay informed on
      board activities, local news, and community documents.
    </p>
  </div>

  <!-- Transparent Header Overlay Cards -->
  <div class="max-w-7xl mx-auto w-full px-2 sm:px-4 grid gap-6 lg:grid-cols-3 mt-10 sm:mt-16 text-left">
    <!-- Card 1: News -->
    <article
      class="rounded-3xl bg-white/10 p-6 sm:p-8 shadow-xl border border-white/20 backdrop-blur-md flex flex-col justify-between min-w-0"
    >
      <div class="space-y-4">
        <div class="flex flex-col gap-3">
          <div class="flex items-center gap-3">
            <div class="p-2.5 bg-blue-500/20 text-blue-300 border border-blue-400/20 rounded-2xl flex-shrink-0">
              <Newspaper class="w-5 h-5" />
            </div>
            <h3 class="text-lg sm:text-xl font-black text-white leading-tight">Community News</h3>
          </div>
          {#if latestNews}
            <div class="w-fit text-[10px] font-bold uppercase tracking-wider text-blue-300 bg-blue-500/20 border border-blue-400/20 px-3.5 py-1 rounded-2xl">
              Latest Bulletin: {latestNews.date}
            </div>
          {/if}
        </div>
        
        <ul class="space-y-3.5 text-slate-200 text-sm">
          {#each latestThreeNews as item}
            <li class="flex items-start gap-2.5">
              <ArrowRight class="w-4 h-4 text-blue-400 flex-shrink-0 mt-0.5" />
              <span class="font-medium hover:text-white transition-colors cursor-pointer leading-snug">{item.title}</span>
            </li>
          {/each}
        </ul>
      </div>

      <a
        href="/news-records"
        class="inline-flex items-center gap-2 font-bold text-blue-300 hover:text-blue-200 mt-6 group text-sm"
      >
        View News Records
        <ArrowRight class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" />
      </a>
    </article>

    <!-- Card 2: Arch -->
    <article
      class="rounded-3xl bg-white/10 p-6 sm:p-8 shadow-xl border border-white/20 backdrop-blur-md flex flex-col justify-between min-w-0"
    >
      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <div class="p-2.5 bg-blue-500/20 text-blue-300 border border-blue-400/20 rounded-2xl flex-shrink-0">
            <ClipboardList class="w-5 h-5" />
          </div>
          <h3 class="text-lg sm:text-xl font-black text-white leading-tight">Architectural Requests</h3>
        </div>
        <p class="text-slate-200 text-sm leading-relaxed font-medium">
          Planning a home improvement? SCCA requires homeowners to submit an ACR form for fence standards, paint alterations, and exterior changes.
        </p>

        <div class="border-t border-white/15 pt-4">
          <p class="text-slate-300 text-xs leading-relaxed mb-3 font-semibold flex items-center gap-1.5 text-amber-300">
            <ShieldAlert class="w-4 h-4 flex-shrink-0" />
            Woodland Tree Management
          </p>
          <p class="text-slate-200 text-xs leading-relaxed font-medium mb-3">
            Concerned about a dead or leaning tree in common buffers? Report it for safety inspections.
          </p>
          <a
            href="/trees"
            class="inline-flex items-center gap-2 font-bold text-blue-300 hover:text-blue-200 text-xs"
          >
            Woodland Trees & Safety →
          </a>
        </div>
      </div>

      <a
        href="/architecture-requests"
        class="inline-flex items-center gap-2 font-bold text-blue-300 hover:text-blue-200 mt-6 group text-sm"
      >
        View Requirements & ACR Form
        <ArrowRight class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" />
      </a>
    </article>

    <!-- Card 3: Newsletter Sign-Up -->
    <article
      class="rounded-3xl bg-white/10 p-6 sm:p-8 shadow-xl border border-white/20 backdrop-blur-md flex flex-col justify-between min-w-0"
    >
      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <div class="p-2.5 bg-blue-500/20 text-blue-300 border border-blue-400/20 rounded-2xl flex-shrink-0">
            <Mail class="w-5 h-5" />
          </div>
          <h3 class="text-lg sm:text-xl font-black text-white leading-tight">Stay Connected</h3>
        </div>
        <p class="text-slate-200 text-sm leading-relaxed font-medium">
          Register your email address to receive official SCCA newsletters, board notices, financial summaries, and critical neighborhood safety updates directly in your inbox.
        </p>

        <div class="border-t border-white/15 pt-4">
          <p class="text-slate-200 text-xs leading-relaxed font-semibold mb-2">
            For official inquiries, direct board matters, or legal correspondence:
          </p>
          <a
            href="mailto:shipleyschoice.scca@gmail.com"
            class="inline-flex items-center gap-2 font-bold text-blue-300 hover:text-blue-200 text-xs break-all"
          >
            shipleyschoice.scca@gmail.com
          </a>
        </div>
      </div>

      <a
        href="/register"
        class="inline-flex items-center gap-2 font-bold text-blue-300 hover:text-blue-200 mt-6 group text-sm"
      >
        Register for SCCA Updates
        <ArrowRight class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" />
      </a>
    </article>
  </div>
</section>

<!-- Main Details Layout with elegant graphical items -->
<section class="max-w-7xl mx-auto py-16 px-4">
  <div class="grid gap-8 lg:grid-cols-2">
    <!-- Card 1: Community Overview -->
    <article class="rounded-3xl bg-white p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
      <div>
        <h2
          class="text-2xl font-black text-slate-900 mb-4 border-b-4 border-blue-500 inline-block pb-1"
        >
          Community Overview
        </h2>
        <p class="text-slate-600 mb-6 leading-relaxed">
          Shipley’s Choice is a community of single family homes in the Greater
          Severna Park area north of Annapolis, MD, nestled in the suburbs between
          Washington, DC and Baltimore.
        </p>
        <p class="text-slate-700 font-bold text-sm mb-4">
          The neighborhood is divided into two separate, independent community organizations:
        </p>
        
        <div class="space-y-4">
          <!-- SCCA Info -->
          <div
            class="rounded-2xl bg-blue-50/50 p-5 border border-blue-100 shadow-sm"
          >
            <div class="flex items-center gap-2 mb-2">
              <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
              <p class="font-bold text-slate-900 text-sm md:text-base">
                Shipley's Choice Community Association (SCCA)
              </p>
            </div>
            <p class="text-slate-600 text-xs md:text-sm leading-relaxed">
              This site is dedicated to serving the <strong>283 homes</strong> that make up
              <strong>sections 1 and 2</strong> of Shipley's Choice.
            </p>
            <p class="mt-3 text-xs">
              For a list of streets and addresses in the SCCA, please refer to the 
              <a href="/information" class="text-blue-600 font-bold hover:underline">Street Directory Information</a> page.
            </p>
          </div>

          <!-- SCHOA Info -->
          <div
            class="rounded-2xl bg-amber-50/50 p-5 border border-amber-100 shadow-sm"
          >
            <div class="flex items-center gap-2 mb-2">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-600"></span>
              <p class="font-bold text-slate-900 text-sm md:text-base">
                Shipley's Choice Home Owners Association (SCHOA)
              </p>
            </div>
            <p class="text-slate-600 text-xs md:text-sm leading-relaxed">
              The SCHOA is a <em>separate</em> organization which represents the
              homes of <strong>sections 3 through 12</strong> of Shipley's Choice.
            </p>
            <p class="mt-3 text-xs">
              Please refer to the 
              <a href="https://www.shipleyschoice.com/" class="text-amber-700 font-bold hover:underline">SCHOA Website</a> for information regarding sections 3-12.
            </p>
          </div>
        </div>
      </div>
    </article>

    <!-- Card 2: Location & History -->
    <article class="rounded-3xl bg-white p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
      <div>
        <h3 class="text-2xl font-black text-slate-900 mb-4 border-b-4 border-slate-700 inline-block pb-1">
          Location & History
        </h3>
        <p class="text-slate-600 text-sm leading-relaxed">
          Shipley’s Choice is ideally located in Anne Arundel County, MD; about 10
          miles north of <a href="http://www.ci.annapolis.md.us/" class="text-blue-600 hover:underline font-semibold">Annapolis</a>, the
          <a href="http://www.annapolis.gov/visitors/gateway-to-discovery/americas-sailing-capital" class="text-blue-600 hover:underline font-semibold">sailing capital</a>
          of the United States and the seat of Maryland state
          <a href="http://www.maryland.gov/Pages/default.aspx" class="text-blue-600 hover:underline font-semibold">government</a>.
          Annapolis is also home to the <a href="http://www.usna.edu/homepage.php" class="text-blue-600 hover:underline font-semibold">United States Naval Academy</a>
          and <a href="http://www.sjc.edu/" class="text-blue-600 hover:underline font-semibold">St. John’s College</a>.
        </p>

        <!-- Historical Landmark Style Box -->
        <div class="rounded-2xl border border-amber-200 bg-amber-50/30 p-4 mt-4 text-xs md:text-sm text-amber-900">
          <p class="font-bold flex items-center gap-1.5 text-amber-800 mb-1">
            <History class="w-4 h-4" />
            Historical Acquisition: 1668
          </p>
          <p class="text-amber-800/80 leading-relaxed">
            The land on which Shipley's Choice was established was originally
            acquired by <a href="http://www.geni.com/people/Adam-Shipley/6000000001192363964" class="underline font-semibold">Adam Shipley</a> in 1668, and he patented 200 acres on the south side of the Severn River in 1681.
          </p>
        </div>
      </div>

      <div class="map-responsive mt-6">
        <iframe
          title="Map of Shipley's Choice location"
          class="rounded-2xl border border-slate-200 shadow-inner w-full h-[240px]"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12385.800755948954!2d-76.62084217450997!3d39.09621964502504!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b7fb111c0912cd%3A0x69ab2c3623adff8c!2sShipleys%20Choice%2C%20Severna%20Park%2C%20MD%2021108!5e0!3m2!1sen!2sus!4v1780952424946!5m2!1sen!2sus"
          style="border:0;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </article>

    <!-- Card 3: Transit & Amenities -->
    <article class="rounded-3xl bg-white p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
      <div class="space-y-4">
        <h3 class="text-2xl font-black text-slate-900 border-b pb-2">
          Schools, Transit & Amenities
        </h3>

        <!-- Clickable School Badges -->
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Local Public Schools</p>
          <div class="flex flex-wrap gap-2">
            <a href="http://www.aacps.org/html/schol/elementary/shipches.asp" class="px-3 py-1.5 bg-blue-50 text-blue-700 font-bold text-xs rounded-xl border border-blue-100 hover:bg-blue-100 transition-colors">
              Shipley's Choice Elementary
            </a>
            <a href="http://www.severnaparkmiddle.org/" class="px-3 py-1.5 bg-blue-50 text-blue-700 font-bold text-xs rounded-xl border border-blue-100 hover:bg-blue-100 transition-colors">
              Severna Park Middle
            </a>
            <a href="http://www.severnaparkhigh.org/" class="px-3 py-1.5 bg-blue-50 text-blue-700 font-bold text-xs rounded-xl border border-blue-100 hover:bg-blue-100 transition-colors">
              Severna Park High
            </a>
          </div>
        </div>

        <p class="text-slate-600 text-sm leading-relaxed mt-2">
          Shipley’s Choice is 1½ miles from Exit 10 of I-97, 17 miles from Baltimore, and 8 miles from BWI Airport. The nearby BWI Amtrak station connects to DC via MARC and Baltimore via light rail.
        </p>
        <p class="text-slate-600 text-sm leading-relaxed">
          The community features walkable access to the public elementary school and the privately managed <a href="http://www.shipleyspool.com/" class="text-blue-600 hover:underline font-bold">Shipley’s Choice Swim & Tennis Club</a>, featuring a clubhouse, two pools, and four tennis courts.
        </p>
        <p class="text-slate-600 text-sm leading-relaxed">
          SCCA homes are primarily two-story structures with well-treed lots. Anne Arundel County provides snow removal, street repairs, and curbside recycling services.
        </p>
      </div>

      <img
        src="data/revolving/4241525_orig.jpg"
        alt="The brick facade of Shipley's Choice Elementary School on a sunny day"
        class="rounded-2xl mt-6 border border-slate-200 shadow-sm w-full h-[180px] object-cover"
      />
    </article>

    <!-- Card 4: SCCA Mission -->
    <article class="rounded-3xl bg-white p-8 border border-slate-200 shadow-sm flex flex-col justify-between">
      <div class="space-y-4">
        <h3 class="text-2xl font-black text-slate-900 border-b pb-2">SCCA Mission</h3>
        <p class="text-slate-700 font-bold text-sm">
          Founded in 1979, SCCA operates under these three core principles:
        </p>
        
        <!-- Objective items matching other site sections -->
        <ol class="space-y-3.5">
          <li class="flex items-start gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
            <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold flex-shrink-0">1</span>
            <p class="text-slate-600 text-xs md:text-sm">Encourage cooperative community projects designed to protect welfare, convenience, and home appearance values.</p>
          </li>
          <li class="flex items-start gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
            <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold flex-shrink-0">2</span>
            <p class="text-slate-600 text-xs md:text-sm">Promote active compliance and discourage violations of the neighborhood's recorded protective covenants.</p>
          </li>
          <li class="flex items-start gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
            <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-800 text-xs flex items-center justify-center font-bold flex-shrink-0">3</span>
            <p class="text-slate-600 text-xs md:text-sm">Exercise all legal corporate powers and authority established in SCCA's charter of incorporation.</p>
          </li>
        </ol>

        <div class="border-t border-slate-100 pt-3">
          <p class="text-slate-700 font-bold text-sm mb-2">Stewardship Mandates:</p>
          <ul class="list-disc list-inside space-y-1 text-slate-600 text-xs md:text-sm font-medium">
            <li>Utilize annual resident dues responsibly for common areas.</li>
            <li>Maintain regular local news and directory services.</li>
          </ul>
        </div>
      </div>

      <img
        src="data/revolving/9319905_orig.jpg"
        alt="Pink and yellow flowers planted at the Shipley's Choice community entrance sign"
        class="rounded-2xl mt-6 border border-slate-200 shadow-sm w-full h-[180px] object-cover"
      />
    </article>
  </div>
</section>
