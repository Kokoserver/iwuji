import { writable, type Writable } from 'svelte/store';

export type BookType = {
	is_series: boolean;
	normal_book: boolean;
	filter: string;
};

export const bookType: Writable<BookType> = writable({
	is_series: false,
	normal_book: true,
	filter: ''
});
