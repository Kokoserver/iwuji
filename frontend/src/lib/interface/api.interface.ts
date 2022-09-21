// const baseUrl = "http://localhost:8000/api/v1"
// export type Endpoint = {
// 	user: string
// }

// const generate_url = (name: string): string => {
// 	return `${baseUrl}/${name}`
// }

export const API = {
	permissions: '/permissions',
	user: '/users',
	auth: '/auth',
	author: '/authors',
	product: '/products',
	variation: '/variations',
	address: '/address',
	cart: '/carts',
	review: '/reviewS',
	category: '/products/category'
};

export type APIErrorResponse = {
	detail: object | string;
};
