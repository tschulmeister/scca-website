<script>
	import SparkChart from "$components/charts/SparkChart.svelte";
	import ComparisonBar from "$components/charts/ComparisonBar.svelte";
	import ExpenseDonut from "$components/charts/ExpenseDonut.svelte";
	import financials from "$data/financials.json";
	import { format } from "d3-format";

	const duesRateData = financials.participation_trends.map((r) => ({
		year: r.year,
		value: r.participation_rate_pct / 100,
	}));

	const insuranceExp = financials.annual_expenses_breakdown.find(
		(e) => e.category === "Insurance",
	);
	const insuranceCostsData = [
		{ year: 2022, value: insuranceExp["2022_budget"] },
		{ year: 2023, value: insuranceExp["2023_budget"] },
		{ year: 2024, value: insuranceExp["2024_actual"] },
		{ year: 2025, value: insuranceExp["2025_actual"] },
		{ year: 2026, value: insuranceExp["2026_ytd_actual"] },
	];

	const cashReservesData = financials.statements_of_financial_condition
		.filter((r) => !r.as_of_date.startsWith("2020"))
		.map((r) => ({
			label: r.as_of_date.substring(0, 4),
			value:
				r.balances.net_unencumbered_balance_usd ??
				r.balances.ending_net_balance_usd,
		}));

	const expenses2025 = financials.annual_expenses_breakdown
		.map((e) => ({
			label: e.category,
			value: e["2025_actual"],
		}))
		.filter((e) => e.value > 0);

	const possibleRevenue = [
		{ label: "Operational Baseline", value: 21225, subtitle: "Fully Funded" },
		{ label: "100% Participation", value: 21225, subtitle: "All Homes Share Cost" },
	];

	// New Data for Graph 1: Fair Share vs. Reality
	const fairShareRealityData = [
		{ label: "Target Fair Share", value: 75, subtitle: "Target" },
		{ label: "Actual Paid by Contributors", value: 110, subtitle: "Burden" },
	];

	// New Data for Graph 2: Revenue & Coverage Gap
	const revenueGapData = [
		{ label: "Voluntary System", value: 17829, subtitle: "Current (~$63 avg)" },
		{ label: "SCBD Mandatory", value: 21225, subtitle: "Target ($75/home)" },
	];

	// New Data for Graph 3: Participation (This will be used differently, perhaps a simple representation)
	const participationData = [
		{ label: "Contributing", value: 0.68, subtitle: "~192 homes" },
		{ label: "Non-Contributing", value: 0.32, subtitle: "~91 homes" },
	];

	const gapRevenue = [
		{ label: "Current Revenue", value: 17832, subtitle: "~$63 avg/home" },
		{ label: "Shortfall", value: 3393, subtitle: "Needed to reach $21,225" },
	];

	const schoaComparison = [
		{ label: "SCCA (Current)", value: 17832, subtitle: "~$63 avg/home" },
		{ label: "SCHOA", value: 177120, subtitle: "864 homes @ $205" },
	];

	const comparisonColors = {
		"Current Revenue": "bg-slate-400",
		"Shortfall": "bg-red-500",
		"Operational Baseline": "bg-blue-500",
		"100% Participation": "bg-emerald-500",
		"Target Fair Share": "bg-slate-900",
		"Actual Paid by Contributors": "bg-red-500",
		"Voluntary System": "bg-slate-400",
		"SCBD Mandatory": "bg-blue-500",
		"Contributing": "bg-emerald-500",
		"Non-Contributing": "bg-slate-400",
		"Standard": "bg-slate-400",
		"Effective": "bg-red-500",
		"SCHOA": "bg-emerald-500",
	};
</script>

<svelte:head>
	<title>The Case for an SCBD | SCCA</title>
	<meta
		name="description"
		content="A data-backed analysis of the financial trends driving the need for a Special Community Benefits District (SCBD) in Shipley's Choice."
	/>
</svelte:head>

<section class="page-header py-20">
	<div class="max-w-7xl mx-auto px-4 text-center">
		<p class="text-sm uppercase tracking-[0.24em] text-blue-300">
			Special Announcement
		</p>
		<h1 class="mt-4 text-4xl font-extrabold tracking-tight">
			Be in the Know: Special Community Benefits District
		</h1>
		<p class="mt-4 max-w-2xl mx-auto text-slate-300">
			Why should Shipley's Choice pursue SCBD desgination? Understanding
			the costs and challenges facing our community.
		</p>
	</div>
</section>

<!-- Proposed addition right after the page header -->
<div class="mt-8 mx-auto max-w-4xl px-4">
	<div
		class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-xl p-8 text-white text-center shadow-lg transform transition-transform hover:scale-[1.01]"
	>
		<h2 class="text-2xl font-bold flex items-center justify-center gap-2">
			<span class="text-3xl">🤝</span> Driven by Volunteers
		</h2>
		<p class="mt-4 text-blue-100 text-lg max-w-2xl mx-auto leading-relaxed">
			The Shipley's Choice Community Association Board is comprised
			entirely of <strong>volunteers</strong>—your friends and
			neighbors—who generously contribute their own time to maintain and
			protect our shared community assets.
		</p>
	</div>
</div>

<!-- High-Impact TL;DR Header Card -->
<div class="mt-8 mx-auto max-w-4xl px-4">
	<div
		class="bg-slate-900 text-white rounded-xl border border-slate-700 p-8 shadow-xl"
	>
		<h2 class="text-2xl font-bold text-center text-blue-400">
			⚡ SCBD in 30 Seconds: The Essential Math
		</h2>
		<div class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
			<div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
				<div
					class="text-sm uppercase tracking-wider text-slate-400 font-bold"
				>
					The Goal
				</div>
				<div class="mt-2 text-3xl font-black text-white">$21,225</div>
				<div class="mt-1 text-xs text-slate-300">
					To maintain common grounds, trees, and liability insurance
					annually.
				</div>
			</div>
			<div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
				<div
					class="text-sm uppercase tracking-wider text-slate-400 font-bold"
				>
					Your Share
				</div>
				<div class="mt-2 text-3xl font-black text-emerald-400">
					$75 / Year
				</div>
				<div class="mt-1 text-xs text-slate-300">
					Equates to only <strong>$6.25 per month</strong> per household.
				</div>
			</div>
			<div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
				<div
					class="text-sm uppercase tracking-wider text-slate-400 font-bold"
				>
					The Reality
				</div>
				<div class="mt-2 text-3xl font-black text-red-400">
					$110+ / Year
				</div>
				<div class="mt-1 text-xs text-slate-300">
					Currently paid by donors to cover the 32% of households who
					do not pay.
				</div>
			</div>
		</div>
	</div>
</div>

<div
	class="mt-8 bg-blue-50 py-8 px-4 rounded-xl border border-blue-100 max-w-4xl mx-auto text-center"
>
	<h2 class="text-2xl font-bold text-slate-800">
		The "Invisible" Essentials of Our Community
	</h2>
	<p class="mt-3 text-slate-600 max-w-2xl mx-auto">
		Most of the work the SCCA does operates quietly in the background.
		Without consistent funding, these essential, everyday benefits are at
		risk:
	</p>
	<div
		class="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4 text-sm text-slate-700 font-medium"
	>
		<div class="p-4 bg-white rounded-lg shadow-sm">
			🌳 Maintaining common grounds & trees
		</div>
		<div class="p-4 bg-white rounded-lg shadow-sm">
			🛡️ Securing liability insurance
		</div>
		<div class="p-4 bg-white rounded-lg shadow-sm">
			🚜 Regular mowing & landscaping
		</div>
	</div>
</div>

<div class="container mx-auto px-4">
	<div class="max-w-5xl mx-auto">
		<div
			class="mt-12 rounded-xl bg-gradient-to-br from-slate-800 to-slate-900 p-8 text-white shadow-lg overflow-hidden relative"
		>
			<div
				class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start relative z-10"
			>
				<div>
					<h3 class="text-2xl font-bold text-blue-200">
						Putting It Into Perspective: The True Cost of
						Participation
					</h3>
					<p class="mt-4 text-slate-300">
						Currently, our voluntary collections average just <strong
							class="text-white">$63 per household</strong
						>
						because not everyone contributes. To sustain even minimal
						operations, many households generously donate
						<strong>extra funds</strong>, effectively subsidizing
						those who do not pay.
					</p>
					<p class="mt-4 text-slate-300">
						This dynamic creates an inequitable burden: while the
						fair annual share to run our community is <strong
							>$75</strong
						>, those who do contribute are often forced to pay an
						<strong>effective cost of $110</strong> or more to cover
						the shortfall left by non-donating households.
					</p>
					<p class="mt-4 text-slate-300">
						If the SCCA transitioned to a mandatory <strong
							class="text-white">$75 SCBD assessment</strong
						>, the burden would be shared equally by all 283
						households, ensuring sustainable funding of
						<strong class="text-white">$21,225</strong> without requiring
						anyone to over-contribute.
					</p>
				</div>

				<div class="flex flex-col space-y-6">
					<!-- Graph 1: Fair Share vs. Reality -->
					<div
						class="bg-white/10 rounded-xl p-4 h-[220px] flex items-center justify-center backdrop-blur-sm border border-white/20"
					>
						<ComparisonBar
							data={fairShareRealityData}
							colorMap={comparisonColors}
							valueFormat={format("$,.0f")}
							title="Fair Share vs. Reality"
						/>
					</div>

					<!-- Graph 2: Revenue & Coverage Gap -->
					<div
						class="bg-white/10 rounded-xl p-4 h-[220px] flex items-center justify-center backdrop-blur-sm border border-white/20"
					>
						<ComparisonBar
							data={revenueGapData}
							colorMap={comparisonColors}
							valueFormat={format("$,.0f")}
							title="Total Revenue & Coverage Gap"
						/>
					</div>

					<!-- Graph 3: Household Participation -->
					<div
						class="bg-white/10 rounded-xl p-4 h-[220px] flex items-center justify-center backdrop-blur-sm border border-white/20"
					>
						<ComparisonBar
							data={participationData}
							colorMap={comparisonColors}
							valueFormat={format(".0%")}
							title="Current Household Participation"
						/>
					</div>
				</div>
			</div>
		</div>

		<!-- Breakdown Section -->
		<div
			class="mt-16 rounded-xl bg-white p-8 border border-slate-200 shadow-sm"
		>
			<div class="text-center mb-8">
				<h3 class="text-2xl font-bold text-slate-900">
					Where Does the Money Go?
				</h3>
				<p class="mt-2 text-slate-600 max-w-2xl mx-auto">
					A breakdown of SCCA's actual expenditures in 2025. It
					illustrates how unavoidable costs (tree removal and
					insurance) dominate the budget, leaving little room for
					enhancements.
				</p>
			</div>

			<div class="max-w-3xl mx-auto">
				<ExpenseDonut
					data={expenses2025}
					valueFormat={format("$,.0f")}
				/>
			</div>
		</div>

		<div class="mt-16 rounded-xl bg-red-50 p-8 border border-red-100">
			<h3 class="text-2xl font-bold text-center text-red-900">
				The Problem: The Current Funding Model is Unsustainable
			</h3>
			<p
				class="mt-4 text-red-800 text-lg max-w-3xl mx-auto text-center leading-relaxed"
			>
				The voluntary dues model we rely on today is fundamentally
				broken. As household participation steadily declines, the SCCA
				is forced to shoulder skyrocketing insurance premiums and
				unpredictable emergency maintenance costs—like hazardous tree
				removals—with a shrinking budget. This persistent funding gap
				has depleted our cash reserves and left the community struggling
				to maintain even the most basic neighborhood standards.
			</p>
		</div>

		<!-- Key Arguments Grid -->
		<div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2">
			<!-- Card 1: Eroding Dues Model -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					1. Challenges with the Voluntary Model
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={duesRateData}
						yDomain={[0.6, 0.8]}
						yFormat={format(".0%")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Loss of Paying Households:</strong>
						Participation has steadily declined from
						<strong>74%</strong> in 2020 down to
						<strong>68%</strong> in 2026.
					</li>
					<li>
						<strong>Declining Participation Gap:</strong> Nearly
						<strong>32% of the community (90 homes)</strong> currently
						does not contribute to essential maintenance (often simply
						due to the friction of mailing a physical check).
					</li>
					<li>
						<strong>Annual Revenue Shortfall:</strong> Annual revenue
						collections have dropped while operating costs continue to
						outpace income by significant margins.
					</li>
				</ul>
			</div>

			<!-- Card 2: Exploding Costs -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					2. Rising Costs of Essential Services
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={insuranceCostsData}
						type="bar"
						customMargin={{ left: 45 }}
						yFormat={format("$,.0f")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Insurance Costs Escalated 151%+:</strong>
						Premiums more than doubled, jumping from $1,700 to
						<strong>$4,279</strong> between 2022 and 2026.
					</li>
					<li>
						<strong>Fixed Overhead Swallows Revenue:</strong>
						Insurance alone now consumes roughly
						<strong>29% of total collected dues</strong>, severely
						limiting funds for physical improvements.
					</li>
					<li>
						<strong>Living Within Our Means:</strong> To balance the
						budget, the SCCA has already had to stretch out the time
						between mowings, reduce mulching, and cut back on community
						aesthetics.
					</li>
				</ul>
			</div>

			<!-- Card 3: Volatility -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					3. High Volatility in Common-Ground Liabilities
				</h3>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Exploding Tree Expenses:</strong> Tree care
						costs escalated from $7,550 in 2020 to
						<strong>$15,050 in 2025</strong>, consuming over
						<strong>100% of collected dues</strong> for that year.
					</li>
					<li>
						<strong>Physical risk to residents and property:</strong
						> Dead trees can fall unexpectedly, causing severe or deadly
						harm when they do.
					</li>
					<li>
						<strong>Inability to Plan:</strong> Unpredictable emergencies
						leave zero room for proactive maintenance or long-term enhancements.
					</li>
				</ul>
			</div>

			<!-- Card 4: Shrinking Reserves -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					4. The Need for Sustainable Reserves
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={cashReservesData}
						type="bar"
						customMargin={{ left: 45 }}
						yFormat={format("$,.0f")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Operating Deficits:</strong> Recent years have
						seen significant deficits. In 2025, actual expenses
						($20,896) exceeded collected dues ($17,625) by over
						<strong>$3,200</strong>.
					</li>
					<li>
						<strong>Depleting Cash:</strong> Community unencumbered
						balances collapsed from over
						<strong>$13,100</strong> at the end of 2024 down to
						<strong>$1,017</strong> by mid-2026, proving the current
						model is unsustainable.
					</li>
				</ul>
			</div>
		</div>

		<div class="mt-16 rounded-xl p-8 border">
			<h3 class="text-2xl font-bold text-center">
				A Search for Solutions
			</h3>
			<p class="mt-3 text-center max-w-2xl mx-auto">
				Faced with these seemingly insurmountable problems, the board
				recognized that defeatism is not the solution. Instead, it
				launched an initiative to identify and explore <strong
					>all</strong
				> options for a new funding approach that will best meet the needs
				of the community. After months of research, investigation, and due
				diligence, we believe we have accomplished this objective. Work has
				been underway to assemble the materials to present the facts to our
				members in time for the October 2026 annual meeting with a strong
				recommendation to proceed.
			</p>
		</div>

		<!-- Updated Summary Section -->
		<div
			class="mt-16 rounded-xl bg-emerald-50 p-8 border border-emerald-100"
		>
			<h3 class="text-2xl font-bold text-center text-emerald-900">
				The SCBD Solution: Investing in Our Future
			</h3>
			<p class="mt-3 text-center text-emerald-700 max-w-2xl mx-auto">
				An SCBD isn't just about covering costs—it's an upbeat,
				proactive step toward a beautifully maintained and thriving
				Shipley's Choice.
			</p>
			<ul
				class="mt-8 grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-3 text-center"
			>
				<li>
					<strong class="text-emerald-900 text-lg"
						>Shared Pride</strong
					><br />
					<span class="text-sm text-emerald-700"
						>A fair system where everyone chips in a small amount
						($75) so no one carries an unfair burden.</span
					>
				</li>
				<li>
					<strong class="text-emerald-900 text-lg"
						>Consistent Beauty</strong
					><br />
					<span class="text-sm text-emerald-700"
						>Guaranteed funding means we can afford regular mowing,
						fresh mulch, and proactive landscaping.</span
					>
				</li>
				<li>
					<strong class="text-emerald-900 text-lg"
						>Peace of Mind</strong
					><br />
					<span class="text-sm text-emerald-700"
						>Strong reserves to easily handle unexpected tree
						removal and comprehensive liability insurance.</span
					>
				</li>
			</ul>
		</div>

		<div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2">
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					Special Community Benefit Districts
				</h3>
				<p class="mt-4 mb-4 space-y-3 text-slate-700">
					Have been formed for a variety of purposes, including:
				</p>
				<ul class="ml-8 list-disc">
					<li>
						Maintenance of community property, including
						community-owned roads
					</li>
					<li>Special security or special police protection</li>
					<li>Improvements to community facilities</li>
					<li>Insect and pest control</li>
				</ul>
			</div>

			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					What it is NOT:
				</h3>
				<ul class="mt-6 ml-8 list-disc">
					<li>
						Part of the County Government - the County merely
						collects and distributes the taxes in a fiduciary role;
					</li>
					<li>
						A legal entity - they cannot borrow funds, buy property,
						be sued
					</li>
					<li>
						A Home Owners Association - nor do they “replace the
						Home Owners Association”
					</li>
				</ul>
			</div>
		</div>

		<!-- How SCBD Collections Work -->
		<div
			class="mt-16 rounded-xl bg-slate-900 border border-slate-700 p-8 text-white shadow-lg"
		>
			<h3 class="text-2xl font-bold text-center text-blue-400">
				How SCBD Collection Actually Works: A Transparent Billing
				Service
			</h3>
			<p
				class="mt-3 text-center text-slate-300 max-w-2xl mx-auto text-sm leading-relaxed"
			>
				Some online rumors suggest the SCBD gives Anne Arundel County
				power over SCCA. In reality, the County's role is strictly
				administrative and fiduciary—acting as our billing department.
			</p>
			<div class="mt-8 grid grid-cols-1 md:grid-cols-4 gap-6 text-sm">
				<div
					class="p-4 bg-slate-800 rounded-lg border border-slate-700 relative pt-8"
				>
					<div
						class="absolute -top-4 left-4 bg-blue-500 text-white rounded-full h-8 w-8 flex items-center justify-center font-bold shadow"
					>
						1
					</div>
					<h4 class="font-bold text-base text-white">
						Community Proposes Rate
					</h4>
					<p class="mt-2 text-slate-300 leading-relaxed text-xs">
						Every year, the SCCA board (your volunteer neighbors)
						proposes a budget and flat rate (e.g., $75) based
						strictly on actual community maintenance needs.
					</p>
				</div>
				<div
					class="p-4 bg-slate-800 rounded-lg border border-slate-700 relative pt-8"
				>
					<div
						class="absolute -top-4 left-4 bg-blue-500 text-white rounded-full h-8 w-8 flex items-center justify-center font-bold shadow shadow"
					>
						2
					</div>
					<h4 class="font-bold text-base text-white">
						County Prints Bill
					</h4>
					<p class="mt-2 text-slate-300 leading-relaxed text-xs">
						The county lists the proposed $75 fee as a flat
						line-item on your existing annual property tax bill. No
						separate checks or mailing required.
					</p>
				</div>
				<div
					class="p-4 bg-slate-800 rounded-lg border border-slate-700 relative pt-8"
				>
					<div
						class="absolute -top-4 left-4 bg-blue-500 text-white rounded-full h-8 w-8 flex items-center justify-center font-bold shadow shadow"
					>
						3
					</div>
					<h4 class="font-bold text-base text-white">
						SCCA Receives Funds
					</h4>
					<p class="mt-2 text-slate-300 leading-relaxed text-xs">
						The county collects a 5% administrative fee and returns
						the other 95% to the SCCA.
					</p>
				</div>
				<div
					class="p-4 bg-slate-800 rounded-lg border border-slate-700 relative pt-8"
				>
					<div
						class="absolute -top-4 left-4 bg-blue-500 text-white rounded-full h-8 w-8 flex items-center justify-center font-bold shadow shadow"
					>
						4
					</div>
					<h4 class="font-bold text-base text-white">
						SCCA Board Allocates
					</h4>
					<p class="mt-2 text-slate-300 leading-relaxed text-xs">
						The SCCA board spends the collected funds exclusively on
						neighborhood grass, trees, signs, and insurance. The
						county has <strong>zero say</strong> in how funds are allocated.
					</p>
				</div>
			</div>
		</div>

		<!-- Fact vs. Myth Section -->
		<div
			class="mt-16 rounded-xl bg-white border border-slate-200 p-8 shadow-sm"
		>
			<h3 class="text-2xl font-bold text-slate-900 text-center">
				Fact vs. Myth: Debunking the Rumors
			</h3>
			<p
				class="mt-2 text-slate-600 text-center max-w-2xl mx-auto leading-relaxed text-sm"
			>
				Social media is a great tool for staying in touch, but it is
				often a hotbed for unverified rumors and false claims. Here are
				the facts regarding the proposed SCBD:
			</p>

			<div class="mt-8 space-y-6">
				<!-- Row 1 -->
				<div
					class="grid grid-cols-1 md:grid-cols-2 gap-4 pb-6 border-b border-slate-100"
				>
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"The SCCA Board is acting in secret and hiding
							financial records."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							The SCCA Board is comprised entirely of <strong
								>unpaid volunteer neighbors</strong
							> who donate their time to keep the community running.
							The board meets monthly (or more) to discuss community
							matters, manage finances, and maintain records of board
							activity. The volunteers on the board make every effort
							possible to keep clean records and make them available
							to residents upon request.
						</p>
					</div>
				</div>

				<div
					class="grid grid-cols-1 md:grid-cols-2 gap-4 pb-6 border-b border-slate-100"
				>
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"The SCCA has already been approved by the County
							without the knowledge or participation of property
							owners."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60 text-slate-700 text-sm leading-relaxed"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2">
							The SCCA announced last year to our membership that
							we will be exploring the formation of an SCBD during
							2026. At this point all that has occurred is
						</p>
						<ol>
							<li>1. the County has confirmed our eligibility</li>
							<li>
								2. it approved the wording of our proposed
								petition.
							</li>
						</ol>
						<p class="mt-2">
							Approval of the SCBD will not happen until
						</p>
						<ol>
							<li>
								1. two-thirds of our homeowners sign the
								petitions
							</li>
							<li>
								2. the petitions are reviewed and approved by
								County.
							</li>
						</ol>
						<p class="mt-2">
							The SCCA is currently at the point where a full
							information packet is being prepared for
							distribution to all property owners in advance of
							the regular annual meeting at which point the
							process of trying to obtain signatures will begin.
						</p>
					</div>
				</div>

				<div
					class="grid grid-cols-1 md:grid-cols-2 gap-4 pb-6 border-b border-slate-100"
				>
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"This is a sinister new tax imposed on us by the
							County."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							The Board cannot impose this unilaterally; it can
							only pass with a <strong
								>2/3 supermajority of households signing a
								petition in favor</strong
							>. The county acts purely as an administrative
							billing service, collecting the flat $75/year
							assessment on your tax bill and returning almost all
							of it fback to the SCCA.
						</p>
					</div>
				</div>

				<div
					class="grid grid-cols-1 md:grid-cols-2 gap-4 pb-6 border-b border-slate-100"
				>
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"The SCCA can't hold or maintain land in Section 2
							because the covenants expired."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							The SCCA owns 25 acres of common area in Section 2.
							The expiration of architectural restrictions in
							Section 2 in 2012 does <strong>not</strong> change SCCA's
							deeded ownership of this land, nor does it eliminate
							SCCA's ongoing legal liability and maintenance duties
							(mowing, hazardous tree removal, insurance) for it.
						</p>
					</div>
				</div>

				<!-- Row 4 -->
				<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"If we don't pay dues, the SCCA will just magically
							keep finding money."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							SCCA unencumbered reserves have been depleted from <strong
								>$13,100 to just $1,017</strong
							>. If dues continue to decline, the association
							faces <strong>insolvency</strong>. This would mean
							canceling landscaping services entirely and dropping
							liability insurance, opening up individual
							homeowners to personal litigation risks in the event
							of an accident on unmaintained common ground.
						</p>
					</div>
				</div>

				<!-- Row 5 -->
				<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"The SCCA is subject to Maryland Real Property Law
							Title 11B - Maryland Homeowners Association Act"
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							Under Maryland law, the SCCA is considered to be a
							“Community Association” and not an HOA. Unlike HOAs
							Community Associations do not have authority to
							impose mandatory dues or assessments on property
							owners. Note that HOAs are not permitted to form an
							SCBD since they already have the ability to fund
							their needs. During our research into eligibility
							requirements, the Anne Arundel County Office of Law
							reviewed our documents and confirmed we are not an
							HOA. HOAs that fall under Title 11B have extensive
							regulations regarding governance, record keeping,
							replacement reserve funds and others. Under Title
							11B, the State of Maryland can even step in and take
							over if it feels the community is unable or
							unwilling to properly comply exposing property
							owners to large unexpected assessments. The SCCA
							does NOT fall under Title 11B and, therefore, cannot
							be in violations of any of its provisions.
						</p>
					</div>
				</div>

				<!-- Row 6 -->
				<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<div
						class="bg-red-50/60 p-4 rounded-lg border border-red-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-800 uppercase"
							>Myth</span
						>
						<p class="mt-2 font-bold text-slate-900">
							"The community should create an HOA and make
							assessments mandatory."
						</p>
					</div>
					<div
						class="bg-emerald-50/60 p-4 rounded-lg border border-emerald-100/60"
					>
						<span
							class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 uppercase"
							>Fact</span
						>
						<p class="mt-2 text-slate-700 text-sm leading-relaxed">
							The developer of Sections 1 and 2 opted not to
							establish an HOA. Once a lot has been sold, there is
							no legal avenue to impose an HOA retroactively
							without approval of 100% of property owners. This
							also means that it is impossible to merge the SCCA
							with the Shipley's Choice HOA which has a mandatory
							annual assessment of $205 per home at the current
							time.
						</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Covenant Clarification Section -->
		<div class="mt-16 rounded-xl bg-blue-50 p-8 border border-blue-100">
			<h3 class="text-2xl font-bold text-slate-900 text-center">
				Section 2 Covenants & Community Liability Risk
			</h3>
			<p
				class="mt-4 text-slate-700 max-w-3xl mx-auto text-center leading-relaxed"
			>
				Some online discussions have confused the expiration of Section
				2's individual architectural covenants with the SCCA's ongoing
				physical property ownership. We want to be fully transparent
				about the legal realities and why this impacts every single
				homeowner.
			</p>
			<div class="mt-8 space-y-6 text-slate-700 max-w-4xl mx-auto">
				<div
					class="p-4 bg-white rounded-lg border border-blue-100 shadow-sm"
				>
					<p class="font-bold text-slate-900">
						1. Property Ownership vs. Architectural Control
					</p>
					<p class="mt-2 leading-relaxed text-sm">
						The Declaration of Covenants for Section 2 (which
						allowed SCCA to enforce building and aesthetic
						guidelines on individual homes) expired in 2012. While
						this means architectural restrictions are gone, it <strong
							>did not change SCCA's deeded ownership</strong
						> of the 25 acres of common areas inside Section 2.
					</p>
				</div>

				<div
					class="p-4 bg-white rounded-lg border border-blue-100 shadow-sm"
				>
					<p class="font-bold text-slate-900">
						2. The Legal Obligation to Maintain and Insure
					</p>
					<p class="mt-2 leading-relaxed text-sm">
						Because SCCA holds the deeds to these 25 acres, the
						association is <strong
							>legally responsible and strictly liable</strong
						> for any injuries, falling trees, or accidents occurring
						on that land. The association is legally required to carry
						comprehensive general liability insurance and perform safety
						maintenance (like cutting hazardous dead trees) across the
						entire community.
					</p>
				</div>

				<div
					class="p-4 rounded-lg border border-red-100 bg-red-50/50 shadow-sm"
				>
					<p class="font-bold text-red-950 flex items-center gap-1.5">
						⚠️ The Devastating Risk of Insolvency
					</p>
					<p class="mt-2 text-red-900 leading-relaxed text-sm">
						If voluntary collections continue to collapse and we
						cannot afford the rising $4,200+ annual liability
						premiums, SCCA faces losing insurance coverage entirely.
						In that scenario, any slip-and-fall, tree-related
						injury, or property damage lawsuit on common ground
						could result in a catastrophic legal judgment. Because
						the association consists of its individual members, such
						judgments could result in severe financial liens or
						legal claims directly impacting SCCA property owners.
					</p>
				</div>

				<div
					class="p-4 bg-white rounded-lg border border-blue-100 shadow-sm"
				>
					<p class="font-bold text-slate-900 font-bold">
						The Bottom Line
					</p>
					<p class="mt-2 leading-relaxed text-sm">
						The expiration of restrictive covenants over a decade
						ago is completely unrelated to the SCBD proposal. The
						SCBD is a necessary, practical safety net to ensure SCCA
						remains solvent, insured, and capable of protecting all
						residents from legal and physical liability.
					</p>
				</div>
			</div>
		</div>

		<!-- Community Participation Section -->
		<div class="mt-16 rounded-xl bg-amber-50 p-8 border border-amber-100">
			<div class="text-center mb-8">
				<h3 class="text-2xl font-bold text-amber-900">
					A Note on Community Participation
				</h3>
				<p
					class="mt-4 text-amber-800 text-lg max-w-3xl mx-auto leading-relaxed"
				>
					The SCCA Board holds a public annual meeting every October,
					and all residents are strongly encouraged to attend. These
					meetings are crucial for discussing the community's
					financial health, maintenance needs, and future planning.
				</p>
			</div>

			<!-- comparison of homes to residents at membership meetings -->
			<div
				class="flex flex-col md:flex-row items-center justify-center gap-8 max-w-4xl mx-auto"
			>
				<div
					class="bg-white p-6 rounded-lg shadow-sm border border-amber-200 text-center flex-1 w-full"
				>
					<div class="text-4xl font-black text-amber-600 mb-2">
						283
					</div>
					<div class="text-amber-900 font-medium">
						Total Homes in SCCA
					</div>
				</div>
				<div
					class="bg-white p-6 rounded-lg shadow-sm border border-amber-200 text-center flex-1 w-full"
				>
					<div class="text-4xl font-black text-amber-600 mb-2">
						&le; 5
					</div>
					<div class="text-amber-900 font-medium">
						Max Annual Attendees (Last 5 Yrs)
					</div>
				</div>
			</div>

			<p class="mt-8 text-amber-800 text-center max-w-2xl mx-auto">
				Active participation is essential for a healthy community
				association. When only a handful of residents attend out of
				nearly 300 households, it places the burden of decision-making
				on a very small group. We welcome and need your voice.
			</p>
		</div>

		<!-- Governance & Decision-Making Process Section -->
		<div
			class="mt-16 rounded-xl bg-slate-100 p-8 border border-slate-200 shadow-sm"
		>
			<h3 class="text-2xl font-bold text-slate-900 text-center">
				Board Governance &amp; Community Decision-Making
			</h3>
			<p
				class="mt-2 text-slate-600 text-center max-w-2xl mx-auto text-sm leading-relaxed"
			>
				Understanding how meeting notices, preliminary board actions,
				and resident petitions work under our SCCA By-Laws.
			</p>

			<div class="mt-8 space-y-6 max-w-4xl mx-auto text-slate-700">
				<div
					class="p-5 bg-white rounded-lg border border-slate-200 shadow-sm"
				>
					<h4
						class="font-bold text-slate-900 text-lg flex items-center gap-2"
					>
						<span>📩</span> Meeting Notices &amp; Annual Communication
					</h4>
					<p class="mt-2 text-sm leading-relaxed">
						Under <strong>Article VII, Section 3</strong> of the SCCA
						By-Laws, written notice for annual membership meetings must
						be provided at least 7 days prior. The Board fulfills this
						obligation by mailing the date, time, and location directly
						to every household alongside the annual newsletter, ballots,
						and dues notices.
					</p>
				</div>

				<div
					class="p-5 bg-white rounded-lg border border-slate-200 shadow-sm"
				>
					<h4
						class="font-bold text-slate-900 text-lg flex items-center gap-2"
					>
						<span>🔍</span> Exploratory Due Diligence &amp; Administrative
						Actions
					</h4>
					<p class="mt-2 text-sm leading-relaxed">
						Under <strong>Article VIII, Section 1</strong>, the
						Board of Directors is tasked with executive
						administrative duties and operational due diligence.
						Submitting an initial inquiry to Anne Arundel County to
						verify SCBD eligibility was a standard, zero-cost
						fact-finding action (not a binding vote or policy
						change). It is the Board's duty to gather preliminary
						facts and county guidelines first so verified data can
						be presented to the neighborhood.
					</p>
				</div>

				<div
					class="p-5 bg-blue-50/70 rounded-lg border border-blue-200 shadow-sm"
				>
					<h4
						class="font-bold text-blue-950 text-lg flex items-center gap-2"
					>
						<span>🗳️</span> The Choice Rests 100% with Homeowners
					</h4>
					<p class="mt-2 text-sm text-blue-900 leading-relaxed">
						An SCBD cannot be established by the Board alone.
						Verifying county eligibility simply opened the door for
						a formal petition process. The final decision rests
						entirely in the hands of the property owners: if a <strong
							>2/3 majority of households</strong
						> choose to sign the petition, it moves forward; if not,
						it does not.
					</p>
				</div>
			</div>
		</div>

		<!-- Summary Section -->
		<div class="mt-16 rounded-xl bg-slate-50 p-8 border border-slate-200">
			<h3 class="text-2xl font-bold text-center text-slate-900">
				Where can I get more information?
			</h3>

			<ul
				class="mt-8 grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-3 text-center"
			>
				<li>
					The <a
						class="app-link"
						href="https://www.aacounty.org/budget/special-taxing-districts"
						>Anne Arundel County Website</a
					> has a wealth of helpful information about SCBDs and all residents
					are encouraged to review.
				</li>
				<li>
					As always, the SCCA board is available to field questions
					through email, in-person, on the phone, or via the <a
						href="https://groups.google.com/u/1/g/shipleys-choice-community-association"
						class="app-link">Google Group</a
					> for SCCA residents.
				</li>
				<li>
					<strong
						>Note that the Shipley's Choice Facebook page is NOT an
						authoritative source for community information on SCCA
						matters.</strong
					>
				</li>
			</ul>
			<div class="mt-8 flex justify-center">
				<img
					src="data/img/community_overhead.png"
					class="rounded-3xl border border-slate-200 shadow-sm"
					alt="Community Overhead View"
				/>
			</div>
		</div>
	</div>
</div>
