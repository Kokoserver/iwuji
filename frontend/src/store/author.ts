import { API } from '$root/lib/interface/api.interface';
import type { AuthorIn } from '$root/lib/interface/author.interface';

import api from '$root/lib/utils/api';
import { status as Status } from '$root/lib/utils/status';
import { writable } from 'svelte/store';
interface InitResponse {
	loading: boolean | false;
	data: AuthorIn[] | [];
	error: string | '';
}
interface IResponse {
	loading: boolean | false;
	data: AuthorIn | undefined;
	error: string | undefined;
}

function AuthorStore(initialState: InitResponse) {
	const { set, subscribe, update } = writable<InitResponse>(initialState);

	const get_authors = () => {
		const response = {} as InitResponse;
		response.loading = true;

		api
			.get(`${API.author}?limit=1&offset=0`)
			.then((res) => {
				response.data = res.data as AuthorIn[];
				response.loading = false;
				set(response);
			})
			.catch((err) => {
				response.loading = false;
				response.error = 'Error getting author';
				set(response);
				console.error(err);
			});
	};

	function initState() {
		if (initialState.data[0]) return;
		get_authors();
	}

	initState();

	const getAuthor = async (authorId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const check_product = initialState.data.find((author) => author.id === authorId);
			if (check_product) {
				response.loading = false;
				return check_product;
			}
			const { data, status } = await api.get(`${API.author}/${authorId}`);
			if (status === Status.HTTP_200_OK) {
				response.data = data as AuthorIn;
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'author is not found';
			}
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting author';
			return response;
		}
	};

	const updateAuthor = async (authorId: number, data: FormData) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			if (!authorId || data) {
				response.loading = false;
				response.error = 'provide  a valid data';
				return response;
			}
			const { status } = await api.put(`${API.author}/${authorId}`, data, {
				'Content-type': 'multipart/form-data'
			});
			if (status === Status.HTTP_200_OK) {
				const { data, status } = await api.get(`${API.author}/${authorId}`);
				if (status === Status.HTTP_200_OK) {
					const updated_state: AuthorIn[] = initialState.data.map((author) => {
						if (author.id === authorId) {
							author = data as AuthorIn;
							return author;
						}
						return author;
					});
					const defaultState = {} as InitResponse;
					defaultState.data = updated_state;
					defaultState.error = '';
					defaultState.loading = false;
					set(defaultState);
				}
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'author is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error updating author';
			return response;
		}
	};
	const deleteAuthor = async (authorId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const { status } = await api.delete(`${API.author}/${authorId}`);
			if (status === Status.HTTP_204_NO_CONTENT) {
				update((defaultState) => {
					const Updated_response = {} as InitResponse;
					Updated_response.data = defaultState.data.filter(
						(author: AuthorIn) => author.id !== authorId
					);
					return Updated_response;
				});
			}

			if (status === Status.HTTP_404_NOT_FOUND) {
				response.loading = false;
				response.error = 'author is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting author';
			return response;
		}
	};

	return {
		get_authors,
		getAuthor,
		updateAuthor,
		deleteAuthor,
		subscribe
	};
}

export const authorStore = AuthorStore({ loading: false, error: '', data: [] });
