<script lang="ts">
	import IntersectionObserver from "svelte-intersection-observer"
	import { fade } from "svelte/transition"
	let element: any
	let intersecting
</script>

<IntersectionObserver {element} let:intersecting>
	<div bind:this={element}>
		{#if intersecting}
			<div transition:fade={{ delay: 200 }}>
				<slot />
			</div>
		{/if}
	</div>
</IntersectionObserver>
