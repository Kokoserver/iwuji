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
					<h1 class="text-xl font-semibold">forgot your password</h1>
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

					<div class="flex items-start">
						<div class="text-center">
							<span class="text-xs text-gray-400 font-semibold"
								>remember your password</span
							>
							<a href="/login" class="text-xs font-semibold text-purple-700"
								>Login here</a
							>
						</div>
					</div>
					<Button type="submit" class="w-full1 capitalize">submit</Button>
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
