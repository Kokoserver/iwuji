import type { LayoutServerLoad } from '../../.svelte-kit/types/src/routes/$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	return { is_login: locals.is_login, user: locals.user };
};
