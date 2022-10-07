import type { PageServerLoad } from './$types';
import { get_ProductList, get_VariationList } from './crud';

export const load: PageServerLoad = async () => {
	return {
		products: get_ProductList('', 10, 0, false, false, true),
		variations: get_VariationList('', 10, 0, true)
	};
};
