import type { AuthorIn } from '$root/lib/interface/author.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async (event) => {
	const res = await api.get('/authors/2');
	if (res.status === status.HTTP_200_OK) {
		console.log(res.data);

		return res.data as AuthorIn;
	}

	throw error(status.HTTP_404_NOT_FOUND);
};
