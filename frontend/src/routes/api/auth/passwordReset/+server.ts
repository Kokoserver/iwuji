import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { get_jwt_data } from '$root/lib/utils/get_token_data';
import dayjs from 'dayjs';
import { clearCookies } from '$root/lib/utils/getCookies';

export const POST: RequestHandler = async (event) => {
	try {
		clearCookies(event);
		const userData = await event.request.json();
		const token_data = get_jwt_data(userData.token);
		const isExpire: boolean = dayjs.unix(token_data.exp).diff(dayjs()) < 1;
		if (isExpire) throw error(status.HTTP_400_BAD_REQUEST, 'link already expire');
		const res = await api.put('/users/', userData, {
			'Content-type': 'application/json'
		});
		if (res.status !== status.HTTP_200_OK) {
			const error_message = res.data as { detail: string | undefined };

			return json({ error: error_message.detail }, { status: status.HTTP_400_BAD_REQUEST });
		}
		return json(res.data);
	} catch (err) {
		throw error(status.WS_1011_INTERNAL_ERROR, 'Error resetting password please try again');
	}
};
