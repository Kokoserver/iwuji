import type { PageServerLoad } from './$types';
import { get_singleProduct, get_singleVariation } from '$root/routes/books/crud';

export const load: PageServerLoad = async ({ params, url }) => {
	const is_series = url.searchParams.get('is_series');
	const { bookId } = params;
	return {
		product: get_singleProduct(Number(bookId)),
		variation: is_series === 'true' ? get_singleVariation(Number(bookId)) : {},
		is_single_product: !is_series,
		is_variation: is_series === 'true' ? true : false
	};
};
