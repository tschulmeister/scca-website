<script>
    import Seo from "$components/Seo.svelte";
    import financialsData from "../../../static/data/financials/scca-financials.json";

    // Format helpers
    const formatCurrency = (val) =>
        new Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
        }).format(val ?? 0);

    const formatPercent = (val) =>
        new Intl.NumberFormat("en-US", {
            style: "percent",
            minimumFractionDigits: 1,
        }).format(val ?? 0);

    const formatDate = (dateStr) => {
        if (!dateStr) return "";
        const [year, month, day] = dateStr.split("-").map(Number);
        return new Intl.DateTimeFormat("en-US", {
            year: "numeric",
            month: "long",
            day: "numeric",
        }).format(new Date(year, month - 1, day));
    };

    // Sort reports with the most recent year first
    const reports = [...(financialsData.reports || [])].sort((a, b) => b.year - a.year);

    // Selected year state rune, default to latest report
    let selectedYear = $state(reports[0]?.year ?? 2026);

    // Derived active report rune
    let activeReport = $derived(
        reports.find((r) => r.year === selectedYear) ?? reports[0]
    );

    let balances = $derived(activeReport?.balance_summary ?? {});
    let expenses = $derived(activeReport?.expenses ?? []);
    let totals = $derived(activeReport?.total_expenses ?? {});
    let duesStats = $derived(activeReport?.dues_statistics ?? []);

    // Derived playground funds calculation
    let playgroundTotal = $derived(
        (balances.remaining_playground_funds ?? 0) + (balances.playground_deposits ?? 0)
    );

    // Overall percent spent
    let percentSpent = $derived(
        totals.budgeted > 0 ? totals.actual / totals.budgeted : 0
    );
</script>

<Seo
    title="Financial Condition"
    description="Official annual statements of financial condition, operating expenditures, balance sheets, and member dues metrics for Shipley's Choice Community Association."
/>

<!-- Header Section -->
<section class="page-header py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm uppercase tracking-[0.24em] text-blue-300">
            Official Disclosures & Transparency
        </p>
        <h1 class="mt-4 text-4xl font-extrabold tracking-tight text-white">
            Statements of Financial Condition
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            Review certified balance sheets, operational expenditures, and historical
            member dues metrics for Shipley's Choice Community Association.
        </p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
    <!-- Statement Date Picker / Tabs -->
    <div
        class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5"
    >
        <div>
            <h2 class="text-xl font-bold text-slate-900">
                Archived Statements of Financial Condition
            </h2>
            <p class="text-xs text-slate-500 mt-1">
                Select an annual reporting period statement compiled by the SCCA Treasurer
            </p>
        </div>
        <div
            class="inline-flex flex-wrap rounded-xl bg-slate-100 p-1 border border-slate-200 shadow-inner"
        >
            {#each reports as r}
                <button
                    type="button"
                    class="px-5 py-2.5 rounded-lg text-xs font-bold transition-all {selectedYear ===
                    r.year
                        ? 'bg-white text-blue-700 shadow-sm'
                        : 'text-slate-600 hover:text-slate-900'}"
                    onclick={() => (selectedYear = r.year)}
                >
                    {r.year} Statement
                    {#if r.is_final === false}
                        <span class="ml-1.5 text-[10px] font-semibold px-1.5 py-0.5 rounded bg-amber-100 text-amber-800 border border-amber-300">
                            Interim (Not Final)
                        </span>
                    {:else if r.year === 2025}
                        <span class="ml-1.5 text-[10px] font-semibold px-1.5 py-0.5 rounded bg-blue-100 text-blue-700">
                            Latest Final
                        </span>
                    {/if}
                </button>
            {/each}
        </div>
    </div>

    <!-- Interim / Unfinalized Notice Banner -->
    {#if activeReport.is_final === false}
        <div
            class="bg-amber-50/90 border-l-4 border-amber-500 rounded-xl p-4 sm:p-5 shadow-sm space-y-2"
        >
            <div class="flex items-start gap-3">
                <span class="p-1.5 bg-amber-100 rounded-lg text-amber-700 mt-0.5 flex-shrink-0">
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
                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                        />
                    </svg>
                </span>
                <div class="space-y-1">
                    <div class="flex items-center gap-2 flex-wrap">
                        <h3 class="text-sm font-bold text-amber-900">
                            Interim Report Notice — Fiscal Year {activeReport.year} (Not Finalized)
                        </h3>
                        <span
                            class="text-[10px] uppercase font-extrabold px-2 py-0.5 rounded-full bg-amber-200/90 text-amber-900"
                        >
                            In Progress / Unfinalized
                        </span>
                    </div>
                    <p class="text-xs text-slate-700 leading-relaxed">
                        {activeReport.notes || `The financial condition figures for fiscal year ${activeReport.year} represent interim year-to-date accounts as of ${formatDate(activeReport.as_of_date)}. Because the fiscal year is actively underway, revenues, remaining vendor invoices, and reserve allocations are subject to ongoing reconciliation until annual fiscal year-end close.`}
                    </p>
                </div>
            </div>
        </div>
    {/if}

    <!-- Official Memorandum Section -->
    <div
        class="bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden"
    >
        <div class="bg-slate-900 px-6 py-4 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
                <span class="p-1.5 bg-blue-500/20 rounded-lg text-blue-400">
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
                            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                        />
                    </svg>
                </span>
                <span
                    class="text-white font-semibold text-sm uppercase tracking-wider"
                    >Treasurer's Annual Statement</span
                >
            </div>
            <span class="text-xs text-slate-400 font-medium"
                >Effective Date: {formatDate(activeReport.as_of_date)}</span
            >
        </div>
        <div class="p-6 md:p-8 space-y-6">
            <div
                class="grid grid-cols-1 md:grid-cols-4 gap-x-8 gap-y-4 text-sm border-b border-slate-100 pb-6"
            >
                <div>
                    <span
                        class="text-slate-400 uppercase tracking-wider text-xs font-bold block"
                        >Organization:</span
                    >
                    <span class="font-semibold text-slate-800 text-base"
                        >Shipley's Choice Community Association</span
                    >
                </div>
                <div>
                    <span
                        class="text-slate-400 uppercase tracking-wider text-xs font-bold block"
                        >Treasurer:</span
                    >
                    <span class="font-semibold text-slate-800 text-base"
                        >{activeReport.treasurer}</span
                    >
                </div>
                <div>
                    <span
                        class="text-slate-400 uppercase tracking-wider text-xs font-bold block"
                        >Reporting Period:</span
                    >
                    <span class="font-semibold text-slate-800 text-base"
                        >FY {activeReport.year} ({activeReport.is_final === false ? 'YTD as of ' : 'as of '}{formatDate(activeReport.as_of_date)})</span
                    >
                </div>
                <div>
                    <span
                        class="text-slate-400 uppercase tracking-wider text-xs font-bold block"
                        >Report Status:</span
                    >
                    {#if activeReport.is_final === false}
                        <span class="inline-flex items-center gap-1.5 font-bold text-amber-700 text-xs bg-amber-50 px-2.5 py-1 rounded-md border border-amber-200 mt-1">
                            <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
                            Interim / Not Final
                        </span>
                    {:else}
                        <span class="inline-flex items-center gap-1.5 font-semibold text-emerald-700 text-xs bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200 mt-1">
                            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                            Final / Closed FY
                        </span>
                    {/if}
                </div>
            </div>
            <p class="text-slate-600 leading-relaxed text-sm">
                {#if activeReport.is_final === false}
                    This statement presents interim, year-to-date financial condition metrics for the Shipley's Choice Community Association (SCCA) during the {activeReport.year} fiscal year as of {formatDate(activeReport.as_of_date)}. These figures reflect current operating account balances, held reserves, and YTD expenditures against the approved annual operating budget. All accounts remain subject to final year-end reconciliation and closing.
                {:else}
                    This statement presents the official financial condition of the Shipley's Choice Community Association (SCCA) for the {activeReport.year} fiscal year. As an all-volunteer community association, funds are dedicated to neighborhood safety, common ground maintenance, entrance landscaping, utility lighting, and required liability insurance. Below is the full disclosure of operating accounts, designated reserves, and line-item actual expenditures relative to the approved budget.
                {/if}
            </p>
        </div>
    </div>

    <!-- Accounts Balance Grid -->
    <div class="space-y-4">
        <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
            <svg
                class="h-5 w-5 text-blue-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
                />
            </svg>
            Summary of Cash Positions ({activeReport.is_final === false ? 'Interim as of ' : 'as of '}{formatDate(activeReport.as_of_date)})
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <!-- Checking Balance -->
            <div
                class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden"
            >
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg
                        class="h-16 w-16"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="1.5"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"
                        />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p
                        class="text-xs font-bold text-slate-400 uppercase tracking-wider"
                    >
                        Checking Balance
                    </p>
                    <p class="mt-2 text-3xl font-black text-slate-900">
                        {formatCurrency(balances.checking_balance)}
                    </p>
                    <p class="mt-1 text-xs text-slate-500">
                        {activeReport.is_final === false ? 'Interim operating account balance' : 'Gross funds in operating bank account'}
                    </p>
                </div>
            </div>

            <!-- Playground Funds / Deposits -->
            <div
                class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden"
            >
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg
                        class="h-16 w-16"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="1.5"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p
                        class="text-xs font-bold text-slate-400 uppercase tracking-wider"
                    >
                        Playground Reserves / Escrow
                    </p>
                    <p class="mt-2 text-3xl font-black text-amber-600">
                        {formatCurrency(playgroundTotal)}
                    </p>
                    <p class="mt-1 text-xs text-slate-500">
                        {#if (balances.remaining_playground_funds ?? 0) > 0 && (balances.playground_deposits ?? 0) > 0}
                            Reserve: {formatCurrency(balances.remaining_playground_funds)} | Deposits: {formatCurrency(balances.playground_deposits)}
                        {:else if (balances.remaining_playground_funds ?? 0) > 0}
                            Section 2 playground reserve funds
                        {:else if (balances.playground_deposits ?? 0) > 0}
                            Section 2 playground escrow deposits
                        {:else}
                            No restricted playground funds held
                        {/if}
                    </p>
                </div>
            </div>

            <!-- Outstanding Checks -->
            <div
                class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden"
            >
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg
                        class="h-16 w-16"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="1.5"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p
                        class="text-xs font-bold text-slate-400 uppercase tracking-wider"
                    >
                        Outstanding Checks
                    </p>
                    <p
                        class="mt-2 text-3xl font-black {(balances.outstanding_checks ?? 0) > 0
                            ? 'text-rose-600'
                            : 'text-slate-900'}"
                    >
                        {formatCurrency(balances.outstanding_checks)}
                    </p>
                    <p class="mt-1 text-xs text-slate-500">
                        Issued but uncashed vendor payments
                    </p>
                </div>
            </div>

            <!-- Final Balance -->
            <div
                class="rounded-xl border p-5 shadow-sm relative overflow-hidden transition-colors {(balances.final_balance ?? 0) < 0
                    ? 'bg-rose-50/50 border-rose-200'
                    : 'bg-gradient-to-br from-blue-50 to-blue-100/50 border-blue-200/80'}"
            >
                <div
                    class="absolute right-3 top-3 {(balances.final_balance ?? 0) < 0
                        ? 'text-rose-200/40'
                        : 'text-blue-200/40'}"
                >
                    <svg
                        class="h-16 w-16"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="1.5"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"
                        />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p
                        class="text-xs font-bold uppercase tracking-wider {(balances.final_balance ?? 0) < 0
                            ? 'text-rose-600'
                            : 'text-blue-600'}"
                    >
                        {activeReport.is_final === false ? 'Interim Net Balance' : 'Final Net Balance'}
                    </p>
                    <p
                        class="mt-2 text-3xl font-black {(balances.final_balance ?? 0) < 0
                            ? 'text-rose-800'
                            : 'text-blue-800'}"
                    >
                        {formatCurrency(balances.final_balance)}
                    </p>
                    <p
                        class="mt-1 text-xs {(balances.final_balance ?? 0) < 0
                            ? 'text-rose-600/80'
                            : 'text-blue-600/80'}"
                    >
                        {activeReport.is_final === false ? 'Interim net cash (pending remainder of FY)' : 'Unencumbered cash after escrow & checks'}
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- Expenses & Budget Performance Table -->
    <div class="space-y-4">
        <div
            class="flex flex-col sm:flex-row sm:items-center justify-between gap-4"
        >
            <div>
                <h2
                    class="text-xl font-bold text-slate-900 flex items-center gap-2"
                >
                    <svg
                        class="h-5 w-5 text-blue-600"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                    {activeReport.year} Operating Budget vs. {activeReport.is_final === false ? 'YTD Actual (Interim)' : 'Actual Expenditures'}
                </h2>
                <p class="text-sm text-slate-500 mt-1">
                    {activeReport.is_final === false
                        ? `Itemized year-to-date spending against approved annual budget (not finalized, as of ${formatDate(activeReport.as_of_date)})`
                        : `Itemized expenses and variance relative to the approved annual budget (compiled as of ${formatDate(activeReport.as_of_date)})`}
                </p>
            </div>

            <div
                class="inline-flex items-center gap-2 bg-slate-100 rounded-lg p-1.5 text-xs font-semibold text-slate-700 border border-slate-200"
            >
                <span
                    class="inline-block w-2.5 h-2.5 rounded-full {(totals.difference ?? 0) < 0
                        ? 'bg-rose-500'
                        : 'bg-emerald-500'}"
                ></span>
                <span>
                    {(totals.difference ?? 0) < 0 ? 'Net Variance: ' : (activeReport.is_final === false ? 'Remaining Budget: ' : 'Net Surplus: ')}
                    {(totals.difference ?? 0) >= 0 ? '+' : ''}{formatCurrency(totals.difference)}
                </span>
            </div>
        </div>

        <div
            class="bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden"
        >
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr
                            class="bg-slate-50 border-b border-slate-200 text-xs font-bold uppercase tracking-wider text-slate-500"
                        >
                            <th class="px-6 py-4">Expense Category</th>
                            <th class="px-6 py-4 text-right">{activeReport.is_final === false ? 'Actual Spent (YTD)' : 'Actual Spent'}</th>
                            <th class="px-6 py-4 text-right">Approved Budget</th>
                            <th class="px-6 py-4 text-right">{activeReport.is_final === false ? 'Remaining Budget' : 'Difference (Variance)'}</th>
                            <th class="px-6 py-4 text-center">Budget Spent</th>
                        </tr>
                    </thead>
                    <tbody
                        class="divide-y divide-slate-150 text-sm text-slate-700"
                    >
                        {#each expenses as item}
                            {@const budget = item.budgeted ?? 0}
                            {@const actual = item.actual ?? 0}
                            {@const diff = item.difference ?? (budget - actual)}
                            {@const hasBudget = budget > 0}
                            {@const pct = hasBudget ? actual / budget : (actual > 0 ? 1 : 0)}
                            {@const isOver = hasBudget ? actual > budget : actual > 0}
                            <tr
                                class="hover:bg-slate-50/50 transition-colors group"
                            >
                                <td class="px-6 py-4 font-semibold text-slate-900">
                                    {item.category}
                                </td>
                                <td
                                    class="px-6 py-4 text-right font-medium text-slate-800"
                                >
                                    {actual > 0 ? formatCurrency(actual) : "$0.00"}
                                </td>
                                <td
                                    class="px-6 py-4 text-right font-medium text-slate-600"
                                >
                                    {budget > 0 ? formatCurrency(budget) : "$0.00"}
                                </td>
                                <td class="px-6 py-4 text-right font-semibold">
                                    {#if diff < 0}
                                        <span class="text-rose-600">
                                            {formatCurrency(diff)}
                                        </span>
                                    {:else if diff > 0}
                                        <span class="text-emerald-600">
                                            +{formatCurrency(diff)}
                                        </span>
                                    {:else}
                                        <span class="text-slate-500">
                                            $0.00
                                        </span>
                                    {/if}
                                </td>
                                <td class="px-6 py-4">
                                    <div
                                        class="flex flex-col items-center gap-1.5 min-w-[120px] mx-auto"
                                    >
                                        <div
                                            class="w-full bg-slate-100 rounded-full h-2 overflow-hidden border border-slate-200/50"
                                        >
                                            <div
                                                class="h-full rounded-full transition-all duration-500 {isOver
                                                    ? 'bg-rose-500'
                                                    : 'bg-blue-600'}"
                                                style="width: {hasBudget
                                                    ? Math.min(100, Math.max(0, pct * 100))
                                                    : (actual > 0 ? 100 : 0)}%"
                                            ></div>
                                        </div>
                                        <span
                                            class="text-[11px] font-bold {isOver
                                                ? 'text-rose-600'
                                                : 'text-slate-500'}"
                                        >
                                            {#if hasBudget}
                                                {formatPercent(pct)}
                                            {:else if actual > 0}
                                                Unbudgeted
                                            {:else}
                                                —
                                            {/if}
                                        </span>
                                    </div>
                                </td>
                            </tr>
                        {/each}

                        <!-- Summary Row -->
                        <tr class="bg-slate-900 text-white font-bold text-sm">
                            <td class="px-6 py-5">
                                <div class="text-base text-white">
                                    Consolidated Operating Totals
                                </div>
                                <div
                                    class="text-xs text-slate-400 font-normal mt-1 leading-normal"
                                >
                                    {activeReport.is_final === false
                                        ? 'Year-to-date spending vs. full-year operating budget (subject to final year-end closing).'
                                        : 'Total verified actual expenses against the approved annual operating budget.'}
                                </div>
                            </td>
                            <td
                                class="px-6 py-5 text-right text-base text-blue-300"
                            >
                                {formatCurrency(totals.actual)}
                            </td>
                            <td
                                class="px-6 py-5 text-right text-base text-slate-300"
                            >
                                {formatCurrency(totals.budgeted)}
                            </td>
                            <td
                                class="px-6 py-5 text-right text-base {(totals.difference ?? 0) < 0
                                    ? 'text-rose-400'
                                    : 'text-emerald-400'}"
                            >
                                {(totals.difference ?? 0) >= 0 ? '+' : ''}{formatCurrency(totals.difference)}
                            </td>
                            <td class="px-6 py-5">
                                <div
                                    class="flex flex-col items-center gap-1.5 min-w-[120px] mx-auto"
                                >
                                    <div
                                        class="w-full bg-slate-800 rounded-full h-2.5 overflow-hidden border border-slate-700"
                                    >
                                        <div
                                            class="h-full rounded-full transition-all duration-500 {percentSpent > 1
                                                ? 'bg-rose-500'
                                                : 'bg-blue-500'}"
                                            style="width: {Math.min(100, Math.max(0, percentSpent * 100))}%"
                                        ></div>
                                    </div>
                                    <span
                                        class="text-xs font-black {percentSpent > 1 ? 'text-rose-400' : 'text-blue-300'}"
                                    >
                                        {formatPercent(percentSpent)} spent
                                    </span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Member Dues Collection Statistics -->
    {#if duesStats && duesStats.length > 0}
        <div class="space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <svg
                            class="h-5 w-5 text-blue-600"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                            stroke-width="2"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                            />
                        </svg>
                        Member Dues Collection History
                    </h2>
                    <p class="text-xs text-slate-500 mt-1">
                        Annual voluntary dues collection metrics as recorded in the {activeReport.year} Statement of Financial Condition
                    </p>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
                {#each duesStats as stat}
                    <div class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">
                                {stat.payment_year} Fiscal Year
                                {#if stat.payment_year === 2026}
                                    <span class="text-[10px] font-semibold text-amber-700 bg-amber-100 px-1 py-0.2 rounded ml-1">YTD</span>
                                {/if}
                            </span>
                            <span class="text-sm font-black text-slate-900">
                                {stat.percentage}%
                            </span>
                        </div>
                        <div>
                            <span class="text-2xl font-black text-slate-800">
                                {stat.members_paid}
                            </span>
                            <span class="text-xs text-slate-500 ml-1">
                                / 283 households
                            </span>
                        </div>
                        <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden border border-slate-200/50">
                            <div
                                class="h-full rounded-full transition-all duration-500 {stat.percentage >= 75
                                    ? 'bg-blue-600'
                                    : stat.percentage >= 70
                                      ? 'bg-indigo-500'
                                      : 'bg-amber-500'}"
                                style="width: {stat.percentage}%"
                            ></div>
                        </div>
                        <p class="text-[11px] text-slate-500 font-medium">
                            Voluntary dues participation rate
                        </p>
                    </div>
                {/each}
            </div>
        </div>
    {/if}

    <!-- Multi-Year Comparative Summary -->
    <div class="space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
                <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                    <svg
                        class="h-5 w-5 text-blue-600"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                        />
                    </svg>
                    Multi-Year Comparative Summary
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                    Side-by-side annual comparison of approved budgets, actual operating expenses, and ending balances
                </p>
            </div>
        </div>

        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden">
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-50 border-b border-slate-200 text-xs font-bold uppercase tracking-wider text-slate-500">
                            <th class="px-6 py-4">Fiscal Year</th>
                            <th class="px-6 py-4">Effective Date</th>
                            <th class="px-6 py-4 text-right">Budgeted Expenses</th>
                            <th class="px-6 py-4 text-right">Actual Expenses</th>
                            <th class="px-6 py-4 text-right">Net Variance</th>
                            <th class="px-6 py-4 text-right">Final Operating Balance</th>
                            <th class="px-6 py-4 text-center">Action</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-sm text-slate-700">
                        {#each reports as r}
                            <tr class="hover:bg-slate-50/60 transition-colors {selectedYear === r.year ? 'bg-blue-50/40 font-semibold' : ''}">
                                <td class="px-6 py-4">
                                    <span class="font-bold text-slate-900">{r.year} Statement</span>
                                    {#if r.is_final === false}
                                        <span class="ml-2 text-[10px] font-semibold px-1.5 py-0.5 rounded bg-amber-100 text-amber-800 border border-amber-300">Interim (Not Final)</span>
                                    {:else if r.year === 2025}
                                        <span class="ml-2 text-[10px] font-semibold px-1.5 py-0.5 rounded bg-blue-100 text-blue-700">Latest Final</span>
                                    {/if}
                                </td>
                                <td class="px-6 py-4 text-slate-600 text-xs font-medium">
                                    {formatDate(r.as_of_date)}
                                </td>
                                <td class="px-6 py-4 text-right text-slate-600 font-medium">
                                    {formatCurrency(r.total_expenses?.budgeted)}
                                </td>
                                <td class="px-6 py-4 text-right text-slate-900 font-semibold">
                                    {formatCurrency(r.total_expenses?.actual)}
                                    {#if r.is_final === false}
                                        <span class="text-xs text-amber-600 font-bold ml-0.5" title="Interim year-to-date figure">*</span>
                                    {/if}
                                </td>
                                <td class="px-6 py-4 text-right font-semibold">
                                    {#if (r.total_expenses?.difference ?? 0) < 0}
                                        <span class="text-rose-600">{formatCurrency(r.total_expenses?.difference)}</span>
                                    {:else}
                                        <span class="text-emerald-600">+{formatCurrency(r.total_expenses?.difference)}</span>
                                    {/if}
                                </td>
                                <td class="px-6 py-4 text-right text-slate-900 font-bold">
                                    {formatCurrency(r.balance_summary?.final_balance)}
                                </td>
                                <td class="px-6 py-4 text-center">
                                    <button
                                        type="button"
                                        class="text-xs font-bold px-3 py-1.5 rounded-lg border transition-all {selectedYear === r.year
                                            ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                                            : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-100'}"
                                        onclick={() => (selectedYear = r.year)}
                                    >
                                        {selectedYear === r.year ? 'Selected' : 'View Report'}
                                    </button>
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
            <div class="px-6 py-3 bg-slate-50 border-t border-slate-100 text-[11px] text-slate-500">
                * Note: Fiscal Year 2026 data reflects interim year-to-date figures as of September 19, 2026 and has not been finalized.
            </div>
        </div>
    </div>

    <!-- Official Ledger & Open Data Download Callout -->
    <div
        class="bg-slate-900 rounded-2xl border border-slate-800 p-8 text-white relative overflow-hidden shadow-lg"
    >
        <div
            class="absolute right-0 bottom-0 transform translate-x-12 translate-y-12 text-slate-800 opacity-20 pointer-events-none"
        >
            <svg
                class="h-64 w-64"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="1.5"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                />
            </svg>
        </div>
        <div class="relative z-10 max-w-3xl space-y-4">
            <span
                class="bg-blue-500/20 text-blue-300 border border-blue-500/30 px-3 py-1 text-xs font-bold rounded-full uppercase tracking-wider inline-block"
                >Open Financial Data</span
            >
            <h3 class="text-2xl font-black tracking-tight text-white">
                Official Data Downloads & Schema
            </h3>
            <p class="text-slate-300 text-sm leading-relaxed">
                The SCCA maintains verified Statements of Financial Condition in an open, structured JSON format conforming to Draft 2020-12 JSON Schema. We make raw financial datasets and schema definitions publicly accessible to ensure total transparency, reproducibility, and community oversight.
            </p>
            <div class="pt-2 flex flex-wrap gap-4">
                <a
                    href="/data/financials/scca-financials.json"
                    download="scca-financials.json"
                    class="inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-md transition-all text-sm group"
                >
                    <svg
                        class="h-5 w-5 text-blue-200 group-hover:text-white"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2.5"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                        />
                    </svg>
                    Download Financials JSON
                </a>
                <a
                    href="/data/financials/financials-schema.json"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition-all text-sm font-bold rounded-xl"
                >
                    <svg
                        class="h-5 w-5 text-slate-400 group-hover:text-white"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        stroke-width="2"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                        />
                    </svg>
                    View JSON Schema
                </a>
                <a
                    href="/documents"
                    class="inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition-all text-sm font-bold rounded-xl"
                >
                    View Governing Documents
                </a>
            </div>
        </div>
    </div>
</div>
