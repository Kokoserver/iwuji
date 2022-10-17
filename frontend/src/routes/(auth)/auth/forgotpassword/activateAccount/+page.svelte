<script lang="ts">
	import { goto } from '$app/navigation';
	import { notification } from '$root/lib/notification';
	import type { PageData } from './$types';
	export let data: PageData;
	const { error, message } = data;

	if (message) {
		notification.success(message, 5000);
		goto('/');
	}
	if (error) {
		notification.danger(error, 5000);
		goto('/');
	}
</script>
