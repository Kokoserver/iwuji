import { error } from '@sveltejs/kit';
import api from '$root/lib/utils/api';

import type { PageServerLoad } from './$types';
import type { MessageIn } from '$root/lib/interface/message.interface';
import { deleteCookiesData } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';

export const load: PageServerLoad = async (event) => {
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');

	const res = await api.post(
		'/users/account/activate',
		{
			token: event.params.activateToken
		},
		{
			'Content-Type': 'application/json'
		}
	);
	if (res.status !== 200) {
		const error_message = res.data as { detail: string | 'Error activating account' };
		throw error(res.status ?? status.HTTP_400_BAD_REQUEST, String(error_message.detail));
	}
	return res.data as MessageIn;
};
