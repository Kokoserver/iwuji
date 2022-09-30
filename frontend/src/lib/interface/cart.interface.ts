import type { Media } from './media.interface';

export interface CartProductPropertyIn {
	pdf_price: number;
	paper_back_price: number;
	hard_back_price: number;
}

export interface CartProductIn {
	name: string;
	cover_img?: Media;
	property: CartProductPropertyIn;
}

export interface CartIn extends CartProductPropertyIn {
	id: number;
	pdf: true;
	paper_back_qty: number;
	hard_back_qty: number;
	product: CartProductIn;
}
export interface CartOut {
	productId: number;
	pdf: boolean;
	paper_back_qty: number;
	hard_back_qty: number;
}
export interface CartUpdateOut extends CartProductPropertyIn {
	cartId: number;
}
