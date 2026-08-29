<script>
  import newsItems from "$data/newsItems.json";

  // The `newsItems` are now imported directly.

  $: latestNews = newsItems?.[0];
  $: latestThreeNews = newsItems?.slice(0, 3) ?? [];
</script>

<svelte:head>
  <title>Shipley's Choice Community Association</title>
</svelte:head>

<section class="page-header py-24 px-6 text-center">
  <div class="max-w-3xl mx-auto">
    <div
      class="mb-10 p-6 sm:p-8 bg-slate-900/80 border border-blue-500/30 rounded-2xl shadow-2xl backdrop-blur-md max-w-2xl mx-auto text-center animate-fadeIn"
    >
      <div
        class="inline-flex items-center gap-2 px-3 py-1 bg-blue-500/20 text-blue-300 border border-blue-400/20 text-xs font-semibold rounded-full mb-4"
      >
        <span class="relative flex h-2 w-2">
          <span
            class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"
          ></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"
          ></span>
        </span>
        SCBD Petition & Information Drive Active
      </div>

      <h2 class="text-xl sm:text-2xl font-bold text-white mb-3 tracking-tight">
        Help Secure our Community's Future
      </h2>

      <p class="text-sm text-slate-300 mb-6 leading-relaxed max-w-lg mx-auto">
        We are currently conducting an educational outreach and petition effort
        to establish a Special Community Benefits District (SCBD) in Shipley's
        Choice. Explore how this transition protects our community and find
        answers to common questions.
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a
          href="/why-scbd"
          class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-2.5 bg-blue-600 text-white font-semibold rounded-xl shadow-md hover:bg-blue-500 hover:shadow-lg transition-all text-sm"
        >
          Why SCBD?
          <svg
            class="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M14 5l7 7m0 0l-7 7m7-7H3"
            />
          </svg>
        </a>
        <a
          href="/why-scbd-faq"
          class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-2.5 bg-slate-800 text-blue-300 border border-slate-700/80 font-semibold rounded-xl hover:bg-slate-700 hover:text-white transition-all text-sm"
        >
          SCBD FAQ
          <svg
            class="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </a>
      </div>
    </div>

    <h1 class="text-5xl font-extrabold tracking-tight mb-4">
      Welcome to Shipley's Choice
    </h1>
    <p class="text-xs text-slate-300 leading-relaxed">
      Mailbox: 315 Arbor Oaks Ct, Millersville, MD 21108
    </p>
    <p class="text-xl text-slate-300 leading-relaxed">
      A vibrant community in Anne Arundel County, Maryland. Stay informed on
      board activities, local news, and community documents.
    </p>
  </div>
  <div class="max-w-7xl mx-auto px-4 grid gap-6 lg:grid-cols-3 mt-12 text-left">
    <article
      class="rounded-3xl bg-white/10 p-8 shadow-lg border border-white/20 backdrop-blur-sm"
    >
      <div
        class="flex flex-col-reverse items-start gap-4 sm:flex-row sm:justify-between sm:items-start mb-3"
      >
        <h3
          class="text-xl font-semibold text-white [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]"
        >
          Community News
        </h3>
        {#if latestNews}
          <div
            class="text-xs font-semibold uppercase tracking-wider text-slate-300 bg-white/10 px-2.5 py-1 rounded-full whitespace-nowrap sm:shrink-0"
          >
            Latest: {latestNews.date}
          </div>
        {/if}
      </div>
      <ul
        class="list-disc list-inside space-y-2 text-slate-200 mb-4 text-sm [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]"
      >
        {#each latestThreeNews as item}
          <li>{item.title}</li>
        {/each}
      </ul>
      <a
        href="/news-records"
        class="inline-flex items-center gap-2 font-semibold text-blue-300 hover:text-blue-200"
        >View news →</a
      >
    </article>

    <article
      class="rounded-3xl bg-white/10 p-8 shadow-lg border border-white/20 backdrop-blur-sm"
    >
      <h3
        class="text-xl font-semibold text-white mb-3 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]"
      >
        Architectural Requests
      </h3>
      <p class="text-slate-200 mb-4 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]">
        Planning a home improvement? Find the ACR form and fence standards here.
      </p>
      <a
        href="/architecture-requests"
        class="inline-flex items-center gap-2 font-semibold text-blue-300 hover:text-blue-200"
        >View requirements →</a
      >
    </article>

    <article
      class="rounded-3xl bg-white/10 p-8 shadow-lg border border-white/20 backdrop-blur-sm"
    >
      <h3
        class="text-xl font-semibold text-white mb-3 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]"
      >
        Share your voice
      </h3>
      <p class="text-slate-200 mb-4 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]">
        Residents can openly discuss community matters with our board of
        volunteers on Google Groups.
      </p>
      <a
        href="https://groups.google.com/u/1/g/shipleys-choice-community-association"
        class="inline-flex items-center gap-2 font-semibold text-blue-300 hover:text-blue-200"
        >Join today →</a
      >
    </article>
  </div>
</section>

<section class="max-w-7xl mx-auto py-16 px-4">
  <div class="grid gap-6 md:grid-cols-2">
    <article class="rounded-3xl bg-white p-6 border border-slate-200 shadow-sm">
      <h2
        class="text-2xl font-bold text-slate-800 mb-4 border-b-2 border-blue-500 inline-block pb-1"
      >
        Community Overview
      </h2>
      <p class="text-slate-600 mb-4">
        Shipley’s Choice is a community of single family homes in the Greater
        Severna Park area north of Annapolis, MD, nestled in the suburbs between
        Washington, DC and Baltimore.
      </p>
      <p class="text-slate-600 mb-4">
        The neighborhood is divided into two main community organizations:
      </p>
      <div class="space-y-4 text-slate-600">
        <div
          class="rounded-3xl bg-cyan-50 p-5 border border-slate-200 shadow-sm"
        >
          <p>
            <strong>Shipley's Choice Community Association (SCCA)</strong><br
            />This site is dedicated to serving the 283 homes that make up
            sections 1 and 2 of Shipley's Choice.
          </p>
          <p class="mt-3">
            For a list of streets and addresses in the SCCA, please refer to the <a
              href="/information"
              class="app-link">Information</a
            > page.
          </p>
        </div>
        <div
          class="rounded-3xl bg-amber-50 p-5 border border-slate-200 shadow-sm"
        >
          <p>
            <strong>Shipley's Choice Home Owners Association (SCHOA)</strong><br
            />The SCHOA is a <em>separate</em> organization which represents the
            homes of sections 3 through 12 of Shipley's Choice.
          </p>
          <p class="mt-3">
            Please refer to the <a
              href="https://www.shipleyschoice.com/"
              class="app-link">SCHOA website</a
            > for information regarding the HOA organization.
          </p>
        </div>
      </div>
    </article>

    <article class="rounded-3xl bg-white p-6 border border-slate-200 shadow-sm">
      <h3 class="text-xl font-semibold text-slate-900 mb-4">
        Location & history
      </h3>
      <p class="text-slate-600">
        Shipley’s Choice is ideally located in Anne Arundel County, MD; about 10
        miles north of <a href="http://www.ci.annapolis.md.us/" class="app-link"
          >Annapolis</a
        >, the
        <a
          href="http://www.annapolis.gov/visitors/gateway-to-discovery/americas-sailing-capital"
          class="app-link">sailing boat capital</a
        >
        of the United States and the seat of Maryland state
        <a href="http://www.maryland.gov/Pages/default.aspx" class="app-link"
          >government</a
        >.
      </p>
      <p class="text-slate-600 mt-3">
        Annapolis is also home to the <a
          href="http://www.usna.edu/homepage.php"
          class="app-link">United States Naval Academy</a
        >
        and
        <a href="http://www.sjc.edu/" class="app-link">St. John’s College</a>,
        and preserves its naval heritage and colonial architecture.
      </p>
      <p class="text-slate-600 mt-3">
        The land on which Shipley's Choice was established was originally
        acquired by <a
          href="http://www.geni.com/people/Adam-Shipley/6000000001192363964"
          class="app-link">Adam Shipley</a
        > in 1668, and he patented 200 acres on the south side of the Severn River
        in 1681.
      </p>
      <div class="map-responsive">
        <iframe
          title="Map of Shipley's Choice location"
          class="mt-6 rounded-3xl border border-slate-200 shadow-sm"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12385.800755948954!2d-76.62084217450997!3d39.09621964502504!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89b7fb111c0912cd%3A0x69ab2c3623adff8c!2sShipleys%20Choice%2C%20Severna%20Park%2C%20MD%2021108!5e0!3m2!1sen!2sus!4v1780952424946!5m2!1sen!2sus"
          height="500"
          style="border:0;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </article>

    <article class="rounded-3xl bg-white p-6 border border-slate-200 shadow-sm">
      <h3 class="text-xl font-semibold text-slate-900 mb-4">
        Schools, transit & amenities
      </h3>
      <ul class="list-disc list-inside space-y-2 text-slate-600">
        <li>
          <a
            href="http://www.aacps.org/html/schol/elementary/shipches.asp"
            class="app-link">Shipley’s Choice Elementary School</a
          >
        </li>
        <li>
          <a href="http://www.severnaparkmiddle.org/" class="app-link"
            >Severna Park Middle School</a
          >
        </li>
        <li>
          <a href="http://www.severnaparkhigh.org/" class="app-link"
            >Severna Park High School</a
          >
        </li>
      </ul>
      <p class="text-slate-600 mt-3">
        Shipley’s Choice is 1½ miles from Exit 10 of Interstate 97, 17 miles
        from Baltimore, 34 miles from Washington, D.C., and 8 miles from the <a
          href="http://www.bwiairport.com/en"
          class="app-link">BWI Airport</a
        >. The nearby
        <a
          href="http://www.amtrak.com/servlet/ContentServer?pagename=am/am2Station/Station_Page&code=BWI"
          class="app-link">Amtrak station</a
        > connects to DC via MARC and Baltimore via light rail.
      </p>
      <p class="text-slate-600 mt-3">
        The community features a walkable location for Shipley’s Choice
        Elementary School and the privately managed <a
          href="http://www.shipleyspool.com/"
          class="app-link">Shipley’s Choice Swim & Tennis Club</a
        >, with a clubhouse, two pools, a children’s pool, and four tennis
        courts.
      </p>
      <p class="text-slate-600 mt-3">
        SCCA homes are primarily two-story houses with two-car garages on
        well-treed lots of a quarter acre or more. Anne Arundel County handles
        snow removal, street repairs, trash pickup, recycling, and greens
        removal at the curb.
      </p>
      <p class="text-slate-600 mt-3">
        Many residents commute across the Washington–Baltimore–Annapolis
        triangle, including to Columbia and <a
          href="http://www.ftmeade.army.mil/"
          class="app-link">Fort Meade</a
        >.
      </p>

      <img
        src="data/revolving/4241525_orig.jpg"
        alt="The brick facade of Shipley's Choice Elementary School on a sunny day"
        class="rounded-3xl mt-4 border border-slate-200 shadow-sm"
      />
    </article>

    <article class="rounded-3xl bg-white p-6 border border-slate-200 shadow-sm">
      <h3 class="text-xl font-semibold text-slate-900 mb-4">SCCA mission</h3>
      <p class="text-slate-700 font-semibold">
        Founded in 1979, the mission of the SCCA is to:
      </p>
      <ol class="mt-4 list-decimal list-inside space-y-3 text-slate-600">
        <li>
          Encourage residents to participate cooperatively in projects that
          promote general welfare and protect the appearance, value, and
          convenience of property in Shipley’s Choice.
        </li>
        <li>
          Promote compliance with, and discourage violations of, the covenants
          that apply within Shipley’s Choice.
        </li>
        <li>
          Exercise the powers and authorities set forth in the charter of this
          corporation.
        </li>
      </ol>
      <p class="mt-4 text-slate-700 font-semibold">And also...</p>
      <ul class="mt-3 list-disc list-inside space-y-2 text-slate-600">
        <li>
          <em>Support the community</em> with pertinent neighborhood information.
        </li>
        <li>
          <em>Utilize dues responsibly</em> to enhance the beauty and safety of common
          grounds.
        </li>
      </ul>

      <img
        src="data/revolving/9319905_orig.jpg"
        alt="Pink and yellow flowers planted at the Shipley's Choice community entrance sign"
        class="rounded-3xl mt-4 border border-slate-200 shadow-sm"
      />
    </article>
  </div>
</section>
