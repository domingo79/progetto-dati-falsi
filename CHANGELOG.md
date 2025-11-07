# Changelog

Tutti i cambiamenti significativi a questo progetto saranno documentati in questo file.
Il formato è basato su [Keep a Changelog].

## [0.1.2] - 2025-11-07
### Correzioni (Fixed)
- Risolto il bug `ValueError: Comune/Stato non valido` nella funzione `genera_persona`. È stata implementata la gestione dell'errore tramite `try...except` durante la chiamata a `codicefiscale.genera_codice_fiscale` per assicurare che il programma non si interrompa su nomi di comuni non standardizzati.

## [0.1.1] - 2025-10-25
### Aggiunto (Added)
- Aggiunta la funzione principale `genera_persona()` per l'aggregazione di tutti i dati fittizi.
- Introdotta la generazione di dati sensibili basati sull'età:
    - Calcolo dell'età e della data di nascita (`"eta"`, `"data_nascita"`).
    - Generazione del Codice Fiscale (`"codice_fiscale"`) basato sui dati anagrafici.