<script lang="ts">
	import Section from '../animation/FadeInOut.svelte';

	export let divClass: string = '';
</script>

<Section>
	<div class={`container mx-auto  ${divClass}`}>
		<slot />
	</div>
</Section>
