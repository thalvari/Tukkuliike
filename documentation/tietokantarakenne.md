# Tietokantarakenne

### Tietokantakaavio
![](/documentation/tietokantakaavio.jpg)

### CREATE TABLE -lauseet
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
)
```
```
CREATE TABLE item (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	price INTEGER NOT NULL, 
	stock INTEGER NOT NULL, 
	threshold INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)
```
```
CREATE TABLE invoice (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	user_id INTEGER NOT NULL, 
	total INTEGER NOT NULL, 
	payed BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	CHECK (payed IN (0, 1))
)
```
```
CREATE TABLE user_item (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	item_id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	quantity INTEGER NOT NULL, 
	ordered BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(item_id) REFERENCES item (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	CHECK (ordered IN (0, 1))
```
