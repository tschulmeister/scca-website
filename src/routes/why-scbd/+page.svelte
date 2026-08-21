<script>
	import SparkChart from "$components/charts/SparkChart.svelte";
	import financials from "$data/financials.json";
	import { format } from "d3-format";

	const duesRateData = financials.participation_trends.map(r => ({
		year: r.year,
		value: r.participation_rate_pct / 100
	}));

	const insuranceExp = financials.annual_expenses_breakdown.find(e => e.category === "Insurance");
	const insuranceCostsData = [
		{ year: 2020, value: insuranceExp["2020_actual"] },
		{ year: 2022, value: insuranceExp["2022_budget"] },
		{ year: 2023, value: insuranceExp["2023_budget"] },
		{ year: 2024, value: insuranceExp["2024_actual"] },
		{ year: 2025, value: insuranceExp["2025_actual"] },
		{ year: 2026, value: insuranceExp["2026_ytd_actual"] }
	];

	const cashReservesData = financials.statements_of_financial_condition.map(r => ({
		label: r.as_of_date.substring(0, 4),
		value: r.balances.net_unencumbered_balance_usd ?? r.balances.ending_net_balance_usd
	}));
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
		<!-- Proposed Perspective Callout Box -->
		<div
			class="mt-12 rounded-xl bg-gradient-to-br from-slate-800 to-slate-900 p-8 text-white shadow-lg"
		>
			<h3 class="text-2xl font-bold text-blue-200">
				Putting It Into Perspective: A $75 Investment
			</h3>
			<p class="mt-4 text-slate-300">
				Currently, our voluntary collections average just <strong
					>$52 per household</strong
				>. By comparison, our neighbors in the larger SHOA (854 homes)
				utilize a mandatory
				<strong>$205 annual assessment</strong> with 100% participation.
			</p>
			<p class="mt-4 text-slate-300">
				What does full funding achieve? It allows them to use
				professional tree services, hire commercial landscapers, mow
				more frequently, and replace aging playground equipment.
				Transitioning to a modest $75 SCBD fee ensures SCCA can maintain
				our standards without asking anyone to break the bank.
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
						<strong>Annual Revenue Shortfall:</strong> Annual
						revenue collections have dropped while operating costs continue to outpace income by significant margins.
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
						<strong>Insurance Costs Escalated 131%+:</strong>
						Premiums more than doubled, jumping from $1,851 to
						<strong>$4,279</strong> between 2020 and 2026.
					</li>
					<li>
						<strong>Fixed Overhead Swallows Revenue:</strong>
						Insurance alone now consumes roughly
						<strong>29% of total collected dues</strong>, severely limiting
						funds for physical improvements.
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
						<strong>Exploding Tree Expenses:</strong> Tree care costs
						escalated from $7,550 in 2020 to
						<strong>$15,050 in 2025</strong>, consuming over
						<strong>100% of collected dues</strong> for that year.
					</li>
					<li>
						<strong>Physical risk to residents and property:</strong> Dead trees can fall unexpectedly, causing severe or deadly
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
						<strong>Operating Deficits:</strong> Recent years have seen significant deficits. In 2025, actual expenses ($20,896) exceeded collected dues ($14,700) by over
						<strong>$6,100</strong>.
					</li>
					<li>
						<strong>Depleting Cash:</strong> Community unencumbered balances collapsed from over
						<strong>$13,100</strong> at the end of 2024 down to
						<strong>$6,763</strong> by mid-2026, proving the current model is unsustainable.
					</li>
				</ul>
			</div>
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
					About Special Taxing Districts
				</h3>
				<p class="mt-4 space-y-3 text-slate-700">
					A community might consider forming a special taxing district
					to finance a public benefit for the community that it does
					not have the ability to finance in any other way.
				</p>
				<p class="mt-4 space-y-3 text-slate-700">
					Once the taxing district is formed, the community each year
					determines a tax rate to produce the revenue necessary to
					fund the benefit for the following fiscal year. The property
					owners are taxing themselves to fund the particular
					benefits.
				</p>
			</div>

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
				<h3 class="text-xl font-bold text-slate-900">What it is:</h3>
				<ul class="mt-6 ml-8 list-disc">
					<li>A taxing district</li>
					<li>
						A mechanism to collect taxes from persons that have a
						common need
					</li>
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

		<!-- Covenant Clarification Section -->
		<div class="mt-16 rounded-xl bg-blue-50 p-8 border border-blue-100">
			<h3 class="text-2xl font-bold text-slate-900 text-center">
				Fact vs. Fiction: The Section 2 Covenants
			</h3>
			<p class="mt-4 text-slate-700 max-w-3xl mx-auto text-center">
				You may have seen recent discussions online regarding the
				expiration of restrictive covenants in Section 2. We want to be
				fully transparent and clarify how this relates to the SCBD
				proposal.
			</p>
			<div class="mt-8 space-y-4 text-slate-700 max-w-4xl mx-auto">
				<p>
					<strong>The History:</strong> The Declaration of Covenants for
					Section 2 (which allowed the SCCA to enforce building and land-use
					restrictions on individual homes) expired in 2012. While this
					means the SCCA can no longer enforce architectural restrictions
					in Section 2, it does not change our property ownership.
				</p>
				<p>
					<strong>What Hasn't Changed:</strong> The SCCA still owns the
					25 acres of common area in Section 2 and is legally responsible
					for maintaining them. The association must still cut the grass,
					insure the property, maintain the community signs, and remove
					dangerous dead trees across the entire community.
				</p>
				<p>
					<strong>The Bottom Line:</strong> The expiration of these restrictive
					covenants over a decade ago is unrelated to the SCBD proposal.
					The SCBD is purely a funding mechanism to ensure our shared,
					ongoing maintenance and insurance obligations can be met responsibly.
				</p>
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
