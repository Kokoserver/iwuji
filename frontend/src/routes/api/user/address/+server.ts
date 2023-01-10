import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';

import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { get_token } from '$root/lib/utils/setAuthorization';

export const POST: RequestHandler = async (event) => {
	try {
		const data = await event.request.json();
		const res = await api.post('/address/', data, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});
		if (res.status === status.HTTP_400_BAD_REQUEST) {
			return json({ error: 'address with this details already exist' }, { status: res.status });
		}
		if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
			return json({ error: 'please provide a valid address details' }, { status: res.status });
		}
		return json({ message: 'Address was created successfully' });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'error creating address');
	}
};

export const GET: RequestHandler = async (event) => {
	try {
		const addressId = event.url.searchParams.get('id');
		let url = null;
		if (addressId) {
			url = `/address/${addressId}`;
		} else {
			url = '/address/';
		}

		const res = await api.get(url, {
			...(await get_token(event))
		});
		if (addressId) {
			if (res.status === status.HTTP_404_NOT_FOUND || res.status === status.HTTP_400_BAD_REQUEST) {
				return json({ error: 'address is not found' }, { status: status.HTTP_400_BAD_REQUEST });
			}
		}
		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error getting address');
	}
};

export const PUT: RequestHandler = async (event) => {
	try {
		const data = await event.request.json();
		const res = await api.put(`/address/${data.id}`, data, {
			'Content-Type': 'application/json',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_400_BAD_REQUEST) {
			return json({ error: 'address with details already exist' }, { status: res.status });
		}
		if (res.status === status.HTTP_404_NOT_FOUND) {
			return json({ error: 'address does not exist' }, { status: res.status });
		}
		if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
			return json({ error: 'please provide a valid address details' }, { status: res.status });
		}
		return json({ message: 'address was updated successfully' });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error updating address');
	}
};

export const DELETE: RequestHandler = async (event) => {
	try {
		const data = await event.request.json();
		const res = await api.delete(`/address/${data.addressId ?? 23535}`, {
			...(await get_token(event))
		});
		if (res.status === status.HTTP_404_NOT_FOUND) {
			return json(
				{ error: 'Address with details is not found ' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		if (res.status === status.HTTP_400_BAD_REQUEST) {
			return json(
				{ error: 'you can not delete address that is in use' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		return json({}, { status: status.HTTP_200_OK });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error deleting address');
	}
};
