import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import { API } from '$root/lib/interface/api.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { get_token } from '$root/lib/utils/setAuthorization';

export const POST: RequestHandler = async (event) => {
	try {
		const data = await event.request.formData();
		if (!data) throw error(status.HTTP_400_BAD_REQUEST, 'provide a valid data');
		const res = await api.post(`${API.author}`, data, {
			'Content-type': 'multipart/form-data',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_400_BAD_REQUEST) {
			throw json(
				{ error: 'author with this details already exist' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
			throw json(
				{ error: 'Invalid author details provided' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error updating author');
	}
};

export const GET: RequestHandler = async ({ url }) => {
	try {
		const signal = url.searchParams.get('signal') as 'single' | 'all';
		const limit = url.searchParams.get('limit') || 10;
		const filter = url.searchParams.get('filter') || '';
		const offset = url.searchParams.get('offset') || 0;

		let endpoint = null;
		if (signal === 'single') {
			const authorId = url.searchParams.get('authorId') || null;
			if (!authorId) throw error(status.HTTP_400_BAD_REQUEST, 'Author Id is not specified');
			endpoint = `/authors/${authorId}`;
		} else {
			endpoint = `${API.author}/?limit=${limit}&offset=${offset}${
				filter ? `&filter=${filter}` : ''
			}`;
		}

		const res = await api.get(endpoint);
		if (signal === 'single') {
			if (res.status !== status.HTTP_200_OK) {
				throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
			}
			return json(res.data);
		}

		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error');
	}
};

export const PUT: RequestHandler = async (event) => {
	try {
		const data = await event.request.formData();
		const authorId = data.get('authorId') || null;
		if (!authorId || data) throw error(status.HTTP_400_BAD_REQUEST, 'provide a valid data');
		const res = await api.put(`${API.author}/${authorId}`, data, {
			'Content-type': 'multipart/form-data',
			...(await get_token(event))
		});

		if (res.status === status.HTTP_404_NOT_FOUND) {
			throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
		}
		if (res.status === status.HTTP_400_BAD_REQUEST) {
			throw json(
				{ error: 'author with this details already exist' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
			throw json(
				{ error: 'Invalid author details provided' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}
		return json(res.data);
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error updating author');
	}
};

export const DELETE: RequestHandler = async (event) => {
	try {
		const authorId = event.url.searchParams.get('authorId') || null;

		if (!authorId) throw error(status.HTTP_400_BAD_REQUEST, 'provide  a valid author id');
		const res = await api.delete(`${API.author}/${authorId}`, {
			...get_token(event)
		});
		if (
			res.status === status.HTTP_400_BAD_REQUEST ||
			res.status === status.HTTP_422_UNPROCESSABLE_ENTITY
		) {
			return json(
				{ error: 'Invalid author details provided' },
				{ status: status.HTTP_400_BAD_REQUEST }
			);
		}

		if (res.status === status.HTTP_404_NOT_FOUND) {
			throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
		}
		return json({ message: 'Author removed successfully' });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error getting author');
	}
};
