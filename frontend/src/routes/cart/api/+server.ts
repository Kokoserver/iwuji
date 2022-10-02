import type { CartIn, CartOut } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const data: CartOut = await request.json();

	const res = await api.post('/carts/', data, {
		'Content-Type': 'application/json'
	});
	
	if (
		res.status !== status.HTTP_201_CREATED &&
		Number(res.status) < status.HTTP_500_INTERNAL_SERVER_ERROR
	) {
		return json(res.data);
	}

	return json(res.data);
};
export const GET: RequestHandler = async () => {
	const res = await api.get('/carts/', {
		'Content-Type': 'application/json'
	});
	if (res.status !== status.HTTP_200_OK) {
		return json(res.data);
	}
	return json(res.data);
};
export const PUT: RequestHandler = async ({ request }) => {
	const data: CartIn = await request.json();

	const res = await api.put('/carts/', data, {
		'Content-Type': 'application/json'
	});

	if (res.status !== status.HTTP_200_OK) {
		return json(data);
	}
	return json(res.data);
};

export const DELETE: RequestHandler = async ({ url }) => {
	const bookId = url.searchParams.get('id');
	if (!bookId) {
		return json({ message: 'book id is required' });
	}

	const res = await api.delete(`/carts/${bookId}`, {
		'Content-Type': 'application/json'
	});
	const out_data = {} as { message: string; status: string };

	if (res.status === status.HTTP_204_NO_CONTENT) {
		out_data.message = 'Item remove successfully';
		out_data.status = 'success';
		return json(out_data);
	}

	if (res.status === status.HTTP_404_NOT_FOUND) {
		out_data.message = 'Item not found';
		out_data.status = 'error';
		return json(out_data);
	}

	out_data.message = 'Error deleting item';
	out_data.status = 'error';
	return json(out_data);
};
