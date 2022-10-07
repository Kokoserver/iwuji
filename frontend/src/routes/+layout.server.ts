import api from '$root/lib/utils/api';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	const res = await api.get('/carts/');
	return { is_login: locals.is_login, user: locals.user, carts: res.data };
};
