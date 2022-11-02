import type { AddressIn } from './address.interface';

export interface OrderDetailsIn {
	orderId: string;
	status: string;
}

export interface OrderDetailIn {
	created_at: Date;
	id: number;
	orderId: string;
	order_item_order: OrderItemOrder[];
	order_payment: OrderPayment[];
	shipping_address: AddressIn;
	status: string;
}

export interface OrderItemOrder {
	deliver: boolean;
	hard_back_qty: number;
	id: number;
	paper_back_qty: number;
	pdf: boolean;
	product: Product;
}

export interface Product {
	cover_img?: CoverImg;
	description: string;
	id: number;
	name: string;
	slug: string;
}

export interface CoverImg {
	alt: string;
	content_type: string;
	url: string;
}

export interface OrderPayment {
	amount: number;
	currency: string;
	id: number;
	pay_ref: string;
	status: string;
}
