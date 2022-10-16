import { goto } from '$app/navigation';
import type { OrderDetailsIn } from '$root/lib/interface/order.interface';
import { notification } from '$root/lib/notification';
import { Loading } from '$root/store/modalStore';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';
import { generate_payment_Link } from './payment';

export const create_order = async (addressId: number) => {
	Loading.set(true);
	const res = await fetch('/order/api', {
		method: 'POST',
		body: JSON.stringify({ addressId })
	});

	const data = await res.json();
	if (data.status === status.HTTP_201_CREATED) {
		await generate_payment_Link(data.data.orderId);
		await goto('/');
	}
	if (data.status === status.HTTP_404_NOT_FOUND) {
		notification.danger('address details that was provided does not exist');
		await goto('/');
	}

	if (data.status === status.HTTP_400_BAD_REQUEST) {
		if (Array.isArray(data.data)) {
			const details = [...data.data.details];
			for (let err = 0; err < details.length; err++) {
				notification.info(details[err]);
			}
			await goto('/');
		}

		notification.info(data.data.details);
		await goto('/');
	}
	throw error(status.HTTP_400_BAD_REQUEST, 'Error creating order');
};

export const get_order_list = async () => {
	const res = await api.get('/orders/');
	if (res.status === status.HTTP_200_OK) return res.data as OrderDetailsIn[];
	return [];
};
