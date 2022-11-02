<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import type { UserRegisterInput } from '$root/lib/interface/user.interface';
	import suite from '$root/lib/form/auth/register';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';

	$: email_error = '';

	const formdata = {} as UserRegisterInput;
	let res = suite.get();

	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		res = suite(formdata, inputField.name);
	};

	const handleSubmit = async () => {
		const checkEmail = await fetch('/api/auth/checkEmail', {
			method: 'POST',
			body: JSON.stringify({ email: formdata.email })
		});
		if (checkEmail.ok) {
			email_error = 'User already exist';
		}
		const res = await fetch('/api/auth/register', {
			method: 'POST',
			body: JSON.stringify(formdata)
		});
		const data = await res.json();
		if (!res.ok) {
			email_error = data.error;
		}
		notification.success(data.message);
		await goto('/');
	};
</script>

<Container divClass="md:flex   my-16 w-full content-center justify-center">
	<div class="shadow-md  md:flex sm:px-6 md:px-0">
		<div class="rounded-l-md bg-white h-full px-6 py-10">
			<div class="w-100">
				<div class="pb-5">
					<h1 class="text-xl font-semibold">Create an account</h1>
				</div>
				<form class="flex flex-col space-y-6" on:submit|preventDefault={handleSubmit}>
					<div class=" block md:flex space-y-6 md:space-y-0  md:space-x-3">
						<Label class="space-y-2">
							<span>First name</span>
							<Input
								type="text"
								name="firstname"
								on:change={handleChange}
								bind:value={formdata.firstname}
								placeholder="firstname"
								required
							/>
							<Helper color="red">{res.getErrors('firstname')[0] ?? ''}</Helper>
						</Label>
						<Label class="space-y-2">
							<span>Last name</span>
							<Input
								type="text"
								name="lastname"
								on:change={handleChange}
								bind:value={formdata.lastname}
								placeholder="lastname"
								required
							/>
							<Helper color="red">{res.getErrors('lastname')[0] ?? ''}</Helper>
						</Label>
					</div>
					<Label class="space-y-2">
						<span>Email</span>
						<Input
							type="email"
							name="email"
							on:change={handleChange}
							bind:value={formdata.email}
							placeholder="email"
							required
						/>
						<Helper color="red">{res.getErrors('email')[0] ?? email_error ?? ''}</Helper>
					</Label>
					<div class=" block md:flex space-y-6 md:space-y-0 md:space-x-3">
						<Label class="space-y-2">
							<span>password</span>
							<Input
								autocomplete="false"
								type="password"
								name="password"
								on:change={handleChange}
								bind:value={formdata.password}
								placeholder="********"
								required
							/>

							<Helper color="red">{res.getErrors('password')[0] ?? ''}</Helper>
						</Label>
						<Label class="space-y-2">
							<span>Confirm password</span>
							<Input
								autocomplete="false"
								type="password"
								name="confirm_password"
								on:change={handleChange}
								bind:value={formdata.confirm_password}
								placeholder="********"
								required
							/>
							<Helper color="red">{res.getErrors('confirm_password')[0] ?? ''}</Helper>
						</Label>
					</div>

					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold">Already have account?</span>
							<a href="/auth/login" class="text-xs font-semibold text-purple-700">Login here</a>
						</div>
					</div>
					<Button type="submit" class="w-full">Register new account</Button>
				</form>
			</div>
		</div>

		<!-- Login banner -->
		<div
			class="md:flex md:flex-wrap content-center justify-center rounded-r-md hidden object-contain"
			style="width: 24rem; height: 100%; background:url(/books.jpg)"
		/>
	</div>
</Container>
