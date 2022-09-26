<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import suite from './form';
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import type { ActionData } from '../../../../.svelte-kit/types/src/routes/passwordReset/$types';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';
	import { enhance } from '$app/forms';
	import { error } from '@sveltejs/kit';
	const formdata = { password: '', confirm_password: '' };
	export let form: ActionData;

	let res = suite.get();
	let password_error = '';

	$: {
		if (form?.error) {
			password_error = form.error;
			form.error = '';
		}
		if (form?.message) {
			notification.success(form.message, 6000);
			goto('/', {
				replaceState: true
			});
		}
	}

	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		if (inputField.name === 'password' && form?.error) {
			password_error = '';
		}
		res = suite(formdata, inputField.name);
	};
</script>

<Container divClass="flex flex-wrap min-h-screen w-full content-center justify-center">
	<div class="flex shadow-md">
		<div
			class="flex flex-wrap content-center justify-center rounded-l-md bg-white"
			style="width: 24rem; height: 32rem;"
		>
			<div class="w-72">
				<div class="pb-5">
					<h1 class="text-xl font-semibold">Reset password</h1>
				</div>

				<form class="flex flex-col space-y-6" method="POST" use:enhance>
					<Label class="space-y-2">
						<span>Password</span>
						<Input
							type="password"
							bind:value={formdata.password}
							on:change={handleChange}
							name="password"
							placeholder="*********"
							required
						/>
						{#if res.getErrors('password')}
							<Helper color="red">{res.getErrors('password').concat(password_error) ?? ''}</Helper>
						{/if}
					</Label>
					<Label class="space-y-2">
						<span>Confirm password</span>
						<Input
							type="password"
							bind:value={formdata.confirm_password}
							on:change={handleChange}
							name="confirm_password"
							placeholder="**********"
							required
						/>
						{#if res.getErrors('confirm_password')}
							<Helper color="red">{res.getErrors('confirm_password') ?? ''}</Helper>
						{/if}
					</Label>

					<Button type="submit" class="w-full1 capitalize">submit</Button>
				</form>

				<!-- Footer -->
			</div>
		</div>

		<!-- Login banner -->
		<!-- <div
			class="md:flex md:flex-wrap content-center justify-center rounded-r-md hidden"
			style="width: 24rem; height: 32rem;"
		>
			<img
				class="w-full h-full bg-center bg-no-repeat bg-cover rounded-r-md"
				src="/books.jpg"
				alt="book"
			/>
		</div> -->
	</div>
</Container>
