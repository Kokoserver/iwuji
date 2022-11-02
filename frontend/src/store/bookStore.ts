import { API } from '$root/lib/interface/api.interface';
import type { ProductIn } from '$root/lib/interface/product.interface';
import api from '$root/lib/utils/api';
import { status as Status } from '$root/lib/utils/status';
import { writable } from 'svelte/store';

interface InitResponse {
	loading: boolean | false;
	data: ProductIn[] | [];
	error: string | '';
}
interface IResponse {
	loading: boolean | false;
	data: ProductIn | undefined;
	error: string | undefined;
}

function ProductStore(initialState: InitResponse) {
	const { set, subscribe, update } = writable<InitResponse>(initialState);

	const getProducts = () => {
		const response = {} as InitResponse;
		response.loading = true;

		api
			.get(`${API.product}?limit=10&offset=0&is_series=false&is_assigned=false&is_active=true`)
			.then((res) => {
				response.data = res.data as ProductIn[];
				response.loading = false;
				set(response);
			})
			.catch((err) => {
				response.loading = false;
				response.error = 'Error getting books';
				set(response);
				console.error(err);
			});
	};

	const filterProducts = async (
		limit = 10,
		offset = 0,
		filter = '',
		is_series = false,
		is_assigned = false,
		is_active = true
	) => {
		const response = {} as InitResponse;
		response.loading = true;
		try {
			const res = await api.get(
				`${API.product}?limit=${limit}&${
					filter && `&filter=${filter}`
				}&offset=${offset}&is_series=${is_series}&is_assigned=${is_assigned}&is_active=${is_active}`
			);
			response.data = res.data as ProductIn[];
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting books';
			console.error(error);
			return response;
		}
	};

	const getProduct = async (productId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const check_product = initialState.data.find((product) => product.id === productId);
			if (check_product) {
				response.loading = false;
				return check_product;
			}
			const { data, status } = await api.get(`${API.product}${productId}`);
			if (status === Status.HTTP_200_OK) {
				response.data = data as ProductIn;
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'Book is not found';
			}
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting book';
			return response;
		}
	};

	const updateProduct = async (productId: number, data: FormData) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			if (!productId || data) {
				response.loading = false;
				response.error = 'provide  a valid data';
				return response;
			}
			const { status } = await api.put(`${API.product}/${productId}`, data, {
				'Content-type': 'multipart/form-data'
			});
			if (status === Status.HTTP_200_OK) {
				const { data, status } = await api.get(`${API.product}/${productId}`);
				if (status === Status.HTTP_200_OK) {
					const updated_state: ProductIn[] = initialState.data.map((product) => {
						if (product.id === productId) {
							product = data as ProductIn;
							return product;
						}
						return product;
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
				response.error = 'Book is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error updating book';
			return response;
		}
	};
	const deleteProduct = async (productId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const { status } = await api.delete(`${API.product}/${productId}`);
			if (status === Status.HTTP_204_NO_CONTENT) {
				update((defaultState) => {
					const Updated_response = {} as InitResponse;
					Updated_response.data = defaultState.data.filter(
						(product: ProductIn) => product.id !== productId
					);
					return Updated_response;
				});
			}

			if (status === Status.HTTP_404_NOT_FOUND) {
				response.loading = false;
				response.error = 'Book is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting book';
			return response;
		}
	};
	function initState() {
		if (initialState.error || initialState.loading) return;
		getProducts();
	}

	initState();
	return {
		set,
		filterProducts,
		getProduct,
		getProducts,
		updateProduct,
		deleteProduct,
		subscribe
	};
}

export const productStore = ProductStore({ loading: false, error: '', data: [] });
