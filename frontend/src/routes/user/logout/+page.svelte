<script lang="ts">
	import { browser } from '$app/environment';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	$: {
		if (browser) {
			if (data.logout) {
				window.location.href = '/';
			}
		}
	}
</script>
