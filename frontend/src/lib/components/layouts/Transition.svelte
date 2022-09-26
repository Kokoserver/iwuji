<script lang="ts">
	import { fly } from 'svelte/transition';
	export let animate: boolean = true;
	export let url: URL;
</script>

{#key url}
	{#if animate}
		<div in:fly={{ y: -50, duration: 250, delay: 300 }} out:fly={{ y: -50, duration: 250 }}>
			<slot />
		</div>
	{:else}
		<div><slot /></div>
	{/if}
{/key}
