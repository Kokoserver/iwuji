import type { AddressOut } from '$root/lib/interface/address.interface';
import { create, test, enforce, only } from 'vest';

const suite = create((data: AddressOut, currentField: string) => {
	only(currentField);
	test('street', 'street is required', () => {
		enforce(data.street).isNotBlank();
	});

	test('state', 'state is required', () => {
		enforce(data.city).isNotBlank();
	});

	test('state', 'state is required', () => {
		enforce(data.state).isNotBlank();
	});

	test('country', 'country is required', () => {
		enforce(data.country).isNotBlank();
	});

	test('zipcode', 'zipcode is required', () => {
		enforce(data.zipcode).isNotBlank();
	});
});

export default suite;
