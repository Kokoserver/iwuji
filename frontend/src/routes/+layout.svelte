<script lang="ts">
	import '../app.postcss';
	import { page } from '$app/stores';
	import Navbar from '$root/lib/components/layouts/Navbar.svelte';
	import Footer from '$root/lib/components/layouts/Footer.svelte';
	import { animate } from '$root/lib/store/pageTransitionStore';
	import Transition from '$root/lib/components/layouts/Transition.svelte';
	import { Notification } from '$root/lib/notification';
	import type { LayoutData } from './$types';
	import { Cart } from '$root/lib/store/toggleSeriesStore';
	import type { CartIn } from '$root/lib/interface/cart.interface';
	export let data: LayoutData;
	$: user_data = data;
	$: $Cart = data.carts as CartIn[];
</script>

<div>
	<Navbar
		is_login={user_data.is_login}
		user={user_data.user}
		url={$page.url.pathname}
		cart_count={$Cart.length}
	/>
	<Transition url={$page.url} animate={$animate}>
		<div class="overflow-x-hidden">
			<slot />
		</div>
	</Transition>
	<Footer />
	<Notification />
</div>
