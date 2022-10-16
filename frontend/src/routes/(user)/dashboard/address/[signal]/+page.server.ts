import { get_address } from '../../../../../lib/utils/page/address';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, url }) => {
	const { signal } = params;
	const id = url.searchParams.get('id');
	const redirectTo = url.searchParams.get('redirectTo');
	return {
		address: signal === 'edit' && id ? get_address(Number(id)) : undefined,
		signal,
		redirectTo
	};
};
