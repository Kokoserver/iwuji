import type { RequestEvent } from '@sveltejs/kit';
import dayjs from 'dayjs';
import jwtDecode from 'jwt-decode';
import { status } from '$root/lib/utils/status';
import api from './api';
import type { TokenDataIn } from '$root/lib/interface/user.interface';
import { deleteCookiesData, setCookies } from './getCookies';

export const get_jwt_data = (token: string) => {
	const token_details = jwtDecode(token);
	return token_details;
};

type tokenData = { id: number; firstname: string; is_active: boolean; exp: number };

export const refresh_token = async (event: RequestEvent): Promise<boolean> => {
	const token_detail = get_jwt_data(event.locals.token.access_token) as tokenData;
	const isExpire: boolean = dayjs.unix(token_detail.exp).diff(dayjs()) < 1;
	if (isExpire) {
		const res = await api.post(
			'/auth/refresh-token',
			{ refresh_token: event.locals.token.refresh_token },
			{
				'Content-Type': 'application/json'
			}
		);
		if (res?.status === status.HTTP_200_OK) {
			const token = res.data as TokenDataIn;
			setCookies(token.refresh_token, token, 'session', event.cookies);

			return true;
		}
		if (res?.status === status.HTTP_401_UNAUTHORIZED || res?.status === status.HTTP_400_BAD_REQUEST) {
			deleteCookiesData(event, 'session');
			deleteCookiesData(event, 'details');
			deleteCookiesData(event, 'is_login');
			return false;
		}
	}
};
