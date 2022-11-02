<script>
	import { toggleSidebar } from '$root/store/pageUtilsStore';
</script>

<div class=" w-full flex items-center justify-between space-x-20 px-2 md:px-8  py-2">
	<div class="self-center flex items-center space-x-5">
		<a href="/dashboard"><h1 class="uppercase font-bold hidden md:flex">dashboard</h1></a>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			fill="none"
			viewBox="0 0 24 24"
			stroke-width="1.2"
			stroke="currentColor"
			class="w-8 h-8 cursor-pointer md:hidden"
			on:click={() => ($toggleSidebar = !$toggleSidebar)}
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5"
			/>
		</svg>
	</div>
	<a href="/" data-sveltekit-prefetch="">
		<div class="flex items-center justify-center space-x-10">
			<span class="border p-2 font-bold cursor-pointer hover:bg-secondary rounded-full bg-primary">
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
						d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5"
					/>
				</svg>
			</span>
		</div>
	</a>
</div>
