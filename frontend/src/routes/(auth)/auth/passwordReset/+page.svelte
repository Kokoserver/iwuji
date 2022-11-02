<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import suite from '$root/lib/form/auth/passwordReset';
	import { Button } from 'flowbite-svelte';
	import { notification } from '$root/lib/notification';
	import { goto } from '$app/navigation';
	import LableInput from '$root/lib/components/form/LableInput.svelte';
	import { page } from '$app/stores';
	const formdata = {
		password: '',
		confirm_password: '',
		token: $page.url.searchParams.get('reset_token')
	};

	let res = suite.get();
	$: password_error = '';

	const handleSubmit = async () => {
		const res = await fetch('/api/auth/passwordReset', {
			method: 'POST',
			body: JSON.stringify(formdata)
		});
		const data = await res.json();
		if (!res.ok) {
			password_error = data.error;
		}

		notification.success(data.message);
		await goto('/');
	};

	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
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

				<form class="flex flex-col space-y-6" on:submit|preventDefault={handleSubmit}>
					<LableInput
						name="password"
						value={formdata.password}
						{handleChange}
						type="password"
						placeholder="***********"
						required
						labeleValue="new password"
						error={res.getErrors('password')[0]}
					/>
					<LableInput
						name="confirm_password"
						value={formdata.confirm_password}
						{handleChange}
						type="password"
						placeholder="***********"
						required
						labeleValue="confirm password"
						error={res.getErrors('confirm_password')[0]}
					/>

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
