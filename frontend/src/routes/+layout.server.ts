import type { CartIn } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	const res = await api.get('/carts/');
	const my_cart = (res.data as CartIn[]) || [];
	return { is_login: locals.is_login, user: locals.user, carts: my_cart};
};
