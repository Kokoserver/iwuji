import { PUBLIC_BASE_URL } from '$env/static/public';
import dayjs from 'dayjs';
import { get } from 'svelte/store';
import { TokenData } from '../store/tokenStore';
import { get_jwt_data } from './get_token_data';
type APIResponse = {
	data?: object | undefined | null;
	status?: number;
	text?: string | undefined;
};

const tokens = get(TokenData);

class API {
	constructor(protected baseurl: string) {}

	async get_token() {
		const token_detail = get_jwt_data(tokens.access_token) as { exp: number };
		const isExpire: boolean = dayjs.unix(token_detail.exp).diff(dayjs()) < 1;
		let new_token = get(TokenData);
		if (isExpire) {
			new_token = get(TokenData);
		}
		return { Authorization: `Bearer ${new_token.access_token}` };
	}

	get_url(endpoint: string) {
		if (!endpoint) {
			return this.baseurl;
		}
		return `${this.baseurl}${endpoint}`;
	}

	async handleResponse(response: Response): Promise<APIResponse> {
		const text = await response.text();

		if (!response.ok) {
			try {
				const data = text && JSON.parse(text);
				if (data) return { data, status: response.status };
			} catch (error) {
				return { text, status: response.status };
			}
		} else {
			try {
				const data = text && JSON.parse(text);
				if (data) return { data, status: response.status };
			} catch (error) {
				return { text, status: response.status };
			}
		}
		return {};
	}

	async send(form: HTMLFormElement, config: object = {}) {
		const response = await fetch(form.action, {
			method: form.method,
			body: new FormData(form),
			headers: { ...config, ...(await this.get_token()), accept: 'application/json' }
		});
		return this.handleResponse(response);
	}

	async get(endpoint: string, config: object = {}, fromAPI = true) {
		const requestOptions = {
			method: 'GET',
			headers: { ...config, ...(await this.get_token()), accept: 'application/json' }
		};
		if (fromAPI) {
			const response = await fetch(this.get_url(endpoint), requestOptions);
			return this.handleResponse(response);
		} else {
			const response = await fetch(endpoint, requestOptions);
			return this.handleResponse(response);
		}
	}
	/* eslint-disable @typescript-eslint/no-explicit-any */
	async post(endpoint: string, body: any, config = {}) {
		const requestOptions = {
			method: 'POST',
			headers: { ...config, ...(await this.get_token()), accept: 'application/json' },
			body: body
		};
		if (typeof body === 'object') {
			requestOptions.body = JSON.stringify(requestOptions.body);
		}

		const response = await fetch(this.get_url(endpoint), requestOptions);

		return this.handleResponse(response);
	}

	async put(endpoint: string, body: any, config = {}) {
		const requestOptions = {
			method: 'PUT',
			headers: { ...config, ...(await this.get_token()), accept: 'application/json' },
			body: body
		};
		if (typeof body === 'object') {
			requestOptions.body = JSON.stringify(requestOptions.body);
		}

		const response = await fetch(this.get_url(endpoint), requestOptions);
		return this.handleResponse(response);
	}

	// prefixed with underscored because delete is a reserved word in javascript
	async delete(endpoint: string, config: object = {}) {
		const requestOptions = {
			method: 'DELETE',
			headers: { ...config, ...(await this.get_token()), accept: 'application/json' }
		};
		const response = await fetch(this.get_url(endpoint), requestOptions);
		return this.handleResponse(response);
	}
}

const api = new API(PUBLIC_BASE_URL);

export default api;
