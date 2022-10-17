<script>
	import { page } from '$app/stores';
	import { toggleSidebar } from '$root/store/pageUtilsStore';
	import {
		Sidebar,
		SidebarBrand,
		SidebarGroup,
		SidebarItem,
		SidebarWrapper
	} from 'flowbite-svelte';
	$: activeUrl = $page.url.pathname;

</script>

<aside
	id="sidebar"
	class="fixed {$toggleSidebar
		? 'hidden'
		: 'flex'} z-20 h-full top-0 left-0 pt-16  lg:flex flex-shrink-0 flex-col w-64 transition-width duration-75"
	aria-label="Sidebar"
>
	<div class="relative flex-1 flex flex-col min-h-0 border-r border-gray-200 bg-white pt-0">
		<Sidebar asideClass="w-full flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
			<SidebarWrapper>
				<SidebarGroup>
					<SidebarItem
						label="Shipping Address"
						active={activeUrl.includes('address') ? true : false}
						href="/dashboard/address"
					>
						<svelte:fragment slot="icon">
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
									d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
								/>
							</svg>
						</svelte:fragment>
					</SidebarItem>
					<SidebarItem
						label="Order"
						active={activeUrl.includes('order') ? true : false}
						href="/dashboard/order"
					>
						<svelte:fragment slot="icon">
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
									d="M15.75 10.5V6a3.75 3.75 0 10-7.5 0v4.5m11.356-1.993l1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 01-1.12-1.243l1.264-12A1.125 1.125 0 015.513 7.5h12.974c.576 0 1.059.435 1.119 1.007zM8.625 10.5a.375.375 0 11-.75 0 .375.375 0 01.75 0zm7.5 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
								/>
							</svg>
						</svelte:fragment>
					</SidebarItem>
					<SidebarItem
						label="Payment"
						active={activeUrl.includes('payment') ? true : false}
						href="/dashboard/payment"
					>
						<svelte:fragment slot="icon">
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
									d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 002.25-2.25V6.75A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25v10.5A2.25 2.25 0 004.5 19.5z"
								/>
							</svg>
						</svelte:fragment>
					</SidebarItem>
					<SidebarGroup border>
						<SidebarItem label="Sign Out" href="/auth/logout">
							<svelte:fragment slot="icon">
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
										d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3"
									/>
								</svg>
							</svelte:fragment>
						</SidebarItem>
					</SidebarGroup>
				</SidebarGroup>
			</SidebarWrapper>
		</Sidebar>
	</div>
</aside>
