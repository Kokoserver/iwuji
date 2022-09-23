import type { PageServerLoad } from './$types';
import type { ProductIn } from '$root/lib/interface/product.interface';
import { get_singleProduct } from '$root/routes/books/crud';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
	const { bookId } = params;
	const out_data = {} as { product: ProductIn };
	const product = await get_singleProduct(Number(bookId));

	if (product.name !== undefined || null) {
		out_data.product = product;
		return out_data;
	} else {
		throw error(404, 'book not found');
	}
};
