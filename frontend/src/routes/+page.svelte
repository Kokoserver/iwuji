<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import Grid from "$root/lib/components/layouts/Grid.svelte"
</script>

<Container divClass=" pt-10 pb-28 px-5">
	<div class="flex flex-col md:flex-row items-center justify-center gap-12">
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="527" height="627" alt="" srcset="" />
		</div>
		<div class="md:w-2/5 space-y-4 p-3 ">
			<h1 class="font-semibold uppercase text-2xl text-center md:text-left">
				consequence
			</h1>
			<p class="font-normal text-gray-700 text-center md:text-left">
				Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque hic odio
				illum ipsam consequuntur in rem vero placeat possimus adipisci harum
				debitis ab provident quam enim, porro dolor repellat cum laboriosam
				culpa? Aliquid ducimus eos vero adipisci! Voluptatibus possimus culpa ut
				ullam repellendus voluptates quam fugit iure consectetur magnam. Ex.
			</p>
			<div class="pt-6">
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>buy now</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase"
					>see more books</a
				>
			</div>
		</div>
	</div>
</Container>

<Container divClass="pb-28 px-5">
	<h3 class="font-bold text-3xl uppercase text-center pb-7">Reviews</h3>
	<Grid>
		<div class="flex  justify-between  gap-4">
			<div class="w-1/3">
				<img src="/books.jpg" alt="" srcset="" class="rounded-full w-24 h-24" />
			</div>
			<div class="w-2/3">
				<h1 class="capitalize font-semibold text-md text-gray-500">jon doe</h1>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis dolorem,
				quisquam nemo vel quae quibusdam labore nulla exercitationem nihil voluptatibus.
			</div>
		</div>
		<div class="flex  justify-between gap-4">
			<div class="w-1/3">
				<img src="/books.jpg" alt="" srcset="" class="rounded-full w-24 h-24" />
			</div>
			<div class="w-2/3">
				<h1 class="capitalize font-semibold text-md">jon doe</h1>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis dolorem,
				quisquam nemo vel quae quibusdam labore nulla exercitationem nihil voluptatibus.
			</div>
		</div>
		<div class="flex  justify-between gap-4">
			<div class="w-1/3">
				<img src="/books.jpg" alt="" srcset="" class="rounded-full w-24 h-24" />
			</div>
			<div class="w-2/3">
				<h1 class="capitalize font-semibold text-md">jon doe</h1>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis dolorem,
				quisquam nemo vel quae quibusdam labore nulla exercitationem nihil voluptatibus.
			</div>
		</div>
	</Grid>
</Container>
<Container divClass=" pt-10 pb-28 px-5">
	<div class="flex flex-col md:flex-row items-center justify-center gap-6">
		<div class="md:w-1/2 p-2">
			<img src="/author.png" width="500" height="500" alt="" />
		</div>
		<div class="md:w-2/5 space-y-4 p-3 ">
			<h1 class="font-semibold uppercase text-2xl text-center md:text-left">
				The author
			</h1>
			<p class="font-normal text-gray-700 text-center md:text-left">
				Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque hic odio
				illum ipsam consequuntur in rem vero placeat possimus adipisci harum
				debitis ab provident quam enim, porro dolor repellat cum laboriosam
				culpa? Aliquid ducimus eos vero adipisci! Voluptatibus possimus culpa ut
				ullam repellendus voluptates quam fugit iure consectetur magnam. Ex.
				<a href="/" class="font-normal text-blue-300 ">Read more</a>
			</p>
		</div>
	</div>
</Container>
<Container divClass="pb-28 ">
	<h3 class="font-bold text-3xl uppercase text-center pb-20">new release</h3>
	<Grid gap={6}>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
		</div>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
		</div>
		<div class="flex flex-col items-center space-y-7">
			<img src="/hardcover_book.png" alt="" srcset="" class="w-65 h-60" />
			<h1 class="font-normal text-xl uppercase">consequence</h1>
		</div>
	</Grid>
	<div class="flex justify-end pt-20">
		<a href="/" class="rounded-full font-semibold bg-yellow-200 px-5 py-3"
			>view more</a
		>
	</div>
</Container>
