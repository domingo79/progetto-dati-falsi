"""
Generatore di Dati Falsi per eseguire esercizi durante il Corso Python

Un pacchetto leggero e semplice per generare dati casuali di persone, indirizzi, numeri di telefono 
e anagrafiche, utili per popolamento di database, testing o esercizi del corso.

---

Funzione Principale:

- genera_persona(): 
    Restituisce un dizionario completo contenente tutti i dati aggregati (anagrafica, telefono, 
    indirizzo, età, data di nascita, codice fiscale e comune) in una singola chiamata.

---

Altre Funzioni Utili:

Se si ha bisogno di generare solo componenti specifiche, sono disponibili le seguenti:

- genera_anagrafica(): Genera nome, cognome e sesso.
- genera_telefono(): Genera un numero di cellulare fittizio.
- genera_strade(): Genera un indirizzo stradale (odonimo, nome e civico).
- genera_comune(): Genera un Comune, CAP e Provincia.
- genera_eta_e_data_nascita(): Genera una data di nascita casuale e l'età corrispondente.

Tutte le funzioni supportano l'uso di un parametro 'seed' per garantire la riproducibilità dei dati 
generati.
"""

from .funzioni import (
    genera_anagrafica,
    genera_lavoro,
    genera_email,
    genera_stato_civile,
    genera_strade,
    genera_telefono,
    genera_comune,
    genera_persona,
    genera_eta_e_data_nascita,
)
