# Contributing to AskSearch

Grazie per il tuo interesse nel contribuire ad **AskSearch**! 🎉

AskSearch è un motore di ricerca artigianale completamente **offline**, composto da un crawler sviluppato in **Python** e da un motore di ricerca interamente eseguito nel browser.

Sono benvenuti contributi di ogni tipo: correzioni di bug, miglioramenti delle prestazioni, nuove funzionalità, ottimizzazioni del crawler, miglioramenti dell'interfaccia e della documentazione.

---

# Come contribuire

## 1. Fai un fork del repository

Crea una copia del repository nel tuo account GitHub.

## 2. Crea un nuovo branch

Utilizza un nome descrittivo per la modifica che stai sviluppando.

Esempi:

```text
feature/ranking
feature/search-filters
fix/crawler-timeout
fix/results-order
improvement/ui-layout
docs/update-readme
```

## 3. Sviluppa la tua modifica

Puoi contribuire a qualsiasi parte del progetto, ad esempio:

* `index.html` (pagina iniziale)
* `browser/qoc.html` (pagina dei risultati)
* motore di ricerca JavaScript
* crawler Python
* generazione di `mini-db.js`
* documentazione
* ottimizzazioni e refactoring

---

# Modifiche al crawler

Se la tua Pull Request modifica il file:

```text
crawler/domains_settings.py
```

GitHub Actions eseguirà automaticamente il processo di aggiornamento del database:

1. installazione delle dipendenze;
2. esecuzione del crawler;
3. generazione del nuovo `mini-db.js`;
4. copia del file in `browser/mini-db.js`;
5. commit automatico con il messaggio:

```text
Crawl Database
```

Non è necessario eseguire manualmente questi passaggi.

---

# Testare il crawler localmente

Installa le dipendenze:

```bash
pip install requests beautifulsoup4
```

Spostati nella cartella del crawler:

```bash
cd crawler
```

Avvialo:

```bash
python crawl.py
```

Al termine copia il file generato:

```text
mini-db.js
```

nella cartella:

```text
browser/
```

sostituendo quello esistente.

---

# Testare AskSearch

1. Apri `index.html` nel browser.
2. Inserisci una ricerca.
3. Verrai reindirizzato automaticamente a:

```text
browser/qoc.html?q=la_tua_ricerca
```

4. Verifica che i risultati mostrati siano corretti e coerenti con il database generato.

---

# Pull Request

Prima di aprire una Pull Request assicurati che:

* il codice sia leggibile e ben organizzato;
* il crawler funzioni correttamente;
* AskSearch si avvii senza errori;
* eventuali modifiche siano state testate.

Nella descrizione della Pull Request indica:

* cosa hai modificato;
* perché hai apportato la modifica;
* come è possibile testarla.

---

# Linee guida

### HTML e CSS

* Mantieni il codice semplice e leggibile.
* Evita codice duplicato quando possibile.

### JavaScript

* Non utilizzare librerie esterne, salvo casi eccezionali.
* Scrivi codice chiaro e facilmente mantenibile.

### Python

* Mantieni il crawler semplice e portabile.
* Evita dipendenze non necessarie.
* Prediligi nomi di variabili descrittivi.

### Documentazione

* Aggiorna il README quando aggiungi nuove funzionalità.
* Mantieni esempi e istruzioni sempre aggiornati.

---

# Segnalazione di bug

Se trovi un problema:

1. verifica che non sia già stato segnalato;
2. apri una nuova Issue;
3. descrivi il problema nel modo più dettagliato possibile;
4. includi, se possibile, screenshot, log o passaggi per riprodurlo.

---

# Idee e nuove funzionalità

Hai un'idea per migliorare AskSearch?

Apri una **Issue** e descrivi la proposta. Ogni suggerimento è ben accetto e può contribuire a rendere il progetto migliore.

---

# Grazie ❤️

Ogni contributo, piccolo o grande, aiuta AskSearch a crescere.

Grazie per dedicare il tuo tempo al progetto!
