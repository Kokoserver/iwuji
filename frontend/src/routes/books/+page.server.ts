import type { PageServerLoad } from './$types';
import type { ProductIn } from '$root/lib/interface/product.interface';
import { get_ProductList, get_VariationList } from './crud';
import type { VariationIn } from '$root/lib/interface/variation.interface';

export const load: PageServerLoad = async () => {
	const out_data: { products: ProductIn[]; variations: VariationIn[] } = {
		products: [],
		variations: []
	};
	const product_list = await get_ProductList('', 10, 0, false, false, true);
	const variation_list = await get_VariationList('', 10, 0, true);
	if (Array.isArray(product_list) && product_list.length > 0) {
		out_data.products = product_list;
		return out_data;
	} else {
		out_data.products;
	}
	if (Array.isArray(variation_list) && variation_list.length > 0) {
		out_data.variations = variation_list;
		return out_data;
	} else {
		out_data.variations;
	}
	return out_data;
};
