"""
Generatore di Dati Falsi per eseguire esercizi durante il Corso Python

Un pacchetto leggero e semplice per generare dati casuali di persone, indirizzi, numeri di telefono 
e anagrafiche, utili per popolamento di database, testing o esercizi del corso.

---

Funzione Principale:

- genera_persona(): 
    Restituisce un dizionario completo contenente tutti i dati aggregati (anagrafica, telefono, 
    indirizzo e comune) in una singola chiamata.

---

Altre Funzioni Utili:

Se si ha bisogno di generare solo componenti specifiche, sono disponibili le seguenti:

- genera_anagrafica(): Genera nome, cognome e sesso.
- genera_telefono(): Genera un numero di cellulare fittizio.
- genera_strade(): Genera un indirizzo stradale (odonimo, nome e civico).
- genera_comune(): Genera un Comune, CAP e Provincia.

Tutte le funzioni supportano l'uso di un parametro 'seed' per garantire la riproducibilità dei dati 
generati.
"""

from .funzioni import (
    genera_anagrafica,
    genera_strade,
    genera_telefono,
    genera_comune,
    genera_persona
)
