import type { CartOut } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';
import { get_token } from '$root/lib/utils/setAuthorization';
import { status } from '$root/lib/utils/status';
import { error, json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async (event) => {
	try {
		const data: CartOut = await event.request.json();
		const res = await api.post('/carts/', data, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_201_CREATED) {
			return json(res.data, { status: status.HTTP_201_CREATED });
		}
		return json({ error: 'Error adding product to cart' }, { status: status.HTTP_400_BAD_REQUEST });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error adding product to cart');
	}
};

export const GET: RequestHandler = async (event) => {
	try {
		const signal = event.url.searchParams.get('signal');
		let url = '';
		if (signal === 'single') {
			const id = event.url.searchParams.get('id');
			if (id) {
				url = `/carts/${id}`;
			}
		} else {
			url = '/carts/';
		}

		const res = await api.get(url, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_200_OK) {
			return json(res.data, { status: status.HTTP_200_OK });
		}
		return json({}, { status: status.HTTP_400_BAD_REQUEST });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error getting user cart list');
	}
};
export const PUT: RequestHandler = async (event) => {
	try {
		const data: CartOut = await event.request.json();
		const res = await api.put('/carts/', data, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});
		if (res.status !== status.HTTP_200_OK) {
			return json(data, { status: status.HTTP_400_BAD_REQUEST });
		}
		return json(res.data);
	} catch (err) {
		throw error(status.WS_1011_INTERNAL_ERROR, 'Error updating cart');
	}
};

export const DELETE: RequestHandler = async (event) => {
	try {
		const bookId = event.url.searchParams.get('id');
		if (!bookId) {
			return json({ message: 'book id is required' }, { status: status.HTTP_400_BAD_REQUEST });
		}

		const res = await api.delete(`/carts/${bookId}`, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_204_NO_CONTENT) {
			return json({}, { status: status.HTTP_204_NO_CONTENT });
		}

		if (res.status === status.HTTP_404_NOT_FOUND) {
			return json({}, { status: status.HTTP_404_NOT_FOUND });
		}
		return json(
			{ error: 'Error deleting product from cart' },
			{ status: status.HTTP_400_BAD_REQUEST }
		);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error removing product from cart');
	}
};
