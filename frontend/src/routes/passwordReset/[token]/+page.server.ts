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
	default: async ({ request, params }) => {
		const token: string = params.token;
		const form = await request.formData();
		const user_data = Object.fromEntries(form.entries());
		user_data['token'] = token;
		const res = await api.put('/users/', user_data, {
			'Content-type': 'application/json'
		});

		if (res.status !== status.HTTP_200_OK) {
			const error_message = res.data as { detail: string | undefined };
			return invalid(status.HTTP_400_BAD_REQUEST, {
				error: error_message.detail
			});
		}
		return { ...res.data } as MessageIn;
	}
};
