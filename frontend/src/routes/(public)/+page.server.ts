import type { PageServerLoad } from './$types';
import { get_authorData } from '$root/lib/utils/page/author';
import { get_ProductList, get_Reviews } from '$root/lib/utils/page/products';

export const load: PageServerLoad = async () => {
	return {
		products: get_ProductList('', 5, 0, false, false, true),
		reviews: get_Reviews(4, 0),
		author: get_authorData()
	};
};
