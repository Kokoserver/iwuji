<script lang="ts">
	import '../app.postcss';
	import { page } from '$app/stores';
	import Navbar from '$root/lib/components/layouts/Navbar.svelte';
	import Footer from '$root/lib/components/layouts/Footer.svelte';
	import { animate } from '$root/lib/store/pageTransitionStore';
	import Transition from '$root/lib/components/layouts/Transition.svelte';
	import { Notification } from '$root/lib/notification';
	import type { LayoutData } from './$types';
	export let data: LayoutData;
	$: user_data = data;
</script>

<div>
	<Navbar is_login={user_data.is_login} user={user_data.user} />
	<!-- <Transition url={$page.url} animate={$animate}> -->
	<slot />
	<!-- </Transition> -->
	<Footer />
	<Notification />
</div>
