<script lang="ts">
	import { page } from '$app/stores';
	import Navbar from '$root/lib/components/layouts/Navbar.svelte';
	import Footer from '$root/lib/components/layouts/Footer.svelte';
	import type { LayoutData } from './$types';
	import { Cart } from '$root/store/toggleSeriesStore';
	import type { CartIn } from '$root/lib/interface/cart.interface';
	import Transition from '$root/lib/components/animation/Transition.svelte';
	export let data: LayoutData;
	$: user_data = data;
	$: $Cart = data.carts as CartIn[];
</script>

<Navbar
	is_login={user_data.is_login}
	user={user_data.user}
	url={$page.url.pathname}
	cart_count={$Cart.length}
/>
<div class="relative px-8">
	<main class="overflow-x-hidden">
		<Transition url={$page.url}>
			<slot />
		</Transition>
	</main>
</div>
<Footer />
