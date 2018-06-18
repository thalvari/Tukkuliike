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

### Asennusohje
1. kloonataan repo komennolla ```git clone git@github.com:thalvari/Tukkuliike.git```
2. siirrytään kansioon ```Tukkuliike```
3. luodaan sovellukselle paikka Herokuun komennolla ```heroku create```
4. asetetaan vaadittu ympäristömuuttuja komennolla ```heroku config:set HEROKU=1```
5. lisätään Herokuun tietokanta komennolla ```heroku addons:add heroku-postgresql:hobby-dev```
6. työnnetään projekti Herokuun komennolla ```git push heroku master```
7. sovellus löytyy nyt Herokusta edellisen komennon antamasta osoitteesta

### Käyttöohje
##### Vierailija
* yläpalkista löytyy linkit tuotteideen selaamiseen, kirjautumiseen, sekä rekisteröitymiseen
* käyttäjällä on joko asiakkaan tai ylläpitäjän rooli
* tuotteiden selaussivulla voidaan tuotetta hakea sen nimen perusteella sekä tarkastella tiettyä tuotetta

##### Asiakas
* yläpalkista löytyy linkki tuotteiden selaamiseen
* tuotteiden selaussivulla voidaan tuotetta hakea sen nimen perusteella sekä tarkastella tiettyä tuotetta
* tuotteen tarkastelusivulla se voidaan lisätä ostoskoriin
* klikkaamalla yläpalkin oikeasta laidasta löytyvää käyttäjänimeä, aukeaa valikko, josta löytyy linkit omien käyttäjätietojen muokkaamiseen, omien laskujen/omien tilausten/ostoskorin selaamiseen ja uloskirjautumiseen
* omien laskujen selaussivulla tietty lasku voidaan maksaa
* ostoskorin selaussivulla sen sisältö voidaan tilata, tietyn tuotteen määrää ostoskorissa voidaan muuttaa tai tuote voidaan poistaa ostoskorista

##### Ylläpitäjä
* yläpalkista löytyy linkit uuden tuotteen lisäämiseen sekä käyttäjien/laskujen/tuotteiden selaamiseen
* klikkaamalla yläpalkin oikeasta laidasta löytyvää käyttäjänimeä, aukeaa valikko, josta löytyy linkit omien käyttäjätietojen muokkaamiseen ja uloskirjautumiseen
* käyttäjien selaussivulla voidaan käyttäjää hakea käyttäjänimen perusteella sekä poistaa tietty asiakas
* tuotteiden selaussivulla voidaan lisäksi muokata tiettyä tuotetta tai se voidaan poistaa järjestelmästä

### Muu dokumentaatio
* [asiakkaan käyttötapauskaavio](https://raw.githubusercontent.com/thalvari/Tukkuliike/master/documentation/asiakas_käyttötapauskaavio.jpg)
* [vierailijan käyttötapauskaavio](https://raw.githubusercontent.com/thalvari/Tukkuliike/master/documentation/vierailija_käyttötapauskaavio.jpg)
* [ylläpitäjän käyttötapauskaavio](https://raw.githubusercontent.com/thalvari/Tukkuliike/master/documentation/ylläpitäjä_käyttötapauskaavio.jpg)
* [tietokantakaavio](https://raw.githubusercontent.com/thalvari/Tukkuliike/master/documentation/tietokantakaavio.jpg)

### Heroku
* https://tsoha-tukkuliike.herokuapp.com/
* testiasiakas: ```user:12345678```
* testiylläpitäjä: ```admin:password```
