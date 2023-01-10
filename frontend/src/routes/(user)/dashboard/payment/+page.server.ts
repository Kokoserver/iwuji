import { get_payment_list } from '$root/lib/utils/page/payment';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, fetch, request }) => {
	if (!locals.user) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, `/auth/login/?redirectTo=${request.url}`);
	}
	return {
		payment_list: get_payment_list(fetch)
	};
};
