# DAT158-1 26H Maskinlæring og videregående algoritmer

Mirrored from Canvas by `src/canvas_sync.py`. **Do not edit by hand** —
re-run the script instead. Per-week records are in `weeks/*/README.md`.

Course: `DAT158-1 26H` (id 35853)

## Canvas sections

| Section | Link |
|---|---|
| Heim | /courses/35853 |
| Personar | /courses/35853/users |
| Kunngjeringar | /courses/35853/announcements |
| Modular | /courses/35853/modules |
| Oppgåver | /courses/35853/assignments |
| Vurderingar | /courses/35853/grades |
| Panopto video | /courses/35853/external_tools/1650 |
| Zoom | /courses/35853/external_tools/1247 |
| Pensum/Litteratur | /courses/35853/external_tools/2182 |
| Notebook | /courses/35853/notebook |

## Modules

### ML modul 1: Introduksjon til maskinlæring

- **Introduksjon til maskinlæring** — Page
- **Kom igang med Python og ML-bibliotekene** — Page

### Advanced algorithms

- **Veke 35 (24.08 - 30.08)** — Page

## Pages

### DAT158-1 25H Maskinlæring og videregående algoritmer

*Module: Front page · updated 2026-08-21T07:07:49Z*

Velkommen til DAT158 - Maskinlæring og videregående algoritmer

Gå til Moduler for å komme i gang.

Praktisk informasjon

Emnebeskrivelse: https://www.hvl.no/studier/studieprogram/emne/DAT158

Forelesere: Sven-Olai Høyland, Steffen Mæland og Erlend Raa Vagset

Studentassistenter: TBA

Timeplan og rom: TimeEdit

Repo for ML-delen: GitHub

Discord-server: invite

Fremdriftsplan

Planen oppdateres underveis -- sjekk innom regelmessig

Uke
Del
 Tema

34
17. - 23. aug

ML

 ML modul 1: Introduksjon til maskinlæring

 Zoomlenke for Førde og Haugesund: Zoom

Onsdag: Forelesningsnotater

Fredag: Forelesningsnotater

35
24. - 30. aug

Alg

 Algoritmer - Tekstprosessering

36
31. aug - 6. sep
ML

 ML modul 1: Introduksjon til maskinlæring

37
7. - 13. sep
Alg

 Algoritmer - NP-completeness, Chapter 1

38
14. - 20. sep
Alg

Chapter 2

39
21. - 27. sep
ML

 ML modul 2: Maskinlæringsmodeller

40
28. sep - 4. okt
ML

 ML modul 2: Maskinlæringsmodeller

41
5. - 11. okt
Alg

 Chapter 3 & Chapter 4

42
12. - 18. okt
Alg

43
19. - 25. okt
ML

 ML modul 3: End-to-end maskinlæringssystem

44
26. okt - 1. nov
ML

  ML modul 3: End-to-end maskinlæringssystem

45
2. - 8. nov
Alg

Chapter 6 & 7

46
9. - 15. nov
Alg

47
16. - 21. nov
ML

Eksamen

 08.12.2026 kl. 09:00

 Mer info på StudentWeb

**Attached files:**
- DAT158-course-logo.png
- FinalCurriculum_2025.pdf

**Links:**
- https://www.hvl.no/studier/studieprogram/emne/DAT158
- https://www.hvl.no/en/employee/?user=3600298
- https://www.hvl.no/person/?user=Steffen.Meland
- https://www.hvl.no/person/?user=Erlend.Raa.Vagset
- https://cloud.timeedit.net/hvl/web/pen/riqY8y5X0gvZ71QZQ525717Q67876X6Y71161Z5Q60o8YY76X1876Q77Y767c8Zp7QZq1Qo.html
- https://github.com/HVL-ML/DAT158
- https://discord.gg/fYu4yh7kp
- https://hvl.zoom.us/j/63122964590?pwd=uCdb8RGnzbjZJNeafwlnOVJbEA9vpl.1
- https://hvl-ml.github.io/DAT158/slides/1-intro/1-intro.html
- https://hvl-ml.github.io/DAT158/slides/1-intro/2-python.html
- https://hvl-ml.github.io/DAT158/slides/3-systems/lecture3.html

### Introduksjon til maskinlæring

*Module: ML modul 1: Introduksjon til maskinlæring · updated 2026-08-04T13:54:35Z*

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

**Attached files:**
- CCComputing-CompAtCERN_7090-1.jpg

**Links:**
- https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/ch01.html
- https://github.com/HVL-ML/DAT158
- https://developers.google.com/machine-learning/problem-framing

### Kom igang med Python og ML-bibliotekene

*Module: ML modul 1: Introduksjon til maskinlæring · updated 2026-08-05T06:27:25Z*

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

**Attached files:**
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

### Veke 35 (24.08 - 30.08)

*Module: Advanced algorithms · updated 2026-08-20T08:42:30Z*

Startar med tekst behandling

Zoomlenke: Sjå praktisk informasjon på startsida

Kapittel frå lærebok: Kapittel_9_GoodrichAndTammassia.pdf

Det blir lagt ut lysark for heile tema / kapittel og så vil det bli opplyst kvar vi startar.

Lysark: Chapter 9 TextProcessing.pdf

Onsdag 26. augsust - Frå starten

Fredag 28. august - Planlagt, men kan bli endre: Forsettelse på lysark 31 (Standard tries)

Mentimeter for spørsmål: Mentimeter for Spørsmål.pdf

Oppgaver (obligatorisk): Kommer

**Attached files:**
- Kapittel_9_GoodrichAndTammassia.pdf
- Chapter 9 TextProcessing.pdf
- Mentimeter for Spørsmål.pdf

## Announcements

### Første forelesning

*Posted 2026-08-18T14:02:56Z*

Hei og velkommen til første forelesning i DAT158 i morgen kl 10.15. I Bergen møtes vi i F118 (Aud 14), i Førde i VIE1070 (Balchen), og i Haugesund i Auditorium B. Det blir sprek info om innhold og opplegg i kurset, så møt opp!

## Assignments

*None published yet.*
