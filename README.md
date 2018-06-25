# Tukkuliikkeen tilaustenkäsittely

### Aihekuvaus (muokattu [IS98JP2](https://advancedkittenry.github.io/suunnittelu_ja_tyoymparisto/aiheet/Tukkuliikkeen_tilaustenksittely.html))
Tehtävänä on laatia järjestelmä, jolla voidaan hoitaa tukkuliikkeen tilaustenkäsittely, varaston ylläpito sekä asiakaslaskutus. Asiakkaat jättävät tilaukset elektronisten lomakkeiden avulla. Tuotteet pitää ensin lisätä ostoskoriin. Järjestelmä osaa myös tarvittaessa ilmoittaa miksi tilausta ei voida hyväksyä. Tilausta ei voida hyväksyä, jos tilattavaa tuotemäärä ei ole varastossa tai asiakkaalla on maksamattomia karhuja. Jokaiselle varastotuotteelle on määritelty tilauskynnys ja sen tultua alitetuksi luodaan automaattisesti varaston täydennystilaus tuotteen tuottajalle. Asiakkaalle toimistetuista tuotteista pidetään kirjaa. Toimistusten jälkeen asiakkaalle lähetetään lasku. Myös laskujen maksuseuranta kuuluu järjestelmän piiriin.

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
7. muokataan Herokun tietokantaa komennolla ```heroku pg:psql```
8. lisätään ylläpitäjä komennolla ```INSERT INTO account (date_created, date_modified, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'admin', 'password', 'ADMIN')```
9. sovelluksen osoite Herokussa saadaan komennolla ```heroku info -s  | grep web_url | cut -d= -f2```

### Käyttöohje

##### Vierailija
* yläpalkista löytyy linkit tuotteiden selaamiseen, kirjautumiseen, sekä rekisteröitymiseen
* rekisteröitymissivulla voi rekisteröityä vain asiakkaan roolissa
* tuotteiden selaussivulla tuotteita voidaan hakea nimen perusteella tai siirtyä tietyn tuotteen tarkastelusivulle

##### Asiakas
* yläpalkista löytyy linkki tuotteiden selaamiseen
* klikkaamalla yläpalkin oikeasta laidasta löytyvää käyttäjänimeä, aukeaa valikko, josta löytyy linkit omien käyttäjätietojen muokkaamiseen, omien laskujen/omien tilausten/ostoskorin selaamiseen sekä uloskirjautumiseen
* tuotteiden selaussivulla tuotteita voidaan hakea nimen perusteella tai siirtyä tietyn tuotteen tarkastelusivulle
* tuotteen tarkastelusivulla voidaan sitä lisätä ostoskoriin haluttu määrä
* omien laskujen selaussivulla tietty lasku tai karhu voidaan maksaa
* ostoskorin selaussivulla sen sisältö voidaan tilata, tietyn tuotteen määrää ostoskorissa voidaan muuttaa tai tuote voidaan poistaa ostoskorista

##### Ylläpitäjä
* yläpalkista löytyy linkit uuden tuotteen lisäämiseen sekä käyttäjien/maksamattomien laskujen/tuotteiden selaamiseen
* klikkaamalla yläpalkin oikeasta laidasta löytyvää käyttäjänimeä, aukeaa valikko, josta löytyy linkit omien käyttäjätietojen muokkaamiseen sekä uloskirjautumiseen
* käyttäjien selaussivulla käyttäjiä voidaan hakea käyttäjänimen perusteella, siirtyä tietyn käyttäjän tarkastelusivulle/omien käyttäjätietojen muokkaamissivulle sekä poistaa tietty asiakas
* laskujen selaamissivulla laskuja voidaan hakea käyttäjänimen perusteella sekä luoda karhu erääntyneen laskun tilalle
* tuotteiden selaussivulla tuotteita voidaan hakea nimen perusteella, siirtyä tietyn tuotteen tarkastelu-/muokkaussivulle tai poistaa se järjestelmästä

### Rajoitteet
* ylläpitäjät lisätään tietokantaan manuaalisesti asennusohjeiden mukaisesti
* ylläpitäjiä ei voi poistaa
* sivutus on toteutettu s.e. kaikilla selaussivuilla on viisi alkiota
* kaikki laskut on asetettu erääntymään yhdessä minuutissa
* kaikkien karhujen viivästyskorko on 10%
* varaston täydennystilaus on aina kaksi kertaa tuotteen tilauskynnys
* tiettyä tuotetta voi olla ostoskorissa korkeintaan 99 kpl
* kaikki ajat UTC

### Puuttuvat ominaisuudet
* tuotekategoriat
* salasanojen tallennus salatussa muodossa
* erillinen asetussivu esim. sivutukselle, viivästyskorolle, erääntymisajalle ja aikavyöhykkeelle
* indeksien käyttö

### Omat kokemukset
* minulla oli aiemmin jonkin verran Python-kokemusta, mutta tämä oli ensimmäinen isompi projekti
* koska Python on kompakti kieli ja malli/näkymä -arkkitehtuuri selkeä, koodaaminen oli mukavaa ja uusien ominaisuuksien lisääminen suoraviivaista
* en ollut ennen käyttänyt Bootstrapia, mutta sen avulla oli helppo toteuttaa yleisiä web-sivujen komponentteja

### Muu dokumentaatio
* [käyttötapaukset](/documentation/käyttötapaukset.md)
* [tietokantarakenne](/documentation/tietokantarakenne.md)

### Heroku
* https://tsoha-tukkuliike.herokuapp.com/
* testiasiakas: ```user:12345678```
* testiylläpitäjä: ```admin:password```
