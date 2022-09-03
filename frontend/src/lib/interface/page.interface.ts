export interface NavItem {
	name: string
	url: string
	external?: boolean
	id?: string
}

export interface PageItem {
	pageName: string
	pageUrl: string
	actions: object
	hasSearchBar?: boolean
}
