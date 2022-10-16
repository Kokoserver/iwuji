import { API } from '$root/lib/interface/api.interface';

import { error } from '@sveltejs/kit';
import type { AuthorIn } from '$root/lib/interface/author.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';

export const get_authorData = async () => {
	const res = await api.get('/authors/2');
	if (res.status === status.HTTP_200_OK) {
		const author_data = res.data as AuthorIn;
		return author_data;
	}
};

export const get_authors = () => {
	api
		.get(`${API.author}?limit=1&offset=0`)
		.then((res) => {
			return res.data as AuthorIn[];
		})
		.catch((err) => {
			console.error(err);
		});
};

export const getAuthor = async (authorId: number) => {
	try {
		const res = await api.get(`${API.author}/${authorId}`);
		if (res.status === status.HTTP_200_OK) {
			return res.data as AuthorIn;
		}
		if (res.status === status.HTTP_404_NOT_FOUND) {
			throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
		}
	} catch (error) {
		console.table(error);
	}
};

export const updateAuthor = async (authorId: number, data: FormData) => {
	try {
		if (!authorId || data) throw error(status.HTTP_400_BAD_REQUEST, 'provide  a valid data');
		const res = await api.put(`${API.author}/${authorId}`, data, {
			'Content-type': 'multipart/form-data'
		});
		if (res.status === status.HTTP_200_OK) {
			return res.data as { message: string };
		}
		if (res.status === status.HTTP_404_NOT_FOUND) {
			throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
		}
	} catch (error) {
		console.table('Error updating author');
	}
};
export const deleteAuthor = async (authorId: number) => {
	try {
		const res = await api.delete(`${API.author}/${authorId}`);
		if (res.status === status.HTTP_204_NO_CONTENT) {
			return { message: 'item removed successfully' };
		}

		if (res.status === status.HTTP_404_NOT_FOUND) {
			throw error(status.HTTP_404_NOT_FOUND, 'author is not found');
		}
	} catch (error) {
		console.table('Error getting author');
	}
};
