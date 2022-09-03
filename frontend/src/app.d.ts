// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces

import type { UserDataIn } from "./lib/interface/user.interface"

// and what to do when importing types
declare interface Role {
	name: string
}
declare namespace App {
	interface Locals {
		user: UserDataIn
		is_login: boolean
		token: {
			access_toke: string
			refresh_token: string
		}
	}
	// interface PageData {}
	// interface Platform {}
}
