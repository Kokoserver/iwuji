<script>
	import { page } from '$app/stores';
</script>

<div class="flex flex-col justify-center items-center">
	<div>
		<img src="https://i.ibb.co/ck1SGFJ/Group.png" alt="" />
	</div>
	<div class="xl:pt-24 w-full xl:w-1/2 relative pb-12 lg:pb-0">
		<div class="">
			<h1 class="my-2 text-gray-800 font-bold text-2xl">
				{$page.status}
			</h1>
			<p class="my-2 text-gray-800">
				{$page.error?.message}
			</p>
			<button
				class="sm:w-full lg:w-auto my-2 border rounded md py-4 px-8 text-center bg-indigo-600 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-700 focus:ring-opacity-50"
				>Take me home</button
			>
		</div>
	</div>
</div>
