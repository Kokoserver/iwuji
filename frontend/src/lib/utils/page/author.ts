import type { AuthorIn } from '$root/lib/interface/author.interface';

export const get_authorData = async (
	Fetch: typeof fetch,
	authorId?: number,
	limit = 1,
	offset = 0,
	filter = '',
	single = true
) => {
	let url = null;
	if (authorId) {
		url = `/api/author/${authorId}/?signal=single`;
	} else {
		url = `/api/author/?signal=all&limit=${limit}&offset=${offset}&filter=${filter}`;
	}
	const res = await Fetch(url);
	const data = await res.json();
	if (authorId) {
		return data as AuthorIn;
	}
	if (single) return data[0];
	return data as AuthorIn[];
};
