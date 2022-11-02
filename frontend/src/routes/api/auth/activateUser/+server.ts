import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';

import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { clearCookies } from '$root/lib/utils/getCookies';

export const POST: RequestHandler = async (event) => {
	try {
		clearCookies(event);
		const tokenData = event.request.json();
		const res = await api.post('/users/account/activate', tokenData, {
			'Content-Type': 'application/json'
		});
		if (res.status !== 200) {
			return json(
				{ error: 'token expire' },
				{
					status: status.HTTP_400_BAD_REQUEST
				}
			);
		}
		return json({ message: 'account was activated successfully' });
	} catch (err) {
		throw error(
			status.HTTP_500_INTERNAL_SERVER_ERROR,
			'Error activating account, please try again'
		);
	}
};
