import type { PageServerLoad } from './$types';
import { get_order_list } from '$root/lib/utils/page/order';

export const load: PageServerLoad = async ({ fetch }) => {
	return {
		order_list: get_order_list(fetch)
	};
};
