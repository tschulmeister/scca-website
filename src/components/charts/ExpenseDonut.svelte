<script>
	import { pie, arc } from "d3-shape";
	import { scaleOrdinal } from "d3-scale";
	import { format } from "d3-format";

	export let data = []; // e.g. [{ label: "Insurance", value: 3823 }, ...]
	export let valueFormat = (d) => d;
	
	let width;
	let height;
	
	$: minDim = Math.min(width || 300, height || 300);
	$: radius = minDim / 2;
	$: innerRadius = radius * 0.6; // Donut hole
	
	// Ensure data is sorted by value descending for better visual flow
	$: sortedData = [...data].sort((a, b) => b.value - a.value).filter(d => d.value > 0);

	$: colorScale = scaleOrdinal()
		.domain(sortedData.map(d => d.label))
		.range([
			"#3b82f6", // blue-500
			"#10b981", // emerald-500
			"#f59e0b", // amber-500
			"#8b5cf6", // violet-500
			"#ef4444", // red-500
			"#06b6d4", // cyan-500
			"#ec4899", // pink-500
			"#64748b", // slate-500
			"#84cc16", // lime-500
			"#14b8a6"  // teal-500
		]);

	$: pieGenerator = pie()
		.value(d => d.value)
		.sort(null); // Already sorted

	$: arcGenerator = arc()
		.innerRadius(innerRadius)
		.outerRadius(radius * 0.95);

	$: arcHoverGenerator = arc()
		.innerRadius(innerRadius)
		.outerRadius(radius); // Slightly larger on hover

	$: pieArcs = pieGenerator(sortedData);
	
	$: totalValue = sortedData.reduce((sum, d) => sum + d.value, 0);

	let hoveredIndex = null;
</script>

<div class="flex flex-col md:flex-row w-full items-center justify-center gap-8">
	<!-- Chart -->
	<div 
		class="relative aspect-square w-full max-w-[300px]" 
		bind:clientWidth={width} 
		bind:clientHeight={height}
	>
		{#if width > 0 && height > 0}
			<svg {width} {height} class="overflow-visible">
				<g transform="translate({width / 2}, {height / 2})">
					{#each pieArcs as arcData, i}
						<path
							d={hoveredIndex === i ? arcHoverGenerator(arcData) : arcGenerator(arcData)}
							fill={colorScale(arcData.data.label)}
							class="transition-all duration-300 ease-out cursor-pointer stroke-white stroke-2"
							on:mouseenter={() => (hoveredIndex = i)}
							on:mouseleave={() => (hoveredIndex = null)}
						/>
					{/each}
				</g>
			</svg>
			
			<!-- Center text -->
			<div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
				{#if hoveredIndex !== null}
					<span class="text-[10px] sm:text-xs text-slate-500 font-semibold uppercase tracking-wider text-center px-4 leading-tight">
						{pieArcs[hoveredIndex].data.label}
					</span>
					<span class="text-lg sm:text-xl font-bold text-slate-800">
						{valueFormat(pieArcs[hoveredIndex].data.value)}
					</span>
					<span class="text-[10px] sm:text-xs text-slate-400">
						{format(".0%")(pieArcs[hoveredIndex].data.value / totalValue)}
					</span>
				{:else}
					<span class="text-[10px] sm:text-xs text-slate-500 font-semibold uppercase tracking-wider">Total</span>
					<span class="text-lg sm:text-xl font-bold text-slate-800">{valueFormat(totalValue)}</span>
				{/if}
			</div>
		{/if}
	</div>
	
	<!-- Legend -->
	<div class="flex flex-col w-full max-w-[300px] space-y-1">
		{#each sortedData as d, i}
			<div 
				class="flex items-center justify-between text-xs sm:text-sm p-1.5 rounded-md transition-colors cursor-pointer {hoveredIndex === i ? 'bg-slate-100' : ''}"
				on:mouseenter={() => (hoveredIndex = i)}
				on:mouseleave={() => (hoveredIndex = null)}
			>
				<div class="flex items-center space-x-2 truncate">
					<div 
						class="w-3 h-3 rounded-full flex-shrink-0" 
						style="background-color: {colorScale(d.label)}"
					></div>
					<span class="text-slate-700 truncate" title={d.label}>{d.label}</span>
				</div>
				<span class="font-semibold text-slate-900 ml-2">{format("$,.0f")(d.value)}</span>
			</div>
		{/each}
	</div>
</div>