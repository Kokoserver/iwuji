<script>
	import Container from "$root/lib/components/layouts/Container.svelte"
	import { Button, Helper, Input, Label } from "flowbite-svelte"
</script>

<Container
	divClass="flex flex-wrap min-h-screen w-full content-center justify-center"
>
	<div class="flex shadow-md">
		<div
			class="flex flex-wrap content-center justify-center rounded-l-md bg-white  h-[50rem] md:h-[32rem] w-[24rem] md:w-[34rem]"
		>
			<div class="w-100">
				<div class="pb-5">
					<h1 class="text-xl font-semibold">Create an account</h1>
				</div>

				<form class="flex flex-col space-y-6" action="/">
					<div class=" block md:flex space-y-6 md:space-y-0  md:space-x-3">
						<Label class="space-y-2">
							<span>First name</span>
							<Input
								type="text"
								name="firstname"
								placeholder="name@company.com"
								required
							/>
							<Helper color="red">check name</Helper>
						</Label>
						<Label class="space-y-2">
							<span>Last name</span>
							<Input
								type="text"
								name="lastname"
								placeholder="lastname"
								required
							/>
							<Helper>check name</Helper>
						</Label>
					</div>
					<Label class="space-y-2">
						<span>Email</span>
						<Input type="email" name="email" placeholder="email" required />
						<Helper>check name</Helper>
					</Label>
					<div class=" block md:flex space-y-6 md:space-y-0 md:space-x-3">
						<Label class="space-y-2">
							<span>password</span>
							<Input
								type="password"
								name="password"
								placeholder="********"
								required
							/>
							<Helper>check name</Helper>
						</Label>
						<Label class="space-y-2">
							<span>Confirm password</span>
							<Input
								type="password"
								name="confirm_password"
								placeholder="********"
								required
							/>
							<Helper>check name</Helper>
						</Label>
					</div>

					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold"
								>Already have account?</span
							>
							<a href="/login" class="text-xs font-semibold text-purple-700"
								>Login here</a
							>
						</div>
					</div>
					<Button type="submit" class="w-full">Register new account</Button>
				</form>

				<!-- Footer -->
			</div>
		</div>

		<!-- Login banner -->
		<div
			class="md:flex md:flex-wrap content-center justify-center rounded-r-md hidden object-contain"
			style="width: 24rem; height: 36rem; background:url(/books.jpg)"
		/>
	</div>
</Container>
