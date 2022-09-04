import type { Handle } from "@sveltejs/kit"
import { API } from "./lib/interface/api.interface"
import axios from "./lib/utils/axios"
import { status } from "./lib/utils/status"
import type {
	UserRefreshTokenInput,
	TokenDataIn
} from "./lib/interface/user.interface"
import * as cookie from "cookie"

export const handle: Handle = async ({ event, resolve }) => {
	event.locals.user = {
		firstname: "ola",
		lastname: "ola",
		email: "koko",
		is_active: true,
		role: {
			name: "customer"
		}
	}

	const cookies = cookie.parse(event.request.headers.get("cookie") || "")
	const jwt =
		cookies.tokens && Buffer.from(cookies.jwt, "base64").toString("utf-8")
	event.locals.user = jwt ? JSON.parse(jwt) : null
	return await resolve(event)
}
