import { error, redirect } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import type { MessageIn } from '$root/lib/interface/message.interface';
import { status } from '$root/lib/utils/status';

export const load: PageLoad = async ({ fetch, url }) => {
	try {
		const token = url.searchParams.get('activate_token');
		if (token) {
			const res = await fetch('/api/activateUser', {
				method: 'POST',
				body: JSON.stringify({ token })
			});
			const data = await res.json();
			return data as MessageIn;
		}
		throw redirect(status.HTTP_307_TEMPORARY_REDIRECT, '/');
	} catch (err) {
		throw error(status.HTTP_400_BAD_REQUEST, 'Error activating account');
	}
};
