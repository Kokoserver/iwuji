<script lang="ts">
	import type { CartIn, CartUpdateOut } from '$root/lib/interface/cart.interface';


	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
     import type { Writable } from 'svelte/store';
	import { get_total_price, handleRemoveFromCart, handleUpdateCart } from '$root/routes/shop/crud';
	export let data: { carts: CartIn[] };
    export let cartStore:Writable<CartIn[]>
   

	const handleUpdate = async (
		cartItemObj: CartIn,
		type: 'hard_back' | 'paper_back' | 'pdf',
		direction: 'up' | 'down'
	) => {
		if (type === 'pdf') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj) {
					item.pdf = !cartItemObj.pdf;
					return item;
				}
				return item;
			});
		}
		if (type === 'hard_back' && direction == 'up') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.hard_back_qty < 41) {
					item.hard_back_qty++;
					return item;
				}
				return item;
			});
		}
		if (type === 'hard_back' && direction == 'down') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.hard_back_qty != 0) {
					item.hard_back_qty--;
					return item;
				}
				return item;
			});
		}
		if (type === 'paper_back' && direction == 'up') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.paper_back_qty <= 40) {
					item.paper_back_qty++;
					return item;
				}
				return item;
			});
		}
		if (type === 'paper_back' && direction == 'down') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.paper_back_qty !== 0) {
					item.paper_back_qty--;
					return item;
				}
				return item;
			});
		}
		if (data.carts !== $cartStore) {
			const to_update: CartUpdateOut = {
				cartId: cartItemObj.id,
				pdf: cartItemObj.pdf,
				paper_back_qty: cartItemObj.paper_back_qty,
				hard_back_qty: cartItemObj.hard_back_qty
			};

			setTimeout(async () => {
				await handleUpdateCart(to_update);
			}, 5000);
		}
	};
</script>

{#if $cartStore[0]?.id}
	{#each $cartStore as item}
		<div
			class="flex flex-col md:flex-row items-center md:items-start justify-center  md:gap-20 border-b-2 border-b-secondary py-14"
		>
			<img
				src={item.product.cover_img?.url}
				alt={item.product.name}
				id={String(item.id)}
				class="w-60"
			/>
			<div class="flex-1 ">
				<div class="flex justify-between space-x-8 pb-10">
					<div class="flex flex-col  gap-5 items-start justify-start mb-5 ml-5">
						<h1 class="text-capitalize uppercase font-bold text-md md:text-xl ">
							{item.product.name}
						</h1>
						<img src="/logo.svg" class="h-3" alt="" srcset="" />
					</div>
					<div>
						<svg
							on:click={() => handleRemoveFromCart(item.id)}
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.2"
							stroke="currentColor"
							class="w-6 h-6 cursor-pointer"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
							/>
						</svg>
					</div>
				</div>
				<div>
					<Table divClass="bg-transperent ">
						<TableHead theadClass="bg-none capitalize text-left">
							<TableHeadCell><span class="font-normal">qty</span></TableHeadCell>
							<TableHeadCell><span class="font-normal">price per unit</span></TableHeadCell>
							<TableHeadCell><span class="font-normal">price</span></TableHeadCell>
						</TableHead>
						<TableBody>
							<TableBodyRow trClass="bg-transparent capitalize">
								<TableBodyCell>
									<div class="flex items-center justify-start">
										<h1 class="font-normal">
											Hard back <span class="pl-5 pr-7">x{item.hard_back_qty}</span>
										</h1>
										<div>
											<svg
												on:click={() => handleUpdate(item, 'hard_back', 'up')}
												xmlns="http://www.w3.org/2000/svg"
												fill="none"
												viewBox="0 0 24 24"
												stroke-width=".9"
												stroke="currentColor"
												class="w-6 h-6 cursor-pointer"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													d="M4.5 15.75l7.5-7.5 7.5 7.5"
												/>
											</svg>
											<svg
												on:click={() => handleUpdate(item, 'hard_back', 'down')}
												xmlns="http://www.w3.org/2000/svg"
												fill="none"
												viewBox="0 0 24 24"
												stroke-width=".9"
												stroke="currentColor"
												class="w-6 h-6 cursor-pointer"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													d="M19.5 8.25l-7.5 7.5-7.5-7.5"
												/>
											</svg>
										</div>
									</div>
								</TableBodyCell>
								<TableBodyCell
									><span class="font-normal">${item.product.property.hard_back_price}</span
									></TableBodyCell
								>
								<TableBodyCell
									><span class="font-normal"
										>${item.hard_back_qty * item.product.property.hard_back_price}</span
									></TableBodyCell
								>
							</TableBodyRow>
							<TableBodyRow trClass="bg-transparent capitalize">
								<TableBodyCell>
									<div class="flex items-center justify-start">
										<h1 class="capiterlize font-normal">
											paper back <span class="pl-5 pr-6">x{item.paper_back_qty}</span>
										</h1>
										<div>
											<svg
												on:click={() => handleUpdate(item, 'paper_back', 'up')}
												xmlns="http://www.w3.org/2000/svg"
												fill="none"
												viewBox="0 0 24 24"
												stroke-width=".9"
												stroke="currentColor"
												class="w-6 h-6"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													d="M4.5 15.75l7.5-7.5 7.5 7.5"
												/>
											</svg>
											<svg
												on:click={() => handleUpdate(item, 'paper_back', 'down')}
												xmlns="http://www.w3.org/2000/svg"
												fill="none"
												viewBox="0 0 24 24"
												stroke-width=".9"
												stroke="currentColor"
												class="w-6 h-6"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													d="M19.5 8.25l-7.5 7.5-7.5-7.5"
												/>
											</svg>
										</div>
									</div>
								</TableBodyCell>
								<TableBodyCell
									><span class="font-normal">${item.product.property.paper_back_price}</span
									></TableBodyCell
								>
								<TableBodyCell
									><span class="font-normal">
										${item.paper_back_qty * item.product.property.paper_back_price}</span
									></TableBodyCell
								>
							</TableBodyRow>
							<TableBodyRow trClass="bg-transparent capitalize">
								<TableBodyCell>
									<div
										class="flex items-center justify-start gap-16 font-normal cursor-pointer"
										on:click={() => handleUpdate(item, 'pdf', 'up')}
									>
										<h1 class="pr-1">pdf</h1>
										<span class="font-normal">{item.pdf ? 'X1' : 'X0'}</span>
									</div>
								</TableBodyCell>
								<TableBodyCell
									><span class="font-normal">${item.product.property.pdf_price}</span
									></TableBodyCell
								>
								<TableBodyCell
									><span class="font-normal">${item.pdf ? item.product.property.pdf_price : 0}</span
									></TableBodyCell
								>
							</TableBodyRow>
							<TableBodyRow trClass="bg-transparent">
								<TableBodyCell />
								<TableBodyCell />
								<TableBodyCell class="" tdClass="pt-10 "
									><span class="capitalize  ">total: </span><span class="font-bold "
										>${get_total_price(item)}</span
									></TableBodyCell
								>
							</TableBodyRow>
						</TableBody>
					</Table>
				</div>
			</div>
		</div>
	{/each}
{:else}
	<h1 class="h-screen"><p class="text-center text-4xl">cart is empty</p></h1>
{/if}
