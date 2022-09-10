<script>
	import "../app.postcss"
	import Navbar from "$root/lib/components/layouts/Navbar.svelte"
	import Footer from "$root/lib/components/layouts/Footer.svelte"
</script>

<div>
	<Navbar />
	<slot />
	<Footer />
</div>
