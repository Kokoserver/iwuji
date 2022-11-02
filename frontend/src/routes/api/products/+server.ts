import { error, json, redirect } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import { get_ProductList, get_VariationList } from '$root/lib/utils/page/products';

export const POST: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};

export const GET: RequestHandler = async ({ url }) => {
	const limit = Number(url.searchParams.get('limit')) || 10;
	const offset = Number(url.searchParams.get('offset')) || 0;
	const filter = String(url.searchParams.get('filter')) || '';
	if (url.searchParams.get('is_series') === 'true') {
		const products = await get_VariationList(filter, 10, 0, true);
		return json(products);
	} else {
		const products = await get_ProductList(filter, limit, offset, false, false, true);
		return json(products);
	}
};

export const PUT: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};

export const DELETE: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};
