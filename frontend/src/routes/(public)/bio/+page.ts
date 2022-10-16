import type { PageLoad } from './$types';
import { get_authorData } from '$root/lib/utils/page/author';
import { get_ProductList } from '$root/lib/utils/page/products';

export const load: PageLoad = async () => {
	return {
		products: get_ProductList('', 3, 0, false, false, true),
		author: get_authorData()
	};
};
