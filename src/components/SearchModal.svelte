<script>
    import { onMount, tick } from "svelte";
    import newsItems from "$data/newsItems.json";
    import meetingNotes from "$data/meetingNotes.json";

    // Svelte 5 runes for bindings and states
    let { isOpen = $bindable(false) } = $props();
    let query = $state("");
    let selectedIndex = $state(0);
    let inputEl = $state(null);
    let resultsContainerEl = $state(null);

    // Eagerly import all .htm files under src/components/news as raw strings for full-text search
    const newsFiles = import.meta.glob("/src/components/news/**/*.htm", {
        query: "?raw",
        import: "default",
        eager: true,
    });

    // Prepare static index for high-fidelity pages
    const staticPages = [
        {
            title: "Home Page",
            path: "/",
            description:
                "Shipley's Choice Community Association home page, sliders, and general overview.",
            tags: ["home", "main"],
        },
        {
            title: "News & Records",
            path: "/news-records",
            description:
                "Latest community announcements, news articles, local safety notes, and historical updates.",
            tags: ["news", "announcements", "records", "updates", "letters"],
        },
        {
            title: "SCBD Overview (Special Community Benefit District)",
            path: "/why-scbd",
            description:
                "All information regarding the petition to establish an SCBD for SCCA to stabilize and automate dues collection.",
            tags: [
                "scbd",
                "dues",
                "tax",
                "benefits",
                "special",
                "district",
                "petition",
            ],
        },
        {
            title: "SCBD FAQ",
            path: "/why-scbd-faq",
            description:
                "Frequently asked questions regarding the proposed Special Community Benefit District.",
            tags: ["scbd", "faq", "questions", "answers", "dues", "petition"],
        },
        {
            title: "2026 SCCA Annual Membership Meeting Virtual Signup",
            path: "/annual-meeting-virtual-signup",
            description:
                "Register to attend the 2026 SCCA Annual Membership Meeting virtually via Google Meet on October 20, 2026.",
            tags: [
                "annual",
                "meeting",
                "membership",
                "virtual",
                "signup",
                "register",
                "google meet",
                "scbd",
                "2026",
            ],
        },
        {
            title: "Community Information",
            path: "/information",
            description:
                "SCCA community history, garbage collection schedules, local utilities, schools, and neighborhood overview.",
            tags: [
                "info",
                "trash",
                "history",
                "school",
                "utilities",
                "garbage",
                "recycling",
            ],
        },
        {
            title: "Official Documents",
            path: "/documents",
            description:
                "Bylaws, covenants, legal filings, and community plats index.",
            tags: [
                "docs",
                "documents",
                "bylaws",
                "covenants",
                "plats",
                "legal",
                "restrictions",
            ],
        },
        {
            title: "Architectural Requests",
            path: "/architecture-requests",
            description:
                "Guidelines, forms, and standards for submitting structural/exterior property updates (e.g. fences, decks, additions).",
            tags: [
                "architecture",
                "arc",
                "requests",
                "fence",
                "standards",
                "form",
                "acr",
                "changes",
                "application",
            ],
        },
        {
            title: "Common Area Trees",
            path: "/trees",
            description:
                "SCCA policies on tree removal, hazardous trees, and common area forest maintenance.",
            tags: [
                "trees",
                "common",
                "removal",
                "forest",
                "hazard",
                "maintenance",
                "developer",
                "wooded",
            ],
        },
        {
            title: "Maintenance Information",
            path: "/maintenance-info",
            description:
                "Details on Shipley's Choice common grounds, mowing schedules, landscaping, and community-owned property.",
            tags: [
                "maintenance",
                "landscaping",
                "common",
                "mowing",
                "grass",
                "ground",
            ],
        },
        {
            title: "Frequently Asked Questions (FAQ)",
            path: "/faq",
            description:
                "General community FAQs regarding dues, architectural controls, and neighborhood rules.",
            tags: ["faq", "questions", "answers", "rules", "dues"],
        },
        {
            title: "Board Responsibilities",
            path: "/board",
            description:
                "The role of the SCCA Board of Directors, list of members, duties, and officers.",
            tags: [
                "board",
                "directors",
                "officers",
                "responsibilities",
                "elections",
                "bylaws",
            ],
        },
        {
            title: "Board Meeting Notes",
            path: "/meeting-notes",
            description:
                "Official SCCA board meeting minutes and records since 2025.",
            tags: [
                "meetings",
                "notes",
                "minutes",
                "discussions",
                "votes",
                "decisions",
            ],
        },
        {
            title: "Contact SCCA Board",
            path: "/contact",
            description:
                "Contact information, emails, and address to reach the SCCA Board of Directors.",
            tags: [
                "contact",
                "email",
                "address",
                "help",
                "support",
                "president",
            ],
        },
        {
            title: "Register with SCCA",
            path: "/register",
            description:
                "Register your household with the Shipley's Choice Community Association (SCCA).",
            tags: [
                "register",
                "membership",
                "resident",
                "realtor",
                "signup",
                "dues",
            ],
        },
    ];

    // Prepare static index for PDF documents and Plats
    const officialDocs = [
        {
            title: "SCCA Bylaws (PDF Document)",
            path: "/data/docs/scca_by-laws.pdf",
            description: "Official SCCA governing bylaws.",
            tags: ["bylaws", "bylaw", "governance", "rules"],
        },
        {
            title: "Fence Standards & Guidelines (PDF Document)",
            path: "/data/docs/scca_fence_standards_v4[389].pdf",
            description:
                "Specific SCCA standards for installing or modifying backyard fences.",
            tags: [
                "fence",
                "standards",
                "fences",
                "backyard",
                "guidelines",
                "height",
            ],
        },
        {
            title: "Section 1 Covenants (PDF Document)",
            path: "/data/docs/scca_section_1_covenants.pdf",
            description:
                "Official covenants, conditions, and restrictions for homes in Section 1.",
            tags: [
                "covenants",
                "section 1",
                "restrictions",
                "covenant",
                "easement",
            ],
        },
        {
            title: "Section 2 Covenants (PDF Document)",
            path: "/data/docs/scca_section_2_covenants.pdf",
            description:
                "Official covenants, conditions, and restrictions for homes in Section 2.",
            tags: [
                "covenants",
                "section 2",
                "restrictions",
                "covenant",
                "easement",
            ],
        },
        {
            title: "Architectural Change Request (ACR) Form (Word Document)",
            path: "/data/docs/scca_architectural_request_form.docx",
            description:
                "Official Word document application form for making exterior property changes.",
            tags: [
                "acr",
                "form",
                "arc",
                "request",
                "architectural",
                "change",
                "download",
            ],
        },
        {
            title: "SCCA Covenants Legal Filing (PDF Document)",
            path: "/data/docs/scca_covenants_legal_filing.pdf",
            description:
                "SCCA original covenants legal recording documentation.",
            tags: ["covenants", "legal", "filing"],
        },
        {
            title: "Section 1 Covenants Extension (PDF Document)",
            path: "/data/docs/sect_1_covenents_extention.pdf",
            description:
                "Legal extension documents of the covenants for Section 1.",
            tags: ["covenants", "extension", "section 1"],
        },
        {
            title: "Section 1 Assignment to SCCA - 1980 (PDF Document)",
            path: "/data/docs/sect_1_assignment_to_scca__1980-08-01_.pdf",
            description:
                "Assignment document transferring developers' rights to SCCA in 1980.",
            tags: ["assignment", "section 1", "history", "1980"],
        },
        {
            title: "Section 1 - Plat 1 (JPG Plats)",
            path: "/data/plats/section_1_-_plat_1.jpg",
            description: "High-resolution lot plat map for Section 1, Plat 1.",
            tags: ["plat", "section 1", "map", "lot", "boundary"],
        },
        {
            title: "Section 1 - Plat 2 (JPG Plats)",
            path: "/data/plats/section_1_-_plat_2.jpg",
            description: "High-resolution lot plat map for Section 1, Plat 2.",
            tags: ["plat", "section 1", "map", "lot", "boundary"],
        },
        {
            title: "Section 1 - Plat 3 (JPG Plats)",
            path: "/data/plats/section_1_-_plat_3.jpg",
            description: "High-resolution lot plat map for Section 1, Plat 3.",
            tags: ["plat", "section 1", "map", "lot", "boundary"],
        },
        {
            title: "Section 1 - Plat 4 (JPG Plats)",
            path: "/data/plats/section_1_-_plat_4.jpg",
            description: "High-resolution lot plat map for Section 1, Plat 4.",
            tags: ["plat", "section 1", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 1 Original (JPG Plats)",
            path: "/data/plats/section_2_-_plat_1__original_.jpg",
            description:
                "High-resolution original plat map for Section 2, Plat 1.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 1 Revised (JPG Plats)",
            path: "/data/plats/section_2_-_plat_1__revised_.jpg",
            description:
                "High-resolution revised plat map for Section 2, Plat 1.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 2 (JPG Plats)",
            path: "/data/plats/section_2_-_plat_2.jpg",
            description: "High-resolution lot plat map for Section 2, Plat 2.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 3 (JPG Plats)",
            path: "/data/plats/section_2_-_plat_3.jpg",
            description: "High-resolution lot plat map for Section 2, Plat 3.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 4 (JPG Plats)",
            path: "/data/plats/section_2_-_plat_4.jpg",
            description: "High-resolution lot plat map for Section 2, Plat 4.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 5 (JPG Plats)",
            path: "/data/plats/section_2_-_plat_5.jpg",
            description: "High-resolution lot plat map for Section 2, Plat 5.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
        {
            title: "Section 2 - Plat 6 (JPG Plats)",
            path: "/data/plats/section_2_-_plat_6.jpg",
            description: "High-resolution lot plat map for Section 2, Plat 6.",
            tags: ["plat", "section 2", "map", "lot", "boundary"],
        },
    ];

    // Process and clean up raw HTML contents of all news files for local search indexing
    const newsSearchItems = newsItems.map((item) => {
        let rawText = "";
        if (item.contentPath) {
            const fullPath = `/src/components/news/${item.contentPath}`;
            const rawHtml = newsFiles[fullPath] || "";
            // Strip HTML tags and replace multiple spaces
            rawText = rawHtml
                .replace(/<[^>]*>/g, " ")
                .replace(/\s+/g, " ")
                .trim();
        }
        return {
            id: item.id,
            title: item.title,
            date: item.date,
            tags: item.tags || [],
            fullText: rawText,
            path: `/news-records#${item.id}`,
        };
    });

    // Prepare searchable board meeting notes
    const meetingNotesSearchItems = meetingNotes.map((note) => {
        return {
            id: note.id,
            dateLabel: note.dateLabel,
            participants: note.participants,
            content: note.content,
            path: `/meeting-notes#${note.id}`,
        };
    });

    // Helper: safe text extraction & visual highlighted snippet generator
    function createSnippet(text, term) {
        if (!text || !term) return "";
        const index = text.toLowerCase().indexOf(term.toLowerCase());
        if (index === -1) {
            return text.length > 110 ? text.substring(0, 110) + "..." : text;
        }

        const start = Math.max(0, index - 45);
        const end = Math.min(text.length, index + term.length + 55);
        let snippet = text.substring(start, end);

        if (start > 0) {
            snippet = "..." + snippet;
        }
        if (end < text.length) {
            snippet = snippet + "...";
        }

        // Safety check & escape HTML to protect from raw input injection before marking
        let escapedSnippet = snippet
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");

        // Highlight matches using regex (case-insensitive)
        const escapedTerm = term.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
        const regex = new RegExp(`(${escapedTerm})`, "gi");

        return escapedSnippet.replace(
            regex,
            '<mark class="bg-blue-100 text-blue-900 font-semibold px-0.5 rounded">$1</mark>',
        );
    }

    // Svelte 5 reactive derived search calculations
    let results = $derived.by(() => {
        const term = query.trim().toLowerCase();
        if (term.length < 2) return [];

        let matched = [];

        // 1. Static Informational Pages
        staticPages.forEach((p) => {
            const matchTitle = p.title.toLowerCase().includes(term);
            const matchDesc = p.description.toLowerCase().includes(term);
            const matchTags = p.tags.some((t) =>
                t.toLowerCase().includes(term),
            );
            if (matchTitle || matchDesc || matchTags) {
                matched.push({
                    type: "Page",
                    title: p.title,
                    subtitle: p.description,
                    path: p.path,
                    icon: "page",
                });
            }
        });

        // 2. Official PDF Documents & Plats
        officialDocs.forEach((d) => {
            const matchTitle = d.title.toLowerCase().includes(term);
            const matchDesc = d.description.toLowerCase().includes(term);
            const matchTags = d.tags.some((t) =>
                t.toLowerCase().includes(term),
            );
            if (matchTitle || matchDesc || matchTags) {
                matched.push({
                    type: "Document",
                    title: d.title,
                    subtitle: d.description,
                    path: d.path,
                    icon: "doc",
                });
            }
        });

        // 3. Dynamic News Records (Full text)
        newsSearchItems.forEach((n) => {
            const matchTitle = n.title.toLowerCase().includes(term);
            const matchTags = n.tags.some((t) =>
                t.toLowerCase().includes(term),
            );
            const matchText = n.fullText.toLowerCase().includes(term);

            if (matchTitle || matchTags || matchText) {
                let snippet = "";
                if (matchText) {
                    snippet = createSnippet(n.fullText, term);
                } else {
                    snippet =
                        n.fullText.length > 110
                            ? n.fullText.substring(0, 110) + "..."
                            : n.fullText;
                }
                matched.push({
                    type: "News",
                    title: n.title,
                    subtitle: snippet,
                    path: n.path,
                    icon: "news",
                    isHtml: true,
                });
            }
        });

        // 4. Board Meeting Notes
        meetingNotesSearchItems.forEach((m) => {
            const matchDate = m.dateLabel.toLowerCase().includes(term);
            const matchParticipants = m.participants
                .toLowerCase()
                .includes(term);
            const matchContent = m.content.toLowerCase().includes(term);

            if (matchDate || matchParticipants || matchContent) {
                let snippet = "";
                if (matchContent) {
                    snippet = createSnippet(m.content, term);
                } else if (matchParticipants) {
                    snippet = `Attendees: ${m.participants}`;
                } else {
                    snippet =
                        m.content.length > 110
                            ? m.content.substring(0, 110) + "..."
                            : m.content;
                }
                matched.push({
                    type: "Meeting",
                    title: `Meeting Minutes: ${m.dateLabel}`,
                    subtitle: snippet,
                    path: m.path,
                    icon: "meeting",
                    isHtml: true,
                });
            }
        });

        return matched;
    });

    // Reset selected result on query change
    $effect(() => {
        query;
        selectedIndex = 0;
    });

    // Auto-focus input when modal opens
    $effect(() => {
        if (isOpen) {
            tick().then(() => {
                if (inputEl) inputEl.focus();
            });
            // Lock scroll on body
            document.body.style.overflow = "hidden";
        } else {
            query = "";
            document.body.style.overflow = "";
        }
    });

    // Hotkey listener (Ctrl+K, Cmd+K, or / to search)
    onMount(() => {
        const handleKeyDown = (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === "k") {
                e.preventDefault();
                isOpen = !isOpen;
            } else if (
                e.key === "/" &&
                !isOpen &&
                document.activeElement.tagName !== "INPUT" &&
                document.activeElement.tagName !== "TEXTAREA"
            ) {
                e.preventDefault();
                isOpen = true;
            }
        };

        window.addEventListener("keydown", handleKeyDown);
        return () => {
            window.removeEventListener("keydown", handleKeyDown);
            document.body.style.overflow = "";
        };
    });

    // Handle navigation & closing modal
    function navigateTo(path) {
        isOpen = false;
        // Standard link navigation, but if it is an anchor on the same page, force scroll/hash update
        window.location.href = path;
    }

    // Handle keydown while search is focused
    function handleInputKeyDown(e) {
        if (e.key === "Escape") {
            e.preventDefault();
            isOpen = false;
        } else if (e.key === "ArrowDown") {
            e.preventDefault();
            if (results.length > 0) {
                selectedIndex = (selectedIndex + 1) % results.length;
                scrollToActiveItem();
            }
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            if (results.length > 0) {
                selectedIndex =
                    (selectedIndex - 1 + results.length) % results.length;
                scrollToActiveItem();
            }
        } else if (e.key === "Enter") {
            e.preventDefault();
            if (results.length > 0 && results[selectedIndex]) {
                navigateTo(results[selectedIndex].path);
            }
        }
    }

    // Keep selected item visible in list container
    function scrollToActiveItem() {
        tick().then(() => {
            if (!resultsContainerEl) return;
            const activeEl = resultsContainerEl.querySelector(
                `[data-index="${selectedIndex}"]`,
            );
            if (activeEl) {
                activeEl.scrollIntoView({ block: "nearest" });
            }
        });
    }

    // Suggested search terms
    const suggestions = [
        "bylaws",
        "covenants",
        "fence standards",
        "scbd",
        "trees",
    ];
</script>

{#if isOpen}
    <!-- Backdrop Overlay -->
    <div
        class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm transition-opacity"
        onclick={() => (isOpen = false)}
        onkeydown={(e) => e.key === "Escape" && (isOpen = false)}
        role="button"
        tabindex="-1"
        aria-label="Close search overlay"
    ></div>

    <!-- Search Window Wrapper -->
    <div
        class="fixed inset-0 z-50 overflow-y-auto p-4 sm:p-6 md:p-20 flex justify-center items-start"
    >
        <div
            class="relative bg-white rounded-2xl shadow-2xl border border-slate-200/80 overflow-hidden flex flex-col max-w-2xl w-full max-h-[80vh] transition-all transform scale-100"
            onclick={(e) => e.stopPropagation()}
            role="none"
        >
            <!-- Search input header -->
            <div class="relative flex items-center border-b border-slate-100">
                <!-- Search Icon -->
                <svg
                    class="pointer-events-none absolute left-4 h-5 w-5 text-slate-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        fill-rule="evenodd"
                        d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                        clip-rule="evenodd"
                    />
                </svg>

                <input
                    bind:this={inputEl}
                    type="text"
                    bind:value={query}
                    onkeydown={handleInputKeyDown}
                    placeholder="Search news, minutes, bylaws, plats..."
                    class="w-full bg-transparent pl-12 pr-12 py-4 text-slate-800 placeholder-slate-400 focus:outline-none sm:text-base"
                    aria-label="Search field"
                />

                <!-- Close button / hint -->
                <button
                    type="button"
                    onclick={() => (isOpen = false)}
                    class="absolute right-4 text-slate-400 hover:text-slate-600 focus:outline-none flex items-center gap-1"
                >
                    <span
                        class="hidden sm:inline text-xs bg-slate-100 px-1.5 py-0.5 rounded text-slate-400 border border-slate-200"
                        >ESC</span
                    >
                    <svg
                        class="h-5 w-5"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M6 18L18 6M6 6l12 12"
                        />
                    </svg>
                </button>
            </div>

            <!-- Search results and instructions -->
            <div
                bind:this={resultsContainerEl}
                class="overflow-y-auto flex-1 min-h-[150px]"
            >
                {#if query.trim().length === 0}
                    <!-- Idle / Suggested state -->
                    <div class="p-6">
                        <h3
                            class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3"
                        >
                            Popular Searches
                        </h3>
                        <div class="flex flex-wrap gap-2 mb-6">
                            {#each suggestions as term}
                                <button
                                    type="button"
                                    onclick={() => (query = term)}
                                    class="px-3 py-1.5 bg-slate-50 border border-slate-200/80 hover:bg-blue-50 hover:border-blue-300 hover:text-blue-600 text-slate-600 rounded-full text-xs font-medium transition-colors"
                                >
                                    {term}
                                </button>
                            {/each}
                        </div>

                        <div
                            class="mt-4 border-t border-slate-100 pt-4 text-xs text-slate-400"
                        >
                            <p>
                                Type keywords to search community bylaws,
                                covenants, meeting minutes, news archives, and
                                subdivision plats instantly.
                            </p>
                        </div>
                    </div>
                {:else if query.trim().length < 2}
                    <!-- Prompt to enter more chars -->
                    <div class="p-10 text-center text-slate-400">
                        <p class="text-sm">
                            Type at least 2 characters to search...
                        </p>
                    </div>
                {:else if results.length === 0}
                    <!-- No results found -->
                    <div class="p-12 text-center text-slate-400">
                        <svg
                            class="mx-auto h-12 w-12 text-slate-300 mb-3"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.5"
                                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                        </svg>
                        <p class="text-sm">
                            No results found for <span
                                class="font-semibold text-slate-600"
                                >"{query}"</span
                            >
                        </p>
                        <p class="text-xs mt-1">
                            Try another keyword or search term.
                        </p>
                    </div>
                {:else}
                    <!-- Results list -->
                    <div class="p-2 space-y-0.5">
                        <div
                            class="px-3 py-2 text-[10px] font-semibold uppercase tracking-wider text-slate-400 flex justify-between"
                        >
                            <span>Search Results ({results.length})</span>
                            <span class="hidden sm:inline"
                                >Use ↑↓ keys to navigate, ↵ to open</span
                            >
                        </div>

                        {#each results as item, index}
                            <button
                                type="button"
                                data-index={index}
                                onclick={() => navigateTo(item.path)}
                                class="w-full text-left flex items-start gap-3 p-3 rounded-xl transition-all {selectedIndex ===
                                index
                                    ? 'bg-blue-600 text-white shadow-md'
                                    : 'hover:bg-slate-50 text-slate-800'}"
                            >
                                <!-- Category Icon -->
                                <div
                                    class="shrink-0 mt-0.5 p-1 rounded-lg {selectedIndex ===
                                    index
                                        ? 'bg-blue-700/60 text-blue-100'
                                        : 'bg-slate-100 text-slate-500'}"
                                >
                                    {#if item.icon === "page"}
                                        <!-- Page Icon -->
                                        <svg
                                            class="h-4 w-4"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                        >
                                            <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                                            />
                                        </svg>
                                    {:else if item.icon === "doc"}
                                        <!-- Doc / PDF Icon -->
                                        <svg
                                            class="h-4 w-4"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                        >
                                            <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                                            />
                                        </svg>
                                    {:else if item.icon === "news"}
                                        <!-- Megaphone / News Icon -->
                                        <svg
                                            class="h-4 w-4"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                        >
                                            <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"
                                            />
                                        </svg>
                                    {:else}
                                        <!-- Calendar / Meeting Notes Icon -->
                                        <svg
                                            class="h-4 w-4"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                        >
                                            <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                                            />
                                        </svg>
                                    {/if}
                                </div>

                                <!-- Title & text snippet -->
                                <div class="flex-1 min-w-0">
                                    <div
                                        class="flex items-center justify-between gap-2"
                                    >
                                        <span
                                            class="font-semibold text-sm truncate"
                                            >{item.title}</span
                                        >
                                        <span
                                            class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded shrink-0 {selectedIndex ===
                                            index
                                                ? 'bg-blue-500 text-white'
                                                : 'bg-slate-100 text-slate-500'}"
                                        >
                                            {item.type}
                                        </span>
                                    </div>
                                    <p
                                        class="text-xs mt-1 leading-normal line-clamp-2 {selectedIndex ===
                                        index
                                            ? 'text-blue-100'
                                            : 'text-slate-500'}"
                                    >
                                        {#if item.isHtml}
                                            <!-- Highlight snippet with mark tag -->
                                            {@html item.subtitle}
                                        {:else}
                                            {item.subtitle}
                                        {/if}
                                    </p>
                                </div>
                            </button>
                        {/each}
                    </div>
                {/if}
            </div>

            <!-- Keyboard instructions footer bar -->
            <div
                class="bg-slate-50 border-t border-slate-100 px-4 py-2 flex items-center justify-between text-[10px] text-slate-400"
            >
                <div class="flex gap-3">
                    <span class="flex items-center gap-1">
                        <kbd
                            class="bg-white border px-1 rounded shadow-sm font-sans font-semibold text-slate-500"
                            >↑↓</kbd
                        > Navigate
                    </span>
                    <span class="flex items-center gap-1">
                        <kbd
                            class="bg-white border px-1 rounded shadow-sm font-sans font-semibold text-slate-500"
                            >↵</kbd
                        > Select
                    </span>
                    <span class="flex items-center gap-1">
                        <kbd
                            class="bg-white border px-1 rounded shadow-sm font-sans font-semibold text-slate-500"
                            >ESC</kbd
                        > Close
                    </span>
                </div>
                <span class="hidden sm:inline"
                    >Search by Shipley's Choice Community Association</span
                >
            </div>
        </div>
    </div>
{/if}
