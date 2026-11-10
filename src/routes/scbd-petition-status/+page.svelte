<script>
    import Seo from "$components/Seo.svelte";
    import {
        CheckCircle2,
        XCircle,
        AlertCircle,
        Clock,
        Users,
        FileText,
        TrendingUp,
        Download,
        Info,
        ChevronRight,
        ArrowRight,
    } from "@lucide/svelte";
    import { pie, arc } from "d3-shape";
    import { scaleOrdinal } from "d3-scale";
    import { format } from "d3-format";
    import rawVoteSummary from "../../../static/data/financials/vote_summary.csv?raw";

    let { data } = $props();

    // Use loaded CSV string or bundled raw fallback
    let csvSource = $derived(data?.csvRaw || rawVoteSummary);

    // Robust CSV parser supporting tabs or commas
    function parseCsv(text) {
        if (!text) return [];
        const lines = text
            .trim()
            .split(/\r?\n/)
            .filter((l) => l.trim().length > 0);
        if (lines.length < 2) return [];

        const delimiter = lines[0].includes("\t") ? "\t" : ",";
        const headers = lines[0]
            .split(delimiter)
            .map((h) => h.trim().toLowerCase());

        const voteIdx = headers.findIndex(
            (h) => h.includes("vote") || h.includes("status"),
        );
        const countIdx = headers.findIndex(
            (h) => h.includes("count") || h.includes("property"),
        );
        const dateIdx = headers.findIndex((h) => h.includes("date"));

        const results = [];
        for (let i = 1; i < lines.length; i++) {
            const parts = lines[i].split(delimiter).map((p) => p.trim());
            if (parts.length < 2) continue;
            const vote = parts[voteIdx !== -1 ? voteIdx : 0];
            const count =
                parseInt(parts[countIdx !== -1 ? countIdx : 1], 10) || 0;
            const asOfDate =
                dateIdx !== -1 && parts[dateIdx] ? parts[dateIdx] : "";
            results.push({ vote, count, asOfDate });
        }
        return results;
    }

    let parsedRows = $derived(parseCsv(csvSource));

    // Extract as-of date from CSV data or default
    let asOfDateRaw = $derived(
        parsedRows.find((r) => r.asOfDate)?.asOfDate || "11/5/2026",
    );

    let formattedAsOfDate = $derived.by(() => {
        if (!asOfDateRaw) return "November 5, 2026";
        const parts = asOfDateRaw.split("/");
        if (parts.length === 3) {
            const month = parseInt(parts[0], 10) - 1;
            const day = parseInt(parts[1], 10);
            const year = parseInt(parts[2], 10);
            return new Intl.DateTimeFormat("en-US", {
                month: "long",
                day: "numeric",
                year: "numeric",
            }).format(new Date(year, month, day));
        }
        return asOfDateRaw;
    });

    // Lookup counts by vote category
    let yesCount = $derived(
        parsedRows.find((r) => r.vote.toLowerCase() === "yes")?.count ?? 53,
    );
    let splitCount = $derived(
        parsedRows.find((r) => r.vote.toLowerCase() === "split")?.count ?? 2,
    );
    let noCount = $derived(
        parsedRows.find((r) => r.vote.toLowerCase() === "no")?.count ?? 43,
    );
    let noResponseCount = $derived(
        parsedRows.find((r) => r.vote.toLowerCase().includes("no response"))
            ?.count ?? 185,
    );

    let totalProperties = $derived(
        yesCount + splitCount + noCount + noResponseCount,
    );

    // 2/3 supermajority threshold required to pass
    // 283 * 2/3 = 188.666... => 189 homes
    let passThreshold = $derived(Math.ceil((totalProperties * 2) / 3));
    let remainingNeeded = $derived(Math.max(0, passThreshold - yesCount));
    let yesPctOfTotal = $derived(
        totalProperties > 0 ? (yesCount / totalProperties) * 100 : 0,
    );
    let yesPctOfGoal = $derived(
        passThreshold > 0 ? (yesCount / passThreshold) * 100 : 0,
    );
    let thresholdPct = $derived(
        totalProperties > 0 ? (passThreshold / totalProperties) * 100 : 66.7,
    );

    // Breakdown dataset with colors and descriptors
    let breakdownCategories = $derived([
        {
            id: "yes",
            label: "In Favor (Yes)",
            shortLabel: "In Favor",
            count: yesCount,
            pct: totalProperties > 0 ? (yesCount / totalProperties) * 100 : 0,
            color: "#10b981", // emerald-500
            bgColor: "bg-emerald-500",
            lightBg: "bg-emerald-50",
            textColor: "text-emerald-700",
            borderColor: "border-emerald-200",
            badgeColor: "bg-emerald-100 text-emerald-800 border-emerald-300",
            statusImpact: "Counts toward 2/3 threshold",
            description:
                "Both deed owners (or sole owner) signed in favor of the petition.",
        },
        {
            id: "split",
            label: "Split Decision (1 Yes / 1 No)",
            shortLabel: "Split Vote",
            count: splitCount,
            pct: totalProperties > 0 ? (splitCount / totalProperties) * 100 : 0,
            color: "#f59e0b", // amber-500
            bgColor: "bg-amber-500",
            lightBg: "bg-amber-50",
            textColor: "text-amber-700",
            borderColor: "border-amber-200",
            badgeColor: "bg-amber-100 text-amber-800 border-amber-300",
            statusImpact: "Does NOT count toward passing",
            description:
                "One deed owner signed Yes, but the co-owner voted No. Both deed owners must agree and sign Yes for the property to count in favor.",
        },
        {
            id: "no",
            label: "In Opposition (No)",
            shortLabel: "Opposition",
            count: noCount,
            pct: totalProperties > 0 ? (noCount / totalProperties) * 100 : 0,
            color: "#ef4444", // red-500
            bgColor: "bg-red-500",
            lightBg: "bg-red-50",
            textColor: "text-red-700",
            borderColor: "border-red-200",
            badgeColor: "bg-red-100 text-red-800 border-red-300",
            statusImpact: "Counts in opposition",
            description:
                "Homeowners submitted petition indicating opposition to creating an SCBD.",
        },
        {
            id: "no-response",
            label: "Awaiting Response / Not Yet Signed",
            shortLabel: "No Response",
            count: noResponseCount,
            pct:
                totalProperties > 0
                    ? (noResponseCount / totalProperties) * 100
                    : 0,
            color: "#94a3b8", // slate-400
            bgColor: "bg-slate-400",
            lightBg: "bg-slate-50",
            textColor: "text-slate-600",
            borderColor: "border-slate-200",
            badgeColor: "bg-slate-100 text-slate-700 border-slate-300",
            statusImpact: "Pending potential signature",
            description:
                "Homes in Sections 1 & 2 that have not yet submitted a petition response.",
        },
    ]);

    // D3 Donut Chart dimensions & calculations
    let chartWidth = $state(280);
    let chartHeight = $state(280);
    let hoveredIndex = $state(null);

    let radius = $derived(Math.min(chartWidth, chartHeight) / 2);
    let innerRadius = $derived(radius * 0.64);

    let pieArcs = $derived.by(() => {
        const pieGen = pie()
            .value((d) => d.count)
            .sort(null);
        return pieGen(breakdownCategories.filter((d) => d.count > 0));
    });

    let arcGen = $derived(
        arc()
            .innerRadius(innerRadius)
            .outerRadius(radius * 0.94),
    );

    let arcHoverGen = $derived(
        arc()
            .innerRadius(innerRadius)
            .outerRadius(radius * 0.99),
    );

    let activeHoveredCategory = $derived(
        hoveredIndex !== null && pieArcs[hoveredIndex]
            ? pieArcs[hoveredIndex].data
            : null,
    );

    function triggerCsvDownload() {
        const blob = new Blob([csvSource], {
            type: "text/csv;charset=utf-8;",
        });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "scca_scbd_vote_summary.csv";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
</script>

<Seo
    title="SCBD Petition Status & Signature Tally"
    description="Track the current tally and progress of the Shipley's Choice SCBD petition. Verified signature counts for in favor, opposition, split deed votes, and pending households toward the required 2/3 threshold."
/>

<!-- Header Banner -->
<section class="page-header py-16 sm:py-20">
    <div class="max-w-7xl mx-auto px-4 text-center">
        <div
            class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full text-xs font-semibold tracking-wide uppercase bg-blue-500/20 text-blue-300 border border-blue-400/30 mb-4"
        >
            <TrendingUp size={14} />
            Special Community Benefit District
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white">
            SCBD Petition Status
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-base sm:text-lg text-slate-300">
            Current tally of community petition responses across all 283 homes in Sections 1 and 2.
            A two-thirds supermajority (189 affirmative homes) is required for County approval.
        </p>

        <div class="mt-6 flex flex-wrap items-center justify-center gap-3 text-xs sm:text-sm">
            <span
                class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800/80 text-slate-300 border border-slate-700 backdrop-blur-sm"
            >
                <Clock size={15} class="text-blue-400" />
                Updated as of <strong class="text-white">{formattedAsOfDate}</strong>
            </span>
            <button
                type="button"
                onclick={triggerCsvDownload}
                class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition-colors"
                title="Download raw CSV data"
            >
                <Download size={14} class="text-emerald-400" />
                Download CSV Data
            </button>
        </div>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 py-10 sm:py-14 space-y-10">
    <!-- Key Milestone Metric Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <!-- Yes Signatures -->
        <div
            class="bg-white rounded-2xl p-6 border border-emerald-200 shadow-sm relative overflow-hidden flex flex-col justify-between"
        >
            <div
                class="absolute -top-10 -right-10 w-28 h-28 bg-emerald-50 rounded-full pointer-events-none"
            ></div>
            <div>
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">
                        In Favor (Yes)
                    </span>
                    <span
                        class="p-1.5 rounded-lg bg-emerald-100 text-emerald-600"
                    >
                        <CheckCircle2 size={18} />
                    </span>
                </div>
                <div class="mt-3 flex items-baseline gap-2">
                    <span class="text-4xl font-extrabold text-slate-900">{yesCount}</span>
                    <span class="text-sm font-semibold text-emerald-600">
                        {yesPctOfTotal.toFixed(1)}% of homes
                    </span>
                </div>
                <p class="mt-2 text-xs text-slate-500 leading-relaxed">
                    Verified affirmative petitions with both deed holders signed.
                </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-100">
                <div class="flex justify-between text-xs text-slate-500 mb-1">
                    <span>Progress to 2/3 Goal</span>
                    <span class="font-bold text-emerald-700">{yesPctOfGoal.toFixed(1)}%</span>
                </div>
                <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                    <div
                        class="bg-emerald-500 h-full rounded-full transition-all duration-500"
                        style="width: {Math.min(100, yesPctOfGoal)}%"
                    ></div>
                </div>
            </div>
        </div>

        <!-- 2/3 Goal Requirement -->
        <div
            class="bg-white rounded-2xl p-6 border border-blue-200 shadow-sm relative overflow-hidden flex flex-col justify-between"
        >
            <div
                class="absolute -top-10 -right-10 w-28 h-28 bg-blue-50 rounded-full pointer-events-none"
            ></div>
            <div>
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-blue-700">
                        Target to Pass (2/3)
                    </span>
                    <span class="p-1.5 rounded-lg bg-blue-100 text-blue-600">
                        <TrendingUp size={18} />
                    </span>
                </div>
                <div class="mt-3 flex items-baseline gap-2">
                    <span class="text-4xl font-extrabold text-slate-900">{passThreshold}</span>
                    <span class="text-sm font-semibold text-blue-600">
                        {thresholdPct.toFixed(1)}% required
                    </span>
                </div>
                <p class="mt-2 text-xs text-slate-500 leading-relaxed">
                    Anne Arundel County Code requires 2/3 of all 283 assessable homes to sign Yes.
                </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-600">
                <span class="font-semibold text-slate-800">Supermajority Rule:</span>
                Based on total community parcels, not just ballots cast.
            </div>
        </div>

        <!-- Remaining Needed -->
        <div
            class="bg-white rounded-2xl p-6 border border-amber-200 shadow-sm relative overflow-hidden flex flex-col justify-between"
        >
            <div
                class="absolute -top-10 -right-10 w-28 h-28 bg-amber-50 rounded-full pointer-events-none"
            ></div>
            <div>
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-700">
                        Signatures Needed
                    </span>
                    <span class="p-1.5 rounded-lg bg-amber-100 text-amber-600">
                        <Clock size={18} />
                    </span>
                </div>
                <div class="mt-3 flex items-baseline gap-2">
                    <span class="text-4xl font-extrabold text-slate-900">{remainingNeeded}</span>
                    <span class="text-sm font-semibold text-amber-600">
                        more Yes votes
                    </span>
                </div>
                <p class="mt-2 text-xs text-slate-500 leading-relaxed">
                    Affirmative signatures still required from pending or split households.
                </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-600">
                Requires <strong class="text-slate-800">{((remainingNeeded / noResponseCount) * 100).toFixed(1)}%</strong> of remaining uncommitted homes to sign Yes.
            </div>
        </div>

        <!-- Opposition & Split -->
        <div
            class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm relative overflow-hidden flex flex-col justify-between"
        >
            <div
                class="absolute -top-10 -right-10 w-28 h-28 bg-rose-50/50 rounded-full pointer-events-none"
            ></div>
            <div>
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-600">
                        Opposed / Split
                    </span>
                    <span class="p-1.5 rounded-lg bg-rose-100 text-rose-600">
                        <XCircle size={18} />
                    </span>
                </div>
                <div class="mt-3 flex items-baseline gap-2">
                    <span class="text-4xl font-extrabold text-slate-900">{noCount + splitCount}</span>
                    <span class="text-sm font-semibold text-rose-600">
                        {(((noCount + splitCount) / totalProperties) * 100).toFixed(1)}%
                    </span>
                </div>
                <p class="mt-2 text-xs text-slate-500 leading-relaxed">
                    <strong>{noCount}</strong> signed in opposition; <strong>{splitCount}</strong> homes split (1 Yes / 1 No on deed).
                </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500">
                Split votes do not count toward the affirmative threshold.
            </div>
        </div>
    </div>

    <!-- Visual Progress to 2/3 Goal Meter -->
    <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-100">
            <div>
                <h2 class="text-xl sm:text-2xl font-bold text-slate-900 flex items-center gap-2.5">
                    <span class="text-2xl">🎯</span> Petition Threshold Progress
                </h2>
                <p class="mt-1 text-sm text-slate-600">
                    Visualizing all 283 homes relative to the Anne Arundel County 2/3 (189 homes) requirement.
                </p>
            </div>
            <div class="flex items-center gap-3 text-xs sm:text-sm">
                <span class="px-3 py-1.5 rounded-xl bg-emerald-50 text-emerald-800 font-semibold border border-emerald-200">
                    {yesCount} of {passThreshold} Yes Votes
                </span>
                <span class="px-3 py-1.5 rounded-xl bg-blue-50 text-blue-800 font-semibold border border-blue-200">
                    2/3 Threshold: 189 Homes
                </span>
            </div>
        </div>

        <!-- Stacked Progress Bar with Threshold Marker -->
        <div class="mt-8 space-y-4">
            <div class="relative pt-6 pb-2">
                <!-- Target Goal Pin Marker -->
                <div
                    class="absolute top-0 transform -translate-x-1/2 flex flex-col items-center pointer-events-none z-10"
                    style="left: {(passThreshold / totalProperties) * 100}%"
                >
                    <span class="px-2 py-0.5 text-[11px] font-bold bg-blue-600 text-white rounded-md shadow-sm whitespace-nowrap">
                        2/3 Target ({passThreshold} homes)
                    </span>
                    <div class="w-0.5 h-3 bg-blue-600"></div>
                </div>

                <!-- Multi-segment bar -->
                <div class="h-9 w-full bg-slate-100 rounded-2xl overflow-hidden flex shadow-inner relative">
                    <!-- Yes Segment -->
                    <div
                        class="bg-emerald-500 h-full transition-all duration-500 flex items-center justify-center text-white text-xs font-bold"
                        style="width: {(yesCount / totalProperties) * 100}%"
                        title="Yes: {yesCount} homes ({yesPctOfTotal.toFixed(1)}%)"
                    >
                        {#if yesCount >= 15}
                            {yesCount} Yes
                        {/if}
                    </div>

                    <!-- Split Segment -->
                    <div
                        class="bg-amber-500 h-full transition-all duration-500 flex items-center justify-center text-white text-xs font-bold"
                        style="width: {(splitCount / totalProperties) * 100}%"
                        title="Split: {splitCount} homes"
                    >
                        {#if splitCount >= 5}
                            {splitCount}
                        {/if}
                    </div>

                    <!-- No Segment -->
                    <div
                        class="bg-rose-500 h-full transition-all duration-500 flex items-center justify-center text-white text-xs font-bold"
                        style="width: {(noCount / totalProperties) * 100}%"
                        title="No: {noCount} homes ({((noCount / totalProperties) * 100).toFixed(1)}%)"
                    >
                        {#if noCount >= 15}
                            {noCount} No
                        {/if}
                    </div>

                    <!-- No Response Segment -->
                    <div
                        class="bg-slate-300 h-full transition-all duration-500 flex items-center justify-center text-slate-700 text-xs font-medium"
                        style="width: {(noResponseCount / totalProperties) * 100}%"
                        title="No Response: {noResponseCount} homes ({((noResponseCount / totalProperties) * 100).toFixed(1)}%)"
                    >
                        {#if noResponseCount >= 20}
                            {noResponseCount} Awaiting Response
                        {/if}
                    </div>

                    <!-- Vertical Threshold Line on Bar -->
                    <div
                        class="absolute top-0 bottom-0 w-0.5 bg-blue-700 z-10"
                        style="left: {(passThreshold / totalProperties) * 100}%"
                    ></div>
                </div>

                <!-- Axis Scale Labels -->
                <div class="mt-2 flex justify-between text-[11px] text-slate-400 font-mono">
                    <span>0 Homes</span>
                    <span style="margin-left: {(passThreshold / totalProperties) * 100}%" class="text-blue-700 font-bold -translate-x-1/2">
                        66.7% (189)
                    </span>
                    <span>283 Homes (100%)</span>
                </div>
            </div>

            <!-- Legend items -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-slate-100">
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-md bg-emerald-500 shrink-0"></span>
                    <span class="text-xs text-slate-700">
                        <strong>In Favor (Yes):</strong> {yesCount} ({yesPctOfTotal.toFixed(1)}%)
                    </span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-md bg-amber-500 shrink-0"></span>
                    <span class="text-xs text-slate-700">
                        <strong>Split Vote:</strong> {splitCount} ({((splitCount / totalProperties) * 100).toFixed(1)}%)
                    </span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-md bg-rose-500 shrink-0"></span>
                    <span class="text-xs text-slate-700">
                        <strong>In Opposition:</strong> {noCount} ({((noCount / totalProperties) * 100).toFixed(1)}%)
                    </span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-md bg-slate-300 shrink-0"></span>
                    <span class="text-xs text-slate-700">
                        <strong>Awaiting Response:</strong> {noResponseCount} ({((noResponseCount / totalProperties) * 100).toFixed(1)}%)
                    </span>
                </div>
            </div>
        </div>
    </div>

    <!-- Chart & Table Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <!-- Donut Chart Breakdown (5 cols) -->
        <div class="lg:col-span-5 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm flex flex-col items-center">
            <h3 class="text-lg font-bold text-slate-900 self-start mb-1">
                Community Distribution
            </h3>
            <p class="text-xs text-slate-500 self-start mb-6">
                Hover over or tap any slice to inspect category statistics.
            </p>

            <div
                class="relative aspect-square w-full max-w-[280px] flex items-center justify-center my-2"
                bind:clientWidth={chartWidth}
                bind:clientHeight={chartHeight}
            >
                {#if chartWidth > 0 && chartHeight > 0}
                    <svg width={chartWidth} height={chartHeight} class="overflow-visible">
                        <g transform="translate({chartWidth / 2}, {chartHeight / 2})">
                            {#each pieArcs as arcData, i}
                                <path
                                    d={hoveredIndex === i
                                        ? arcHoverGen(arcData)
                                        : arcGen(arcData)}
                                    fill={arcData.data.color}
                                    class="transition-all duration-200 ease-out cursor-pointer stroke-white stroke-2"
                                    onmouseenter={() => (hoveredIndex = i)}
                                    onmouseleave={() => (hoveredIndex = null)}
                                    role="presentation"
                                />
                            {/each}
                        </g>
                    </svg>

                    <!-- Center Display -->
                    <div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none px-4 text-center">
                        {#if activeHoveredCategory}
                            <span class="text-[11px] font-semibold uppercase tracking-wider text-slate-500">
                                {activeHoveredCategory.shortLabel}
                            </span>
                            <span class="text-2xl sm:text-3xl font-extrabold text-slate-900 mt-0.5">
                                {activeHoveredCategory.count}
                            </span>
                            <span class="text-xs font-semibold" style="color: {activeHoveredCategory.color}">
                                {activeHoveredCategory.pct.toFixed(1)}% of homes
                            </span>
                        {:else}
                            <span class="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                                Total Properties
                            </span>
                            <span class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-0.5">
                                {totalProperties}
                            </span>
                            <span class="text-xs text-slate-500">
                                Sections 1 & 2
                            </span>
                        {/if}
                    </div>
                {/if}
            </div>

            <!-- Interactive Legend List -->
            <div class="w-full mt-6 space-y-2 border-t border-slate-100 pt-5">
                {#each breakdownCategories as cat, i}
                    <button
                        type="button"
                        class="w-full flex items-center justify-between p-2.5 rounded-xl transition-all text-left {hoveredIndex === i ? 'bg-slate-100 ring-1 ring-slate-300' : 'hover:bg-slate-50'}"
                        onmouseenter={() => (hoveredIndex = i)}
                        onmouseleave={() => (hoveredIndex = null)}
                    >
                        <div class="flex items-center gap-2.5 min-w-0">
                            <span
                                class="w-3.5 h-3.5 rounded-md shrink-0"
                                style="background-color: {cat.color}"
                            ></span>
                            <span class="text-xs sm:text-sm font-semibold text-slate-800 truncate">
                                {cat.label}
                            </span>
                        </div>
                        <div class="flex items-center gap-2 shrink-0">
                            <span class="text-xs font-bold text-slate-900">{cat.count}</span>
                            <span class="text-xs text-slate-400 font-mono w-12 text-right">
                                {cat.pct.toFixed(1)}%
                            </span>
                        </div>
                    </button>
                {/each}
            </div>
        </div>

        <!-- Detailed Breakdown & County Rule Table (7 cols) -->
        <div class="lg:col-span-7 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
            <div>
                <h3 class="text-lg font-bold text-slate-900">
                    Detailed Signature Breakdown
                </h3>
                <p class="mt-1 text-xs sm:text-sm text-slate-600">
                    How each category of response is verified and factored into the Anne Arundel County 2/3 threshold.
                </p>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead>
                        <tr class="border-b border-slate-200 text-slate-400 uppercase text-[11px] tracking-wider font-semibold">
                            <th class="pb-3 pr-4">Category</th>
                            <th class="pb-3 px-3 text-center">Homes</th>
                            <th class="pb-3 px-3 text-center">% Community</th>
                            <th class="pb-3 pl-4">County Impact</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        {#each breakdownCategories as item}
                            <tr class="hover:bg-slate-50/80 transition-colors">
                                <td class="py-3.5 pr-4 align-top">
                                    <div class="font-bold text-slate-900 flex items-center gap-2">
                                        <span class="w-2.5 h-2.5 rounded-full" style="background-color: {item.color}"></span>
                                        {item.label}
                                    </div>
                                    <div class="text-xs text-slate-500 mt-1 pl-4 leading-relaxed">
                                        {item.description}
                                    </div>
                                </td>
                                <td class="py-3.5 px-3 text-center align-top font-bold text-slate-900 text-base">
                                    {item.count}
                                </td>
                                <td class="py-3.5 px-3 text-center align-top font-mono text-slate-600">
                                    {item.pct.toFixed(1)}%
                                </td>
                                <td class="py-3.5 pl-4 align-top">
                                    <span class="inline-block px-2.5 py-1 text-xs font-semibold rounded-lg border {item.badgeColor}">
                                        {item.statusImpact}
                                    </span>
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                    <tfoot>
                        <tr class="border-t-2 border-slate-200 font-bold text-slate-900 bg-slate-50/60">
                            <td class="py-3 px-2">Total Assessable Properties</td>
                            <td class="py-3 px-3 text-center text-base">{totalProperties}</td>
                            <td class="py-3 px-3 text-center font-mono">100.0%</td>
                            <td class="py-3 pl-4 text-xs text-slate-600 font-normal">
                                Sections 1 & 2 Combined
                            </td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <!-- Critical Takeaways Box -->
            <div class="p-4 rounded-2xl bg-blue-50/80 border border-blue-100 text-slate-700 text-xs sm:text-sm space-y-2">
                <div class="font-bold text-blue-900 flex items-center gap-1.5">
                    <Info size={16} class="text-blue-600 shrink-0" />
                    Key Observation for Homeowners:
                </div>
                <p class="leading-relaxed">
                    With <strong>{yesCount}</strong> homes confirmed in favor, <strong>{remainingNeeded} additional homes</strong> must sign in favor to meet the 189 threshold. Because 185 homes have not yet returned a petition, the petition will pass if approximately <strong>{((remainingNeeded / noResponseCount) * 100).toFixed(0)}%</strong> of remaining uncommitted households submit an affirmative petition.
                </p>
            </div>
        </div>
    </div>

    <!-- Essential Guidelines & Rule Explanations -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Both Owners on Deed Rule -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-4">
            <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold">
                <Users size={20} />
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-slate-900">
                Why Both Deed Owners Must Sign Yes
            </h3>
            <p class="text-slate-600 text-sm leading-relaxed">
                Under Anne Arundel County rules governing Special Community Benefit Districts, <strong>each property receives exactly one vote</strong>.
            </p>
            <ul class="text-xs sm:text-sm text-slate-600 space-y-2.5 list-disc pl-5">
                <li>
                    <strong>Both deed owners must agree:</strong> If a property is titled to two people (such as a married couple or co-owners), <em>both signatures</em> are legally required on the petition for the vote to be counted as affirmative.
                </li>
                <li>
                    <strong>Split votes do not count in favor:</strong> If one owner on the deed votes in favor and the other owner votes in opposition (or declines to sign), the household cannot be certified by the County and does <em>not</em> count toward the 2/3 threshold.
                </li>
                <li>
                    <strong>Single deed owner:</strong> Properties owned by an individual only require that single owner's signature.
                </li>
                <li>
                    <strong>Trusts & Partnerships:</strong> If property is held in a trust, the first and signature pages of the trust agreement must accompany the petition. All partners in a partnership must sign.
                </li>
            </ul>
        </div>

        <!-- The 2/3 Supermajority Rule -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-4">
            <div class="w-10 h-10 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold">
                <FileText size={20} />
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-slate-900">
                Understanding the 2/3 Supermajority (189 Homes)
            </h3>
            <p class="text-slate-600 text-sm leading-relaxed">
                Article 4, Title 7 of the Anne Arundel County Code governs the establishment of Special Community Benefit Districts.
            </p>
            <ul class="text-xs sm:text-sm text-slate-600 space-y-2.5 list-disc pl-5">
                <li>
                    <strong>Calculation:</strong> There are 283 total assessable households across Sections 1 & 2. Two-thirds of 283 is 188.67, which rounds up to <strong>189 affirmative votes</strong>.
                </li>
                <li>
                    <strong>Not a plurality vote:</strong> Unlike municipal general elections where a candidate wins by receiving a percentage of votes actually cast, County SCBD law requires signatures from <em>two-thirds of all assessable properties</em> in the district.
                </li>
                <li>
                    <strong>No response functions as a non-affirmative:</strong> A household that does not submit a petition cannot be counted toward the required 189 threshold.
                </li>
                <li>
                    <strong>Ongoing verification:</strong> There is no single "voting day." Petitions are reviewed and validated by the Anne Arundel County Budget Office continuously.
                </li>
            </ul>
        </div>
    </div>

    <!-- How to Submit or Update Petitions -->
    <div
        class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 rounded-3xl p-8 sm:p-10 text-white shadow-lg space-y-6"
    >
        <div class="max-w-3xl">
            <span class="text-xs uppercase tracking-widest text-blue-400 font-semibold">
                Get Involved & Participate
            </span>
            <h3 class="text-2xl sm:text-3xl font-extrabold mt-2 tracking-tight">
                How to Submit Your SCBD Petition
            </h3>
            <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                Whether you wish to submit your household's petition, resolve a split deed situation, or update your signature, the SCCA Board facilitates submission directly to Anne Arundel County.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
            <div class="bg-white/10 rounded-2xl p-5 border border-white/10 backdrop-blur-sm">
                <h4 class="font-bold text-base text-white flex items-center gap-2">
                    <span>📬</span> Mail by Post
                </h4>
                <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                    Mail signed petitions to:<br />
                    <strong class="text-white">Shipley's Choice Community Association</strong><br />
                    315 Arbor Oaks Ct<br />
                    Millersville, MD 21108
                </p>
            </div>

            <div class="bg-white/10 rounded-2xl p-5 border border-white/10 backdrop-blur-sm">
                <h4 class="font-bold text-base text-white flex items-center gap-2">
                    <span>🤝</span> Lost your petition?
                </h4>
                <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                    Send an email to <a href="mailto:shipleyschoice.scca@gmail.com" class="text-blue-300 underline font-semibold">shipleyschoice.scca@gmail.com</a> and coordinate to receive a new copy.
                </p>
            </div>

            <div class="bg-white/10 rounded-2xl p-5 border border-white/10 backdrop-blur-sm">
                <h4 class="font-bold text-base text-white flex items-center gap-2">
                    <span>⚖️</span> Split Deed Resolution
                </h4>
                <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                    If your household was marked split because only one deed owner signed or there was a discrepancy, both owners may sign a new unified petition to update your status.
                </p>
            </div>
        </div>

        <div class="pt-4 border-t border-white/10 flex flex-wrap items-center justify-between gap-4">
            <div class="flex flex-wrap items-center gap-3">
                <a
                    href="/why-scbd"
                    class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs sm:text-sm transition-all shadow"
                >
                    SCBD Overview
                    <ArrowRight size={14} />
                </a>
                <a
                    href="/why-scbd-faq"
                    class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs sm:text-sm border border-slate-700 transition-all"
                >
                    SCBD Frequently Asked Questions
                    <ArrowRight size={14} />
                </a>
            </div>
        </div>
    </div>
</div>
