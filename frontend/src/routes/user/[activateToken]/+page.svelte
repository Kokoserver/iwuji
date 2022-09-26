<script lang="ts">
	import { browser } from '$app/environment';
	import { goto } from '$app/navigation';
	import { notification } from '$root/lib/notification';
	import type { PageServerData } from './$types';
	export let data: PageServerData;

	if (data.message) {
		notification.success(data.message, 5000);
		if (browser) {
			goto('/', {
				replaceState: true
			});
		}
	}
</script>
