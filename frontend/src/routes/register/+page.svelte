<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import type { ActionData } from './$types';
	import { Alert, Button, Helper, Input, Label } from 'flowbite-svelte';
	import type { UserRegisterInput } from '$root/lib/interface/user.interface';
	import suite from './form';
	import { enhance } from '$app/forms';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';

	export let form: ActionData;

	let email_error: string | null;

	$: {
		if (form?.error) {
			email_error = form.error;
		}

		if (form?.message !== undefined) {
			email_error = '';
			notification.success(form?.message, 12000);
			goto('/', {
				replaceState: true
			});
		}
	}

	const formdata = {} as UserRegisterInput;
	let res = suite.get();

	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		if (inputField.name === 'email') {
			// email_error = '';
			const response = await fetch('/register/api', {
				method: 'POST',
				body: JSON.stringify({ email: inputField.value })
			});
			const field_error = await response.json();
			email_error = field_error.email;
		}

		res = suite(formdata, inputField.name);
	};
</script>

<Container divClass="md:flex   my-16 w-full content-center justify-center">
	<div class="shadow-md  md:flex sm:px-6 md:px-0">
		<div class="rounded-l-md bg-white h-full px-6 py-10">
			<div class="w-100">
				<div class="pb-5">
					<h1 class="text-xl font-semibold">Create an account</h1>
				</div>
				<form class="flex flex-col space-y-6" method="post" use:enhance>
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
							<a href="/login" class="text-xs font-semibold text-purple-700">Login here</a>
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
