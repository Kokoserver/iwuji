<script lang="ts">
	export let gap: number = 6
	export let column: number = 3
	export let row: number = 1
</script>

<div class={`grid  md:grid-cols-${column} gap-${gap} grid-rows-${row}`}>
	<slot />
</div>
