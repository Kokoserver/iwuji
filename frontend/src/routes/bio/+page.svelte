<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import Grid from "$root/lib/components/layouts/Grid.svelte"
</script>

<Container divClass=" pt-10 pb-28 px-5">
	<div class="flex flex-col md:flex-row items-center justify-center gap-6">
		<div class="md:w-1/2 p-2">
			<img src="/author.png" width="500" height="500" alt="" />
		</div>
		<div class="md:w-2/5 space-y-4 p-3 ">
			<p class="font-normal text-gray-700 text-center md:text-left">
				Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque hic odio
				illum ipsam consequuntur in rem vero placeat possimus adipisci harum
				debitis ab provident quam enim, porro dolor repellat cum laboriosam
				culpa? Aliquid ducimus eos vero adipisci! Voluptatibus possimus culpa ut
				ullam repellendus voluptates quam fugit iure consectetur magnam. Ex.
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam sit harum
				eum quasi, deleniti quod recusandae culpa quas quis iste enim sequi
				dicta facilis quaerat vel. Ipsa nam libero veniam fuga voluptates qui,
				non unde quis quaerat eos? Repellendus placeat dicta at repudiandae
				excepturi voluptas ullam sit esse dolorum. Dicta sint assumenda error
				enim perferendis illum numquam facere excepturi amet delectus, non
				dignissimos ducimus ab deserunt quae praesentium tenetur totam voluptas?
				Fugit sunt accusamus veniam consequatur maiores deserunt cum alias
				aperiam, tempora consequuntur ullam illum facilis voluptatem explicabo
				mollitia quisquam voluptate voluptatum incidunt exercitationem? Quae
				dolores ratione natus placeat sed.
			</p>
		</div>
	</div>
</Container>

<Container divClass="pb-28 ">
	<h3 class="font-bold text-3xl uppercase text-center pb-20">authors works</h3>
	<Grid gap={6}>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
			<a
				href="/"
				class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase"
				>preview</a
			>
		</div>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
			<a
				href="/"
				class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase"
				>preview</a
			>
		</div>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
			<a
				href="/"
				class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase"
				>preview</a
			>
		</div>
	</Grid>
</Container>
