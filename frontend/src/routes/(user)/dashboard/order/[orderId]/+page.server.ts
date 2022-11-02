// import { error } from "@sveltejs/kit"
import type { RequestHandler } from "@sveltejs/kit"

export const POST: RequestHandler = ({ url }) => {
	url.username
	return new Response()
}

export const PUT: RequestHandler = ({ url }) => {
	url.username
	return new Response()
}

export const GET: RequestHandler = ({ url }) => {
	url.username
	return new Response()
}
