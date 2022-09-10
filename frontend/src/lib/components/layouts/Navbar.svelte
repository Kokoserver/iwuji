<script lang="ts">
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from "flowbite-svelte"
	import { page } from "$app/stores"
	import { BaseRoutes } from "./baseroute"
</script>

<div class="mt-4">
	<Navbar let:hidden let:toggle>
		<div class="container mx-auto md:space-y-6">
			<div class="flex justify-center items-center space-x-10">
				<NavBrand href="/" class="md:block">
					<img src="/logo.svg" class="h-5" alt="iwuji Logo" />
				</NavBrand>
				<NavHamburger on:click={toggle} />
			</div>
			<div class="flex justify-center items-center px-2">
				<NavUl {hidden}>
					{#each BaseRoutes as route}
						<NavLi
							href={route.url}
							active={true && $page.url.pathname === route.url}
							activeClass="border-b-blue-600"
							class={`uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  ${!route.is_last && "mr-10"}`}>{route.name}</NavLi
						>
					{/each}
				</NavUl>
			</div>
		</div>
	</Navbar>
</div>
