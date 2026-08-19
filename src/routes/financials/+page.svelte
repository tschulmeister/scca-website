<script>
	import { LayerCake, Svg } from "layercake";
	import { scaleBand, scaleLinear } from "d3-scale";
	import { format } from "d3-format";

	import AxisX from "$components/charts/AxisX.svelte";
	import AxisY from "$components/charts/AxisY.svelte";
	import Bar from "$components/charts/Bar.svelte";

	/** @type {import('./$types').PageData} */
	export let data;

	const xKey = "year";
	const yKey = "rate";

	// Filter out years with no data for a cleaner chart
	const chartData = data.stats.filter((d) => d.rate !== null);
</script>

<svelte:head>
	<title>Financial Overview | SCCA</title>
	<meta
		name="description"
		content="An overview of the Shipley's Choice Community Association's financial health and dues participation trends."
	/>
</svelte:head>

<div
	class="page-header py-12 sm:py-16"
	style="--page-header-bg: url('/img/shipleys-choice-sign-fall.jpg')"
>
	<div class="container mx-auto px-4 text-center">
		<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">
			Financial Overview
		</h1>
		<p class="mt-3 max-w-2xl mx-auto text-lg text-slate-200">
			A look at the association's financial health, including dues
			participation and budget trends.
		</p>
	</div>
</div>

<div class="container mx-auto px-4 py-12 sm:py-16">
	<div class="max-w-4xl mx-auto">
		<h2 class="text-2xl font-semibold text-slate-800">
			Dues Participation Rate (2020-2025)
		</h2>
		<p class="mt-2 text-slate-600">
			The percentage of households paying annual dues has been trending
			downward, impacting our ability to fund key community maintenance
			like tree removal and insurance.
		</p>

		<!-- Chart container -->
		<div class="chart-container mt-8 h-80 w-full">
			<LayerCake
				{chartData}
				x={xKey}
				y={yKey}
				xScale={scaleBand().padding(0.1)}
				yScale={scaleLinear()}
				yDomain={[0, 1]}
			>
				<Svg>
					<AxisX gridlines={false} tickFormat={(d) => d} />
					<AxisY gridlines={true} tickFormat={format(".0%")} />
					<Bar />
				</Svg>
			</LayerCake>
		</div>

		<div class="mt-8 prose prose-slate max-w-none">
			<h3 class="text-xl font-semibold text-slate-800">
				Why This Matters
			</h3>
			<p>
				As outlined in the <a
					href="/news/scbd-announcement-dec-2025"
					class="app-link"
					>Special Community Benefits District (SCBD) announcement</a
				>, our income from dues is not keeping pace with rising
				expenses. While dues have remained at $75, costs for essential
				services have increased significantly:
			</p>
			<ul>
				<li>
					<strong>Insurance Premiums:</strong> Our liability insurance
					costs have more than doubled since 2020.
				</li>
				<li>
					<strong>Tree Removal:</strong> This remains our largest and most
					unpredictable expense, often costing $8,000 - $12,000 annually.
				</li>
			</ul>
			<p>
				Ensuring full participation in dues collection via the SCBD
				would provide the financial stability needed to maintain our
				community's common areas and property values.
			</p>
		</div>
	</div>
</div>
