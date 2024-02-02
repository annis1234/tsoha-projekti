# Instagrammable Helsinki


Sovellus on karttasovellus, joka näyttää Helsingin parhaimmat Instagram-kuvauslokaatiot. Sisäänkirjautumisen jälkeen
sovelluksen etusivulla on karttanäkymä, joka näyttää sovellukseen lisätyt kohteet pisteinä. Karttaa napauttamalla käyttäjä voi
lisätä sovellukseen uuden kohteen. Jokaisella kohteella on nimi ja lyhyt tekstimuotoinen kuvaus. Kohteille on myös mahdollista
antaa tykkäyksiä ja kommentteja. Kohdetta klikkaamalla käyttäjälle avautuu näkymä kohteen tiedoista sekä sen saamista
tykkäyksistä ja kommenteista.

Ylläpito-oikeudet omaava käyttäjä voi poistaa luotuja kohteita.

# Käynnistysohjeet

Kloonaa repositorio koneellesi ja siirry sen juurihakemistoon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavasti:\
DATABASE_URL=<"tietokannan paikallinen osoite">\
SECRET_KEY=<"salainen-avain">

Aktivoi virtuaaliympäristö ja asenna riippuvuudet:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements
```

Sovellus käyttää PostgreSQL-tietokantaa. Tietokannan skeema määritetään komennolla:
```bash
psql < schema.sql
```

Sovellus käynnistetään komennolla
```bash
flask run
```

# Välipalautus 4.2.

Käyttäjä pystyy luomaan käyttäjätunnuksen ja kirjautumaan sisään sovellukseen. Toistaiseksi kaikki käyttäjät ovat peruskäyttäjiä, joilla on
samat käyttöoikeudet.

Sisäänkirjautumisen jälkeen käyttäjä näkee pohjakartan, jossa näkyvät kaikki tietokantaan lisätyt pisteet. Käyttäjä voi lisätä pisteen kartalle
klikkaamalla karttaa, jolloin kartan alapuolelle aukeaa lomake, johon syötetään kohteen nimi ja kuvaus. Kohde lisätään klikkaamalla painiketta
"Lisää uusi kohde". Käyttäjä voi klikata kartalla näkyviä pisteitä, jolloin aukeaa kohteen tiedot näyttävä sivu.
