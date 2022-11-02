<script>
	import { fade, scale } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
</script>

<section in:fade={{ delay: 250, duration: 300, easing: quintOut }}>
	<slot />
</section>
