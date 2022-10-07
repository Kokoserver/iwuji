import { writable } from 'svelte/store';

export const showModel = writable(false);
export const showStep = writable(1);
export const Loading = writable(false);
