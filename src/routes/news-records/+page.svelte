<script>
  import { onMount, onDestroy } from "svelte";

  const newsItems = [
    {
      id: "scbd-update-aug-2026",
      title:
        "Designating Shipley’s Choice Community Association as a Special Community Benefits District",
      date: "August 2026",
      tags: [],
      content: `
        <p>
          In December 2025, we announced the SCCA Board of Directors voted to
          pursue designation as a Special Community Benefits District (SCBD).
          This would allow Anne Arundel County to collect annual SCCA dues
          through the property tax process.
        </p>
        <p>
          We are pursuing this because currently only about 70 percent of SCCA
          homeowners pay annual dues, while community income does not keep
          pace with expenses. An SCBD would ensure all homes contribute and
          provide the financial stability needed to address maintenance and
          improvements.
        </p>
        <p>
          On July 24, Anne Arundel County staff approved our request to begin
          the process. The next step is obtaining signatures from two-thirds
          of SCCA homeowners. Beginning in September, we will share more
          information on our website and in the annual newsletter, with an
          informational Q&A planned for our October annual meeting. We are
          committed to keeping the community informed and being open and
          transparent throughout the process.
        </p>
        <p>More information to come!</p>
      `,
    },
    {
      id: "common-ground-maintenance-summer-2026",
      title: "A Reminder on Common Ground Maintenance",
      date: "Summer 2026",
      tags: [],
      content: `
        <p class="font-semibold text-slate-800 bg-slate-50 border-l-4 border-blue-500 p-3 rounded-r-lg">
          A friendly reminder: all work on community-owned common grounds must
          be approved by the SCCA Board before it is undertaken.
        </p>
        <p>
          While we deeply appreciate the spirit of volunteerism, this policy
          is essential for several reasons. First and foremost is safety and
          liability; uncoordinated work can create hazards and expose our
          community to legal and financial risks. Additionally, any
          modifications to common areas must comply with county zoning laws
          and align with the community's long-term landscaping and maintenance
          plans.
        </p>
        <p>
          Under SCCA bylaws Article IV, Sections 1 & 4, Association-owned facilities and common properties are 
          reserved strictly for the managed use and enjoyment of members in good standing under rules established by 
          the Association. Individual homeowners do not have individual property rights to alter, landscape, 
          or build on common property.
        </p>
      `,
    },
    {
      id: "pedestrian-safety-summer-2026",
      title: "A Note on Pedestrian Safety",
      date: "Summer 2026",
      tags: [],
      content: `
        <p>
          We've noticed an increase in residents walking in the street,
          especially during evenings and on weekends. While we love to see our
          neighbors out and about, this can create hazardous situations for
          both pedestrians and drivers.
        </p>
        <p>
          For everyone's safety, we strongly urge all residents to use
          sidewalks whenever they are available. When walking on a street
          without a sidewalk, please walk facing traffic and stay as far to
          the side of the road as possible. Let's all do our part to keep
          Shipley's Choice a safe community for everyone.
        </p>
      `,
    },
    {
      id: "scbd-announcement-dec-2025",
      title:
        "Designating Shipley’s Choice Community Association as a Special Community Benefits District",
      date: "Dec 2025",
      tags: ["Official Notice", "Financials"],
      content: `
        <p class="font-semibold text-slate-800 bg-slate-50 border-l-4 border-blue-500 p-3 rounded-r-lg">
          During our SCCA Board of Directors meeting on December 12, 2025, the
          Board voted to pursue designating SCCA as a Special Community
          Benefits District (SCBD).
        </p>
        <p>
          Such a designation would result in Anne Arundel County collecting
          our annual dues through annual county tax collection. We are
          pursuing this action for one reason: <span class="font-bold">only 70 percent of houses that are part of SCCA pay annual dues</span>
          and the community’s income doesn’t match our expenses. There are many
          homeowners’ associations designated as SCBDs in Anne Arundel County,
          including our neighbors in Chartwell.
        </p>
        <p>
          Two-thirds of SCCA homeowners must sign a petition in order for our
          community to become a SCBD. Establishing a SCBD will likely be a
          lengthy process; we will be sure to share information regularly and
          provide an opportunity for members of the community to share their
          opinions about this initiative.
        </p>
      `,
    },
    {
      id: "street-safety-summer-2026",
      title: "Street Safety",
      date: "Summer 2026",
      tags: ["Community Safety"],
      content: `
        <p>
          Riding bikes and scooters can be a lot of fun, but it's also
          important to teach our children about the potential dangers,
          especially when riding at night. To help keep our community safe, we
          encourage all parents to talk to their kids about bike and scooter
          safety. Here are some important safety tips to share:
        </p>

        <ul class="list-disc list-inside">
          <li>Always wear a helmet.</li>
          <li>Ride defensively and be aware of your surroundings.</li>
          <li>Use bike paths and sidewalks when available.</li>
          <li>Avoid riding at night.</li>
        </ul>

        <p>
          The intersection of Governor Stone and Benfield can be especially
          perilous, as well as the intersection of Severncrest and W Benfield.
          It is vitally important for children to learn their safety basics
          and for drivers to be vigilant.
        </p>
        <p>
          For more information regarding children and e-scooters, please visit <a href="https://www.healthychildren.org/English/safety-prevention/on-the-go/Pages/E-Scooters.aspx" class="app-link">HealthyChildren.org</a>
          and watch this short video from MarylandEMS.
        </p>

        <div class="mt-4">
          <iframe
            class="responsive-video"
            src="https://www.youtube.com/embed/Pj82m4gIRbw?si=lGGHeTlsvg_GV24K"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </div>
      `,
    },
  ];

  let activeId = "";
  let observer;

  onMount(() => {
    const sections = newsItems.map((item) => document.getElementById(item.id));

    const observerOptions = {
      root: null,
      rootMargin: "0px 0px -60% 0px",
      threshold: 0,
    };

    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeId = entry.target.id;
        }
      });
    }, observerOptions);

    sections.forEach((section) => {
      if (section) observer.observe(section);
    });
  });

  onDestroy(() => {
    if (observer) observer.disconnect();
  });
</script>

<svelte:head>
  <title>News & Records | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
      News &amp; records
    </p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
      News, newsletters, and meeting minutes
    </h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Download the latest community newsletter and browse community news items
      shared by the board
    </p>
    <div
      class="mt-8 flex flex-col items-center gap-4 sm:flex-row sm:justify-center"
    >
      <a
        href="/data/newsletter/2025-10.pdf"
        target="_blank"
        rel="noreferrer"
        class="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 text-white font-semibold shadow-sm hover:bg-blue-700 transition-colors"
      >
        Latest newsletter (PDF)
      </a>
    </div>
  </div>
</section>

<section class="max-w-7xl mx-auto px-4 py-12">
  <div class="lg:grid lg:grid-cols-12 lg:gap-12">
    <aside class="hidden lg:block lg:col-span-3">
      <nav class="sticky top-24">
        <h3 class="font-semibold text-slate-900">On this page</h3>
        <ul class="mt-4 space-y-1 border-l-2 border-slate-100">
          {#each newsItems as item}
            <li>
              <a
                href="#{item.id}"
                class="block w-full pl-3.5 pr-2 py-1.5 -ml-px border-l-2 text-sm transition-colors"
                class:border-blue-500={activeId === item.id}
                class:text-blue-600={activeId === item.id}
                class:font-semibold={activeId === item.id}
                class:border-transparent={activeId !== item.id}
                class:text-slate-500={activeId !== item.id}
                class:hover:border-slate-300={activeId !== item.id}
                class:hover:text-slate-700={activeId !== item.id}
              >
                {item.title}
              </a>
            </li>
          {/each}
        </ul>
      </nav>
    </aside>

    <div class="lg:col-span-9">
      <article
        class="rounded-2xl border border-slate-200/80 bg-white p-6 md:p-8 shadow-sm"
      >
        <h2
          class="text-2xl font-bold tracking-tight text-slate-900 border-b border-slate-100 pb-4 mb-6"
        >
          Community News & Announcements
        </h2>

        <div class="divide-y divide-slate-100">
          {#each newsItems as item}
            <div
              id={item.id}
              class="py-6 first:pt-0 last:pb-0 group scroll-mt-20"
            >
              <div
                class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-2 mb-3"
              >
                <h3
                  class="text-lg font-bold text-slate-900 leading-snug group-hover:text-blue-600 transition-colors"
                >
                  {item.title}
                </h3>
                <time
                  class="text-xs font-semibold uppercase tracking-wider text-slate-400 whitespace-nowrap sm:shrink-0"
                >
                  {item.date}
                </time>
              </div>

              <div
                class="space-y-3 text-slate-600 text-sm sm:text-base leading-relaxed"
              >
                {@html item.content}
              </div>

              {#if item.tags.length}
                <div class="mt-4 flex flex-wrap gap-2">
                  {#each item.tags as tag}
                    <span
                      class="inline-flex items-center rounded-md bg-slate-100 px-2.5 py-1 text-xs font-medium text-slate-600"
                    >
                      {tag}
                    </span>
                  {/each}
                </div>
              {/if}
            </div>
          {/each}
        </div>
      </article>
    </div>
  </div>
</section>
