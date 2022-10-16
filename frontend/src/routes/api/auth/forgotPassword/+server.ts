import { error, json, type RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { clearCookies } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';

export const POST: RequestHandler = async (event) => {
	try {
		clearCookies(event);
		const userData = await event.request.json();
		const res = await api.post('/users/passwordResetLink', userData, {
			'Content-type': 'application/json'
		});

		if (res.status !== status.HTTP_200_OK) {
			return json({ error: 'Error resetting password' }, { status: res.status });
		}
		return json({ ...res.data });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error resetting password');
	}
};
