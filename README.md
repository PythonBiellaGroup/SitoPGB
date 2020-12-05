# SitoPGB

Sito di riferimento del Python Biella Group sviluppato durante il Corso Flask.

In questo portale si può:
1. Visualizzare l'elenco dei corsi attivi e passati
2. Inserire un nuovo corso
3. Definire delle giornate di corso
4. Fare login con un particolare utente (amministratore o normale)
5. A seconda dei permessi si potranno modificare o creare nuovi corsi oppure visualizzare l'elenco dei corsi
6. Creare articoli di blog con commenti

Ogni contributo al progetto è ben accetto! Sentitevi liberi di fare delle Pull Request attraverso GitHub con eventuali cambiamenti.
Oppure segnalare eventuali malfunzionamenti all'interno della sezione: **Issues** sempre su GitHub.

L'applicazione è stata realizzata interamente con Python Flask e Jinja 2 Template con Bootstrap.

**Step progettuali**
Elenco di cose trattate durante il corso:

1. Suddivisione in cartelle del progetto
2. Creare ambiente con venv
3. Definire app.py e __init__ del progetto + configurazione bootstrap locale
4. Definire i modelli dei dati e lanciare costruzione del database
5. Costruire i templates base usando bootstrap con pagine di errore
6. Costruire la vista dei corsi con form di compilazione + Visualizzazione dei risultati
7. Agganciare i corsi al DB
8. Costruire funzionalità di visualizzazione di tutti i corsi esistenti all'interno del database
9. Costruire funzionalità delle serate
10. Maschera di Login con funzionalità di Login e permessi di visualizzazione
11. Pagina di Blog
12. Finalizzazione e test sulla pagina
13. Gestione della sicurezza
14. Deploy
15. Heroku

**Bonus track** se abbiamo tempo di farlo
- Import dei dati passando da script SQL con SQLAlchemy (in modo da scriptare i dati di inizializzazione in modo più facile)
- Login con Google
- Docker con docker-compose
- Pipeline di deploy CI/CD con GitLab
- Pipeline di deploy CI/CD con GitHub
- Test browser con Selenium
- Test browser con Behave

Link e materiale utile
- Tema Bootstrap Italia: https://italia.github.io/bootstrap-italia/
- Behave: https://behave.readthedocs.io/en/latest/
  

# Lanciare l'app

Per lanciare l'applicazione in sviluppo è necessario configurare due variabili d'ambiente:
- FLASK_CONFIG : che consente di indicare il tipo di ambiente che si intende lanciare
- FLASK_APP : che si intende qual è il main file all'interno della cartella

Su Linux o Mac OS è sufficiente fare:
```
export FLASK_CONFIG="development" & FLASK_APP="app.py" python app.py
```

Per lanciare invece il docker contenente l'applicazione è necessario lanciare i seguenti comandi dopo esserti posizionato all'interno della cartella di progetto con il terminale
```
docker-compose build
docker-compose up -d
```
Dopo di che raggiungere l'indirizzo: http://localhost:5000 per visualizzare l'applicazione all'interno del docker container.

Per visualizzare i logs se dovessero esserci errori con docker: 
```
#consente di visualizzare i container lanciati
docker ps -a
#consente di visualizzare i log di errore
docker logs -t <nomecontainer> 

#per lanciare direttamente il dockerfile dopo averlo buildato (a scopo di test)
docker run -d --name sitopgb_web_test -p 5000:5000 -e "FLASK_APP=app.py" -e "FLASK_ENV=production" sitopgb_web flask run /usr/src/app/app.py --host 0.0.0.0
```