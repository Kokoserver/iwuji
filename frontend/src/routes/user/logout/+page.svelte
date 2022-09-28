<script lang="ts">
	import { goto } from '$app/navigation';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	$: {
		if (data.logout) {
			window.location.href = '/';
		}
	}
	goto('/');
</script>
