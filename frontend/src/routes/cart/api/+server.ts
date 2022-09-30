import type { CartOut } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const data: CartOut = await request.json();

	const res = await api.post('/carts/', data, {
		'Content-Type': 'application/json'
	});

	//    const out_data = {} as {detail?:string, message?:string}
	if (
		res.status !== status.HTTP_200_OK &&
		Number(res.status) < status.HTTP_500_INTERNAL_SERVER_ERROR
	) {
		console.log(res.data);

		// out_data.detail = res.data as { detail: string };
		return json(data);
	}
	return json(res.data);
};
export const GET: RequestHandler = async () => {
	const res = await api.get('/carts/', {
		'Content-Type': 'application/json'
	});

	//    const out_data = {} as {detail?:string, message?:string}
	if (res.status !== status.HTTP_200_OK) {
		console.log(res.data);

		// out_data.detail = res.data as { detail: string };
		return json(res.data);
	}
	return json(res.data);
};
export const PUT: RequestHandler = async ({ request }) => {
	const data: CartOut = await request.json();

	const res = await api.put('/carts/', data, {
		'Content-Type': 'application/json'
	});

	//    const out_data = {} as {detail?:string, message?:string}
	if (res.status !== status.HTTP_200_OK) {
		console.log(res.data);

		// out_data.detail = res.data as { detail: string };
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

	//    const out_data = {} as {detail?:string, message?:string}
	if (res.status !== status.HTTP_200_OK) {
		console.log(res.data);

		// out_data.detail = res.data as { detail: string };
		// return json(data);
	}
	return json(res.data);
};
