// import type { AddressOut } from '$root/lib/interface/address.interface';
import { goto } from '$app/navigation';
import { page } from '$app/stores';
import type { AddressIn } from '$root/lib/interface/address.interface';
import { notification } from '$root/lib/notification';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { error, redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';
import { AddressStore } from '../../../store/address';

// eslint-disable-next-line @typescript-eslint/ban-ts-comment

export const get_address = async (addressId: number, Fetch: typeof fetch) => {
	const res = await Fetch(`/api/user/address/?id=${addressId}`);
	if (res.status === status.HTTP_200_OK) {
		const data = await res.json();
		return data as AddressIn;
	}
	const data = await res.json();
	throw error(status.HTTP_400_BAD_REQUEST, data.error);
};

export const get_addressList = async (Fetch: typeof fetch) => {
	const res = await Fetch(`/api/user/address`);
	if (res.status === status.HTTP_200_OK) {
		const data = await res.json();
		return data as AddressIn[];
	}
	return [];
};

export const delete_address = async (addressId: number) => {
	try {
		const res = await fetch(`/api/user/address/`, {
			method: 'DELETE',
			body: JSON.stringify({ addressId })
		});
		const data = await res.json();

		if (res.status === status.HTTP_204_NO_CONTENT) {
			await goto('/address');
			const currentState = get(AddressStore);
			AddressStore.set(currentState.filter((item) => item.id !== addressId));
			notification.success('Address was removed successfully');
		}
		if (res.status === status.HTTP_404_NOT_FOUND) {
			notification.danger('Address does not exist');
		}
		if (res.status === status.HTTP_400_BAD_REQUEST) {
			notification.danger(data.error);
		}
	} catch (error) {
		console.error(error);
	}
};
