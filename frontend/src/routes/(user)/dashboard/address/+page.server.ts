import type { PageServerLoad } from './$types';
import { get_addressList } from '../../../../lib/utils/page/address';

export const load: PageServerLoad = async () => {
	return {
		addressList: get_addressList()
	};
};
