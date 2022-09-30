import { writable, type Writable } from 'svelte/store';

export type BookType = {
	is_series: boolean;
	normal_book: boolean;
	filter: string;
};
export type CartItemType = {
	pdf: boolean;
	hard_back: boolean;
	paper_back: boolean;
	paper_back_qty: number;
	hard_back_qty: number;
};

export const bookType: Writable<BookType> = writable({
	is_series: false,
	normal_book: true,
	filter: ''
});

export const CartType: Writable<CartItemType> = writable({
	pdf: true,
	hard_back: false,
	paper_back: false,
	paper_back_qty: 0,
	hard_back_qty: 0
});
