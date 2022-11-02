import { get_authorData } from '$root/lib/utils/page/author';
import { getCarts } from '$root/lib/utils/page/cart';
import { get_ProductList, get_Reviews, get_VariationList } from '$root/lib/utils/page/products';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals, fetch }) => {
	return {
		is_login: locals.is_login,
		user: locals.user,
		carts: locals.user ? getCarts(fetch) : [],
		variations: get_VariationList('', 10, 0, true),
		products: get_ProductList('', 5, 0, false, false, true),
		reviews: get_Reviews(4, 0),
		author: get_authorData(fetch, undefined, 1, 0, undefined, true)
	};
};
