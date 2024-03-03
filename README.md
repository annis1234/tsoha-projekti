# Instagrammable Helsinki

# Loppupalautus 3.3.

Sovellus on karttasovellus, joka näyttää Helsingin parhaimmat Instagram-kuvauslokaatiot. Sisäänkirjautumisen jälkeen
sovelluksen etusivulla on karttanäkymä, joka näyttää sovellukseen lisätyt kohteet pisteinä. Lisäksi etusivulla näkyy
lisättyjen kohteiden lukumäärä sekä viisi tykätyintä kohdetta. Käyttäjän on mahdollista zoomata karttanäkymä
suosituimpiin kohteisiin ja avata niiden kohdetiedot etusivun linkkien kautta.

Karttaa napauttamalla käyttäjä voi lisätä sovellukseen uuden kohteen. Jokaisella kohteella on nimi ja tekstimuotoinen kuvaus.
Kohteille on myös mahdollista antaa tykkäyksiä ja kommentteja. Kohdetta klikkaamalla käyttäjälle avautuu näkymä kohteen tiedoista sekä sen saamista
tykkäyksistä ja kommenteista.

Käyttäjä voi poistaa tietokannasta ne kohteet, jotka hän on itse sinne lisännyt.

# Välipalautus 18.2.

Sovellukseen lisätty tykkäys- ja kommentointimahdollisuus kohteille. Kohteita voi nyt myös poistaa. Lisätty myös mahdollisuus
lisätä kohteesta kuva kohdesivulle.

Toistaiseksi kaikilla käyttäjillä on samat oikeudet. Viimeistelyvaiheessa on tarkoitus lisätä käyttäjille peruskäyttäjän
ja ylläpitäjän käyttöoikeudet, ja parannella virheidenkäsittelyä sekä sovelluksen ulkoasua.

# Välipalautus 4.2.

Käyttäjä pystyy luomaan käyttäjätunnuksen ja kirjautumaan sisään sovellukseen. Toistaiseksi kaikki käyttäjät ovat peruskäyttäjiä,
joilla on samat käyttöoikeudet.

Sisäänkirjautumisen jälkeen käyttäjä näkee pohjakartan, jossa näkyvät kaikki tietokantaan lisätyt pisteet. Käyttäjä voi lisätä
kohteen klikkaamalla karttaa, jolloin kartan alapuolelle aukeaa lomake, johon syötetään kohteen nimi ja kuvaus. Kohde lisätään
klikkaamalla painiketta "Lisää uusi kohde". Käyttäjä voi klikata kartalla näkyviä pisteitä, jolloin aukeaa kohteen tiedot näyttävä
sivu.

# Käynnistysohjeet

Kloonaa repositorio koneellesi ja siirry sen juurihakemistoon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavasti:

```bash
DATABASE_URL=<'tietokannan-paikallinen-osoite'>
SECRET_KEY=<'salainen-avain'>
```

Aktivoi virtuaaliympäristö ja asenna riippuvuudet:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

Sovellus käyttää PostgreSQL-tietokantaa. Tietokannan skeema määritetään komennolla:
```bash
psql < schema.sql
```

Sovellus käynnistetään komennolla
```bash
flask run
```
