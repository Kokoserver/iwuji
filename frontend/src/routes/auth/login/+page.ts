import { error } from "@sveltejs/kit"
import type { PageLoad } from "./$types"

export const load: PageLoad = ({ url }) => {
	console.log(url.searchParams.get("next"))

	// throw error(404, "Not found")
}
