import { status } from '$root/lib/utils/status';
import type { PageServerLoad } from '../../../.svelte-kit/types/src/routes/bio/$types';
import { error } from '@sveltejs/kit';
import { get_authorData } from './crud';
import type { AuthorIn } from '$root/lib/interface/author.interface';
import type { ProductIn } from '$root/lib/interface/product.interface';
import { get_ProductList } from '../books/crud';

export const load: PageServerLoad = async ({ setHeaders }): Promise<{ author: AuthorIn; products: ProductIn[] }> => {
	const author_data = await get_authorData();
	const data_out = {} as { author: AuthorIn; products: ProductIn[] };
	if (author_data) {
		data_out.author = author_data;
	} else {
		data_out.author = {} as AuthorIn;
	}
	const product_list = await get_ProductList('', 3, 0, true, false, true);
	if (Array.isArray(product_list) && product_list.length > 0) {
		data_out.products = product_list;
	} else {
		data_out.products = [];
	}

	return data_out;
};
