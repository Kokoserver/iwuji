import { error, json, redirect } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import { setCookies } from '$root/lib/utils/getCookies';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import type { TokenDataIn, UserDataIn } from '$root/lib/interface/user.interface';
import type { UserLoginInput } from '$root/lib/interface/auth.interface';
import { get_token } from '$root/lib/utils/setAuthorization';

export const POST: RequestHandler = async (event) => {
	
	try {
		const userData = (await event.request.json()) as UserLoginInput;
		const res = await api.post(
			'/auth/login',
			`grant_type=&username=${userData.username}&password=${userData.password}&scope=&client_id=&client_secret=`,
			{
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		);

		if (res.status !== status.HTTP_200_OK) {
			const error = res.data as { detail: string | undefined };
			return json({ error: error.detail }, { status: res.status });
		}

		const token: TokenDataIn = res.data as TokenDataIn;
		setCookies(token.refresh_token, token, 'session', event.cookies);
		event.locals.token = token;
		const user = await api.get('/users/whoami', {
			...(await get_token(event))
		});
		const user_data = user.data as UserDataIn;
		setCookies(token.refresh_token, user_data, 'details', event.cookies);
		setCookies(token.refresh_token, { is_login: true }, 'is_login', event.cookies);
		event.locals.is_login = true;
		if (event.url.searchParams.get('redirectTo')) {
			const location = String(event.url.searchParams.get('redirectTo'));
			throw redirect(status.HTTP_301_MOVED_PERMANENTLY, location);
		}
		return json({}, { status: status.HTTP_200_OK });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'error login is user');
	}
};
