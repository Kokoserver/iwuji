import type { CartIn, CartOut, CartUpdateOut } from '$root/lib/interface/cart.interface';
import { notification } from '$root/lib/notification';
import { Cart, CartType } from '$root/store/toggleSeriesStore';
import { get } from 'svelte/store';

export const handleAddCart = async (data: CartOut) => {
	const res = await fetch('/api/cart', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	const res_data = await res.json();
	if (!res.ok) {
		if (Array.isArray(res_data.detail)) {
			notification.danger(res_data.detail.toString());
		}
		notification.danger(res_data.error);
	}

	const all_cart = get(Cart);
	console.log(all_cart);

	Cart.set([res_data, ...all_cart]);
	CartType.set({
		pdf: true,
		hard_back: false,
		paper_back: false,
		paper_back_qty: 0,
		hard_back_qty: 0
	});
};

export const handleUpdateCart = async (data: CartUpdateOut) => {
	const res = await fetch('/api/cart', {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	const res_data = await res.json();
	if (!res.ok) {
		if (Array.isArray(res_data.detail)) {
			notification.danger(res_data.detail.toString());
		}
		notification.danger(res_data.error);
	}
};

export const get_total_price = (item: CartIn | CartIn[]) => {
	if (!Array.isArray(item)) {
		let total =
			item.product.property.hard_back_price * item.hard_back_qty +
			item.product.property.paper_back_price * item.paper_back_qty;
		if (item.pdf) {
			total += item.product.property.pdf_price;
		}
		return total;
	} else if (Array.isArray(item)) {
		let total_price = 0;
		for (let index = 0; index < item.length; index++) {
			total_price +=
				item[index].product.property.hard_back_price * item[index].hard_back_qty +
				item[index].product.property.paper_back_price * item[index].paper_back_qty;
			if (item[index].pdf) {
				total_price += item[index].product.property.pdf_price;
			}
		}
		return total_price;
	}
	return 0;
};

export const handleRemoveFromCart = async (id: number) => {
	const res = await fetch(`/api/cart/?id=${id}`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json'
		}
	});
	const res_data = await res.json();

	if (!res.ok) {
		if (Array.isArray(res_data.detail)) {
			notification.danger(res_data.detail.toString());
		}
		notification.danger(res_data.error);
	}

	if (res.ok) {
		const all_cart = get(Cart);
		const updated_cart = all_cart.filter((item: CartIn) => item.id !== id);
		Cart.set(updated_cart);
	}
};

export const getCart = async (id: number) => {
	const all_cart = get(Cart);
	const get_cart = all_cart.filter((item: CartIn) => item.id === id);
	if (get_cart) {
		return get_cart[0];
	}
	const res = await fetch(`/api/cart/?signal=single&id=${id}`, {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (!res.ok) {
		notification.danger('Error getting user carts');
	}
	const res_data = await res.json();
	if (res.ok) {
		return res_data as CartIn;
	}
};

export const getCarts = async (Fetch: typeof fetch) => {
	const res = await Fetch(`/api/cart/`);
	const res_data = await res.json();
	if (!res.ok) {
		notification.danger('Error getting user carts');
	}

	if (res.ok) {
		if (Array.isArray(res_data)) {
			Cart.set(res_data);
			return res_data as CartIn[];
		}
	}
};
