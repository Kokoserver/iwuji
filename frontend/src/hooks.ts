import type { Handle } from "@sveltejs/kit"
import { API } from "./lib/interface/api.interface"
import axios from "./lib/utils/axios"
import { status } from "./lib/utils/status"
import type {
	UserRefreshTokenInput,
	TokenDataIn
} from "./lib/interface/user.interface"
export const handle: Handle = async ({ event, resolve }) => {
	let response = await resolve(event)

	if (response.status === status.HTTP_401_UNAUTHORIZED) {
		// @TODO check if user refresh_token is available
		const refresh_token: UserRefreshTokenInput = {
			refresh_token: "hwerheoitheriterhterihteirhtoierhtierht"
		}

		const res = await axios.post(
			API.auth + "/refresh_token",
			JSON.stringify(refresh_token),
			{
				headers: { "Content-Type": "application/json" }
			}
		)
		const token: TokenDataIn = res.data
		if (res.status === status.HTTP_200_OK) {
			event.setHeaders({
				Authorization: `bearer ${token.access_token}`
			})
		}
	}
	response = await resolve(event)

	return response
}
