import { get_addressList } from '$root/lib/utils/page/address';
import { getCarts } from '$root/lib/utils/page/cart';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, fetch }) => {
	if (!locals.user) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/auth/login?redirectTo=/checkout');
	}

	return {
		address_list: get_addressList(fetch),
		carts: locals.user ? getCarts(fetch) : []
	};
};
