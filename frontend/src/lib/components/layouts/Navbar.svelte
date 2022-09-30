<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import type { UserDataIn } from '$root/lib/interface/user.interface';
	export let is_login: boolean = false;
	export let user: UserDataIn;
	export let cart_count: number = 0;
	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Avatar,
		Dropdown,
		DropdownItem,
		DropdownHeader,
		DropdownDivider,
		Button,
		Badge
	} from 'flowbite-svelte';
	const handleLogout = async () => {
		await goto('/user/logout', {
			replaceState: true
		});
	};
</script>

<Navbar let:hidden let:toggle DivClass="px-3 md:px-0">
	<div class="w-full flex items-center justify-center pb-4 mt-2">
		<NavBrand href="/">
			<img src="/logo.svg" class="h-5" alt="iwuji Logo" />
		</NavBrand>
	</div>
	<div class="flex items-center md:order-2">
		<Avatar id="avatar-menu" src="/author.png" />
		<NavHamburger on:click={toggle} class1="w-full md:flex md:w-auto md:order-1" />
	</div>
	<div>
		<Dropdown placement="bottom" triggeredBy="#avatar-menu">
			{#if is_login}
				<DropdownHeader>
					<span class="block text-sm">{`${user.firstname} ${user.lastname}`}</span>
					<span class="block truncate text-sm font-medium">{user.email} </span>
				</DropdownHeader>
				<DropdownItem><a href="/user/dashboard">Dashboard</a></DropdownItem>
				<DropdownDivider />
				<DropdownItem on:click={handleLogout}>sign out</DropdownItem>
			{:else if !is_login}
				<DropdownItem><a href="/login">login</a></DropdownItem>
			{/if}
		</Dropdown>
		<Button href="/cart" id="cartbtn" size="sm">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="w-6 h-6"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"
				/>
			</svg>

			<span class="sr-only">Cart</span>
			<Badge rounded={true} index color="yellow">{cart_count}</Badge>
			cart
		</Button>
	</div>
	<NavUl {hidden}>
		<NavLi
			href="/"
			active={$page.url.pathname === '/'}
			activeClass="border-b-blue-600"
			data-sveltekit-prefetch=""
			class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-5">home</NavLi
		>

		<NavLi
			href="/bio"
			active={$page.url.pathname === '/bio'}
			activeClass="border-b-blue-600"
			data-sveltekit-prefetch=""
			class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-5">bio</NavLi
		>

		<NavLi
			href="/books"
			active={$page.url.pathname === '/books'}
			activeClass="border-b-blue-600"
			data-sveltekit-prefetch=""
			class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  mr-5">books</NavLi
		>

		<NavLi
			href="#contact"
			active={$page.url.pathname === '/#contact'}
			activeClass="border-b-blue-600"
			data-sveltekit-prefetch=""
			class="uppercase border-b-transparent border-b-2 text-gray-700 font-normal md:pb-3
							  ">contact</NavLi
		>
	</NavUl>
</Navbar>
