import { error, redirect, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';

import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';

export const POST: RequestHandler = async ({ request }) => {
	const data = await request.json();
	const res = await api.post('/address/', data, {
		'Content-Type': 'application/json'
	});
	if (res.status === status.HTTP_201_CREATED) {
		return json({ message: 'address was created successfully' });
	}
	if (res.status === status.HTTP_400_BAD_REQUEST) {
		return json({ error: 'address with this details already exist' });
	}
	if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
		return json({ error: 'please provide a valid address details' });
	}
	return json({ error: 'error creating address' });
};

export const GET: RequestHandler = async () => {
	const res = await api.get('/address/');
	if (res.status === status.HTTP_200_OK) {
		return json({ address: res.data });
	}

	return json({ error: 'error getting address' });
};

export const PUT: RequestHandler = async ({ request }) => {
	const data = await request.json();

	const res = await api.put(`/address/${data.id}`, data, {
		'Content-Type': 'application/json'
	});
	if (res.status === status.HTTP_200_OK) {
		return json({ message: 'address was updated successfully' });
	}
	if (res.status === status.HTTP_400_BAD_REQUEST) {
		return json({ error: 'address with details already exist' });
	}
	if (res.status === status.HTTP_404_NOT_FOUND) {
		return json({
			error: 'address does not exist'
		});
	}
	if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
		return json({
			error: 'please provide a valid address details'
		});
	}
	return json({
		error: 'error updating address'
	});
};

export const DELETE: RequestHandler = async ({ request }) => {
	const data = await request.json();
	const res = await api.delete(`/address/${data.addressId ?? 23535}`);
	return json({ ...res });
};
