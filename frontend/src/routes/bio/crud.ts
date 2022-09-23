import type { AuthorIn } from '$root/lib/interface/author.interface';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';

export const get_authorData = async () => {
	const res = await api.get('/authors/2');
	if (res.status === status.HTTP_200_OK) {
		const author_data = res.data as AuthorIn;
		return author_data;
	}
};
