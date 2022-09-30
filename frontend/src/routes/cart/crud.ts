import type { CartOut } from "$root/lib/interface/cart.interface";

export const handleDeleteItem = async (id: number) => {
	await fetch(`/cart/api?id=${id}`);
};

export const handleAddCart = async (data: CartOut) => {
	const res = await fetch('/cart/api', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	console.log(await res.json());
};

