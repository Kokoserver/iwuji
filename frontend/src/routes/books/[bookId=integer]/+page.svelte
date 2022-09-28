<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import Grid from '$root/lib/components/layouts/Grid.svelte';
	import { AccordionItem, Badge, Button } from 'flowbite-svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	$: product = data.product;
	$: is_single_product = data.is_single_product;
	$: variation = data.variation;
	$: is_variation = data.is_variation;
</script>

{#if is_single_product && product}
	<Container divClass="my-20 px-3 md:px-0 space-y-20">
		<div class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 py-10 ">
			<div class="md:w-1/2 p-2">
				<img src={product.cover_img.url} width="427" height="527" alt={product.name} srcset="" />
			</div>
			<div class="md:w-2/5 space-y-4 p-3 ">
				<h1 class="font-semibold uppercase text-2xl text-center md:text-left">{product.name}</h1>
				<p class="font-normal text-gray-700 text-center md:text-left">
					{product.description}
				</p>
				<div class="pt-6  t space-y-6  flex flex-col md:items-start items-center">
					<a
						href="/"
						class="rounded-full font-semibold bg-primary px-4 py-3 w-24 text-center uppercase"
						>Pdf
					</a>
					<div class="flex flex-col md:items-start md:flex-row gap-6">
						<div class="flex items-center justify-center space-x-1">
							<Button
								btnClass="rounded-full border border-gray-600 h-12 w-12 text-3xl text-center font-bold text-2xl"
								><svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-12 h-12"
								>
									<path stroke-linecap="round" stroke-linejoin="round" d="M19.5 12h-15" />
								</svg>
							</Button>
							<a
								href="/"
								class=" relative rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
							>
								<span>Hard back</span>
								<Badge rounded index color="red">20</Badge>
							</a>
							<Button
								btnClass="rounded-full border border-gray-600 h-12 w-12 text-3xl text-center font-bold text-2xl"
								><svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-12 h-12"
								>
									<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
								</svg>
							</Button>
						</div>
						<div class="flex md:items-center justify-center space-x-1">
							<Button
								btnClass="rounded-full border border-gray-600 h-12 w-12 text-3xl text-center font-bold text-2xl"
								><svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-12 h-12"
								>
									<path stroke-linecap="round" stroke-linejoin="round" d="M19.5 12h-15" />
								</svg>
							</Button>
							<a
								href="/"
								class=" relative rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase flex items-center space-x-2"
							>
								<span>Paper back</span>
								<Badge rounded index color="red">20</Badge>
							</a>
							<Button
								btnClass="rounded-full border border-gray-600 h-12 w-12 text-3xl text-center font-bold text-2xl"
								><svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-12 h-12"
								>
									<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
								</svg>
							</Button>
						</div>
					</div>

					<div class="flex flex-col md:flex-row gap-6">
						<a
							href="/"
							class="rounded-full font-semibold border border-gray-700 px-4 py-3 w-48 text-center uppercase flex items-center space-x-2"
						>
							<span><img src="/icons/cart.svg" class="h-5 w-5" alt="" srcset="" /></span>
							<span>add to cart</span></a
						>
					</div>
				</div>
			</div>
		</div>
	</Container>
{:else if is_variation && variation}
	<Container divClass=" my-10 md:px-0 shadow-xl md:shadow-none ">
		<div class=" flex flex-col md:flex-row items-center  md:items-start justify-center gap-20">
			<div class="md:w-3/4 ">
				<div class="p-2">
					<img src={variation.cover_img.url} width="427" height="527" alt={variation.name} />
				</div>
				<div class="space-y-4 p-3 ">
					<h1 class="font-semibold uppercase text-2xl text-center md:text-left">
						{variation.name}
					</h1>
					<div class={variation.description.length > 1500 ? `h-[25rem] overflow-y-scroll` : ``}>
						<h2 class="capitalize text-xl font-semibold pb-4">descriptions</h2>
						<p class="mb-2 text-gray-500 dark:text-gray-400">
							{variation.description}
						</p>
					</div>
				</div>
			</div>
			<div class="md:w-3/5  space-y-3 flex flex-col items-center justify-center shadow-xl px-4">
				<h1 class="text-3xl font-semibold pt-3">Series books</h1>
				<div
					class="{variation.items[0]?.name
						? `h-[50rem] overflow-y-scroll overflow-x-hidden`
						: `h-[10rem]`} w-full "
				>
					{#each variation.items as product}
						<div
							class="flex md:flex-row flex-col   items-center justify-center  md:gap-0 border-b border-b-secondary py-10"
						>
							<div class="md:w-1/2 p-2">
								<img
									src={product.cover_img.url}
									width="427"
									height="527"
									alt={product.name}
									srcset=""
								/>
							</div>
							<div class="md:w-3/5 space-y-2 p-2 ">
								<h1 class="font-semibold uppercase text-xl text-center md:text-left">
									{product.name}
								</h1>
								<p class="font-normal text-gray-700 text-center md:text-left">
									{product.description.slice(1, 300)}...
								</p>
								<div class="pt-6 space-x-2 flex items-center justify-start">
									<a
										href="/books/{product.id}"
										class="rounded-full font-semibold bg-primary p-2 text-sm text-center uppercase "
										>preview</a
									>

									<a
										href="/"
										class="rounded-full font-semibold 
									text-sm bg-primary px-1 py-2 text-center uppercase ">view on amazon</a
									>
								</div>
							</div>
						</div>
					{:else}
						<p class="text-center font-semibold text-xl">Series parts is not available yet</p>
					{/each}
				</div>
			</div>
		</div>
	</Container>
{:else}
	<div class="h-screen flex justify-center items-center">
		<p class="text-center text-4xl font-bold">Book is not found</p>
	</div>
{/if}
