import type { PageServerLoad } from './$types';
import { deleteCookiesData } from '$root/lib/utils/getCookies';

import type { TokenDataIn, UserDataIn } from '$root/lib/interface/user.interface';
import { TokenData } from '$root/lib/store/tokenStore';

export const load: PageServerLoad = async (event) => {
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');
	event.locals.is_login = false;
	event.locals.token = {} as TokenDataIn;
	event.locals.user = {} as UserDataIn;
	TokenData.set({ access_token: '', refresh_token: '' });
	return { logout: true };
};
