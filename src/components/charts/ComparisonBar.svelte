<script>
	import { scaleBand, scaleLinear } from "d3-scale";
	import { max } from "d3-array";
	import { fade } from "svelte/transition";

	export let data = []; // e.g. [{ label: 'SCCA', value: 75, subtitle: '284 homes' }]
	export let valueFormat = (d) => d;
	export let labelFormat = (d) => d;
	export let colorMap = {}; // e.g. { 'SCCA': 'bg-blue-500', 'SHOA': 'bg-emerald-500' }
	export let title = "";

	let width;
	let height;

	const margin = { top: 30, right: 10, bottom: 56, left: 10 };
	$: innerWidth = width > 0 ? width - margin.left - margin.right : 0;
	$: innerHeight = height > 0 ? height - margin.top - margin.bottom : 0;

	// Use fixed max domain if single item, otherwise dynamic
	$: yDomainMax = data.length === 1 
		? data[0].value * 1.2 
		: max(data, (d) => d.value);

	$: xScale = scaleBand()
		.domain(data.map((d) => d.label))
		.range([0, innerWidth])
		.padding(0.3);

	$: yScale = scaleLinear()
		.domain([0, yDomainMax])
		.range([innerHeight, 0])
		.nice();
</script>

<div class="flex flex-col w-full h-full min-h-[200px]">
	{#if title}
		<div class="text-xs font-semibold text-slate-300 text-center mb-2 uppercase tracking-wider">{title}</div>
	{/if}
	<div class="flex-grow w-full relative" bind:clientWidth={width} bind:clientHeight={height}>
		{#if innerWidth > 0 && innerHeight > 0}
			<div class="absolute inset-0" in:fade={{ duration: 300 }}>
				<!-- Grid lines -->
				{#each yScale.ticks(4) as tick}
					<div 
						class="absolute w-full border-t border-slate-600 border-dashed"
						style="bottom: {margin.bottom + (innerHeight - yScale(tick))}px; left: {margin.left}px; width: {innerWidth}px;"
					></div>
				{/each}

				{#each data as d}
					<!-- The Bar -->
					<div
						class="absolute rounded-t-md transition-all duration-500 shadow-sm opacity-90 {colorMap[d.label] || 'bg-slate-300'}"
						style="
							bottom: {margin.bottom}px;
							left: {margin.left + xScale(d.label)}px;
							width: {xScale.bandwidth()}px;
							height: {innerHeight - yScale(d.value)}px;
						"
					></div>
					
					<!-- Label under the bar -->
					<div
						class="absolute bottom-0 text-center w-full flex flex-col items-center justify-start pt-2 leading-tight"
						style="
							left: {margin.left + xScale(d.label)}px;
							width: {xScale.bandwidth()}px;
							height: {margin.bottom}px;
						"
					>
						<span class="text-xs sm:text-sm font-bold text-slate-100">{labelFormat(d.label)}</span>
						{#if d.subtitle}
							<span class="text-[10px] sm:text-xs text-slate-300 mt-1">{d.subtitle}</span>
						{/if}
					</div>
					
					<!-- Value on top of the bar -->
					<div
						class="absolute text-center text-xs sm:text-sm font-bold w-full"
						style="
							left: {margin.left + xScale(d.label)}px;
							width: {xScale.bandwidth()}px;
							bottom: {margin.bottom + innerHeight - yScale(d.value) + 4}px;
							color: #0f172a;
						"
					>
						<span class="px-1.5 py-0.5 rounded bg-white bg-opacity-90 shadow-sm">{valueFormat(d.value)}</span>
					</div>
				{/each}
			</div>
		{/if}
	</div>
</div>