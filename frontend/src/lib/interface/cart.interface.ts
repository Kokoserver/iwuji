import type { Media } from "./media.interface"

export interface CartProductPropertyIn {
	pdf: boolean
	paper_back_qty: number
	hard_back_qty: number
}

export interface CartProductIn {
	name: string
	cover_img?: Media
	property: CartProductPropertyIn
}

export interface CartIn extends CartProductPropertyIn {
	id: number
	product: CartProductIn
}
export interface CartOut extends CartProductPropertyIn {
	productId: number
}
export interface CartUpdateOut extends CartProductPropertyIn {
	cartId: number
}
