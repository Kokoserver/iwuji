import type { CartIn } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, url }) => {
	if (!locals.is_login && !locals.user && !locals.token) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, `/login?redirectTo=${url.pathname}`);
	}

	const data_out = { carts: [] } as { carts: CartIn[] };

	const res = await api.get('/carts/');
	data_out.carts = res.data as CartIn[];
	return data_out;
};
