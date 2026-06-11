<script>
  import { page } from "$app/stores";

  // Data arrays mapping directly to your static folder structures
  const documents = [
    { filename: "scca_by-laws.pdf", path: "/data/docs/scca_by-laws.pdf" },
    {
      filename: "scca_covenants_legal_filing.pdf",
      path: "/data/docs/scca_covenants_legal_filing.pdf",
    },
    {
      filename: "scca_covenants_renewal_2017_-_pt_1.pdf",
      path: "/data/docs/scca_covenants_renewal_2017_-_pt_1.pdf",
    },
    {
      filename: "scca_covenants_renewal_2017_pt.2.pdf",
      path: "/data/docs/scca_covenants_renewal_2017_pt.2.pdf",
    },
    {
      filename: "scca_fence_standards_v4[389].pdf",
      path: "/data/docs/scca_fence_standards_v4[389].pdf",
    },
    {
      filename: "scca_section_1_covenants.pdf",
      path: "/data/docs/scca_section_1_covenants.pdf",
    },
    {
      filename: "scca_section_2_covenants.pdf",
      path: "/data/docs/scca_section_2_covenants.pdf",
    },
    {
      filename: "sect_1_assignment_to_scca__1980-08-01_.pdf",
      path: "/data/docs/sect_1_assignment_to_scca__1980-08-01_.pdf",
    },
    {
      filename: "sect_1_covenents_extention.pdf",
      path: "/data/docs/sect_1_covenents_extention.pdf",
    },
  ];

  const plats = [
    {
      filename: "section_1_-_plat_1.jpg",
      path: "/data/plats/section_1_-_plat_1.jpg",
    },
    {
      filename: "section_1_-_plat_2.jpg",
      path: "/data/plats/section_1_-_plat_2.jpg",
    },
    {
      filename: "section_1_-_plat_3.jpg",
      path: "/data/plats/section_1_-_plat_3.jpg",
    },
    {
      filename: "section_1_-_plat_4.jpg",
      path: "/data/plats/section_1_-_plat_4.jpg",
    },
    {
      filename: "section_2_-_plat_1__original_.jpg",
      path: "/data/plats/section_2_-_plat_1__original_.jpg",
    },
    {
      filename: "section_2_-_plat_1__revised_.jpg",
      path: "/data/plats/section_2_-_plat_1__revised_.jpg",
    },
    {
      filename: "section_2_-_plat_2.jpg",
      path: "/data/plats/section_2_-_plat_2.jpg",
    },
    {
      filename: "section_2_-_plat_3.jpg",
      path: "/data/plats/section_2_-_plat_3.jpg",
    },
    {
      filename: "section_2_-_plat_4.jpg",
      path: "/data/plats/section_2_-_plat_4.jpg",
    },
    {
      filename: "section_2_-_plat_5.jpg",
      path: "/data/plats/section_2_-_plat_5.jpg",
    },
    {
      filename: "section_2_-_plat_6.jpg",
      path: "/data/plats/section_2_-_plat_6.jpg",
    },
  ];

  // State management
  let activeTab = "docs"; // 'docs' or 'plats'
  let selectedFile = documents[0]; // Pre-select SCCA By-Laws PDF as default
  let containerWidth = 0;
  let brandWrapper;
  let navWrapper;

  // Helper function to format filenames cleanly for community residents
  function formatTitle(filename) {
    return filename
      .replace(/\.[^/.]+$/, "") // Remove file extension
      .replace(/[_-]/g, " ") // Replace underscores and dashes with spaces
      .replace(/\s+/g, " ") // Collapse multiple spaces
      .trim()
      .split(" ")
      .map((word) => {
        const lower = word.toLowerCase();
        if (lower === "scca") return "SCCA";
        if (lower === "pdf" || lower === "docx") return word.toUpperCase();
        if (lower === "pt") return "Part";
        return word.charAt(0).toUpperCase() + word.slice(1);
      })
      .join(" ");
  }

  // Reactive fallback handler when changing tabs
  function handleTabChange(tab) {
    activeTab = tab;
    selectedFile = tab === "docs" ? documents[1] : plats[0];
  }

  // Compute file extensions to drive conditional preview rendering
  $: fileExtension = selectedFile?.filename.split(".").pop().toLowerCase();
</script>

<svelte:head>
  <title>Community Documents | Shipley's Choice</title>
</svelte:head>

<div
  class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 h-[calc(100vh-140px)] flex flex-col"
>
  <div
    class="flex flex-col sm:flex-row sm:items-center sm:justify-between border-b border-slate-200 pb-4 mb-6 gap-4 shrink-0"
    bind:clientWidth={containerWidth}
  >
    <div>
      <h1 class="text-2xl font-bold tracking-tight text-slate-900">
        Important SCCA Resources
      </h1>
      <p class="text-sm text-slate-500">
        Access governance documents, property guidelines, and neighborhood
        layouts for Shipley's Choice residents.
      </p>
    </div>

    <div
      class="inline-flex rounded-xl bg-slate-100 p-1 self-start sm:self-auto shrink-0 select-none"
    >
      <button
        type="button"
        class="rounded-lg px-4 py-2 text-sm font-medium transition-all {activeTab ===
        'docs'
          ? 'bg-white text-blue-600 shadow-sm'
          : 'text-slate-600 hover:text-slate-900'}"
        on:click={() => handleTabChange("docs")}
      >
        Documents
      </button>
      <button
        type="button"
        class="rounded-lg px-4 py-2 text-sm font-medium transition-all {activeTab ===
        'plats'
          ? 'bg-white text-blue-600 shadow-sm'
          : 'text-slate-600 hover:text-slate-900'}"
        on:click={() => handleTabChange("plats")}
      >
        Neighborhood Plats
      </button>
    </div>
  </div>

  <div
    class="flex-grow grid grid-cols-1 md:grid-cols-3 gap-6 min-h-0 overflow-hidden"
  >
    <div
      class="md:col-span-1 bg-white rounded-2xl border border-slate-200 flex flex-col overflow-hidden shadow-sm"
    >
      <div class="p-4 border-b border-slate-100 bg-slate-50/50">
        <h2
          class="text-xs font-semibold text-slate-400 uppercase tracking-wider"
        >
          Available {activeTab === "docs" ? "Documents" : "Plat Records"} ({activeTab ===
          "docs"
            ? documents.length
            : plats.length})
        </h2>
      </div>

      <nav class="flex-grow overflow-y-auto p-2 space-y-1">
        {#each activeTab === "docs" ? documents : plats as file}
          <button
            type="button"
            class="w-full text-left px-4 py-3 rounded-xl text-sm font-medium transition-all flex items-center gap-3 group border border-transparent {selectedFile?.path ===
            file.path
              ? 'bg-blue-50/70 border-blue-100 text-blue-700'
              : 'text-slate-700 hover:bg-slate-50 hover:text-slate-900'}"
            on:click={() => (selectedFile = file)}
          >
            {#if file.filename.endsWith(".pdf")}
              <svg
                class="h-5 w-5 shrink-0 {selectedFile?.path === file.path
                  ? 'text-blue-600'
                  : 'text-slate-400 group-hover:text-slate-500'}"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                ><path
                  d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"
                /><polyline points="14 2 14 7 19 7" /></svg
              >
            {:else if file.filename.endsWith(".docx")}
              <svg
                class="h-5 w-5 shrink-0 {selectedFile?.path === file.path
                  ? 'text-blue-600'
                  : 'text-slate-400 group-hover:text-slate-500'}"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                ><path
                  d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
                /><polyline points="14 2 14 8 20 8" /><line
                  x1="16"
                  y1="13"
                  x2="8"
                  y2="13"
                /><line x1="16" y1="17" x2="8" y2="17" /><polyline
                  points="10 9 9 9 8 9"
                /></svg
              >
            {:else}
              <svg
                class="h-5 w-5 shrink-0 {selectedFile?.path === file.path
                  ? 'text-blue-600'
                  : 'text-slate-400 group-hover:text-slate-500'}"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                ><rect
                  x="3"
                  y="3"
                  width="18"
                  height="18"
                  rx="2"
                  ry="2"
                /><circle cx="8.5" cy="8.5" r="1.5" /><polyline
                  points="21 15 16 10 5 21"
                /></svg
              >
            {/if}

            <span class="truncate leading-tight"
              >{formatTitle(file.filename)}</span
            >
          </button>
        {/each}
      </nav>
    </div>

    <div
      class="md:col-span-2 bg-slate-100 rounded-2xl border border-slate-200 overflow-hidden flex flex-col relative shadow-inner"
    >
      {#if selectedFile}
        <div
          class="bg-white border-b border-slate-200 px-6 py-3 flex items-center justify-between gap-4 shrink-0"
        >
          <div class="min-w-0">
            <h3 class="text-sm font-semibold text-slate-800 truncate">
              {formatTitle(selectedFile.filename)}
            </h3>
            <p class="text-xs text-slate-400 truncate">
              {selectedFile.filename}
            </p>
          </div>
          <a
            href={selectedFile.path}
            download
            class="inline-flex items-center gap-1.5 rounded-xl bg-slate-900 px-3.5 py-2 text-xs font-semibold text-white shadow-sm hover:bg-slate-800 transition-colors no-underline shrink-0"
          >
            <svg
              class="h-3.5 w-3.5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2.5"
              stroke-linecap="round"
              stroke-linejoin="round"
              ><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v4" /><polyline
                points="7 10 12 15 17 10"
              /><line x1="12" y1="15" x2="12" y2="3" /></svg
            >
            Download File
          </a>
        </div>

        <div
          class="flex-grow overflow-auto p-4 flex items-center justify-center min-h-0 w-full"
        >
          {#if fileExtension === "pdf"}
            <iframe
              src="{selectedFile.path}#toolbar=1"
              title="PDF Document Preview"
              class="w-full h-full rounded-xl border border-slate-200 bg-white shadow-sm"
              frameborder="0"
            ></iframe>
          {:else if fileExtension === "docx"}
            <div
              class="text-center p-8 max-w-md bg-white border border-slate-200 rounded-2xl shadow-sm"
            >
              <div
                class="mx-auto h-12 w-12 text-blue-100 bg-blue-50 rounded-full flex items-center justify-center mb-4"
              >
                <svg
                  class="h-6 w-6 text-blue-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                  ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  /></svg
                >
              </div>
              <h4 class="text-base font-bold text-slate-900 mb-1">
                Document Format (.docx)
              </h4>
              <p class="text-sm text-slate-500 mb-5">
                Microsoft Word application files cannot be directly embedded
                inside the web browser frame. Use the button below to download
                the local resource form file.
              </p>
              <a
                href={selectedFile.path}
                download
                class="inline-flex w-full justify-center items-center rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 transition-colors no-underline"
              >
                Download Request Form
              </a>
            </div>
          {:else}
            <div
              class="max-w-full max-h-full flex items-center justify-center p-2"
            >
              <img
                src={selectedFile.path}
                alt={formatTitle(selectedFile.filename)}
                class="max-w-full max-h-[calc(100vh-280px)] object-contain rounded-lg shadow-md bg-white border border-slate-200"
              />
            </div>
          {/if}
        </div>
      {:else}
        <div class="text-center p-8 select-none">
          <svg
            class="mx-auto h-12 w-12 text-slate-300 mb-3"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="1"
            ><path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            /></svg
          >
          <p class="text-sm font-medium text-slate-500">
            Select a file from the sidebar list to display preview information.
          </p>
        </div>
      {/if}
    </div>
  </div>
</div>
