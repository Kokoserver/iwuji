import type { Media } from "./media.interface"
import type { ProductIn } from "./product.interface"

export interface VariationOut {
	name: string
	description: string
	slug: string
	id: number
	cover_img?: Media
	items: ProductIn[]
	created_at: Date
}

export interface VariationProductOut {
	productId: number
	variationId: number
}
