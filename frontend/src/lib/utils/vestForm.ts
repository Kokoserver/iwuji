export const handleChange = async (event: Event, suite: any, formdata: object) => {
	const inputField = event.target as HTMLInputElement;
	return suite(formdata, inputField.name);
};
