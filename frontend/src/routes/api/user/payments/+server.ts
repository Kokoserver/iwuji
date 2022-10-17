import { error, json, redirect } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import api from '$root/lib/utils/api';


export const POST: RequestHandler = async ({ request }) => {
	const data = await request.json();
	const res = await api.post('/payments/verify', data, {
		'Content-Type': 'application/json'
	});
	return json({ ...res });
};

export const GET: RequestHandler = ({ url }) => {
	const signal: string = url.searchParams.get('signal') || '';
	return new Response();
};

export const PUT: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};

export const DELETE: RequestHandler = ({ url }) => {
	url.username;
	return new Response();
};
