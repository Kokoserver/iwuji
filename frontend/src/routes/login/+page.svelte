<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import { enhance } from '$app/forms';
	import type { ActionData } from './$types';
	import suite from './form';
	import type { UserLoginInput } from '$root/lib/interface/auth.interface';

	export let form: ActionData;
	const formdata = {} as UserLoginInput;
	let res = suite.get();
	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		if (inputField.name === 'username' && form?.error) {
			form.error = '';
		}
		res = suite(formdata, inputField.name);
	};
</script>

<Container divClass="flex flex-wrap py-20 w-full content-center justify-center">
	<div class="flex shadow-md">
		<div
			class="flex flex-wrap content-center justify-center rounded-l-md bg-white"
			style="width: 24rem; height: 32rem;"
		>
			<div class="w-72">
				<div class="pb-10">
					<h1 class="text-xl font-semibold">Welcome back</h1>
				</div>

				<form class="flex flex-col space-y-6" method="post" use:enhance>
					<Label class="space-y-2">
						<span>Email</span>
						<Input
							type="email"
							bind:value={formdata.username}
							name="username"
							on:change={handleChange}
							placeholder="name@company.com"
							required
						/>
						{#if form?.error ?? res.getErrors('username')[0]}
							<Helper color="red"
								>{res.getErrors('username').concat(form?.error ?? '') ?? ''}</Helper
							>
						{/if}
					</Label>
					<Label class="space-y-2">
						<span>Your password</span>
						<Input
							type="password"
							on:change={handleChange}
							name="password"
							bind:value={formdata.password}
							placeholder="***********"
							required
						/>
						{#if res.getErrors('password')[0]}
							<Helper color="red">{res.getErrors('password')[0] ?? ''}</Helper>
						{/if}
					</Label>
					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold">Don't have account?</span>
							<a href="/register" class="text-xs font-semibold text-purple-700">Sign up</a>
						</div>
						<a
							href="/forgotpassword"
							class="ml-auto text-sm text-blue-700 hover:underline dark:text-blue-500"
							>Lost password?</a
						>
					</div>
					<Button disabled={!res.valid} type="submit" class="w-full1">Login to your account</Button>
				</form>

				<!-- Footer -->
			</div>
		</div>

		<!-- Login banner -->
		<!-- <div class="md:flex md:flex-wrap content-center justify-center rounded-r-md hidden" style="width: 24rem; height: 32rem;">
			<img class="w-full h-full bg-center bg-no-repeat bg-cover rounded-r-md" src="/books.jpg" alt="book" />
		</div> -->
	</div>
</Container>
