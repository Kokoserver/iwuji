import { get_order_list } from './crud';

export const load = async () => {
	return {
		order_list: get_order_list()
	};
};
