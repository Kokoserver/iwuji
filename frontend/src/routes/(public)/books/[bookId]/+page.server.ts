import type { PageServerLoad } from './$types';
import { get_singleProduct, get_singleVariation } from '$root/lib/utils/page/products';

export const load: PageServerLoad = async ({ url, params }) => {
	const is_series = url.searchParams.get('is_series');
	const { bookId } = params;
	return {
		product: !is_series ? bookId && get_singleProduct(Number(bookId)) : {},
		variation: is_series ? bookId && get_singleVariation(Number(bookId)) : {},
		is_single_product: !is_series,
		is_variation: is_series ? true : false
	};
};
