import type { PageLoad } from './$types';
import { get_ProductList, get_VariationList } from '$root/lib/utils/page/products';

export const load: PageLoad = async () => {
	return {
		products: get_ProductList('', 10, 0, false, false, true),
		variations: get_VariationList('', 10, 0, true)
	};
};
