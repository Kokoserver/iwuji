import { writable, type Writable } from 'svelte/store';
import type { TokenDataIn } from '../interface/user.interface';

export const TokenData: Writable<TokenDataIn> = writable({
	access_token: '',
	refresh_token: ''
});
