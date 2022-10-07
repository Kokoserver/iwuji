import { API } from '$root/lib/interface/api.interface';
import type { ReviewIn } from '$root/lib/interface/ReviewIn.interface';

import api from '$root/lib/utils/api';
import { status as Status } from '$root/lib/utils/status';
import { writable } from 'svelte/store';

interface InitResponse {
	loading: boolean | false;
	data: ReviewIn[] | [];
	error: string | '';
}
interface IResponse {
	loading: boolean | false;
	data: ReviewIn | undefined;
	error: string | undefined;
}

function ReviewStore(initialState: InitResponse) {
	const { set, subscribe, update } = writable<InitResponse>(initialState);

	const get_Reviews = () => {
		const response = {} as InitResponse;
		response.loading = true;

		api
			.get(`${API.review}?limit=10&offset=0`)
			.then((res) => {
				response.data = res.data as ReviewIn[];
				response.loading = false;
				set(response);
			})
			.catch((err) => {
				response.loading = false;
				response.error = 'Error getting reviews';
				set(response);
				console.error(err);
			});
	};
	function initState() {
		if (initialState.data[0]) return;
		get_Reviews();
	}

	initState();
	const getReview = async (reviewId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const check_product = initialState.data.find((review) => review.id === reviewId);
			if (check_product) {
				response.loading = false;
				return check_product;
			}
			const { data, status } = await api.get(`${API.review}/${reviewId}`);
			if (status === Status.HTTP_200_OK) {
				response.data = data as ReviewIn;
				response.loading = false;
				return response;
			}
			if (status === Status.HTTP_404_NOT_FOUND) {
				response.error = 'Review is not found';
			}
			response.loading = false;
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting review';
			return response;
		}
	};

	const updateReview = async (reviewId: number, data: FormData) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			if (!reviewId || data) {
				response.loading = false;
				response.error = 'provide  a valid data';
				return response;
			}
			const { status } = await api.put(`${API.review}/${reviewId}`, data, {
				'Content-type': 'application/json'
			});
			if (status === Status.HTTP_200_OK) {
				const { data, status } = await api.get(`${API.review}/${reviewId}`);
				if (status === Status.HTTP_200_OK) {
					const updated_state: ReviewIn[] = initialState.data.map((review) => {
						if (review.id === reviewId) {
							review = data as ReviewIn;
							return review;
						}
						return review;
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
				response.error = 'Review is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error updating review';
			return response;
		}
	};
	const deleteReview = async (reviewId: number) => {
		const response = {} as IResponse;
		response.loading = true;
		try {
			const { status } = await api.delete(`${API.review}/${reviewId}`);
			if (status === Status.HTTP_204_NO_CONTENT) {
				update((defaultState) => {
					const Updated_response = {} as InitResponse;
					Updated_response.data = defaultState.data.filter(
						(review: ReviewIn) => review.id !== reviewId
					);
					return Updated_response;
				});
			}

			if (status === Status.HTTP_404_NOT_FOUND) {
				response.loading = false;
				response.error = 'Review is not found';
			}
			return response;
		} catch (error) {
			response.loading = false;
			response.error = 'Error getting review';
			return response;
		}
	};

	return {
		get_Reviews,
		getReview,
		updateReview,
		deleteReview,
		subscribe
	};
}

export const reviewStore = ReviewStore({ loading: false, error: '', data: [] });
