import { get_order_list } from '../../../../lib/utils/page/order';

export const load = async () => {
	return {
		order_list: get_order_list()
	};
};
