<script>
    import { format } from "d3-format";

    // Format helpers
    const formatCurrency = (val) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(val);
    const formatPercent = (val) => new Intl.NumberFormat('en-US', { style: 'percent', minimumFractionDigits: 1 }).format(val);

    // Official data from SCCA_SoFC_as_of_06042026.xlsx
    const balances = {
        checking: 8227.91,
        playgroundFunds: 1464.70,
        outstandingChecks: 0.00,
        netBalance: 6763.21,
        asOfDate: "June 4, 2026",
        treasurer: "Rebecca Blaschak",
        subject: "Statement of Financial Condition"
    };

    const expenses = [
        { 
            category: "Lawn Maintenance", 
            actual: 845.00, 
            budget: 3500.00, 
            notes: "Ongoing contract for commons areas mowing, weed control, and edge-trimming." 
        },
        { 
            category: "Garden Club", 
            actual: 0.00, 
            budget: 400.00, 
            notes: "Annual grant for community entry signs landscaping and flower beds." 
        },
        { 
            category: "Real Property taxes", 
            actual: 0.00, 
            budget: 55.00, 
            notes: "Required property taxes on SCCA-owned common land parcels." 
        },
        { 
            category: "Access Tree Removal", 
            actual: 0.00, 
            budget: 8000.00, 
            notes: "Emergency tree cutting, safety trimming, and hazardous arbor care along common property." 
        },
        { 
            category: "BGE", 
            actual: 153.44, 
            budget: 300.00, 
            notes: "Electricity for lighting the main community entrances." 
        },
        { 
            category: "Insurance", 
            actual: 4279.00, 
            budget: 3850.00, 
            notes: "Comprehensive liability coverage. Exceeded budget due to industry-wide commercial rate hikes." 
        },
        { 
            category: "Association Memberships", 
            actual: 100.00, 
            budget: 200.00, 
            notes: "Dues for Maryland Homeowners Association registries and regional civic coalitions." 
        },
        { 
            category: "Website renewal", 
            actual: 0.00, 
            budget: 125.00, 
            notes: "Annual hosting, domain security certifications, and technical platform licensing." 
        },
        { 
            category: "Misc (checks, paper statements, SCSTC)", 
            actual: 64.64, 
            budget: 120.00, 
            notes: "Treasury printing, postage, billing stationery, state filings, and banking fees." 
        }
    ];

    // Totals calculations
    const totalActual = expenses.reduce((sum, item) => sum + item.actual, 0);
    const totalBudget = expenses.reduce((sum, item) => sum + item.budget, 0);
    const totalDiff = totalBudget - totalActual; // Remaining budget
    const totalPercentSpent = totalActual / totalBudget;

    // Historical trends from spreadsheet notes
    const participationHistory = [
        { year: 2026, paid: 194, rate: 0.69, notes: "Current Fiscal Year (as of June 4)" },
        { year: 2025, paid: 196, rate: 0.69, notes: "Prior Fiscal Year Close" },
        { year: 2024, paid: 205, rate: 0.72, notes: "Stable baseline period" },
        { year: 2023, paid: 210, rate: 0.74, notes: "Post-pandemic transition" },
        { year: 2022, paid: 215, rate: 0.76, notes: "Peak voluntary participation" }
    ];

    // Interactive Svelte 5 Runes for simulator
    let simRate = $state(0.69); // Default is current 69%
    const totalHomes = 283;
    const duesPerHome = 75.00;

    // Derived simulator outputs
    let simPaidHomes = $derived(Math.round(simRate * totalHomes));
    let simUnpaidHomes = $derived(totalHomes - simPaidHomes);
    let simRevenue = $derived(simPaidHomes * duesPerHome);
    let simBudgetComparison = $derived(simRevenue - totalBudget);
    let simEffectiveCostPerPayer = $derived(totalBudget / simPaidHomes);
    let simSubsidyPerPayer = $derived(simEffectiveCostPerPayer - duesPerHome);
</script>

<svelte:head>
    <title>Statement of Financial Condition | SCCA</title>
    <meta name="description" content="Official public financial reports, balance sheets, and annual budget tracking for the Shipley's Choice Community Association (SCCA)." />
</svelte:head>

<!-- Header Section -->
<section class="page-header py-20" style="--page-header-bg: url('/data/img/community_overhead.png');">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm uppercase tracking-[0.24em] text-blue-300">Financial Transparency</p>
        <h1 class="mt-4 text-4xl font-extrabold tracking-tight text-white">Statement of Financial Condition</h1>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">
            View verified accounts, current operational expenses, and historical funding metrics for Shipley's Choice Community Association.
        </p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
    
    <!-- Official Memorandum Section -->
    <div class="bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden">
        <div class="bg-slate-900 px-6 py-4 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
                <span class="p-1.5 bg-blue-500/20 rounded-lg text-blue-400">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                </span>
                <span class="text-white font-semibold text-sm uppercase tracking-wider">Treasurer's Memoranda</span>
            </div>
            <span class="text-xs text-slate-400 font-medium">As of June 4, 2026</span>
        </div>
        <div class="p-6 md:p-8 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4 text-sm border-b border-slate-100 pb-6">
                <div>
                    <span class="text-slate-400 uppercase tracking-wider text-xs font-bold block">To:</span>
                    <span class="font-semibold text-slate-800 text-base">Shipley's Choice Community Assoc. Officers, Directors & Members</span>
                </div>
                <div>
                    <span class="text-slate-400 uppercase tracking-wider text-xs font-bold block">From:</span>
                    <span class="font-semibold text-slate-800 text-base">{balances.treasurer}, Treasurer</span>
                </div>
                <div>
                    <span class="text-slate-400 uppercase tracking-wider text-xs font-bold block">Subject:</span>
                    <span class="font-semibold text-slate-800 text-base">{balances.subject}</span>
                </div>
                <div>
                    <span class="text-slate-400 uppercase tracking-wider text-xs font-bold block">Audited Reference File:</span>
                    <a href="/data/financials/SCCA_SoFC_as_of_06042026.xlsx" class="inline-flex items-center gap-1.5 text-blue-600 hover:text-blue-800 font-semibold hover:underline group">
                        SCCA_SoFC_as_of_06042026.xlsx
                        <svg class="h-4 w-4 transform transition-transform group-hover:translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                        </svg>
                    </a>
                </div>
            </div>
            <p class="text-slate-600 leading-relaxed text-sm">
                This statement offers an unvarnished window into the financial position of the Shipley's Choice Community Association (SCCA) as of June 4, 2026. SCCA is entirely board-volunteer driven, with funds deployed strictly to maintain community safety, preserve common acreage woodlands, and manage liability risks. The report provides checking accounts, restricted-use reserves, outstanding balances, and line-item actual expenditures relative to the approved annual budget.
            </p>
        </div>
    </div>

    <!-- Accounts Balance Grid -->
    <div class="space-y-4">
        <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
            <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
            </svg>
            Summary of Cash Positions
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            
            <!-- Checking Balance -->
            <div class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden">
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wider">Checking Balance</p>
                    <p class="mt-2 text-3xl font-black text-slate-900">{formatCurrency(balances.checking)}</p>
                    <p class="mt-1 text-xs text-slate-500">Gross funds in operating bank account</p>
                </div>
            </div>

            <!-- Playground Funds -->
            <div class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden">
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wider">Restricted Playground Funds</p>
                    <p class="mt-2 text-3xl font-black text-amber-600">{formatCurrency(balances.playgroundFunds)}</p>
                    <p class="mt-1 text-xs text-slate-500">Section 2 playground reserve (restricted)</p>
                </div>
            </div>

            <!-- Outstanding Checks -->
            <div class="bg-white rounded-xl border border-slate-200/80 p-5 shadow-sm relative overflow-hidden">
                <div class="absolute right-3 top-3 text-slate-100">
                    <svg class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wider">Outstanding Checks</p>
                    <p class="mt-2 text-3xl font-black text-slate-900">{formatCurrency(balances.outstandingChecks)}</p>
                    <p class="mt-1 text-xs text-slate-500">Issued but uncashed vendor payments</p>
                </div>
            </div>

            <!-- Net Unencumbered Operating Balance -->
            <div class="bg-gradient-to-br from-blue-50 to-blue-100/50 rounded-xl border border-blue-200/80 p-5 shadow-sm relative overflow-hidden">
                <div class="absolute right-3 top-3 text-blue-200/40">
                    <svg class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                    </svg>
                </div>
                <div class="relative z-10">
                    <p class="text-xs font-bold text-blue-600 uppercase tracking-wider">Unencumbered Balance</p>
                    <p class="mt-2 text-3xl font-black text-blue-800">{formatCurrency(balances.netBalance)}</p>
                    <p class="mt-1 text-xs text-blue-600/80">Available cash for ongoing operations</p>
                </div>
            </div>

        </div>
    </div>

    <!-- Expenses & Budget Performance Table -->
    <div class="space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
                <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                    <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    2026 Operating Budget vs. YTD Actual
                </h2>
                <p class="text-sm text-slate-500 mt-1">Detailed expenditures tracking and remaining budget capacities</p>
            </div>
            
            <div class="inline-flex items-center gap-2 bg-slate-100 rounded-lg p-1.5 text-xs font-semibold text-slate-700 border border-slate-200">
                <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <span>Remaining: {formatCurrency(totalDiff)} ({formatPercent(totalDiff / totalBudget)})</span>
            </div>
        </div>

        <div class="bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden">
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-55 border-b border-slate-200 text-xs font-bold uppercase tracking-wider text-slate-500">
                            <th class="px-6 py-4">Expense Category</th>
                            <th class="px-6 py-4 text-right">Actual YTD</th>
                            <th class="px-6 py-4 text-right">Approved Budget</th>
                            <th class="px-6 py-4 text-right">Difference (Remaining)</th>
                            <th class="px-6 py-4 text-center">Spent (%)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-150 text-sm text-slate-700">
                        {#each expenses as item}
                            <tr class="hover:bg-slate-50/50 transition-colors group">
                                <td class="px-6 py-4">
                                    <div class="font-semibold text-slate-900">{item.category}</div>
                                    <div class="text-xs text-slate-400 mt-1 max-w-sm font-normal leading-normal">{item.notes}</div>
                                </td>
                                <td class="px-6 py-4 text-right font-medium text-slate-800">
                                    {item.actual > 0 ? formatCurrency(item.actual) : "$0.00"}
                                </td>
                                <td class="px-6 py-4 text-right font-medium text-slate-600">
                                    {formatCurrency(item.budget)}
                                </td>
                                <td class="px-6 py-4 text-right font-semibold">
                                    {#if item.budget - item.actual < 0}
                                        <span class="text-red-600">
                                            {formatCurrency(item.budget - item.actual)}
                                        </span>
                                    {:else}
                                        <span class="text-emerald-600">
                                            {formatCurrency(item.budget - item.actual)}
                                        </span>
                                    {/if}
                                </td>
                                <td class="px-6 py-4">
                                    <div class="flex flex-col items-center gap-1.5 min-w-[120px] mx-auto">
                                        <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden border border-slate-200/50">
                                            <div 
                                                class="h-full rounded-full transition-all duration-500 {item.actual / item.budget > 1.0 ? 'bg-red-500' : 'bg-blue-600'}" 
                                                style="width: {Math.min(100, (item.actual / item.budget) * 100)}%"
                                            ></div>
                                        </div>
                                        <span class="text-[11px] font-bold {item.actual / item.budget > 1.0 ? 'text-red-600' : 'text-slate-500'}">
                                            {formatPercent(item.actual / item.budget)}
                                        </span>
                                    </div>
                                </td>
                            </tr>
                        {/each}

                        <!-- Summary Row -->
                        <tr class="bg-slate-900 text-white font-bold text-sm">
                            <td class="px-6 py-5">
                                <div class="text-base text-white">Consolidated Operating Budget Totals</div>
                                <div class="text-xs text-slate-400 font-normal mt-1 leading-normal">Operational ledger summaries. Unspent balances roll over to the general capital reserve.</div>
                            </td>
                            <td class="px-6 py-5 text-right text-base text-blue-300">
                                {formatCurrency(totalActual)}
                            </td>
                            <td class="px-6 py-5 text-right text-base text-slate-300">
                                {formatCurrency(totalBudget)}
                            </td>
                            <td class="px-6 py-5 text-right text-base text-emerald-400">
                                {formatCurrency(totalDiff)}
                            </td>
                            <td class="px-6 py-5">
                                <div class="flex flex-col items-center gap-1.5 min-w-[120px] mx-auto">
                                    <div class="w-full bg-slate-800 rounded-full h-2.5 overflow-hidden border border-slate-700">
                                        <div 
                                            class="h-full rounded-full bg-blue-500 transition-all duration-500" 
                                            style="width: {totalPercentSpent * 100}%"
                                        ></div>
                                    </div>
                                    <span class="text-xs font-black text-blue-300">
                                        {formatPercent(totalPercentSpent)} spent
                                    </span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Historical Trend Visual -->
        <div class="lg:col-span-5 space-y-4">
            <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Multi-Year Participation Trend
            </h2>
            <div class="bg-white rounded-2xl border border-slate-200/80 p-6 shadow-sm space-y-6">
                <p class="text-xs text-slate-500 leading-normal">
                    This table tracks the declining number of contributing households under the voluntary SCCA dues system. Only 194 out of 283 properties contributed in 2026.
                </p>

                <div class="space-y-4">
                    {#each participationHistory as p}
                        <div class="space-y-1.5">
                            <div class="flex items-center justify-between text-sm">
                                <span class="font-bold text-slate-900">{p.year} Fiscal Year <span class="text-xs font-normal text-slate-400">({p.paid} Paid)</span></span>
                                <span class="font-black text-slate-700">{formatPercent(p.rate)}</span>
                            </div>
                            <div class="w-full bg-slate-100 rounded-full h-3.5 overflow-hidden border border-slate-200/50 relative">
                                <div 
                                    class="h-full rounded-full transition-all duration-500 {p.rate >= 0.75 ? 'bg-blue-600' : p.rate >= 0.70 ? 'bg-indigo-500' : 'bg-red-500'}" 
                                    style="width: {p.rate * 100}%"
                                ></div>
                                <span class="absolute inset-0 flex items-center justify-center text-[10px] font-black text-slate-600">{p.notes}</span>
                            </div>
                        </div>
                    {/each}
                </div>

                <div class="bg-red-50 rounded-xl p-4 border border-red-100 text-xs text-red-800 leading-relaxed">
                    <p class="font-bold">⚠️ The Consequence of declining participation:</p>
                    <p class="mt-1">
                        With voluntary participation declining to 69%, the funding burden of maintaining essential community safety assets (common woodlands, entrance signs, and liability insurance) is borne unequally. This financial reality has driven the SCCA Board's decision to pursue designation as a Special Community Benefits District (SCBD) to secure fair and dedicated funding from 100% of community properties.
                    </p>
                </div>
            </div>
        </div>

        <!-- Interactive Simulator -->
        <div class="lg:col-span-7 space-y-4">
            <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Voluntary Dues & Burden Simulator
            </h2>
            <div class="bg-white rounded-2xl border border-slate-200/80 p-6 shadow-sm space-y-6">
                <p class="text-xs text-slate-500 leading-normal">
                    Adjust the slider to simulate voluntary dues participation rates. See how declining participation forces active contributors to carry a higher effective "subsidy" to cover the fixed SCCA operating budget ({formatCurrency(totalBudget)}).
                </p>

                <!-- Slider Control -->
                <div class="bg-slate-50 rounded-xl p-5 border border-slate-200/80 space-y-3">
                    <div class="flex justify-between items-center text-sm">
                        <span class="font-bold text-slate-700">Simulated Participation Rate</span>
                        <span class="text-lg font-black text-blue-600">{formatPercent(simRate)}</span>
                    </div>
                    <input 
                        type="range" 
                        min="0.50" 
                        max="1.00" 
                        step="0.01" 
                        bind:value={simRate} 
                        class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-blue-600 border border-slate-300"
                    />
                    <div class="flex justify-between text-[11px] font-bold text-slate-400">
                        <span>50% (Extreme Shortfall)</span>
                        <span>Current (~69%)</span>
                        <span>100% (SCBD Baseline)</span>
                    </div>
                </div>

                <!-- Simulator Outputs -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Contributing Homes</span>
                        <span class="text-2xl font-black text-slate-800 block mt-1">{simPaidHomes} homes</span>
                        <span class="text-xs text-slate-500">{simUnpaidHomes} homes non-contributing</span>
                    </div>

                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Collected Dues Revenue</span>
                        <span class="text-2xl font-black text-slate-800 block mt-1">{formatCurrency(simRevenue)}</span>
                        <span class="text-xs text-slate-500">at standard rate of {formatCurrency(duesPerHome)}/yr</span>
                    </div>

                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Budget Surplus / Deficit</span>
                        {#if simBudgetComparison >= 0}
                            <span class="text-2xl font-black text-emerald-600 block mt-1">+{formatCurrency(simBudgetComparison)}</span>
                            <span class="text-xs text-slate-500">Funds available for capital reserves</span>
                        {:else}
                            <span class="text-2xl font-black text-red-600 block mt-1">{formatCurrency(simBudgetComparison)}</span>
                            <span class="text-xs text-slate-500">SCCA runs a deficit or defers tree removals</span>
                        {/if}
                    </div>

                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200/60">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Effective Cost / Share</span>
                        <span class="text-2xl font-black text-slate-800 block mt-1">{formatCurrency(simEffectiveCostPerPayer)}</span>
                        {#if simSubsidyPerPayer > 0}
                            <span class="text-xs text-red-600 font-semibold">Includes {formatCurrency(simSubsidyPerPayer)} "unpaid gap" subsidy</span>
                        {:else}
                            <span class="text-xs text-emerald-600 font-semibold">Perfect fair-share allocation</span>
                        {/if}
                    </div>

                </div>

                <div class="bg-blue-50/70 border border-blue-100 rounded-xl p-4 text-xs leading-relaxed text-slate-700 space-y-1.5">
                    <p class="font-bold text-blue-800">💡 Simulator Takeaways:</p>
                    <p>
                        At <strong class="text-blue-800">100% participation (the SCBD model)</strong>, every property pays exactly its fair share of <strong>{formatCurrency(duesPerHome)} per year</strong>, which generates <strong>{formatCurrency(totalHomes * duesPerHome)}</strong>. This fully funds the <strong>{formatCurrency(totalBudget)}</strong> operating budget and leaves a healthy <strong>+{formatCurrency((totalHomes * duesPerHome) - totalBudget)}</strong> yearly surplus to safely build long-term reserves for major projects (like playground restoration or common area reforestation).
                    </p>
                    <p class="mt-2">
                        Under the current <strong class="text-red-700">voluntary system (~69% participation)</strong>, SCCA's collected revenue of <strong>{formatCurrency(194 * duesPerHome)} ({formatCurrency(14550)})</strong> actually falls short of the operating budget requirements by <strong>-{formatCurrency(totalBudget - 14550)}</strong>. Contributing neighbors are effectively overpaying: they pay $75, but the effective cost per paying household is actually <strong>{formatCurrency(totalBudget / 194)}</strong> because they are subsidizing non-paying properties.
                    </p>
                </div>
            </div>
        </div>

    </div>

    <!-- Spreadsheet Download Callout -->
    <div class="bg-slate-900 rounded-2xl border border-slate-800 p-8 text-white relative overflow-hidden shadow-lg">
        <div class="absolute right-0 bottom-0 transform translate-x-12 translate-y-12 text-slate-800 opacity-20 pointer-events-none">
            <svg class="h-64 w-64" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
        </div>
        <div class="relative z-10 max-w-3xl space-y-4">
            <span class="bg-blue-500/20 text-blue-300 border border-blue-500/30 px-3 py-1 text-xs font-bold rounded-full uppercase tracking-wider inline-block">Official Ledger</span>
            <h3 class="text-2xl font-black tracking-tight text-white">Download Statement of Financial Condition</h3>
            <p class="text-slate-300 text-sm leading-relaxed">
                Download the original, verified spreadsheet file prepared directly by the SCCA Treasurer. This spreadsheet has been archived and reviewed by the SCCA Audit Committee. We make all official financial spreadsheets available in their raw format to promote total transparency and community oversight.
            </p>
            <div class="pt-2 flex flex-col sm:flex-row gap-4">
                <a 
                    href="/data/financials/SCCA_SoFC_as_of_06042026.xlsx" 
                    download="SCCA_SoFC_as_of_06042026.xlsx"
                    class="inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-md transition-all text-sm group"
                >
                    <svg class="h-5 w-5 text-blue-200 group-hover:text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    Download SCCA_SoFC_as_of_06042026.xlsx
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
