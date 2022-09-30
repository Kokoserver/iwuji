import { PUBLIC_BASE_URL } from '$env/static/public';
import { status } from '$root/lib/utils/status';
import { redirect } from '$root/lib/utils/redirect';
import { getUserSession, updateCookies } from '$root/lib/utils/getCookies';
import type { Handle, HandleFetch } from '@sveltejs/kit';

import { refresh_token } from '$root/lib/utils/get_token_data';
import { TokenData } from './lib/store/tokenStore';

export const handle: Handle = async ({ event, resolve }) => {
	getUserSession(event, ['session', 'details', 'is_login']);
	await refresh_token(event);
	getUserSession(event, ['session', 'details', 'is_login']);
	TokenData.set(event.locals.token);

	if (event.url.pathname.startsWith('/admin') && event.locals.user.role.name !== 'admin') {
		if (event.locals.token?.access_token && event.locals.token?.refresh_token) {
			return redirect('/');
		}
		return await resolve(event);
	}

	if (
		event.url.pathname.startsWith('/dashboard') &&
		!event.locals.token?.access_token &&
		!event.locals.token?.refresh_token
	) {
		return redirect('/login');
	}

	const response = await resolve(event);
	if (response.status === status.HTTP_401_UNAUTHORIZED) {
		const is_refresh: boolean = await refresh_token(event);
		if (is_refresh) {
			event.request.headers.set('Authorization', `Bearer ${event.locals.token.access_token}`);
			updateCookies(event, 'session', 'token');
			return await resolve(event);
		}
		return await resolve(event);
	}

	return response;
};

export const handleFetch: HandleFetch = async ({ event, request, fetch }) => {
	const baseURL = process.env.BASE_URL ?? '';
	if (baseURL) {
		if (request.url.startsWith(PUBLIC_BASE_URL)) {
			if (event) {
				request.headers.set('Authorization', `bearer ${event.locals.token.access_token}`);
			}
		}
	}
	const res = fetch(request);
	return res;
};
