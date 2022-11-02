import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { get_token } from '$root/lib/utils/setAuthorization';
import { status } from '$root/lib/utils/status';

export const POST: RequestHandler = async (event) => {
	const data = await event.request.json();
	const res = await api.post('/orders/', data, {
		...(await get_token(event)),
		'Content-Type': 'application/json'
	});
	return json({ ...res });
};

export const GET: RequestHandler = async (event) => {
	try {
		const orderId: string = event.url.searchParams.get('id') || '';
		let url = null;
		if (orderId) {
			url = `/orders/${orderId}`;
		} else {
			url = `/orders/`;
		}
		const res = await api.get(url, {
			...(await get_token(event))
		});
		if (orderId) {
			if (
				res.status === status.HTTP_404_NOT_FOUND ||
				res.status === status.HTTP_400_BAD_REQUEST ||
				res.status === status.HTTP_422_UNPROCESSABLE_ENTITY
			) {
				return json({ error: 'order is not found' }, { status: status.HTTP_400_BAD_REQUEST });
			}
		}

		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error getting order');
	}
};

export const PUT: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};

export const DELETE: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};
