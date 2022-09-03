import { error } from "@sveltejs/kit"
import type { PageLoad } from "../../../../.svelte-kit/types/src/routes/admin/$types"

export const load: PageLoad = ({ url }) => {
	if (url.pathname === "hello-world") {
		return {
			title: "Hello world!",
			content: "Welcome to our blog. Lorem ipsum dolor sit amet..."
		}
	}

	throw error(404, "Not found")
}
