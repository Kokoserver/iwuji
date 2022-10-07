import { browser } from '$app/environment';
import { Cart } from '$root/lib/store/toggleSeriesStore';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';

export const generate_payment_Link = async (orderId: number) => {
	const res = await fetch('/user/payment/api', {
		method: 'POST',
		body: JSON.stringify({ orderId })
	});
	const data = await res.json();
	if (data.status === status.HTTP_201_CREATED) {
		if (browser) {
			Cart.set([]);
			window.open(data.data.paymentLink, '_blank');
		}
	}

	if (data.status === status.HTTP_404_NOT_FOUND) {
		throw error(status.HTTP_404_NOT_FOUND, 'order does not exist');
	}

	throw (status.HTTP_400_BAD_REQUEST, 'Error creating order');
};
