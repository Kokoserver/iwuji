<script>
	import AdminFooter from '$root/lib/components/layouts/AdminFooter.svelte';
	import UserNavBar from '$root/lib/components/layouts/UserSideBar.svelte';
	import UserTopBar from '$root/lib/components/layouts/UserTopBar.svelte';
</script>

<div>
	<nav class="bg-white border-b border-gray-200 fixed z-30 w-full">
		<div class="px-3 py-3 lg:px-5 lg:pl-3">
			<div class="flex items-center justify-between">
				<UserTopBar />
			</div>
		</div>
	</nav>
	<div class="flex overflow-hidden bg-white pt-16">
		<UserNavBar />

		<div id="main-content" class="h-full w-full bg-gray-50 relative overflow-y-auto lg:ml-64">
			<main class="mb-20">
				<div class="pt-6 px-4">
					<slot />
				</div>
			</main>
			<AdminFooter />
		</div>
	</div>
</div>
