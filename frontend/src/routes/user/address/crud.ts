// import type { AddressOut } from '$root/lib/interface/address.interface';
import { goto } from '$app/navigation';
import { page } from '$app/stores';
import type { AddressIn } from '$root/lib/interface/address.interface';
import { notification } from '$root/lib/notification';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import { error, redirect } from '@sveltejs/kit';
import { get } from 'svelte/store';
import { AddressStore } from './store';

export const get_address = async (addressId: number) => {
	const res = await api.get(`/address/${addressId}`);
	if (res.status === status.HTTP_200_OK) {
		return res.data;
	}

	if (res.status === 404) {
		throw error(status.HTTP_404_NOT_FOUND, 'Address does not exist');
	}

	if (
		res.status === status.HTTP_400_BAD_REQUEST ||
		res.status === status.HTTP_422_UNPROCESSABLE_ENTITY
	) {
		throw error(status.HTTP_422_UNPROCESSABLE_ENTITY, 'Invalid data was provided');
	}
};

export const get_addressList = async () => {
	const res = await api.get(`/address/`);
	if (res.status === status.HTTP_200_OK) {
		return res.data as AddressIn[];
	}
	throw error(status.HTTP_422_UNPROCESSABLE_ENTITY, 'Invalid data was provided');
};

export const delete_address = async (addressId: number) => {
	try {
		let res = await fetch(`/user/address/api`, {
			method: 'DELETE',
			body: JSON.stringify({ addressId })
		});
		res = await res.json();
		if (res.status === status.HTTP_204_NO_CONTENT) {
			await goto('/user/address');
			const currentState = get(AddressStore);
			AddressStore.set(currentState.filter((item) => item.id !== addressId));
			notification.success('Address was removed successfully');
		}
		if (res.status === status.HTTP_404_NOT_FOUND) {
			notification.danger('Address does not exist');
		}
		throw error(status.HTTP_422_UNPROCESSABLE_ENTITY, 'Invalid data was provided');
	} catch (error) {
		console.error(error);
	}
};
