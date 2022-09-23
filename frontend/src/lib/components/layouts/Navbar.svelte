<script lang="ts">
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	import { page } from '$app/stores';
	export let is_login: boolean = false;
</script>

<div>
	<Navbar let:hidden let:toggle navClass="w-full px-4 md:px-0 pt-4 bg-gray-50">
		<div class="container mx-auto md:space-y-6">
			<div class="flex justify-center items-center space-x-10">
				<NavBrand href="/" class="md:block ">
					<img src="/logo.svg" class="h-5" alt="iwuji Logo" />
				</NavBrand>
				<NavHamburger on:click={toggle} />
			</div>
			<div class="flex justify-center items-center px-2">
				<NavUl {hidden}>
					<NavLi
						href="/"
						active={true && $page.url.pathname === '/'}
						activeClass="border-b-blue-600"
						data-sveltekit-prefetch
						class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-10">home</NavLi
					>

					<NavLi
						href="/bio"
						active={true && $page.url.pathname === '/bio'}
						activeClass="border-b-blue-600"
						data-sveltekit-prefetch
						class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-10">bio</NavLi
					>

					<NavLi
						href="/books"
						active={true && $page.url.pathname === '/books'}
						activeClass="border-b-blue-600"
						data-sveltekit-prefetch
						class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-10">books</NavLi
					>

					<NavLi
						href="/shop"
						active={true && $page.url.pathname === '/shop'}
						activeClass="border-b-blue-600"
						data-sveltekit-prefetch
						class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-10">shop</NavLi
					>
					<NavLi
						href="#contact"
						active={true && $page.url.pathname === '/#contact'}
						activeClass="border-b-blue-600"
						data-sveltekit-prefetch
						class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  ">contact</NavLi
					>
					{#if !is_login}
						<NavLi
							href="/login"
							active={true && $page.url.pathname === '/login'}
							activeClass="border-b-blue-600"
							data-sveltekit-prefetch
							class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-10">login</NavLi
						>
					{/if}
				</NavUl>
			</div>
		</div>
	</Navbar>
</div>
