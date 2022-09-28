import type { PageServerLoad } from './$types';
import type { ProductIn } from '$root/lib/interface/product.interface';
import { get_singleProduct, get_singleVariation } from '$root/routes/books/crud';
import type { VariationIn } from '$root/lib/interface/variation.interface';

export const load: PageServerLoad = async ({ params, url }) => {
	const is_series = url.searchParams.get('is_series');
	const { bookId } = params;
	const out_data = {} as {
		product: ProductIn;
		variation: VariationIn;
		is_variation: boolean;
		is_single_product: boolean;
	};
	if (is_series === 'true') {
		const variation = await get_singleVariation(Number(bookId));
		out_data.variation = variation;
		out_data.is_variation = true;
	}
	if (!is_series) {
		const product = await get_singleProduct(Number(bookId));
		out_data.product = product;
		out_data.is_single_product = true;
	}

	return out_data;
};
