<script>
	import { scaleBand, scaleLinear } from "d3-scale";
	import { line, area } from "d3-shape";
	import { max } from "d3-array";
	import { axisBottom, axisLeft } from "d3-axis";
	import { select } from "d3-selection";
	import { format } from "d3-format";

	export let data = [];
	export let type = "line"; // 'line' or 'bar'
	export let yDomain = [0, null];
	export let yFormat = (d) => d;
	export let customMargin = {};

	let width;
	let height;

	$: margin = { top: 5, right: 5, bottom: 20, left: 35, ...customMargin };
	$: innerWidth = width > 0 ? width - margin.left - margin.right : 0;
	$: innerHeight = height > 0 ? height - margin.top - margin.bottom : 0;

	$: xKey = data.length > 0 ? Object.keys(data[0])[0] : null;
	const yKey = "value";

	$: xScale = scaleBand()
		.domain(data.map((d) => d[xKey]))
		.range([0, innerWidth])
		.paddingInner(type === "bar" ? 0.2 : 0);

	$: yMax = yDomain[1] ?? max(data, (d) => d[yKey]);
	$: yScale = scaleLinear()
		.domain([yDomain[0], yMax])
		.range([innerHeight, 0])
		.nice();

	$: xGet = (d) => xScale(d[xKey]);
	$: yGet = (d) => yScale(d[yKey]);

	$: path = line().x(xGet).y(yGet)(data);

	$: areaPath = area().x(xGet).y0(innerHeight).y1(yGet)(data);

	// --- AXES ---
	$: xAxis = axisBottom(xScale).tickSize(0).tickPadding(8);
	$: yAxis = axisLeft(yScale)
		.ticks(3)
		.tickSize(0)
		.tickPadding(8)
		.tickFormat(yFormat);

	function callAxis(node, axisGenerator) {
		select(node).call(axisGenerator);
	}
</script>

<div class="w-full h-full" bind:clientWidth={width} bind:clientHeight={height}>
	{#if innerWidth > 0 && innerHeight > 0 && data.length > 0}
		<svg {width} {height}>
			<g
				class="axis"
				use:callAxis={yAxis}
				transform="translate({margin.left}, {margin.top})"
			/>
			<g
				class="axis"
				use:callAxis={xAxis}
				transform="translate({margin.left}, {innerHeight + margin.top})"
			/>
			<g transform="translate({margin.left}, {margin.top})">
				{#if type === "line"}
					<path d={areaPath} class="fill-blue-100" />
					<path
						d={path}
						class="stroke-2 stroke-blue-500"
						fill="none"
					/>
				{:else if type === "bar"}
					{#each data as d}
						<rect
							x={xGet(d)}
							y={yGet(d)}
							width={xScale.bandwidth()}
							height={innerHeight - yGet(d)}
							class="fill-blue-500"
						/>
					{/each}
				{/if}
			</g>
		</svg>
	{/if}
</div>

<style>
	.axis :global(text) {
		font-size: 0.75rem;
		fill: #64748b; /* slate-500 */
	}
	.axis :global(path) {
		stroke: #e2e8f0; /* slate-200 */
	}
</style>
