# Tukkuliikkeen tilaustenkäsittely

### Aihekuvaus ([IS98JP2](https://advancedkittenry.github.io/suunnittelu_ja_tyoymparisto/aiheet/Tukkuliikkeen_tilaustenksittely.html))
Tehtävänä on laatia järjestelmä, jolla voidaan hoitaa tukkuliikkeen tilaustenkäsittely, varaston ylläpito sekä asiakaslaskutus. Asiakkaat jättävät tilaukset elektronisten lomakkeiden avulla ja saavat myös järjestelmältä automaattisesti vahvistuksen tai ilmoituksen, miksi tilausta ei voida hyväksyä. Tilausta ei voida hyväksyä, jos tilattavaa tuotemäärä ei ole varastossa tai asiakkaalla on viivästyneitä ja edelleen maksamattomia laskuja. Jokaiselle varastotuotteelle on määritelty tilauskynnys ja sen tultua alitetuksi luodaan automaattisesti varaston täydennystilaus tuotteen tuottajalle. Asiakkaalle toimistetuista tuotteista pidetään kirjaa. Toimistusten jälkeen asiakkaalle lähetetään lasku. Myös laskujen maksuseuranta kuuluu järjestelmän piiriin.

Huom. Eri toimintojen käynnistäminen voi olla manuaalinen toimenpide tai ne voidaan tehdää automaattisiksi laukaisimien avulla. Kysy aiheesta lisää ohjaajalta.

Toimintoja:

* asiakkaan ja ylläpidon kirjautuminen
* tilausten vastaanotto
* tuotteen lisäys/poisto varastosta
* tuotteen muokkaus
* asiakkaan luottokelpoisuuden tarkastus
* laskun tuottaminen
* karhujen tuottaminen
* maksujen vastaanottaminen
* varaston selaus
* asiakastietojen lisäys, muutos, poisto ja selaus

### Käyttötapauskaavio
* [linkki](documentation/käyttötapauskaavio.png)

### Tietokantakaavio
* [linkki](documentation/tietokantakaavio.png)

### Heroku
* https://tsoha-tukkuliike.herokuapp.com/
* user:password
