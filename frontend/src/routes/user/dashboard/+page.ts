import type { PageLoad } from './$types';

export const load: PageLoad = ({ url }) => {
	if (url.pathname === 'hello-world') {
		return {
			title: 'Hello world!',
			content: 'Welcome to our blog. Lorem ipsum dolor sit amet...'
		};
	}

	// throw error(404, "Not found")
};
