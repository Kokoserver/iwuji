import type { CartIn } from '$root/lib/interface/cart.interface';
import api from '$root/lib/utils/api';

import type { PageLoad } from './$types';

export const load: PageLoad = async () => {
	const data_out = { carts: [] } as { carts: CartIn[] };
	const res = await api.get('/carts/');
	data_out.carts = res.data as CartIn[];
	return data_out;
};
