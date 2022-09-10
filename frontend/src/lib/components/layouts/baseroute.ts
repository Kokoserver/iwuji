export interface Route {
	url: string
	name: string
	is_last?: boolean
}

export const BaseRoutes: Route[] = [
	{
		url: "/",
		name: "home"
	},
	{
		url: "/bio",
		name: "bio"
	},
	{
		url: "/book",
		name: "books"
	},
	{
		url: "/cart",
		name: "shop"
	},
	{
		url: "#contact",
		name: "contact",
		is_last: true
	}
]
