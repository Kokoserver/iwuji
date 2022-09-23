import type { TokenDataIn, UserDataIn } from '$root/lib/interface/user.interface';
import api from '$root/lib/utils/api';
import { deleteCookiesData, setCookies } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';
import { invalid, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async (event) => {
	if (event.locals.user && event.locals.is_login) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/');
	}
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');
};

export const actions: Actions = {
	default: async ({ request, cookies, locals, url }) => {
		const form = await request.formData();
		const result = await api.post(
			'/auth/login',
			`grant_type=&username=${form.get('username')}&password=${form.get('password')}&scope=&client_id=&client_secret=`,
			{
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		);
		if (result.status === status.HTTP_200_OK) {
			const token: TokenDataIn = result.data as TokenDataIn;
			setCookies(token.refresh_token, token, 'session', cookies);
			const user = await api.get('/users/whoami', {
				Authorization: `bearer ${token.access_token}`
			});
			if (user.status === status.HTTP_200_OK) {
				const user_data: UserDataIn = user.data as UserDataIn;
				setCookies(token.refresh_token, user_data, 'details', cookies);
				setCookies(token.refresh_token, { is_login: true }, 'is_login', cookies);
			}
			locals.token = token;
			locals.is_login = true;
			if (url.searchParams.get('redirectTo')) {
				const location = String(url.searchParams.get('redirectTo'));
				throw redirect(status.HTTP_308_PERMANENT_REDIRECT, location);
			}
			throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/');
		}
		if (result.status !== status.HTTP_200_OK) {
			const error = 'invalid email or password';
			const email = form.get('username') as string;
			return invalid(status.HTTP_400_BAD_REQUEST, { error, email });
		}
	}
};
