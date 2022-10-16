import { PUBLIC_BASE_URL } from '$env/static/public';

type APIResponse = {
	data?: object | undefined | null;
	status?: number;
	text?: string | undefined;
};

class API {
	constructor(protected baseurl: string) {}

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
				if (data) {
					return { data, status: response.status };
				}
			} catch (error) {
				return { text, status: response.status };
			}
		} else {
			try {
				const data = text && JSON.parse(text);
				return { data, status: response.status };
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
			headers: { ...config, accept: 'application/json' }
		});
		return this.handleResponse(response);
	}

	async get(endpoint: string, config: object = {}, fromAPI = true) {
		const requestOptions = {
			method: 'GET',
			headers: { ...config, accept: 'application/json' }
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
			headers: { ...config, accept: 'application/json' },
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
			headers: { ...config, accept: 'application/json' },
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
			headers: { ...config, accept: 'application/json' }
		};
		const response = await fetch(this.get_url(endpoint), requestOptions);
		return this.handleResponse(response);
	}
}

const api = new API(PUBLIC_BASE_URL);

export default api;
