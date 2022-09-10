<script>
	import Container from "./Container.svelte"
</script>

<footer class=" bg-yellow-200 p-6" id="contact">
	<Container
		divClass="flex flex-col md:flex-row gap-6 justify-between items-center gap-6"
	>
		<div
			class="space-y-4 flex flex-col  justify-center items-center md:items-start"
		>
			<a href="/"><img src="/logo.svg" class="h-5" alt="" /></a>
			<div class="flex items-start gap-6">
				<a href="/"
					><img src="/icons/facebook.svg" class="h-8 w-8" alt="" srcset="" /></a
				>
				<a href="/"><img src="/icons/twitter.svg" class="h-8 w-8" alt="" /></a>
				<a href="/"><img src="/icons/instagram.svg" class="h-8 w-8" alt="" /></a
				>
				<a href="/"><img src="/icons/tiktok.svg" class="h-8 w-8" alt="" /></a>
			</div>
		</div>
		<div
			class="space-y-4 flex flex-col justify-center items-center md:items-start lg:items-start"
		>
			<h4 class="text-xl font-semibold capitalize">
				for bussiness and enquiry
			</h4>
			<div class="flex items-start gap-6">
				<a href="/"
					><img src="/icons/phone.svg" class="h-8 w-8" alt="" srcset="" /></a
				>
				<a href="/"><img src="/icons/mail.svg" class="h-8 w-8" alt="" /></a>
				<a href="/"><img src="/icons/whatsapp.svg" class="h-8 w-8" alt="" /></a>
			</div>
		</div></Container
	>
</footer>
