<script lang="ts">
	import type { ProductIn } from '../interface/product.interface';

	export let product: ProductIn;
</script>

<div
	class="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-0 border-b border-b-secondary py-10"
>
	<div class="md:w-1/2 p-2">
		<img src={product.cover_img.url} width="427" height="527" alt={product.name} srcset="" />
	</div>
	<div class="md:w-2/5 space-y-4 p-3 ">
		<h1 class="font-semibold uppercase text-2xl text-center md:text-left">{product.name}</h1>
		<p class="font-normal text-gray-700 text-center md:text-left">
			{product.description.slice(1, 300)}...
		</p>
		<div class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start">
			<a
				href="/books/{product.id}"
				class="rounded-full font-semibold bg-primary px-4 py-3 text-center uppercase ">preview</a
			>

			<a href="/" class="rounded-full font-semibold bg-primary px-4 py-3 text-center uppercase "
				>view on amazon</a
			>
		</div>
	</div>
</div>
