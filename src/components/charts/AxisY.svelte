<script>
	import { getContext } from 'svelte';

	const { yGet, yScale } = getContext('LayerCake');

	export let gridlines = true;
	export let ticks = 5;
	export let tickFormat = (d) => d;
</script>

<g class="axis y-axis">
	{#each $yScale.ticks(ticks) as tick}
		<g class="tick" transform="translate(0, {$yScale(tick)})">
			{#if gridlines}
				<line x2="100%" />
			{/if}
			<text x="-8" y="4">{tickFormat(tick)}</text>
		</g>
	{/each}
</g>

<style>
	.tick {
		font-size: 12px;
	}
	.tick line {
		stroke: #e2e8f0; /* slate-200 */
		stroke-dasharray: 2;
	}
	.tick text {
		text-anchor: end;
		fill: #64748b; /* slate-500 */
	}
	.tick:first-of-type line {
		stroke-dasharray: 0;
		stroke: #cbd5e1; /* slate-300 */
	}
</style>