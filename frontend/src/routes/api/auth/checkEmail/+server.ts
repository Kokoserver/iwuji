import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { json, error, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	try {
		const data = (await request.json()) as { email: string };
		const check_user = await api.post(
			'/auth/check/dev',
			{ email: data.email },
			{ 'Content-Type': 'application/json' }
		);
		if (check_user.status === status.HTTP_200_OK) {
			return json({});
		}
		return json({}, { status: status.HTTP_404_NOT_FOUND });
	} catch (err) {
		throw error(status.HTTP_500_INTERNAL_SERVER_ERROR, 'error validating user email');
	}
};
