<script lang="ts">
	import type { AddressIn } from '$root/lib/interface/address.interface';
	import type { UserDataIn } from '$root/lib/interface/user.interface';
	export let address: AddressIn;
	export let user: UserDataIn;
	export let url_redirect: string = '';
</script>

<div class="space-y-2 w-[20rem]">
	<h1 class="font-bold capitalize">{user.firstname} {user.lastname}</h1>
	<p>{user.email}</p>
	<p class="font-semibold">
		{address.street}, {address.city}, {address.state}, {address.country}, {address.zipcode}
	</p>
	<div>
		<a
			href="/dashboard/address/edit/?id={address.id}{url_redirect
				? '&redirectTo=' + url_redirect
				: ''}"
			class="font-medium text-blue-600 hover:underline dark:text-blue-500 pr-5 pt-y">Edit</a
		>
	</div>
</div>
