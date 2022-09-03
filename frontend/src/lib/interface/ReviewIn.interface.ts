export interface ReviewOut {
	comment: string
	rating: number
	productId: number
}

export interface ReviewUserIn {
	firstname: string
	lastname: string
	email: string
}

export interface ReviewIn extends ReviewOut {
	id: number
	user: ReviewUserIn
	created_at: Date
}
