<script>
	import SparkChart from "$components/charts/SparkChart.svelte";
	import scbdChartData from "$data/scbdChartData.json";
	import { format } from "d3-format";
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
			Why should Shipley's Choice pursue SCBD desgination? Understanding the costs and challenges facing our community. 
		</p>
	</div>
</section>

<div class="container mx-auto px-4 ">
	<div class="max-w-5xl mx-auto">
		<!-- Key Arguments Grid -->
		<div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2">
			<!-- Card 1: Eroding Dues Model -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					1. The Voluntary Dues Model Is Eroding
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={scbdChartData.duesRate}
						yDomain={[0.6, 0.8]}
						yFormat={format(".0%")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Loss of Paying Households:</strong>
						Participation has steadily declined from
						<strong>76%</strong> in 2022 down to
						<strong>68%</strong> by mid-2026.
					</li>
					<li>
						<strong>Expanding Free-Rider Gap:</strong> Over
						<strong>31% of the community (90 homes)</strong> currently
						does not contribute to essential maintenance.
					</li>
					<li>
						<strong>Annual Revenue Shortfall:</strong> Annual
						revenue is trailing
						<strong>$3,000 to $4,200 below</strong> planned operational
						capacity.
					</li>
				</ul>
			</div>

			<!-- Card 2: Exploding Costs -->
			<div
				class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm"
			>
				<h3 class="text-xl font-bold text-slate-900">
					2. Essential Overhead Costs Are Exploding
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={scbdChartData.insuranceCosts}
						type="bar"
						customMargin={{ left: 45 }}
						yFormat={format("$,.0f")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Insurance Costs Escalated 130%+:</strong>
						Premiums jumped from ~$1,850 to
						<strong>$4,279</strong> between 2024 and mid-2026.
					</li>
					<li>
						<strong>Fixed Overhead Swallows Revenue:</strong>
						Insurance alone now consumes nearly
						<strong>30% of total collected dues</strong>, limiting
						funds for physical improvements.
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
						<strong>Record Tree Expenses:</strong> Tree care costs
						hit
						<strong>$15,050 in 2025</strong>, consuming over
						<strong>70% of all collected dues</strong> for that year.
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
					4. Reserves Are Shrinking to Vulnerable Levels
				</h3>
				<div class="h-24 w-full mt-4">
					<SparkChart
						data={scbdChartData.cashReserves}
						type="bar"
						customMargin={{ left: 45 }}
						yFormat={format("$,.0f")}
					/>
				</div>
				<ul class="mt-4 space-y-3 text-slate-700">
					<li>
						<strong>Operating Deficits:</strong> The SCCA ran a
						<strong>$2,900 net operating deficit in 2025</strong> as
						costs outpaced revenue.
					</li>
					<li>
						<strong>Depleting Cash:</strong> Unencumbered cash
						dropped from
						<strong>$13,166</strong> at YE 2024 to just
						<strong>$6,763</strong> by mid-2026.
					</li>
				</ul>
			</div>
		</div>

		<!-- Summary Section -->
		<div class="mt-16 rounded-xl bg-slate-50 p-8 border border-slate-200">
			<h3 class="text-2xl font-bold text-center text-slate-900">
				The SCBD Solution: A Summary
			</h3>
			<p class="mt-3 text-center text-slate-600 max-w-2xl mx-auto">
				Establishing a Special Community Benefits District provides a
				clear path forward to address these challenges directly.
			</p>
			<ul
				class="mt-8 grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-3 text-center"
			>
				<li>
					<strong class="text-slate-800">Fairness & Equity:</strong> Spreads
					financial responsibility evenly across all 284 properties.
				</li>
				<li>
					<strong class="text-slate-800">Financial Stability:</strong>
					Provides guaranteed funding for recurring liabilities like insurance
					and tree care.
				</li>
				<li>
					<strong class="text-slate-800"
						>Protecting Property Values:</strong
					> Ensures common grounds and neighborhood aesthetics are reliably
					maintained.
				</li>
			</ul>
		</div>
	</div>
</div>
