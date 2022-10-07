import { type Writable, writable } from 'svelte/store';
import type { TokenDataIn } from '../interface/user.interface';

export const AuthStore = (initialState: TokenDataIn) => {
	const { set, subscribe, update } = writable(initialState);
};
