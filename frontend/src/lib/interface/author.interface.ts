import type { Media } from './media.interface';

export interface AuthorIn {
	id: number;
	title: string;
	firstname: string;
	lastname: string;
	email: string;
	description: string;
	profile_img?: Media;
}
