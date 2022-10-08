import { Loading } from '$root/lib/store/modalStore';
import { Cart } from '$root/lib/store/toggleSeriesStore';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ url }) => {
	Loading.set(true);
	const tx_ref = String(url.searchParams.get('tx_ref'));

	if (tx_ref.slice(0, 3) === 'IW-' || tx_ref.slice(0, 3) === 'iw-') {
		const verify_payment = async () => {
			const res = await api.post(
				'/payments/verify',
				{ tx_ref },
				{
					'Content-Type': 'application/json'
				}
			);
			if (res.status === status.HTTP_200_OK) {
				Cart.set([]);
				Loading.set(false);
				return;
			}

			if (res.status === status.HTTP_404_NOT_FOUND) {
				Loading.set(false);
				throw error(
					status.HTTP_404_NOT_FOUND,
					'order does not exist, kindly check your dashboard and try again'
				);
			}

			if (res.status === status.HTTP_402_PAYMENT_REQUIRED) {
				Loading.set(false);
				return;
			}
			Loading.set(false);
			throw error(status.HTTP_400_BAD_REQUEST, 'payment verification failed');
		};
		return {
			status: verify_payment()
		};
	}
	Loading.set(false);
	throw error(status.HTTP_400_BAD_REQUEST, 'invalid data was provided');
};
