# iwaju

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the MIT license.
[tool.poetry]
name = "iwaju"
version = "0.1.0"
description = ""
authors = ["kokoserver <owonikokoolaoluwa@gmail.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.8.10"
ormar = {extras = ["postgresql"], version = "^0.11.2"}
fastapi = {extras = ["all"], version = "^0.80.0"}
python-slugify = "^6.1.2"
aiosqlite = "^0.17.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
passlib = {extras = ["bcrypt"], version = "^1.7.4"}

[tool.poetry.dev-dependencies]
