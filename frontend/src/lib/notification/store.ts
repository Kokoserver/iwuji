import { writable, derived, type Writable, type Readable } from 'svelte/store';

const TIMEOUT = 3000;
type StoreInput = {
	id: string;
	message: string;
	type: string;
	duration: number;
};

function createNotificationStore() {
	const _notifications: Writable<StoreInput[]> = writable([]);

	function push(message: string, type = 'default', duration: number) {
		_notifications.update((state) => {
			return [...state, { id: id(), type, message, duration }];
		});
	}

	const notifications: Readable<StoreInput[]> = derived(_notifications, ($_notifications, set) => {
		set($_notifications);
		if ($_notifications.length > 0) {
			const timer = setTimeout(() => {
				_notifications.update((state) => {
					// const updated_state = pop($_notifications[0].id);
					state = [];
					return state;
				});
			}, $_notifications[0].duration);
			return () => {
				clearTimeout(timer);
			};
		}
	});

	const pop = (id: string): StoreInput[] => {
		_notifications.update((n) => {
			if (!n.length || !id) {
				return [];
			}
			const target = id;
			return n.filter((i) => i.id !== target) as StoreInput[];
		});
		return [];
	};

	const { subscribe } = notifications;

	return {
		subscribe,
		push,
		default: (msg: string, duration = TIMEOUT) => push(msg, 'default', duration),
		danger: (msg: string, duration = TIMEOUT) => push(msg, 'danger', duration),
		dark: (msg: string, duration = TIMEOUT) => push(msg, 'warning', duration),
		warning: (msg: string, duration = TIMEOUT) => push(msg, 'warning', duration),
		info: (msg: string, duration = TIMEOUT) => push(msg, 'info', duration),
		success: (msg: string, duration = TIMEOUT) => push(msg, 'success', duration)
	};
}

function id() {
	return '_' + Math.random().toString(36).substr(2, 9);
}

export const notifications = createNotificationStore();
