<script lang="ts">
	import Container from "$root/lib/components/layouts/Container.svelte"
	import { showModel } from "$root/lib/store/modalStore"
	import { Iconinput, Next, Previous } from "flowbite-svelte"
	showModel
</script>

<Container divClass="mt-28 px-3 md:px-0">
	<div class="space-y-4 ">
		<Iconinput
			noBorder
			inputClass=" rounded-full"
			id="search"
			placeholder="Search"
			class="p-4"
		>
			<svg
				aria-hidden="true"
				class="w-5 h-5 text-gray-500 dark:text-gray-400"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg"
				><path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
				/></svg
			>
		</Iconinput>
		<div class="flex items-center justify-end space-x-5">
			<p class="capitalize">sorte by</p>
			<div class="flex rounded-full items-center">
				<a
					href="/"
					class="border border-transparent rounded-l-full font-semibold bg-yellow-200 px-4 py-3 text-center capitalize  border-gray-600 "
					>books</a
				>
				<a
					href="/"
					class="font-semibold border rounded-r-full px-4 py-3 text-center capitalize  border-gray-600"
					>series</a
				>
			</div>
		</div>
	</div>
</Container>
<Container divClass="pt-10 pb-28 px-5 space-y-7">
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10"
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
					href="/books/232"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>preview</a
				>

				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase "
					>view on amazon</a
				>
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10"
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
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10"
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
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10"
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
			</div>
		</div>
	</div>
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 border-b border-b-blue-400 py-10"
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
			</div>
		</div>
	</div>
	<div class="flex items-center justify-center py-20">
		<Previous on:previous={() => alert("previous is click")} icon />
		<Next on:next={() => alert("next is click")} icon />
	</div>
</Container>
