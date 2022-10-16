<script lang="ts">
	import type { ProductIn } from '../interface/product.interface';

	export let product: ProductIn;
</script>

<div class="flex flex-col items-center space-y-7">
	<a href="/books/{product.id}" data-sveltekit-prefetch="">
		<img src={product.cover_img.url} alt={product.cover_img.alt} class="w-65 h-60" />
	</a>
	<h1 class="font-normal text-xl uppercase">{product.name}</h1>
</div>
