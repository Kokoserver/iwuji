import type { TokenDataIn, UserDataIn } from '$root/lib/interface/user.interface';
import { TokenData } from '$root/lib/store/tokenStore';
import api from '$root/lib/utils/api';
import { deleteCookiesData, setCookies } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';
import type { PageServerLoad } from './$types';
import { invalid, redirect, type Actions } from '@sveltejs/kit';

export const load: PageServerLoad = (event) => {
	if (event.locals.user && event.locals.is_login === true) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/');
	}
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');
};

export const actions: Actions = {
	default: async ({ request, cookies, locals, url }) => {
		const form = await request.formData();
		const res = await api.post(
			'/auth/login',
			`grant_type=&username=${form.get('username')}&password=${form.get(
				'password'
			)}&scope=&client_id=&client_secret=`,
			{
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		);
		if (res.status === status.HTTP_200_OK) {
			const token: TokenDataIn = res.data as TokenDataIn;
			setCookies(token.refresh_token, token, 'session', cookies);
			TokenData.set(token);
			const user = await api.get('/users/whoami');
			const user_data: UserDataIn = user.data as UserDataIn;
			setCookies(token.refresh_token, user_data, 'details', cookies);
			setCookies(token.refresh_token, { is_login: true }, 'is_login', cookies);
			locals.token = token;
			locals.is_login = true;
			if (url.searchParams.get('redirectTo')) {
				const location = String(url.searchParams.get('redirectTo'));
				throw redirect(status.HTTP_301_MOVED_PERMANENTLY, location);
			}
			return { message: 'login successfully' };
		}
		if (res.status !== status.HTTP_200_OK) {
			const error = res.data as { detail: string | undefined };
			const email = form.get('username') as string;
			return invalid(status.HTTP_400_BAD_REQUEST, { error: error.detail, email });
		}
	}
};
