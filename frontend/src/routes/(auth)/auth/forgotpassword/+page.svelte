<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import suite from '$root/lib/form/auth/forgotpassword';
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';
	import FormTitlte from '$root/lib/components/utilities/FormTitlte.svelte';
	const formdata = { email: '' };
	let res = suite.get();
	$: email_error = '';

	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		res = suite(formdata, inputField.name);
	};

	const handleSubmit = async () => {
		const checkEmail = await fetch('/api/auth/checkEmail', {
			method: 'POST',
			body: JSON.stringify({ email: formdata.email })
		});
		if (!checkEmail.ok) {
			email_error = 'Account does not exist';
			return;
		}

		const res = await fetch('/api/auth/forgotPassword', {
			method: 'POST',
			body: JSON.stringify(formdata)
		});
		const data = await res.json();
		if (res.ok) {
			notification.success(data.message);
			await goto('/');
		}
		notification.danger(data.error);
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

				<form class="flex flex-col space-y-6" on:submit|preventDefault={handleSubmit}>
					<Label class="space-y-2">
						<span>Email</span>
						<Input
							type="email"
							bind:value={formdata.email}
							on:change={handleChange}
							name="email"
							placeholder="example@gmail.com"
							required
						/>
						{#if res.getErrors('email')}
							<Helper color="red">{res.getErrors('email')[0] ?? email_error}</Helper>
						{/if}
					</Label>

					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold">remember your password</span>
							<a href="/auth/login" class="text-xs font-semibold text-purple-700">Login here</a>
						</div>
					</div>
					<Button type="submit" class="w-full capitalize" disabled={!res.valid}>submit</Button>
				</form>
			</div>
		</div>
	</div>
</Container>
