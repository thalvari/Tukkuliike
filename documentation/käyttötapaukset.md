# Käyttötapaukset

### Asiakas

##### Käyttötapauskaavio
![](/documentation/asiakas_käyttötapauskaavio.jpg)

##### Valikoituja SQL-kyselyitä
* Lisää tuote ostoskoriin:

```INSERT INTO user_item (date_created, date_modified, item_id, user_id, quantity, ordered) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 2, 10, 0)```

* Selaa ostoskoria:

```SELECT * FROM user_item JOIN item ON item.id = user_item.item_id WHERE user_item.user_id = 2 AND user_item.ordered = 0 ORDER BY item.name LIMIT 5 OFFSET 0```

* Tee tilaus:

```UPDATE user_item SET date_modified=CURRENT_TIMESTAMP, ordered=1 WHERE user_item.id = 1```

```UPDATE item SET date_modified=CURRENT_TIMESTAMP, stock=10 WHERE item.id = 1```

### Vierailija

##### Käyttötapauskaavio
![](/documentation/vierailija_käyttötapauskaavio.jpg)

##### Valikoituja SQL-kyselyitä
* Rekisteröidy:

```INSERT INTO account (date_created, date_modified, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'user', '12345678', 'CUSTOMER')```

* Hae tuotetta:

```SELECT * FROM item WHERE item.name LIKE '%t%' ORDER BY item.name LIMIT 5 OFFSET 0```

### Ylläpitäjä

##### Käyttötapauskaavio
![](/documentation/ylläpitäjä_käyttötapauskaavio.jpg)

##### Valikoituja SQL-kyselyitä
* Luo karhu:

```UPDATE invoice SET date_modified=CURRENT_TIMESTAMP, total=1100 WHERE invoice.id = 1```

* Selaa tuotteita:

```SELECT * FROM item ORDER BY item.name LIMIT 5 OFFSET 0```

* Poista käyttäjä:

```DELETE FROM user_item WHERE user_item.user_id = 2```

```DELETE FROM invoice WHERE invoice.user_id = 2```

```DELETE FROM account WHERE account.id = 2```
