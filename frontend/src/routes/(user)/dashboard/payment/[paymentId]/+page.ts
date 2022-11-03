import { Loading } from '$root/store/modalStore';
import { status } from '$root/lib/utils/status';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ url, fetch }) => {
	Loading.set(true);
	try {
		const tx_ref = String(url.searchParams.get('tx_ref'));
		if (tx_ref.slice(0, 3) === 'IW-' || tx_ref.slice(0, 3) === 'iw-') {
			const res = await fetch('/api/user/payments/?signal=verify', {
				method: 'POST',
				body: JSON.stringify({ tx_ref })
			});

			if (res.ok) {
				return {
					success: true
				};
			}
			return {
				success: false
			};
		}
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error validating payment');
	}
};
