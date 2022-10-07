import { goto } from '$app/navigation';
import { PUBLIC_BASE_URL } from '$env/static/public';
import type { UserLoginInput } from '$root/lib/interface/auth.interface';
import type { TokenDataIn } from '$root/lib/interface/user.interface';
import { notification } from '$root/lib/notification';
import api from '$root/lib/utils/api';
import { status } from '$root/lib/utils/status';
import axios from 'axios';

export const HandleLogin = async (data: UserLoginInput, redirectTo: string | undefined | null) => {
	const res = await api.post(
		'/auth/login',
		`grant_type=&username=${data.username}&password=${data.password}&scope=&client_id=&client_secret=`,
		{
			'Content-Type': 'application/x-www-form-urlencoded'
		}
	);
	if (res.status === status.HTTP_200_OK) {
		const token: TokenDataIn = res.data as TokenDataIn;
		localStorage.setItem('token', JSON.stringify(token));
		const user_data = await axios.get(PUBLIC_BASE_URL + '/users/whoami', {
			headers: {
				Authorization: `Bearer ${token.access_token}`
			}
		});

		localStorage.setItem('user_details', JSON.stringify(user_data.data));
		localStorage.setItem('is_login', JSON.stringify({ is_login: true }));
		console.log(redirectTo);

		if (redirectTo) return goto(redirectTo);
		notification.success('login successfully');
		await goto('/');
	}
	if (res.status !== status.HTTP_200_OK) {
		const error_details = res.data as { detail: string | '' };
		return error_details.detail;
	}
};
