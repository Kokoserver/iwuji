import { API } from '$root/lib/interface/api.interface';
import type { VariationIn } from '$root/lib/interface/variation.interface';

import api from '$root/lib/utils/api';
import { status as Status } from '$root/lib/utils/status';
import { writable } from 'svelte/store';
interface InitResponse {
	loading: boolean | false;
	data: VariationIn[] | [];
	error: string | '';
}
interface IResponse {
	loading: boolean | false;
	data: VariationIn | undefined;
	error: string | undefined;
}

function VariationStore(initialState: InitResponse) {
	const { set, subscribe, update } = writable<InitResponse>(initialState);

	const getVariations = () => {
		const response = {} as InitResponse;
		response.loading = true;

		api
			.get(`${API.variation}?limit=10&offset=0`)
			.then((res) => {
				response.data = res.data as VariationIn[];
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

	const filterVariations = async (
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
				`${API.variation}?limit=${limit}&${
					filter && `&filter=${filter}`
				}&offset=${offset}&is_series=${is_series}&is_assigned=${is_assigned}&is_active=${is_active}`
			);
			response.data = res.data as VariationIn[];
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting series';
			console.error(error);
			return response;
		}
	};

	const getProduct = async (variationId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const check_product = initialState.data.find((variation) => variation.id === variationId);
			if (check_product) {
				response.loading = false;
				return check_product;
			}
			const { data, status } = await api.get(`${API.variation}/${variationId}`);
			if (status === Status.HTTP_200_OK) {
				response.data = data as VariationIn;
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'series is not found';
			}
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting series';
			return response;
		}
	};

	const updateProduct = async (variationId: number, data: FormData) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			if (!variationId || data) {
				response.loading = false;
				response.error = 'provide  a valid data';
				return response;
			}
			const { status } = await api.put(`${API.variation}/${variationId}`, data, {
				'Content-type': 'multipart/form-data'
			});
			if (status === Status.HTTP_200_OK) {
				const { data, status } = await api.get(`${API.variation}/${variationId}`);
				if (status === Status.HTTP_200_OK) {
					const updated_state: VariationIn[] = initialState.data.map((variation) => {
						if (variation.id === variationId) {
							variation = data as VariationIn;
							return variation;
						}
						return variation;
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
				response.error = 'series is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error updating series';
			return response;
		}
	};
	const deleteProduct = async (variationId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const { status } = await api.delete(`${API.variation}/${variationId}`);
			if (status === Status.HTTP_204_NO_CONTENT) {
				update((defaultState) => {
					const Updated_response = {} as InitResponse;
					Updated_response.data = defaultState.data.filter(
						(variation: VariationIn) => variation.id !== variationId
					);
					return Updated_response;
				});
			}

			if (status === Status.HTTP_404_NOT_FOUND) {
				response.loading = false;
				response.error = 'series is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting series';
			return response;
		}
	};
	function initState() {
		if (initialState.loading || initialState.error) return;
		getVariations();
	}

	initState();
	return {
		set,
		getVariations,
		filterVariations,
		getProduct,
		updateProduct,
		deleteProduct,
		subscribe
	};
}

export const variationStore = VariationStore({ loading: false, error: '', data: [] });
