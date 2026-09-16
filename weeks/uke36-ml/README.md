# Uke 36 — Machine Learning

**31. aug - 6. sep** · ML modul 1: Introduksjon til maskinlæring

Reading: [`../../ml/book-homl/chapter-map.md`](../../ml/book-homl/chapter-map.md)

## Posted by the lecturer

### Introduksjon til maskinlæring

I denne første modulen skal vi sette oss inn i hva maskinlæring er og hva det kan brukes til, men vi går ganske rett på sak og skal få oss litt praktisk erfaring med hvordan data brukes til å løse ulike oppgaver.

Læringsmål

  - Forstå grunnleggende begrep og konsept i maskinlæring, og få en forståelse for situasjoner der ML er et godt (eller dårlig) valg for å løse en oppgave

  - Forstå elementene som inngår i oppsett av et komplett softwareprodukt som baserer seg på maskinlæring

  - Kunne bruke verktøy/bibliotek til å kunne trene en maskinlæringsmodell og gjøre prediksjoner på enkle datasett

Kapittel i boken

  - Kap. 1: The Machine Learning Landscape (kan leses gratis her)

  - Kap. 2: End-to-End Machine Learning Project

  - Kap. 3: Classification

Oppgaver

Ligger ute under kursets GitHub-side

Ekstra ressurser

Info om Python og om bibliotekene vi kommer til å bruke er lagt ut under Kom igang med Python og ML-bibliotekene. Bruk gjerne litt ekstra tid de neste to ukene på å bli komfortabel med Python, slik at du blir produktiv resten av semesteret.

For flere eksempler på hvor og når det er bra å bruke maskinlæring, se Google for Developers sitt minikurs i ML Problem Framing.

**Files:**
- CCComputing-CompAtCERN_7090-1.jpg

**Links:**
- https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/ch01.html
- https://github.com/HVL-ML/DAT158
- https://developers.google.com/machine-learning/problem-framing

### Kom igang med Python og ML-bibliotekene

Python

For maskinlæringsdelen av kurset bruker vi Python, som er det mest populære programmeringsspråket for nettopp ML. Vi kommer til å gjøre oppgavene i notebooks, som lar oss blande kode, resultater og dokumentasjon i et lett lesbart dokument. Det er to muligheter for å kjøre notebooks, enten ved å installere python og nødvendige bibliotek på din egen maskin, eller ved å bruke (gratis) skytjenester.

Skybaserte løsninger

Dersom en har en Google-konto (f.eks. gjennom GMail), har en allerede tilgang til Google Colaboratory, der en kan kjøre notebooks som er ferdig satt opp med bibliotekene vi trenger. Notebooks lagres da rett i din Google Disk. Andre tilsvarende alternativer er f.eks. Kaggle Notebooks og DeepNote. Alle disse er gratis (men en kan kjøpe mer lagring og ressurser dersom en føler for det).

Installere Python på egen maskin

Internett er fullt av instruksjoner for å installere Python, så det er god hjelp der. En kan enten laste ned installasjonsfilene direkte fra https://www.python.org/downloads/, eller bruke app store på de respektive plattformene. Vi bruker versjon >= 3.7, så hvis du allerede har en passelig ny versjon installert, så er det tilstrekkelig.

  - Windows: I Microsoft Store, installer "Python 3.12"

  - Mac: Installer XCode (og XCode Command Line Tools, skal i utgangspunktet følge med)

  - Linux:  sudo apt-get install python3

Sjekk at det funker ved å kjøre

python3 --version

(eller bare python --version) i terminalen eller i PowerShell.

Dersom ting funker som det skal, er vi klare til å installere bibliotekene vi skal bruke -- da er bare å gå til kursets GitHub og følge instruksjonene der.

Git

Oppgavene gjøres tilgjengelige i kursets GitHub-repository, og det forventes også at det avsluttende prosjektet leveres som et åpent tilgjengelig repo. For å komme i gang med versjonskontoll i Git, følg gjerne forklaringen under Getting started with Git her.

Ressurser for å lære Python og ML-bibliotekene

Vi går gjennom litt intromateriell om Python og notebooks på forelesning, men det finnes gode tutorials som vi anbefaler å gå gjennom på forhånd, for å stille mer forberedt. Dette er frivillig, men krever ikke så mye tid.

Python:

  - Kaggle Learn sitt kurs i Python går gjennom det meste vi trenger i kurset, og er også skrevet i notebooks. Etter hvert i semesteret er også kurset Intro to Machine Learning supert å gå gjennom -- og det er også linker her til mer avanserte tutorials i maskinlæring. Kurset i Data Visualization er også stilig.

  - Google Edu sitt kurs i Python går inn på en del detaljer i språket som kan være interessant å få med seg, i tillegg til Kaggle-kurset. Her er det også tilhørende youtube-videoer.

Scikit-learn:

  - Dokumentasjonen til scikit-learn-biblioteket har gode beskrivelser av (og referanser til) de ulike maskinlæringsmodellene vi kommer til å bruke. Se User Guide for all info.

Pandas:

  - Kaggle Learn har et eget minikurs i Pandas.

  - Dokumentasjonen inneholder også en 10-minutters guide til de sentrale funksjonene.

**Files:**
- _0f757c07-5f2a-4730-93b3-ebf111f37f86.jpg

**Links:**
- https://jupyter.org/
- https://colab.google/
- https://www.kaggle.com/code
- https://deepnote.com/
- https://www.python.org/downloads/
- https://github.com/HVL-ML/DAT158
- https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources
- https://www.kaggle.com/learn/python
- https://www.kaggle.com/learn/intro-to-machine-learning
- https://www.kaggle.com/learn/data-visualization
- https://developers.google.com/edu/python
- https://scikit-learn.org/stable/
- https://www.kaggle.com/learn/pandas
- https://pandas.pydata.org/docs/user_guide/10min.html

## In this folder

- `slides/` — 4 item(s), 107 KB
  - `3-metrics.html`
  - `3-metrics_files`
  - `4-ml-engineering.html`
  - `4-ml-engineering_files`
- `exercises/` — empty
- `code/` — empty

---

<!-- Generated by src/canvas_sync.py. Do not edit — re-run the script. -->
