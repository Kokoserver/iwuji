<script lang="ts">
	import { flip } from 'svelte/animate';
	import { fly } from 'svelte/transition';

	import { notifications } from '$root/lib/notification/store';
	import { Alert } from 'flowbite-svelte';
	const not_type = {
		success: 'success',
		warning: 'warning',
		danger: 'danger',
		info: 'info',
		dark: 'dark ',
		default: 'default'
	};
</script>

<div class="notifications">
	{#each $notifications as notification (notification.id)}
		<div animate:flip class="toast" transition:fly={{ y: 30 }}>
			{#if notification.type === not_type.success}
				<Alert color="green" dismissable={true}>
					<svg
						slot="icon"
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
							clip-rule="evenodd"
						/></svg
					>
					{@html notification.message}
				</Alert>
			{/if}
			{#if notification.type === not_type.warning}
				<Alert color="yellow" dismissable={true}>
					<svg
						slot="icon"
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
							clip-rule="evenodd"
						/></svg
					>
					{@html notification.message}
				</Alert>
			{/if}
			{#if notification.type === not_type.default}
				<Alert dismissable={true}>
					<svg
						slot="icon"
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
							clip-rule="evenodd"
						/></svg
					>
					{@html notification.message}
				</Alert>
			{/if}
			{#if notification.type === not_type.danger}
				<Alert color="red" dismissable={true}>
					<svg
						slot="icon"
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
							clip-rule="evenodd"
						/></svg
					>
					{@html notification.message}
				</Alert>
			{/if}
			{#if notification.type === not_type.dark}
				<Alert color="dark" dismissable={true}>
					<svg
						slot="icon"
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
							clip-rule="evenodd"
						/></svg
					>
					{@html notification.message}
				</Alert>
			{/if}
		</div>
	{/each}
</div>

<style>
	.notifications {
		position: fixed;
		top: 10px;
		/* left: 0; */
		right: 0;
		margin: 0 auto;
		padding: 0;
		z-index: 9999;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
	}

	.toast {
		flex: 0 0 auto;
		margin-bottom: 10px;
	}
</style>
