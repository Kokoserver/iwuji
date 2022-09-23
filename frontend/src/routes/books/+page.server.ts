import type { PageServerLoad } from './$types';
import type { ProductIn } from '$root/lib/interface/product.interface';
import { get_ProductList } from './crud';

export const load: PageServerLoad = async () => {
	const out_data: { products: ProductIn[] } = { products: [] };
	const product_list = await get_ProductList('', 10, 0, false, false, true);
	if (Array.isArray(product_list) && product_list.length > 0) {
		out_data.products = product_list;
		return out_data;
	} else {
		out_data.products;
	}
	return out_data;
};
