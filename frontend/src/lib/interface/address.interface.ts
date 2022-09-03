export interface AddressOut {
	street: string
	state: string
	city: string
	country: string
	tel: string
	zipcode?: string
}

export interface AddressIn extends AddressOut {
	id: number
}
