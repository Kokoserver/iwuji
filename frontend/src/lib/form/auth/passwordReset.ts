import { create, test, enforce, only } from 'vest';

const suite = create((data = {}, fieldName: string) => {
	only(fieldName);
	test('password', 'password is required', () => {
		enforce(data.password).isNotEmpty();
	});
	test('confirm_password', 'password do not match', () => {
		enforce(data.password).equals(data.confirm_password);
	});
});

export default suite;
