import type { PageLoad } from './$types';
import { get_singleProduct, get_singleVariation } from '$root/lib/utils/page/products';

export const load: PageLoad = async ({url, params}) => {
	const is_series = url.searchParams.get('is_series');
	const { bookId } = params;
	return {
		product: get_singleProduct(Number(bookId)),
		variation: is_series === 'true' ? get_singleVariation(Number(bookId)) : {},
		is_single_product: !is_series,
		is_variation: is_series === 'true' ? true : false
	};
};
