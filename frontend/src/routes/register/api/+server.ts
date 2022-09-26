import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const data = (await request.json()) as { email: string };

	const check_user = await api.post(
		'/auth/check/dev',
		{ email: data.email },
		{ 'Content-Type': 'application/json' }
	);
	if (check_user.status === status.HTTP_200_OK) {
		const data = { email: 'user already taken' } as { email: string };
		return json(data);
	}
	return json({ email: '' });
};
