export function formToJson(event?: Event, formData?: HTMLFormElement) {
	const form: HTMLFormElement = event ? (event.target as HTMLFormElement) : formData;
	const new_form = new FormData(form);
	return JSON.stringify(Object.fromEntries(new_form));
}

export function getFormFromEvent(event: Event) {
	const form = event.target as HTMLFormElement;
	const formData = new FormData(form);
	return formData;
}
