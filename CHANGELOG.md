# Changelog

Tutti i cambiamenti significativi a questo progetto saranno documentati in questo file.
Il formato è basato su [Keep a Changelog].

## [0.2.0] - 2025-11-08
### Aggiunto (Added)
- Aggiunta la funzione `genera_lavoro()` per generare una professione (declinata per sesso ed età pensionabile).
- Aggiunta la funzione `genera_email()` per generare un indirizzo email fittizio (username@dominio) basato sul nome e cognome della persona.
- Aggiunta la funzione `genera_stato_civile()` per generare uno stato civile casuale, declinato in base al sesso.
- Le nuove funzionalità sono state aggregate alla funzione principale `genera_persona()` per completare i dati del profilo fittizio.

## [0.1.2] - 2025-11-07
### Correzioni (Fixed)
- Risolto il bug `ValueError: Comune/Stato non valido` all'interno della funzione `genera_persona`. È stata implementata la gestione dell'errore tramite `try...except` durante la chiamata a `codicefiscale.genera_codice_fiscale` per garantire che il programma non si interrompa su nomi di comuni non standardizzati.

## [0.1.1] - 2025-10-25
### Aggiunto (Added)
- Aggiunta la funzione principale `genera_persona()` per l'aggregazione di tutti i dati fittizi.
- Introdotta la generazione di dati sensibili basati sull'età:
    - Calcolo dell'età e della data di nascita (`"eta"`, `"data_nascita"`).
    - Generazione del Codice Fiscale (`"codice_fiscale"`) basato sui dati anagrafici.