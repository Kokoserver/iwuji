<script lang="ts">
	import '../app.postcss';
	import { page } from '$app/stores';
	import Navbar from '$root/lib/components/layouts/Navbar.svelte';
	import Footer from '$root/lib/components/layouts/Footer.svelte';
	import Transition from '$root/lib/components/layouts/Transition.svelte';
	import type { LayoutData } from './$types';
	export let data: LayoutData;
</script>

<div>
	<Navbar is_login={data.is_login} />
	<Transition url={$page.url}>
		<slot />
	</Transition>
	<Footer />
</div>
