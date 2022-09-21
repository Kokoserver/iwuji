import { create, test, enforce, only } from 'vest';

const suite = create((data = {}, currentField) => {
	only(currentField);
	test('username', 'Email is required', () => {
		enforce(data.username).isNotBlank();
	});

	test('username', 'Username must be at least 3 characters long', () => {
		enforce(data.username).longerThan(2);
	});

	test('username', 'Enter a valid email address', () => {
		enforce(data.username).Matches([/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/]);
	});

	test('password', 'Password is required', () => {
		enforce(data.password).isNotEmpty();
	});

	test('password', 'Password must be longer than 5 character', () => {
		enforce(data.password).longerThan(5);
	});
	if (data.password) {
		test('confirm_password', 'Passwords do not match', () => {
			enforce(data.confirm_password).equals(data.password);
		});
	}
});

export default suite;
