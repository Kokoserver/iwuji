import { type Writable, writable } from 'svelte/store';
import type { TokenDataIn } from '../lib/interface/user.interface';

export const AuthStore = (initialState: TokenDataIn) => {
	const { set, subscribe, update } = writable(initialState);
};
