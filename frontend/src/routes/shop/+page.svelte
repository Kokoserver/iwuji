<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import { Badge } from "flowbite-svelte"
</script>

<Container divClass="mt-20 space-y-20">
	<h1 class="text-center font-bold text-3xl uppercase">Shop</h1>
	<div class="flex  justify-between items-center px-2 md:px-0 ">
		<a
			href="/"
			class="rounded-full border border-transparent font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
			>view books on amazon</a
		>

		<a
			href="/"
			class=" relative rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
		>
			<span /><img src="/icons/cart.svg" class="h-5 w-5" alt="" srcset="" />
			<span>view cart</span>
			<span class="sr-only">Notifications</span>
			<Badge rounded index color="red">20</Badge>
		</a>
	</div>
</Container>

<div />
<Container divClass="mt-20 px-3 md:px-0 space-y-20">
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10  "
	>
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="427" height="527" alt="" srcset="" />
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
			<div
				class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
			>
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
				>
					<span
						><img
							src="/icons/cart.svg"
							class="h-5 w-5"
							alt=""
							srcset=""
						/></span
					> <span>add to cart</span></a
				>
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10 "
	>
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="427" height="527" alt="" srcset="" />
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
			<div
				class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
			>
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
				>
					<span
						><img
							src="/icons/cart.svg"
							class="h-5 w-5"
							alt=""
							srcset=""
						/></span
					> <span>add to cart</span></a
				>
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10 "
	>
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="427" height="527" alt="" srcset="" />
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
			<div
				class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
			>
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
				>
					<span
						><img
							src="/icons/cart.svg"
							class="h-5 w-5"
							alt=""
							srcset=""
						/></span
					> <span>add to cart</span></a
				>
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10 "
	>
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="427" height="527" alt="" srcset="" />
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
			<div
				class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
			>
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
				>
					<span
						><img
							src="/icons/cart.svg"
							class="h-5 w-5"
							alt=""
							srcset=""
						/></span
					> <span>add to cart</span></a
				>
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10 "
	>
		<div class="md:w-1/2 p-2">
			<img src="/hero.png" width="427" height="527" alt="" srcset="" />
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
			<div
				class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
			>
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>
				<a
					href="/"
					class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
				>
					<span
						><img
							src="/icons/cart.svg"
							class="h-5 w-5"
							alt=""
							srcset=""
						/></span
					> <span>add to cart</span></a
				>
			</div>
		</div>
	</div>
</Container>
