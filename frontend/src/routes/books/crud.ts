import type { ProductIn } from '$root/lib/interface/product.interface';
import type { ReviewIn } from '$root/lib/interface/ReviewIn.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';

export const get_ProductList = async (
	filter = '',
	limit = 10,
	offset = 0,
	is_series = false,
	is_assigned = true,
	is_active = true
): Promise<ProductIn[]> => {
	const res = await api.get(
		`/products/?limit=${limit}&offset=${offset}&is_series=${is_series}&is_assigned=${is_assigned}&is_active=${is_active}${
			filter && `&filter=${filter}`
		}`
	);
	if (res.status === status.HTTP_200_OK) {
		return res.data as ProductIn[];
	}
	return [];
};

export const get_singleProduct = async (productId: number): Promise<ProductIn> => {
	const res = await api.get(`/products/${productId}`);
	if (res.status === status.HTTP_200_OK) {
		return res.data as ProductIn;
	}
	return {} as ProductIn;
};

export const get_ProductReview = async (limit = 10, offset = 0, productId: number): Promise<ReviewIn[]> => {
	const res = await api.get(`/reviews/product/${productId}/?limit=${limit}&offset=${offset}`);
	if (res.status === status.HTTP_200_OK) {
		return res.data as ReviewIn[];
	}
	return [];
};
