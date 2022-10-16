import { error, json, redirect } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { clearCookies } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';

export const POST: RequestHandler = async (event) => {
	try {
		clearCookies(event);
		const userData = event.request.json();
		const res = await api.post('/users/auth/register', userData, {
			'Content-type': 'application/json'
		});
		if (res.status === status.HTTP_422_UNPROCESSABLE_ENTITY) {
			return json({ error: 'Invalid information was provided' });
		}
		if (res.status !== status.HTTP_200_OK) {
			const error = res.data as { detail: string | undefined };
			return json({ error: error.detail }, { status: status.HTTP_400_BAD_REQUEST });
		}

		return json({ ...res.data });
	} catch (err) {
		throw error(
			status.HTTP_500_INTERNAL_SERVER_ERROR,
			'error creating account, please try again later'
		);
	}
};
