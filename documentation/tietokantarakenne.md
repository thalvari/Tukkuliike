# Tietokantarakenne

### Tietokantakaavio
![](/documentation/tietokantakaavio.jpg)

### Normalisointi
* kaikki tietokantataulut ovat ensimmäisessä normaalimuodossa, koska sarakkeiden arvot eivät sisällä listoja, eivät muodosta toistuvia ryhmiä, yhden sarakkeen arvot ovat samaa tyyppiä, sarakkeiden nimet ovat uniikkeja kussakin taulussa ja sarakkeiden/rivien järjestys ei vaikuta tietokantataulun toimintaan
* kaikki tietokantataulut ovat toisessa normaalimuodossa, koska ne ovat ensimmäisessä normaalimuodossa ja jokaisessa taulussa on erikseen määritelty pääavain
* taulut invoice ja user_item ovat kolmannessa normaalimuodossa, koska ne ovat toisessa normaalimuodossa ja niiden sarakkeet eivät ole transitiivisesti riippuvaisia taulun pääavaimesta
* taulut item ja account eivät ole kolmannessa normaalimuodossa, koska käytettävyyden kannalta on järkevää, että käyttäjänimet sekä tuotteiden nimet ovat uniikkeja

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
)
```
