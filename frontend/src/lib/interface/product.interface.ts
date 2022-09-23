import type { AuthorIn } from './author.interface';
import type { CategoryOut } from './category.interface';
import type { Media } from './media.interface';

export interface ProductPropertyIn {
	in_stock?: boolean;
	discount?: number;
	paper_back_price: number;
	paper_back_qty?: number;
	hard_back_price?: number;
	hard_back_qty?: number;
	pdf_price?: number;
}

export interface ProductAttributeIn {
	isbn10: string;
	isbn1: string;
	language?: string;
	pub_date?: Date;
	pages: number;
	height?: number;
	width?: number;
	weight?: number;
}

export interface ProductIn {
	name: string;
	description: string;
	slug: string;
	id: number;
	is_series: boolean;
	author?: AuthorIn;
	cover_img: Media;
	categories?: CategoryOut[];
	property: ProductPropertyIn;
	attribute: ProductAttributeIn;
	gallery?: Media[];
	created_at?: Date;
}
