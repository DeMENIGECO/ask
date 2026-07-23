# AskSearch  
AskSearch è un motore di ricerca artigianale completamente offline.  
Utilizza un crawler Python per indicizzare siti reali e genera un file JavaScript (mini-db.js) che viene usato dal motore per mostrare i risultati nel browser.

## Come crawlerare  
Per generare il database dei risultati:

- Assicurati di avere Python installato.  
- Installa le dipendenze richieste:  
  Python + requests + bs4  
- Apri il terminale e vai nella cartella del crawler:  
  cd crawler  
- Avvia il crawler:  
  python crawl.py  
- Al termine, il crawler genererà il file:  
  mini-db.js  
- Copia mini-db.js nella cartella browser/  
  (sovrascrivi quello esistente)

## Come avviare AskSearch  
AskSearch funziona completamente offline.

- Apri index.html nel browser  
- Digita una ricerca nella startpage  
- Verrai reindirizzato automaticamente alla pagina:  
  browser/qoc.html?q=la_tua_ricerca  
- La pagina dei risultati leggerà la query e mostrerà i risultati presenti nel mini-db.js

## Note  
- Il crawler può indicizzare qualsiasi dominio modificando la lista dei siti nel file crawl.py  
- AskSearch non richiede server: funziona interamente lato client  
- Può essere pubblicato facilmente tramite GitHub Pages  

## Licenza  
MIT License.
