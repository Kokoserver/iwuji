import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals, fetch }) => {
	const res = await fetch('/api/cart');
	if (!res.ok) {
		return { is_login: locals.is_login, user: locals.user, carts: [] };
	}
	const carts = await res.json();
	return { is_login: locals.is_login, user: locals.user, carts };
};
