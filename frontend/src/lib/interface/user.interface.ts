export interface UserRegisterInput {
	email: string;
	firstname: string;
	lastname: string;
	password: string;
}

export interface PasswordResetOut {
	token: string;
	password: string;
	confirm_password: string;
}

export interface GetPasswordResetLink {
	email: string;
}

export interface TokenDataIn {
	refresh_token: string;
	access_token: string;
}

export interface UserRefreshTokenInput {
	refresh_token: string;
}

export interface UserPermissionUpdateOut {
	user_id: number;
	role: string;
}

export interface UserAccountVerifyToken {
	token: string;
}

export interface UserRoleIn {
	name: string;
}
export interface UserDataIn {
	id: number;
	email: string;
	firstname: string;
	lastname: string;
	is_active: boolean;
	role: UserRoleIn;
}
