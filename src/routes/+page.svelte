<script>
  let showMessage = false;

  function clickOutside(node) {
    const handleClick = (event) => {
      if (node && !node.contains(event.target) && !event.defaultPrevented) {
        node.dispatchEvent(new CustomEvent("click_outside", node));
      }
    };
    document.addEventListener("click", handleClick, true);
    return {
      destroy: () => document.removeEventListener("click", handleClick, true),
    };
  }
</script>

<svelte:head>
  <title>Shipley's Choice Community Association</title>
</svelte:head>

<section class="page-header py-24 px-6 text-center">
  <div class="max-w-3xl mx-auto">
    <div
      class="inline-flex flex-col items-center mb-4 relative"
      use:clickOutside
      on:click_outside={() => (showMessage = false)}
    >
      <button
        on:click={() => (showMessage = !showMessage)}
        class="inline-flex items-center gap-1.5 px-3 py-1 bg-blue-500/20 text-blue-300 border border-blue-400/30 text-xs font-semibold rounded-full hover:bg-blue-500/30 transition-all"
      >
        <span class="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse"></span>
        Important: Declaring Shipley's Choice a Special Community Benefits District
        • Click to read note
      </button>

      {#if showMessage}
        <div
          class="absolute top-8 mt-2 w-72 bg-slate-900 text-left border border-slate-700 p-4 rounded-xl shadow-xl text-xs text-slate-300 z-10"
        >
          <p class="font-semibold text-white mb-1">
            Hello Shipley's Choice neighbors
          </p>
          <p>
            Please refer to the <a
              class="app-link"
              href="/news-records#scbd-update-aug-2026">news post</a
            > regarding the initiative to declare Shipley's Choice a Special Community
            Benefits District.
          </p>
        </div>
      {/if}
    </div>

    <h1 class="text-5xl font-extrabold tracking-tight mb-4">
      Welcome to Shipley's Choice
    </h1>
    <p class="text-xl text-slate-300 leading-relaxed">
      A vibrant community in Anne Arundel County, Maryland. Stay informed on
      board activities, local news, and community documents.
    </p>
  </div>
  <div class="max-w-7xl mx-auto px-4 grid gap-6 lg:grid-cols-3 mt-12 text-left">
    <article
      class="rounded-3xl bg-white/10 p-8 shadow-lg border border-white/20 backdrop-blur-sm"
    >
      <h3
        class="text-xl font-semibold text-white mb-3 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]"
      >
        Community News
      </h3>
      <p class="text-slate-200 mb-4 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]">
        Stay up-to-date with the latest announcements, events, and community
        news.
      </p>
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
        Register with SCCA
      </h3>
      <p class="text-slate-200 mb-4 [text-shadow:0_1px_2px_rgb(0_0_0_/_0.5)]">
        Register your household to stay informed on community news and updates.
      </p>
      <a
        href="/register"
        class="inline-flex items-center gap-2 font-semibold text-blue-300 hover:text-blue-200"
        >Register now →</a
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
