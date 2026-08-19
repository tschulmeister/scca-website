<script>
	import { getContext } from "svelte";

	const { data, xGet, xScale, yScale } = getContext("LayerCake");

	export let gridlines = true;
	export let tickFormat = (d) => d;
	export let ticks = $xScale.domain();

	$: isBandwidth = typeof $xScale.bandwidth === "function";
</script>

<g class="axis x-axis" transform="translate(0, {$yScale.range()[0]})">
	{#if gridlines}
		{#each ticks as tick}
			<g class="tick" transform="translate({$xScale(tick)}, 0)">
				<line y2="-{$yScale.range()[0]}" />
			</g>
		{/each}
	{/if}

	{#each ticks as tick}
		<g
			class="tick"
			transform="translate({$xScale(tick) +
				(isBandwidth ? $xScale.bandwidth() / 2 : 0)}, 0)"
		>
			<text y="16">{tickFormat(tick)}</text>
		</g>
	{/each}
</g>

<style>
	.tick {
		font-size: 12px;
	}
	.tick text {
		text-anchor: middle;
		fill: #64748b; /* slate-500 */
	}
</style>
