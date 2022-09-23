import type { PageServerLoad } from './$types';
import { get_authorData } from '$root/routes/bio/crud';
import type { AuthorIn } from '$root/lib/interface/author.interface';
import type { ProductIn } from '$root/lib/interface/product.interface';
import type { ReviewIn } from '$root/lib/interface/ReviewIn.interface';
import { get_ProductList, get_ProductReview } from './books/crud';

export const load: PageServerLoad = async () => {
	const auth_data = await get_authorData();
	const data_out = {} as { author: AuthorIn; products: ProductIn[]; reviews: ReviewIn[] };
	if (auth_data) {
		data_out.author = auth_data;
	}
	const product_list = await get_ProductList('', 5, 0, false, false, true);
	if (Array.isArray(product_list) && product_list.length > 0) {
		data_out.products = product_list;
		const product_reviews = await get_ProductReview(4, 0, product_list[0].id);
		if (Array.isArray(product_reviews) && product_reviews.length > 1) {
			data_out.reviews = product_reviews;
		} else {
			data_out.reviews = [];
		}
	} else {
		data_out.products = [] as ProductIn[];
	}

	return data_out;
};
