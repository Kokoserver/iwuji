import type { UserLoginInput } from '$root/lib/interface/auth.interface';
import { create, test, enforce, only } from 'vest';

const suite = create((data: UserLoginInput, currentField: string) => {
	only(currentField);
	test('username', 'email is required', () => {
		enforce(data.username).isNotBlank();
	});

	test('username', 'Enter a valid email address', () => {
		enforce(data.username).matches(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/);
	});

	test('password', 'Username must be at least 3 characters long', () => {
		enforce(data.password).isNotEmpty();
	});
});

export default suite;
