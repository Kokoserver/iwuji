import { clearCookies } from '$root/lib/utils/getCookies';
import { json, type RequestHandler } from '@sveltejs/kit';

export const DELETE: RequestHandler = (event) => {
	clearCookies(event);
    
	return json({});
};
