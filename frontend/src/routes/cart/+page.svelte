<script>
	import Container from '$root/lib/components/layouts/Container.svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
</script>

<Container divClass="mt-20 space-y-20">
	<h1 class="text-center font-bold text-3xl uppercase">Cart</h1>
	<div class="flex justify-end">
		<a href="/checkout" class="rounded-full font-semibold bg-primary px-5 py-3 capitalize"
			>Checkout</a
		>
	</div>

	<div
		class="flex flex-col md:flex-row items-center md:items-start justify-center  md:gap-20 border-b-2 border-b-secondary py-14"
	>
		<img src="/hardcover_book.png" alt="" class="w-60" />
		<div class="flex-1 ">
			<div class="flex justify-between space-x-8 pb-10">
				<div class="flex flex-col  gap-5 items-start justify-start mb-5 ml-5">
					<h1 class="text-capitalize uppercase font-bold text-md md:text-xl ">
						Lorem ipsum dolor sit amet consectetur
					</h1>
					<img src="/logo.svg" class="h-3" alt="" srcset="" />
				</div>
				<div>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.2"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
						/>
					</svg>
				</div>
			</div>
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
								<h1 class="font-normal">Hard back <span class="pl-5 pr-7">x2</span></h1>
								<div>
									<svg
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
						<TableBodyCell><span class="font-normal">$2999</span></TableBodyCell>
						<TableBodyCell><span class="font-normal">$3487463754</span></TableBodyCell>
					</TableBodyRow>
					<TableBodyRow trClass="bg-transparent capitalize">
						<TableBodyCell>
							<div class="flex items-center justify-start">
								<h1 class="capiterlize font-normal">
									paper back <span class="pl-5 pr-6">x2</span>
								</h1>
								<div>
									<svg
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
						<TableBodyCell><span class="font-normal">$2999</span></TableBodyCell>
						<TableBodyCell><span class="font-normal"> $3487463754</span></TableBodyCell>
					</TableBodyRow>
					<TableBodyRow trClass="bg-transparent capitalize">
						<TableBodyCell><span class="font-normal">pdf</span></TableBodyCell>
						<TableBodyCell><span class="font-normal">$2999</span></TableBodyCell>
						<TableBodyCell><span class="font-normal">$3487463754</span></TableBodyCell>
					</TableBodyRow>
					<TableBodyRow trClass="bg-transparent">
						<TableBodyCell />
						<TableBodyCell />
						<TableBodyCell class="!px-0 md:!p-6" tdClass="pt-10 "
							><span class="capitalize  pr-2">total:</span><span class="font-bold "
								>$3487463754</span
							></TableBodyCell
						>
					</TableBodyRow>
				</TableBody>
			</Table>
		</div>
	</div>
</Container>
