# AskSearch

**AskSearch** è un motore di ricerca artigianale che funziona completamente **offline**.

Utilizza un crawler sviluppato in **Python** per indicizzare pagine web reali e generare un database JavaScript (`mini-db.js`). Questo database viene poi letto dal motore di ricerca nel browser per mostrare i risultati, senza richiedere alcun server.

## Caratteristiche

* 🔍 Motore di ricerca completamente offline
* 🐍 Crawler scritto in Python
* 📄 Database dei risultati in formato JavaScript (`mini-db.js`)
* 🌐 Nessun server richiesto
* 🚀 Compatibile con GitHub Pages
* ⚡ Semplice da personalizzare ed espandere

## Generare il database

Per creare o aggiornare il database dei risultati:

1. Assicurati di avere **Python** installato.

2. Installa le dipendenze necessarie:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Apri il terminale e spostati nella cartella del crawler:

   ```bash
   cd crawler
   ```

4. Avvia il crawler:

   ```bash
   python crawl.py
   ```

5. Al termine verrà generato il file:

   ```text
   mini-db.js
   ```

6. Copia `mini-db.js` nella cartella `browser/`, sostituendo il file esistente.

## Utilizzo

AskSearch funziona interamente lato client.

1. Apri `index.html` nel tuo browser.

2. Inserisci una ricerca nella pagina iniziale.

3. Verrai reindirizzato automaticamente a:

   ```text
   browser/qoc.html?q=la_tua_ricerca
   ```

4. La pagina dei risultati leggerà la query e mostrerà le corrispondenze presenti in `mini-db.js`.

## Personalizzazione

Puoi modificare facilmente il comportamento del crawler:

* aggiungere o rimuovere domini da indicizzare;
* modificare la profondità della scansione;

Per farlo è sufficiente modificare il file:

```text
crawler/domains_settings.py
```

## Come funziona

Il funzionamento di AskSearch è composto da due fasi:

1. **Crawler**

   * visita i siti configurati;
   * estrae titolo, descrizione e URL;
   * genera il database `mini-db.js`.

2. **Motore di ricerca**

   * legge il database nel browser;
   * confronta la query dell'utente con i dati indicizzati;
   * mostra i risultati senza effettuare connessioni a un server.

## Licenza

Questo progetto è distribuito con licenza **MIT**.
