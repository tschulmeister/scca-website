<script>
	import { getContext } from 'svelte';
	import { format } from 'd3-format';

	const { data, xGet, yGet, xScale, yScale } = getContext('LayerCake');

	const p = format('.1%');
</script>

<g class="bar-group">
	{#each $data as d}
		<g class="bar-wrapper" transform="translate({$xGet(d)}, 0)">
			<rect
				y={$yGet(d)}
				width={$xScale.bandwidth()}
				height={$yScale.range()[0] - $yGet(d)}
				class="fill-blue-500 transition-all duration-200 hover:fill-blue-600"
			>
				<title>
					{`${$xGet(d, { flat: true })}: ${p($yGet(d, { flat: true }))}`}
				</title>
			</rect>
		</g>
	{/each}
</g>