import api from '$root/lib/utils/api';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const data = await request.json();
	const res = await api.post('/payments/', data, {
		'Content-Type': 'application/json'
	});
	return json({ ...res });
};
