import type { AddressIn } from "$root/lib/interface/address.interface";
import { writable, type Writable } from "svelte/store";

export const AddressStore:Writable<AddressIn[]> = writable()