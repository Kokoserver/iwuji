import type { MessageIn } from '$root/lib/interface/message.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { invalid, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = ({ locals }) => {
	if (locals.is_login === true) {
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/');
	}
};

export const actions: Actions = {
	default: async ({ request }) => {
		const form = await request.formData();
		const user_data = Object.fromEntries(form.entries());

		const res = await api.post('/users/register', user_data, {
			'Content-type': 'application/json'
		});

		if (res.status !== status.HTTP_201_CREATED) {
			return invalid(status.HTTP_400_BAD_REQUEST, {
				error: 'error creating account, please try again '
			});
		}

		return { ...res.data } as MessageIn;
	}
};
