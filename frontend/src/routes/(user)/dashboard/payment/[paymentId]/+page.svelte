<script lang="ts">
	import { browser } from '$app/environment';
	import { goto } from '$app/navigation';
	import { Loading } from '$root/store/modalStore';
	import { Spinner } from 'flowbite-svelte';

	if (browser) {
		goto('/dashboard/payment');
	}
</script>

<div class="h-screen">
	{#if $Loading}
		<div
			class="fixed top-0 bottom-0 left-0 right-0 bg-gray-500 flex justify-center opacity-95 items-center"
		>
			<div class="flex gap-2 items-center justify-center">
				<Spinner size="10" /> <span>loading ...</span>
			</div>
		</div>
	{/if}
</div>
