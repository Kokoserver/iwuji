import { invalid } from '@sveltejs/kit';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import type { Actions, PageServerLoad } from './$types';
import type { MessageIn } from '$root/lib/interface/message.interface';
import { deleteCookiesData } from '$root/lib/utils/getCookies';

export const load: PageServerLoad = (event) => {
	deleteCookiesData(event, 'session');
	deleteCookiesData(event, 'details');
	deleteCookiesData(event, 'is_login');
};

export const actions: Actions = {
	default: async ({ request }) => {
		const form = await request.formData();
		const user_data = Object.fromEntries(form.entries());
		const res = await api.post('/users/passwordResetLink', user_data, {
			'Content-type': 'application/json'
		});

		if (res.status !== status.HTTP_200_OK) {
			return invalid(status.HTTP_400_BAD_REQUEST, {
				error: 'error resetting password, please try again '
			});
		}
		return { ...res.data } as MessageIn;
	}
};
