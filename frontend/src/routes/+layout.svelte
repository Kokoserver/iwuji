<script>
	import '../app.postcss';
	import { page } from '$app/stores';
	import Navbar from '$root/lib/components/layouts/Navbar.svelte';
	import Footer from '$root/lib/components/layouts/Footer.svelte';
	import Transition from '$root/lib/components/layouts/Transition.svelte';
	export const ssr = false;
</script>

<div>
	<Navbar />
	<Transition url={$page.url}>
		<slot />
	</Transition>
	<Footer />
</div>
