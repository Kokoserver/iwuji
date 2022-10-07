import type { PageServerLoad } from './$types';
import { get_addressList } from './crud';

export const load: PageServerLoad = async () => {
	return {
		addressList: get_addressList()
	};
};
