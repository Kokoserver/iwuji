import { browser } from '$app/environment';
import { Cart } from '$root/store/toggleSeriesStore';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';

import type { PaymentIn } from '$root/lib/interface/payment.interface';

export const generate_payment_Link = async (orderId: number) => {
	const res = await fetch('/api/user/payments/?signal=create', {
		method: 'POST',
		body: JSON.stringify({ orderId })
	});
	const data = await res.json();
	if (data.status === status.HTTP_201_CREATED) {
		if (browser) {
			Cart.set([]);
			return data.data.paymentLink;
		}
	}

	if (data.status === status.HTTP_404_NOT_FOUND) {
		throw error(status.HTTP_404_NOT_FOUND, 'order does not exist');
	}

	throw (status.HTTP_400_BAD_REQUEST, 'Error creating order');
};

export const get_payment_list = async (Fetch: typeof fetch) => {
	const res = await Fetch('/api/user/payments');
	if (res.status === status.HTTP_200_OK) {
		return (await res.json()) as PaymentIn[] | [];
	}
};
