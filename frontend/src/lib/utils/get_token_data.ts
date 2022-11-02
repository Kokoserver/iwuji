import type { RequestEvent } from '@sveltejs/kit';
import dayjs from 'dayjs';
import jwtDecode from 'jwt-decode';
import { status } from '$root/lib/utils/status';
import type { TokenDataIn, UserDataIn } from '$root/lib/interface/user.interface';
import { deleteCookiesData, setCookies } from './getCookies';
import { PUBLIC_BASE_URL } from '$root/lib/utils/api';
interface tokenData {
	id: number;
	firstname: string;
	is_active: boolean;
	exp: number;
}
export const get_jwt_data = (token: string) => {
	if (token) {
		const token_details = jwtDecode(token);
		return token_details as tokenData;
	}
	return {} as tokenData;
};

export const refresh_token = async (event: RequestEvent) => {
	if (event.locals.token?.access_token) {
		const token_detail = get_jwt_data(event.locals.token.access_token) as tokenData;
		const isExpire: boolean = dayjs.unix(token_detail.exp).diff(dayjs()) < 1;
		if (isExpire) {
			const res = await fetch(`${PUBLIC_BASE_URL}/auth/token-refresh`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ refresh_token: event.locals.token.refresh_token })
			});
			if (res.status === status.HTTP_200_OK) {
				const token = (await res.json()) as TokenDataIn;
				setCookies(token.refresh_token, token, 'session', event.cookies);
				return true;
			} else {
				deleteCookiesData(event, 'session');
				deleteCookiesData(event, 'details');
				deleteCookiesData(event, 'is_login');
				event.locals.user = {} as UserDataIn;
				event.locals.is_login = false;
				event.locals.token = {} as TokenDataIn;
			}
		}
	}
	return false;
};
