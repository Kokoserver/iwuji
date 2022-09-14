<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import { Button, Helper, Input, Label } from "flowbite-svelte"
</script>

<Container
	divClass="flex flex-wrap min-h-screen w-full content-center justify-center"
>
	<div class="flex shadow-md">
		<div
			class="flex flex-wrap content-center justify-center rounded-l-md bg-white"
			style="width: 24rem; height: 32rem;"
		>
			<div class="w-72">
				<div class="pb-5">
					<h1 class="text-xl font-semibold">Welcome back</h1>
					<small class="text-gray-400"
						>Welcome back! Please enter your details</small
					>
				</div>

				<form class="flex flex-col space-y-6" action="/">
					<Label class="space-y-2">
						<span>Email</span>
						<Input
							type="email"
							name="email"
							placeholder="name@company.com"
							required
						/>
						<Helper color="red">hello</Helper>
					</Label>
					<Label class="space-y-2">
						<span>Your password</span>
						<Input
							type="password"
							name="password"
							placeholder="•••••"
							required
						/>
						<Helper>password is required</Helper>
					</Label>
					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold"
								>Don't have account?</span
							>
							<a href="/register" class="text-xs font-semibold text-purple-700"
								>Sign up</a
							>
						</div>
						<a
							href="/forgotpassword"
							class="ml-auto text-sm text-blue-700 hover:underline dark:text-blue-500"
							>Lost password?</a
						>
					</div>
					<Button type="submit" class="w-full1">Login to your account</Button>
				</form>

				<!-- Footer -->
			</div>
		</div>

		<!-- Login banner -->
		<div
			class="md:flex md:flex-wrap content-center justify-center rounded-r-md hidden"
			style="width: 24rem; height: 32rem;"
		>
			<img
				class="w-full h-full bg-center bg-no-repeat bg-cover rounded-r-md"
				src="/books.jpg"
				alt="book"
			/>
		</div>
	</div>
</Container>
