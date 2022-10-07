import type { PageServerLoad } from '../../../.svelte-kit/types/src/routes/bio/$types';
import { get_authorData } from './crud';
import { get_ProductList } from '../books/crud';

export const load: PageServerLoad = async () => {
	return {
		products: get_ProductList('', 3, 0, false, false, true),
		author: get_authorData()
	};
};
