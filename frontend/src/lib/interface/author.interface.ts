import type { Media } from "./media.interface"

export interface AuthorIn {
	title: string
	firstname: string
	lastname: string
	email: string
	description: string
	profile_img?: Media
}
