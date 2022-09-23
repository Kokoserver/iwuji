export interface Route {
	url: string;
	name: string;
	visible?: boolean;
	is_last?: boolean;
}

export const BaseRoutes: Route[] = [
	{
		url: '/',
		name: 'home'
	},
	{
		url: '/bio',
		name: 'bio'
	},
	{
		url: '/books',
		name: 'books'
	},
	{
		url: '/shop',
		name: 'shop'
	},
	{
		url: '/login',
		name: 'login',
		visible: false
	},
	{
		url: '#contact',
		name: 'contact',
		is_last: true
	}
];
