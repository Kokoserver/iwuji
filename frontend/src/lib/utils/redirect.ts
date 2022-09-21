import { status } from './status';

export function redirect(location: string) {
	return new Response(undefined, {
		status: status.HTTP_307_TEMPORARY_REDIRECT,
		headers: { location }
	});
}
