import type { PageServerLoad } from './$types';
import { get_payment_list } from '../../../../lib/utils/page/payment';

export const load: PageServerLoad = async () => {
	return {
		payment_list: get_payment_list()
	};
};
