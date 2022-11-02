import { PUBLIC_BASE_URL } from '$env/static/public';
import { redirect } from '$root/lib/utils/redirect';
import { getUserSession } from '$root/lib/utils/getCookies';
import type { Handle, HandleFetch } from '@sveltejs/kit';
import { refresh_token } from '$root/lib/utils/get_token_data';

export const handle: Handle = async ({ event, resolve }) => {
	getUserSession(event, ['session', 'details', 'is_login']);
	await refresh_token(event);
	getUserSession(event, ['session', 'details', 'is_login']);

	if (event.url.pathname.startsWith('/admin')) {
		if (!event.locals.user) return redirect(`/auth/login?redirectTo=${event.request.url}`);
		if (event.locals.user.role.name.toLowerCase() !== 'super admin')
			return redirect(`/auth/login?redirectTo=${event.request.url}`);
		return await resolve(event);
	}

	if (event.url.pathname.startsWith('/dashboard')) {
		if (!event.locals.user) return redirect(`/auth/login?redirectTo=${event.request.url}`);
		return await resolve(event);
	}
	if (event.url.pathname.includes('login')) {
		if (event.locals.user && event.locals.token && event.locals.is_login) return redirect('/');
		return await resolve(event);
	}

	return await resolve(event);
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
