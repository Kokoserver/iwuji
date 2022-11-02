import type { RequestEvent } from '@sveltejs/kit';
import { refresh_token } from './get_token_data';

export const get_token = async (event: RequestEvent) => {
	await refresh_token(event);
	return { Authorization: `Bearer ${event.locals.token?.access_token ?? ''}` };
};
