<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import { Badge, Button } from "flowbite-svelte"
</script>

<Container divClass="my-20 px-3 md:px-0 space-y-20">
	<div
		class="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-0 py-10 "
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
			<div class="pt-6  t space-y-6  flex flex-col md:items-start items-center">
				<a
					href="/"
					class="rounded-full font-semibold bg-yellow-200 px-4 py-3 w-24 text-center uppercase"
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
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M19.5 12h-15"
								/>
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
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M12 4.5v15m7.5-7.5h-15"
								/>
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
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M19.5 12h-15"
								/>
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
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M12 4.5v15m7.5-7.5h-15"
								/>
							</svg>
						</Button>
					</div>
				</div>

				<div class="flex flex-col md:flex-row gap-6">
					<a
						href="/"
						class="rounded-full font-semibold border border-gray-700 px-4 py-3 w-48 text-center uppercase flex items-center space-x-2"
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
	</div>
</Container>
