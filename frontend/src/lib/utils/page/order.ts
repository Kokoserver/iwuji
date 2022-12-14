import { goto } from '$app/navigation';
import type { OrderDetailsIn } from '$root/lib/interface/order.interface';
import { notification } from '$root/lib/notification';
import { Loading } from '$root/store/modalStore';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';
import { generate_payment_Link } from './payment';

export const create_order = async (addressId: number) => {
	Loading.set(true);
	const res = await fetch('/api/user/order', {
		method: 'POST',
		body: JSON.stringify({ addressId })
	});

	const data = await res.json();
	if (data.status === status.HTTP_201_CREATED) {
		const payment_link = await generate_payment_Link(data.data.orderId);
		return payment_link;
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

export const get_order_list = async (Fetch: typeof fetch) => {
	const res = await Fetch('/api/user/order');
	const data = (await res.json()) as OrderDetailsIn[];
	return data;
};

export const get_order = async (id: number, Fetch: typeof fetch) => {
	const res = await Fetch(`/api/user/order/?id=${id}`);
	const data = (await res.json()) as OrderDetailsIn;
	return data;
};
