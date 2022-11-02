import { get_addressList } from '$root/lib/utils/page/address';
import { get_order_list } from '$root/lib/utils/page/order';
import { get_payment_list } from '$root/lib/utils/page/payment';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals, fetch, request }) => {
	if (!locals.user) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, `/auth/login/?redirectTo=${request.url}`);
	}
	return {
		order_list: get_order_list(fetch),
		payment_list: get_payment_list(fetch),
		address_list: get_addressList(fetch)
	};
};
