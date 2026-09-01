<script>
  import { onMount, onDestroy } from "svelte";

  // List of actual image files found in static/data/img/trees
  const images = [
    {
      src: "/data/img/trees/20260825_085720.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_091446.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_091612.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_092146.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_092216.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_094708.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_094709Z1.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_095210.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_103843.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_103859.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_104204.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_104549.jpg",
      title: "Common Area Tree Photo",
    },
    {
      src: "/data/img/trees/20260825_151319.jpg",
      title: "Common Area Tree Photo",
    },
  ];

  // Svelte 5 state runes
  let currentIndex = $state(0);
  let isPlaying = $state(true);
  let intervalId;

  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
  }

  function selectImage(index) {
    currentIndex = index;
    if (isPlaying) {
      resetTimer();
    }
  }

  function togglePlay() {
    isPlaying = !isPlaying;
    if (isPlaying) {
      startTimer();
    } else {
      stopTimer();
    }
  }

  function startTimer() {
    stopTimer();
    intervalId = setInterval(nextImage, 4000);
  }

  function stopTimer() {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
  }

  function resetTimer() {
    startTimer();
  }

  onMount(() => {
    if (isPlaying) {
      startTimer();
    }
  });

  onDestroy(() => {
    stopTimer();
  });
</script>

<svelte:head>
  <title>Common Area Trees | Shipley's Choice</title>
</svelte:head>

<section class="page-header py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
      Community Safety & Woodlands
    </p>
    <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
      Common Area Trees & Safety
    </h1>
    <p class="mt-4 max-w-2xl mx-auto text-slate-300">
      Identify hazardous trees, understand the association's policies, and
      report dead trees in common areas for inspection.
    </p>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
    <!-- Photo Gallery Column (Portrait-optimized: Col span 5) -->
    <div class="lg:col-span-5 space-y-4">
      <div class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-bold text-slate-900">
            Hazardous Trees Gallery
          </h2>
          <span
            class="text-sm font-semibold bg-slate-100 text-slate-600 px-3 py-1.5 rounded-full"
          >
            {currentIndex + 1} of {images.length}
          </span>
        </div>

        <!-- Slideshow Container: Optimized portrait 3:4 aspect ratio -->
        <div
          class="relative group overflow-hidden rounded-2xl bg-slate-950 aspect-[3/4] max-h-[550px] w-full flex items-center justify-center shadow-inner"
        >
          <img
            src={images[currentIndex].src}
            alt="Common Area Tree Photo"
            class="w-full h-full object-contain transition-all duration-300"
          />

          <!-- Overlay controls (visible on hover/focus) -->
          <button
            type="button"
            onclick={prevImage}
            class="absolute left-4 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-slate-900/60 text-white hover:bg-slate-900/80 transition-all opacity-0 group-hover:opacity-100 focus:opacity-100 shadow"
            aria-label="Previous Image"
          >
            <svg
              class="h-6 w-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 19l-7-7 7-7"
              />
            </svg>
          </button>

          <button
            type="button"
            onclick={nextImage}
            class="absolute right-4 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-slate-900/60 text-white hover:bg-slate-900/80 transition-all opacity-0 group-hover:opacity-100 focus:opacity-100 shadow"
            aria-label="Next Image"
          >
            <svg
              class="h-6 w-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </button>

          <!-- Floating Play/Pause Status Indicator -->
          <button
            type="button"
            onclick={togglePlay}
            class="absolute bottom-4 right-4 p-2 rounded-full bg-slate-900/60 text-white hover:bg-slate-900/80 transition-all focus:outline-none shadow"
            title={isPlaying ? "Pause Autoplay" : "Start Autoplay"}
            aria-label={isPlaying ? "Pause Autoplay" : "Start Autoplay"}
          >
            {#if isPlaying}
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
              </svg>
            {:else}
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z" />
              </svg>
            {/if}
          </button>
        </div>

        <!-- Metadata Information -->
        <div class="mt-4 p-4 rounded-xl bg-slate-50 border border-slate-100">
          <div class="flex items-baseline justify-between gap-2">
            <h3 class="font-bold text-slate-800 text-sm">
              {images[currentIndex].title} #{currentIndex + 1}
            </h3>
            <span class="text-xs font-mono text-slate-400 shrink-0">
              {images[currentIndex].src.split("/").pop()}
            </span>
          </div>
        </div>

        <!-- Dot Navigation Grid -->
        <div class="mt-4 flex flex-wrap items-center justify-center gap-2">
          {#each images as img, i}
            <button
              type="button"
              onclick={() => selectImage(i)}
              class="h-2.5 rounded-full transition-all duration-300 {currentIndex ===
              i
                ? 'w-8 bg-blue-600'
                : 'w-2.5 bg-slate-200 hover:bg-slate-300'}"
              aria-label="Go to slide {i + 1}"
            ></button>
          {/each}
        </div>
      </div>

      <!-- Quick Tips Card -->
      <div class="rounded-3xl border border-slate-200 bg-slate-50 p-6">
        <h3
          class="font-bold text-slate-900 mb-3 text-base flex items-center gap-2"
        >
          <svg
            class="h-5 w-5 text-amber-500"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          Resident Inspection Tips
        </h3>
        <ul class="space-y-3 text-sm text-slate-700 leading-relaxed">
          <li class="flex gap-2">
            <span class="text-blue-500 font-bold">•</span>
            <span
              >Verify the tree is clearly inside SCCA common areas, not on
              private homeowner lots.</span
            >
          </li>
          <li class="flex gap-2">
            <span class="text-blue-500 font-bold">•</span>
            <span
              >Check for visual signs of decay: severe leaning, complete loss of
              bark, hollowed trunks, or large dead overhanging branches.</span
            >
          </li>
          <li class="flex gap-2">
            <span class="text-blue-500 font-bold">•</span>
            <span
              >Provide detailed location references (e.g. house addresses,
              proximity to trails) when reporting.</span
            >
          </li>
        </ul>
      </div>
    </div>

    <!-- Content & Info Column (Expanded to Col span 7) -->
    <div class="lg:col-span-7 space-y-6">
      <!-- Hazard Information Card -->
      <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-6">
          Dead Trees in Common Areas
        </h2>

        <div class="space-y-6">
          <div>
            <h3
              class="text-lg font-bold text-slate-900 flex items-center gap-2"
            >
              <span
                class="flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-xs font-semibold text-red-600"
              >
                1
              </span>
              The Dangers They Pose
            </h3>
            <p class="text-slate-700 mt-2 leading-relaxed">
              Dead and decaying trees inside common woodland buffers are serious
              structural hazards. High winds, winter storms, or advanced core
              decay can cause limbs or entire trees to collapse without warning,
              resulting in:
            </p>
            <ul
              class="mt-3 pl-8 list-disc text-slate-700 space-y-2 leading-relaxed"
            >
              <li>
                <strong>Physical Safety Risks:</strong> Threat of injury to residents,
                children, or pets utilizing our shared paths, trails, and playgrounds.
              </li>
              <li>
                <strong>Homeowner Property Damage:</strong> Threat to border property
                boundaries, including structural damage to fences, decks, yards,
                or roofs.
              </li>
              <li>
                <strong>Utility Outages:</strong> Danger to overhead telephone and
                electrical lines running near wooded paths.
              </li>
              <li>
                <strong>Increased Fire Hazards:</strong> Dry, dead timber increases
                combustible wood fuel loading inside shared community space.
              </li>
            </ul>
          </div>

          <hr class="border-slate-100" />

          <div>
            <h3
              class="text-lg font-bold text-slate-900 flex items-center gap-2"
            >
              <span
                class="flex h-6 w-6 items-center justify-center rounded-full bg-blue-100 text-xs font-semibold text-blue-600"
              >
                2
              </span>
              SCCA Domain & Property Boundaries
            </h3>
            <p class="text-slate-700 mt-2 leading-relaxed">
              SCCA is strictly responsible for trees growing within <strong
                >official SCCA common properties</strong
              >.
            </p>
            <p class="text-slate-700 mt-2 leading-relaxed">
              If a dead tree is located entirely within a resident's private
              lot, it is the homeowner's responsibility to manage and finance
              its removal. SCCA assessment funds cannot be legally allocated to
              private property maintenance. If you are uncertain of property
              lines, please consult the neighborhood Plat Maps on our <a
                href="/documents"
                class="text-blue-600 hover:underline">Documents page</a
              > or coordinate with the Board.
            </p>
          </div>

          <hr class="border-slate-100" />

          <div>
            <h3
              class="text-lg font-bold text-slate-900 flex items-center gap-2"
            >
              <span
                class="flex h-6 w-6 items-center justify-center rounded-full bg-emerald-100 text-xs font-semibold text-emerald-600"
              >
                3
              </span>
              Evaluation & Action
            </h3>
            <p class="text-slate-700 mt-2 leading-relaxed">
              The SCCA Board coordinates with tree removal contractors to
              evaluate tree health. Removals are scheduled and prioritized based
              on proximity to houses or pedestrian paths, and managed within
              standard annual budgets.
            </p>
          </div>
        </div>
      </div>

      <!-- Reporting / Call-to-action Card -->
      <div
        class="rounded-3xl border border-blue-100 bg-blue-50/50 p-8 shadow-sm"
      >
        <h3 class="text-xl font-bold text-slate-950 mb-3">
          Report a Common Area Tree Hazard
        </h3>
        <p class="text-slate-700 mb-6 leading-relaxed">
          If you have spotted a dead, dying, or dangerously leaning tree inside
          an SCCA common area, please notify our Board of Directors to request
          an inspection.
        </p>

        <div
          class="bg-white rounded-2xl p-4 border border-blue-100 shadow-sm mb-6"
        >
          <div
            class="text-xs text-slate-400 font-semibold uppercase tracking-wider mb-1"
          >
            SCCA Board Email
          </div>
          <a
            href="mailto:shipleyschoice.scca@gmail.com?subject=Common%20Area%20Tree%20Inspection%20Request"
            class="text-blue-600 hover:text-blue-700 font-bold block truncate text-base"
          >
            shipleyschoice.scca@gmail.com
          </a>
        </div>

        <a
          href="mailto:shipleyschoice.scca@gmail.com?subject=Common%20Area%20Tree%20Inspection%20Request&body=Hello%20SCCA%20Board%2C%0D%0A%0D%0AI%20am%20writing%20to%20request%20an%20inspection%20for%20a%20potentially%20dangerous%2Fdead%20tree%20located%20in%20the%20common%20area.%0D%0A%0D%0ALocation%20Details%3A%0D%0A%5BPlease%20describe%20where%20the%20tree%20is%20located%2C%20including%20nearest%20address%20or%20landmarks%5D%0D%0A%0D%0AHazard%20Description%3A%0D%0A%5BPlease%20describe%20the%20tree's%20condition%3B%20e.g.%2C%20fully%20dead%2C%20leaning%20toward%20private%20property%2C%20dropping%20large%20limbs%20over%20a%20pathway%5D%0D%0A%0D%0AThank%20you%2C%0D%0A%5BYour%20Name%5D%0D%0A%5BYour%20Address%5D"
          class="w-full inline-flex items-center justify-center gap-2 rounded-2xl bg-blue-600 px-6 py-4 text-center text-sm font-bold text-white shadow-md hover:bg-blue-700 hover:shadow-lg transition-all"
        >
          <svg
            class="h-5 w-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M3 19v-8.93a2 2 0 01.89-1.664l8-4a2 2 0 011.78 0l8 4A2 2 0 0121 10.07V19M3 19a2 2 0 002 2h14a2 2 0 002-2M3 19l6.75-4.5M21 19l-6.75-4.5M3 10l6.75 4.5M21 10l-6.75-4.5m0 0l-1.14.76a2 2 0 01-2.22 0l-1.14-.76"
            />
          </svg>
          Request Tree Inspection
        </a>
      </div>
    </div>
  </div>
</section>
