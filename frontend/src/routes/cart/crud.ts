import { goto } from '$app/navigation';

import type { CartIn, CartOut, CartUpdateOut } from '$root/lib/interface/cart.interface';
import { notification } from '$root/lib/notification';
import { Cart, CartType } from '$root/lib/store/toggleSeriesStore';
import { get } from 'svelte/store';

export const handleAddCart = async (data: CartOut) => {
	const res = await fetch('/cart/api', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	const res_data = await res.json();

	if (!res_data?.detail) {
		const all_cart = get(Cart);
		Cart.set([res_data, ...all_cart]);
		CartType.set({
			pdf: true,
			hard_back: false,
			paper_back: false,
			paper_back_qty: 0,
			hard_back_qty: 0
		});
	}
	if (res_data?.detail === 'Could not validate credentials')
		goto('/login?redirectTo=/books/' + data.productId);
};
export const handleUpdateCart = async (data: CartUpdateOut) => {
	const res = await fetch('/cart/api', {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	const res_data = await res.json();
	if (res_data?.detail) {
		notification.danger(String(res_data?.detail));
	}
};

export const get_total_price = (item: CartIn | CartIn[]) => {
	if (Array.isArray(item) && item.length > 0) {
		let total_price = 0;
		for (let index = 0; index < item.length; index++) {
			total_price =
				item[index].product.property.hard_back_price * item[index].hard_back_qty +
				item[index].product.property.paper_back_price * item[index].paper_back_qty;
			if (item[index].pdf) {
				total_price += item[index].product.property.pdf_price;
			}
			return total_price;
		}
	} else if (!Array.isArray(item)) {
		let total =
			item.product.property.hard_back_price * item.hard_back_qty +
			item.product.property.paper_back_price * item.paper_back_qty;
		if (item.pdf) {
			total += item.product.property.pdf_price;
		}
		return total;
	}
};

export const handleRemoveFromCart = async (id: number) => {
	const res = await fetch(`/cart/api?id=${id}`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json'
		}
	});
	const out_data = await res.json();
	if (out_data?.status === 'error') {
		notification.danger(String(out_data.message), 4000);
	}

	if (out_data?.status === 'success') {
		const all_cart = get(Cart);
		const updated_cart = all_cart.filter((item: CartIn) => item.id !== id);
		Cart.set(updated_cart);
		notification.success(out_data?.message, 4000);
	}
};
