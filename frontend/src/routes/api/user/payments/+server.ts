import { error, json, redirect } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { get_token } from '$root/lib/utils/setAuthorization';

export const POST: RequestHandler = async ({ request }) => {
	const data = await request.json();
	const res = await api.post('/payments/verify', data, {
		'Content-Type': 'application/json'
	});
	return json({ ...res });
};

export const GET: RequestHandler = async (event) => {
	try {
		const paymentId = event.url.searchParams.get('id');
		let url = null;
		if (paymentId) {
			url = `/payments/${paymentId}`;
		} else {
			url = '/payments/';
		}

		const res = await api.get(url, {
			...(await get_token(event))
		});
		if (paymentId) {
			if (res.status === status.HTTP_404_NOT_FOUND || res.status === status.HTTP_400_BAD_REQUEST) {
				throw error(status.HTTP_400_BAD_REQUEST, 'payment is not found');
			}
		}
		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error getting address');
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
