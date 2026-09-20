<script>
    import Seo from "$components/Seo.svelte";
    import { Mail, Calendar, ChevronRight, ExternalLink } from "@lucide/svelte";
    import emailBlasts from "$data/emailBlasts.json";

    // Eagerly import all .htm files under src/components/emails as raw strings
    const emailFiles = import.meta.glob("/src/components/emails/**/*.htm", {
        query: "?raw",
        import: "default",
        eager: true,
    });

    // Combine metadata and file contents
    const processedEmails = emailBlasts.map((item) => {
        const fullPath = `/src/components/emails/${item.contentPath}`;
        let content =
            emailFiles[fullPath] ||
            "<p class='text-rose-500'>Email content file not found.</p>";

        // Dynamically strip Brevo's unsubscribe links so they don't appear in the archive.
        // This regex matches and deletes any anchor tags (<a>...</a>) containing href="{{ unsubscribe }}"
        content = content.replace(
            /<a[^>]*href=["']\{\{\s*unsubscribe\s*\}\}["'][^>]*>[\s\S]*?<\/a>/gi,
            ""
        );

        return {
            ...item,
            content,
        };
    });

    // Svelte 5 state management
    let selectedId = $state(processedEmails[0]?.id || "");
    let mobileView = $state("list"); // 'list' or 'detail'
    
    const selectedEmail = $derived(
        processedEmails.find((e) => e.id === selectedId) || processedEmails[0]
    );

    function selectEmail(id) {
        selectedId = id;
        mobileView = "detail";
    }

    function openInNewWindow() {
        if (!selectedEmail) return;
        const win = window.open();
        if (win) {
            win.document.write(selectedEmail.content);
            win.document.close();
        }
    }
</script>

<Seo
    title="Email Archive"
    description="Browse previous SCCA email blasts, neighborhood announcements, meeting invitations, and regular community newsletters."
/>

<section class="page-header py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Archive</p>
        <h1 class="mt-4 text-4xl font-extrabold tracking-tight">
            Resident Email Archive
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            Browse previous email communications, announcements, and newsletters
            sent to Shipley's Choice residents through Brevo.
        </p>
    </div>
</section>

<section class="max-w-7xl mx-auto px-4 py-12">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- Sidebar / Email List -->
        <aside class="lg:col-span-4 space-y-4 {mobileView === 'detail' ? 'hidden lg:block' : ''}">
            <h2 class="text-lg font-bold text-slate-900 px-1">Sent Messages ({processedEmails.length})</h2>
            
            <div class="space-y-2 max-h-[700px] overflow-y-auto pr-2">
                {#each processedEmails as email}
                    <button
                        type="button"
                        onclick={() => selectEmail(email.id)}
                        class="w-full text-left p-4 rounded-2xl border transition-all duration-200 shadow-sm block focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
                        class:bg-blue-50={selectedId === email.id}
                        class:border-blue-400={selectedId === email.id}
                        class:bg-white={selectedId !== email.id}
                        class:border-slate-200={selectedId !== email.id}
                        class:hover:border-slate-300={selectedId !== email.id}
                        class:hover:bg-slate-50={selectedId !== email.id}
                    >
                        <div class="flex items-center justify-between gap-2 mb-1.5">
                            <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-500">
                                <Calendar size={14} />
                                {email.date}
                            </span>
                            <ChevronRight size={16} class="text-slate-400" />
                        </div>
                        <h3 class="font-bold text-slate-900 line-clamp-2 leading-snug">
                            {email.title}
                        </h3>
                        {#if email.subject && email.subject !== email.title}
                            <p class="text-xs text-slate-500 mt-1 line-clamp-1 font-normal">
                                Subject: {email.subject}
                            </p>
                        {/if}
                    </button>
                {/each}
            </div>
        </aside>

        <!-- Main Email View -->
        <main class="lg:col-span-8 flex flex-col {mobileView === 'list' ? 'hidden lg:flex' : ''}">
            {#if selectedEmail}
                <div class="bg-white border border-slate-200 rounded-3xl overflow-hidden shadow-sm flex flex-col h-[750px]">
                    <!-- View Header -->
                    <div class="p-6 border-b border-slate-100 bg-slate-50">
                        <button
                            type="button"
                            onclick={() => mobileView = "list"}
                            class="lg:hidden inline-flex items-center gap-1 text-sm font-semibold text-blue-600 hover:text-blue-700 mb-3"
                        >
                            &larr; Back to messages
                        </button>
                        
                        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                            <div class="min-w-0">
                                <div class="flex items-center gap-2 text-xs font-medium text-slate-500 mb-1">
                                    <Mail size={14} />
                                    <span>Sent via Brevo on {selectedEmail.date}</span>
                                </div>
                                <h2 class="text-xl font-bold text-slate-900 leading-tight truncate">
                                    {selectedEmail.title}
                               </h2>
                            </div>
                            
                            <button
                                type="button"
                                onclick={openInNewWindow}
                                class="inline-flex items-center justify-center gap-1.5 rounded-xl bg-blue-50 px-4 py-2 text-blue-600 text-sm font-semibold hover:bg-blue-100 transition-colors whitespace-nowrap self-start sm:self-center"
                            >
                                <ExternalLink size={14} />
                                Full screen
                            </button>
                        </div>
                    </div>

                    <!-- View Frame Container -->
                    <div class="flex-1 bg-slate-100 relative">
                        <iframe
                            title={selectedEmail.title}
                            srcdoc={selectedEmail.content}
                            class="w-full h-full border-0 bg-white outline-none focus:outline-none"
                            style="outline: none;"
                            sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin"
                        ></iframe>
                    </div>
                </div>
            {:else}
                <div class="bg-slate-50 border border-slate-200 rounded-3xl p-12 text-center h-[500px] flex flex-col items-center justify-center">
                    <Mail size={48} class="text-slate-300 mb-4" />
                    <h3 class="text-lg font-bold text-slate-900 mb-1">No Email Selected</h3>
                    <p class="text-slate-500 max-w-sm">
                        Choose an email from the left sidebar to view its contents.
                    </p>
                </div>
            {/if}
        </main>
    </div>
</section>
