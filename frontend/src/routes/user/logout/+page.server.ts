import { error, redirect } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import type { PageServerLoad } from './$types';
import { deleteCookiesData } from '$root/lib/utils/getCookies';
import { status } from '$root/lib/utils/status';
import type { UserDataIn } from '$root/lib/interface/user.interface';

export const load: PageServerLoad = async (event) => {
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');
	return { logout: true };
};
