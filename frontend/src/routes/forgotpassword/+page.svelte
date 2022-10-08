<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import suite from './form';
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import type { ActionData } from './$types';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';
	import FormTitlte from '$root/lib/components/layouts/FormTitlte.svelte';
	const formdata = { email: '' };
	export let form: ActionData;

	let res = suite.get();
	let email_error = '';
	$: {
		if (email_error) {
			res.getErrors('email')[0] = email_error;
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
		if (inputField.name === 'email') {
			email_error = '';
			const response = await fetch('/register/api', {
				method: 'POST',
				body: JSON.stringify({ email: inputField.value })
			});
			const field_error = (await response.json()) as { email: string };
			if (field_error?.email === '') {
				email_error = 'Account does not exist';
			}
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
					<FormTitlte title="Forgot password" />
				</div>

				<form class="flex flex-col space-y-6" method="POST">
					<Label class="space-y-2">
						<span>Email</span>
						<Input
							type="email"
							bind:value={formdata.email}
							on:change={handleChange}
							name="email"
							placeholder="name@company.com"
							required
						/>
						{#if res.getErrors('email')}
							<Helper color="red">{res.getErrors('email') ?? email_error}</Helper>
						{/if}
					</Label>

					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold">remember your password</span>
							<a href="/login" class="text-xs font-semibold text-purple-700">Login here</a>
						</div>
					</div>
					<Button type="submit" class="w-full1 capitalize">submit</Button>
				</form>
			</div>
		</div>
	</div>
</Container>
