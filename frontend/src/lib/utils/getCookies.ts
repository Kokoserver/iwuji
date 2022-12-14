import type { Cookies, RequestEvent } from '@sveltejs/kit';
import type { TokenDataIn, UserDataIn } from '../interface/user.interface';
import { get_jwt_data } from './get_token_data';

export const cookiesData = (event: RequestEvent, name: string) => {
	const cookies = event.cookies.get(name);
	return cookies;
};

export const deleteCookiesData = (event: RequestEvent, name: string) => {
	event.cookies.set(name, '', {
		httpOnly: true,
		path: '/',
		maxAge: 0
	});
};

export const clearCookies = (event: RequestEvent) => {
	const cookiesData = ['session', 'details', 'is_login'];
	for (let index = 0; index < cookiesData.length; index++) {
		deleteCookiesData(event, cookiesData[index]);
	}
	event.locals.user = {} as UserDataIn;
	event.locals.token = {} as TokenDataIn;
	event.locals.is_login = false;
};

export const getUserSession = (event: RequestEvent, names: string[]) => {
	const cookies_string = cookiesData(event, names[0]);
	const details_string = cookiesData(event, names[1]);
	const login_status_str = cookiesData(event, names[2]);

	if (!cookies_string) {
		deleteCookiesData(event, names[0]);
		deleteCookiesData(event, names[1]);
		deleteCookiesData(event, names[2]);
	}
	if (cookies_string && details_string && login_status_str) {
		const cookies_data = JSON.parse(cookies_string) as TokenDataIn;
		const user_details = JSON.parse(details_string) as UserDataIn;
		const login_status = JSON.parse(login_status_str) as { is_login: boolean };

		event.locals.token = cookies_data;
		event.locals.user = user_details;
		event.locals.is_login = login_status.is_login;

		return cookies_data;
	}
};

export const updateCookies = (event: RequestEvent, name: string, toUpdate: string) => {
	const cookies_string = cookiesData(event, name);
	const cookies_data = JSON.parse(String(cookies_string));
	// eslint-disable-next-line @typescript-eslint/ban-ts-comment
	// @ts-ignore
	event.locals[String(toUpdate)] = cookies_data;
};

export const setCookies = (
	token: string, //to get expire time
	data: string | object,
	name: string,
	cookies: Cookies
) => {
	const token_data = get_jwt_data(token) as { exp: number };
	let to_be_store = '';
	if (typeof data === 'object') {
		to_be_store = JSON.stringify(data);
	} else if (typeof data === 'string') {
		to_be_store = data;
	}

	cookies.set(name, to_be_store, {
		path: '/',
		httpOnly: true,
		secure: true,
		maxAge: token_data.exp
	});
};
