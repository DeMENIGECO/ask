# Contributing to AskSearch

Grazie per il tuo interesse nel contribuire ad AskSearch!  
Questo progetto è un motore di ricerca artigianale completamente offline, basato su un crawler Python e un mini‑database JavaScript.  
Ogni contributo è benvenuto: bugfix, miglioramenti, nuove funzionalità, ottimizzazioni del crawler, UI, ranking, ecc.

---

## 🧩 Come contribuire

### 1. Fai un fork del repository
Crea una copia del progetto nel tuo account GitHub.

### 2. Crea un branch per la tua modifica
Usa un nome chiaro, ad esempio:
feature/ranking
fix/crawler-timeout
improvement/ui-layout

Codice

### 3. Applica le modifiche
Puoi contribuire a:

- startpage (index.html)
- pagina dei risultati (browser/qoc.html)
- motore di ricerca JS
- crawler Python
- mini-db.js
- documentazione

---

## 🕷️ Modifiche al crawler

Se modifichi:
crawler/domains_settings.py

Codice

GitHub Actions eseguirà automaticamente:

- installazione dipendenze
- esecuzione crawler
- generazione mini-db.js
- copia in browser/mini-db.js
- commit automatico con messaggio:
Crawl Database

Codice

Non devi fare nulla manualmente.

---

## 🔍 Come testare il crawler localmente

1. Installa Python 3
2. Installa le dipendenze:
pip install requests beautifulsoup4

Codice
3. Avvia il crawler:
cd crawler
python crawl.py

Codice
4. Copia il file generato:
mini-db.js → browser/mini-db.js

Codice

---

## 🌐 Come testare AskSearch

1. Apri `index.html` nel browser
2. Digita una ricerca
3. Verrai reindirizzato a:
browser/qoc.html?q=la_tua_ricerca

Codice
4. Verifica che i risultati siano corretti

---

## 📥 Pull Request

Quando sei pronto:

1. Assicurati che il codice sia pulito e commentato
2. Assicurati che il crawler funzioni
3. Assicurati che AskSearch si avvii correttamente
4. Apri una Pull Request con una descrizione chiara:
   - cosa hai cambiato
   - perché
   - come testarlo

---

## 📄 Linee guida di stile

- HTML/CSS semplice e leggibile
- JavaScript senza dipendenze esterne
- Python chiaro, senza librerie non necessarie
- Commenti brevi e utili
- Nomi di variabili descrittivi

---

## 🤝 Grazie!

Ogni contributo aiuta AskSearch a crescere.  
Se hai idee, suggerimenti o nuove funzionalità, apri pure una Issue.
