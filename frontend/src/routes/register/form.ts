import { create, test, enforce, only } from 'vest';
const suite = create((data = {}, currentField) => {
	only(currentField);
	test('email', 'email is required', () => {
		enforce(data.email).isNotBlank();
	});

	test('email', 'Enter a valid email address', () => {
		enforce(data.email).matches(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/);
	});

	test('firstname', 'firstname is required', () => {
		enforce(data.firstname).isNotEmpty();
	});

	test('firstname', 'firstname must be more than 3 character', () => {
		enforce(data.firstname).longerThan(2);
	});
	test('lastname', 'lastname is required', () => {
		enforce(data.lastname).isNotEmpty();
	});

	test('lastname', 'lastname must be more than 3 character', () => {
		enforce(data.lastname).longerThan(2);
	});

	test('password', 'Password is required', () => {
		enforce(data.password).isNotEmpty();
	});

	test('password', 'Password must be longer than 5 character', () => {
		enforce(data.password).longerThan(5);
	});
	test('confirm_password', 'Passwords do not match', () => {
		enforce(data.confirm_password).equals(data.password);
	});
});

export default suite;
