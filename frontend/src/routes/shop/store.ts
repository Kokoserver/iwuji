import { API } from '$root/lib/interface/api.interface';
import type { CartIn } from '$root/lib/interface/cart.interface';

import api from '$root/lib/utils/api';
import { status as Status } from '$root/lib/utils/status';
import { writable } from 'svelte/store';
export interface InitResponse {
	loading: boolean | false;
	data: CartIn[];
	error: string | '';
}
export interface IResponse {
	loading: boolean | false;
	data: CartIn | undefined;
	error: string | undefined;
}

function CartStore(initialState: InitResponse) {
	const { set, subscribe, update } = writable<InitResponse>(initialState);
	subscribe((currentValue) => (initialState = currentValue));

	const __getInCarts = () => {
		const response = {} as InitResponse;
		response.loading = true;

		api
			.get(`${API.cart}`)
			.then((res) => {
				response.data = res.data as CartIn[];
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

	function initState() {
		if (initialState.loading || initialState.error) return;
		__getInCarts();
	}

	initState();

	const getCarts = async (cartId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const check_product = initialState.data.find((item) => item.id === cartId);
			if (check_product) {
				response.loading = false;
				return check_product;
			}
			const { data, status } = await api.get(`${API.cart}${cartId}`);
			if (status === Status.HTTP_200_OK) {
				response.data = data as CartIn;
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'item is not found';
			}
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting item';
			return response;
		}
	};

	const updateCart = async (cartId: number, data: CartIn) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			if (!cartId || data) {
				response.loading = false;
				response.error = 'provide  a valid data';
				return response;
			}
			const { status } = await api.put(`${API.cart}/${cartId}`, data, {
				'Content-type': 'application/json'
			});
			if (status === Status.HTTP_200_OK) {
				const { data, status } = await api.get(`${API.cart}/${cartId}`);
				if (status === Status.HTTP_200_OK) {
					const updated_state: CartIn[] = initialState.data.map((item) => {
						if (item.id === cartId) {
							item = data as CartIn;
							return item;
						}
						return item;
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
				response.error = 'item is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error updating item';
			return response;
		}
	};
	const deleteCart = async (cartId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const { status } = await api.delete(`${API.cart}/${cartId}`);
			if (status === Status.HTTP_204_NO_CONTENT) {
				update((defaultState) => {
					const Updated_response = {} as InitResponse;
					Updated_response.data = defaultState.data.filter((item: CartIn) => item.id !== cartId);
					return Updated_response;
				});
			}

			if (status === Status.HTTP_404_NOT_FOUND) {
				response.loading = false;
				response.error = 'item is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting item';
			return response;
		}
	};

	return {
		getCarts,
		updateCart,
		deleteCart,
		subscribe
	};
}

export const cartStore = CartStore({ loading: false, error: '', data: [] });
