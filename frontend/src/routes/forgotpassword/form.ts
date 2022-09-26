import { create, test, enforce, only } from 'vest';

const suite = create((data = {}, fieldName: string) => {
	only(fieldName);
	test('email', 'Enter a valid email address', () => {
		enforce(data.email).matches(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/);
	});
});

export default suite;
