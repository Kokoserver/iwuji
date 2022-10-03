import type { AddressIn } from '$root/lib/interface/address.interface';
import type { CartIn } from '$root/lib/interface/cart.interface';
import type { UserDataIn } from '$root/lib/interface/user.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	const address = await api.get('/address/');
	const carts = await api.get('/carts/');

	const data_out = { address: [], user: locals.user ?? [], carts: [] } as {
		address: AddressIn[];
		user: UserDataIn;
		carts: CartIn[];
	};
	if (
		address.status === status.HTTP_401_UNAUTHORIZED ||
		carts.status === status.HTTP_401_UNAUTHORIZED
	) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/login?redirectTo=/checkout');
	}
	if (address.status === status.HTTP_200_OK && Array.isArray(address.data)) {
		data_out.address = address.data as AddressIn[];
	}
	if (carts.status === status.HTTP_200_OK && Array.isArray(carts.data)) {
		data_out.carts = carts.data as CartIn[];
	}
	return data_out;
};
