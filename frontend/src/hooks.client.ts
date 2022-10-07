import type { TokenDataIn } from '$root/lib/interface/user.interface';
import { getUserSession } from '$root/lib/utils/getCookies';
import { redirect } from '$root/lib/utils/redirect';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	// const token_data: TokenDataIn = getUserSession(event, 'session');
	// if (!token_data.access_token && !token_data.refresh_token) {
	// 	// redirect protected pages
	// 	if (event.url.pathname === '/admin') {
	// 		return redirect('/');
	// 	}
	return await resolve(event);
	// }
};
