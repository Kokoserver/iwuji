import { json, type RequestHandler } from '@sveltejs/kit';
import { get_ProductList } from '../crud';

export const GET: RequestHandler = async ({ url }) => {
	const limit = Number(url.searchParams.get('limit')) || 10;
	const offset = Number(url.searchParams.get('offset')) || 0;
	const filter = String(url.searchParams.get('filter')) || '';
	if (url.searchParams.get('is_series') === 'true') {
		const products = await get_ProductList(filter, limit, offset, true, false, true);
		return json(products);
	} else {
		const products = await get_ProductList(filter, 10, 0, false, false, true);
		return json(products);
	}
};
