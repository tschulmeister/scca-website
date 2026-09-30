<script>
    import { page } from "$app/stores";
    import { browser } from "$app/environment";

    let isOpen = $state(false);
    let commentText = $state("");
    let subject = $state("SCCA Website Feedback / Comment");

    function getMailtoUrl() {
        const currentPath = browser ? window.location.href : $page.url.href;
        const fullSubject = `[Website Feedback] ${subject}`;
        const body = `${commentText}\n\n------------------------------------\nRegarding page: ${currentPath}\nShipley's Choice Community Association Website`;
        return `mailto:shipleyschoice.scca@gmail.com?subject=${encodeURIComponent(fullSubject)}&body=${encodeURIComponent(body)}`;
    }

    function handleSubmit(e) {
        e.preventDefault();
        window.location.href = getMailtoUrl();
        isOpen = false;
        commentText = "";
    }

    function handleKeydown(e) {
        if (e.key === "Escape") {
            isOpen = false;
        }
    }
</script>

<svelte:window onkeydown={handleKeydown} />

<!-- Floating Feedback Button -->
<div class="fixed bottom-6 right-6 z-40">
    <button
        type="button"
        onclick={() => (isOpen = true)}
        class="group inline-flex items-center justify-center sm:gap-2.5 bg-blue-600 hover:bg-blue-700 text-white font-medium w-12 h-12 sm:w-auto sm:h-auto sm:px-4 sm:py-3 rounded-full shadow-lg hover:shadow-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer"
        aria-label="Send Feedback to Board"
    >
        <svg
            class="w-5 h-5 transition-transform group-hover:scale-110 shrink-0"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"
            />
        </svg>
        <span class="hidden sm:inline text-sm font-semibold tracking-wide">Feedback</span>
    </button>
</div>

{#if isOpen}
    <!-- Modal Backdrop -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div
        class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4 transition-opacity"
        onclick={() => (isOpen = false)}
    >
        <!-- Modal Dialog -->
        <div
            class="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-lg overflow-hidden p-6 sm:p-8 transform transition-all"
            role="dialog"
            aria-modal="true"
            aria-labelledby="feedback-modal-title"
            tabindex="-1"
            onclick={(e) => e.stopPropagation()}
        >
            <div
                class="flex items-center justify-between pb-4 border-b border-slate-100"
            >
                <div class="flex items-center gap-3">
                    <div
                        class="w-10 h-10 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold"
                    >
                        💬
                    </div>
                    <div>
                        <h3
                            id="feedback-modal-title"
                            class="text-xl font-bold text-slate-900"
                        >
                            Send Feedback to SCCA Board
                        </h3>
                        <p class="text-xs text-slate-500">
                            Direct email to <span
                                class="font-medium text-slate-700"
                                >shipleyschoice.scca@gmail.com</span
                            >
                        </p>
                    </div>
                </div>
                <button
                    type="button"
                    onclick={() => (isOpen = false)}
                    class="text-slate-400 hover:text-slate-600 p-2 rounded-xl hover:bg-slate-100 transition-colors cursor-pointer"
                    aria-label="Close modal"
                >
                    <svg
                        class="w-5 h-5"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M6 18L18 6M6 6l12 12"
                        />
                    </svg>
                </button>
            </div>

            <form onsubmit={handleSubmit} class="mt-6 space-y-5">
                <div>
                    <label
                        for="feedback-subject"
                        class="block text-xs font-semibold uppercase tracking-wider text-slate-600 mb-1.5"
                    >
                        Subject
                    </label>
                    <input
                        id="feedback-subject"
                        type="text"
                        bind:value={subject}
                        class="w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
                        required
                    />
                </div>

                <div>
                    <label
                        for="feedback-message"
                        class="block text-xs font-semibold uppercase tracking-wider text-slate-600 mb-1.5"
                    >
                        Your Comment or Feedback
                    </label>
                    <textarea
                        id="feedback-message"
                        bind:value={commentText}
                        rows="4"
                        placeholder="What's on your mind? Share suggestions, questions, or report issues..."
                        class="w-full rounded-xl border border-slate-300 bg-white p-4 text-sm text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500/20 resize-none"
                        required></textarea>
                    <p class="mt-1.5 text-xs text-slate-500">
                        * Clicking send will open your default email app with
                        this message pre-filled, referencing the current page (<span
                            class="font-mono text-[11px] text-slate-600"
                            >{browser
                                ? window.location.pathname
                                : $page.url.pathname}</span
                        >).
                    </p>
                </div>

                <div class="flex items-center justify-end gap-3 pt-2">
                    <button
                        type="button"
                        onclick={() => (isOpen = false)}
                        class="px-5 py-2.5 rounded-xl border border-slate-300 text-sm font-semibold text-slate-700 hover:bg-slate-50 transition-colors cursor-pointer"
                    >
                        Cancel
                    </button>
                    <button
                        type="submit"
                        class="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-6 py-2.5 rounded-xl text-sm font-semibold shadow-md transition-all cursor-pointer"
                    >
                        <span>Open Email Client</span>
                        <svg
                            class="w-4 h-4"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M14 5l7 7m0 0l-7 7m7-7H3"
                            />
                        </svg>
                    </button>
                </div>
            </form>
        </div>
    </div>
{/if}
