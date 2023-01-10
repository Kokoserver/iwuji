import { get_order_list } from '$root/lib/utils/page/order';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, fetch, request }) => {
	if (!locals.user) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, `/auth/login/?redirectTo=${request.url}`);
	}
	return {
		order_list: get_order_list(fetch)
	};
};
