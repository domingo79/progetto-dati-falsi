# generatore — Progetto 'progetto-dati-falsi'

Pacchetto Python per generare dati fittizi (nomi, indirizzi, numeri di telefono, ecc.) pensato per uso didattico.

## Contenuto del pacchetto
Il pacchetto espone (import da `generatore`):
- `genera_anagrafica(titoli: bool = False, seed: int | None = None)` — genera un dizionario con `nome`, `cognome`, `sesso` e opzionalmente `titolo`. Accetta `seed` per riproducibilità.
- `genera_strade()` — genera un indirizzo casuale (es.: odonimo, nome, civico).
- `genera_telefono(seed: int | None = None)` — genera un numero telefonico casuale; accetta `seed`.
- `genera_comune()` — (funzione presente nel package; restituisce dati relativi a un comune italiano).
- ... `molte altre in arrivo.....`

---

## Requisiti
- Python 3.9+ (il codice usa annotazioni di tipo moderne; adattare se usi versioni precedenti)
- `git` installato per l'installazione dal repository

---

## Installazione

Installa direttamente da terminale
```bash
pip install git+https://github.com/domingo79/progetto-dati-falsi.git
```

Per forzare l'aggiornamento all'ultima versione presente nel repository:
```bash
pip install --upgrade git+https://github.com/domingo79/progetto-dati-falsi.git
```
Per reinstallare da zero:
```bash
pip uninstall generatore
pip install git+https://github.com/domingo79/progetto-dati-falsi.git
```

## Licenza
Questo progetto è rilasciato sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.


## Fonti e Ringraziamenti

Questo progetto utilizza il database dei comuni italiani (file JSON) creato e gentilmente messo a disposizione da Matteo Contrini.

* **Autore:** Matteo Contrini
* **Fonte Originale:** [github.com/matteocontrini/comuni-italiani](https://github.com/matteocontrini/comuni-italiani)
* **Licenza Dati:** [Creative Commons BY 3.0 IT](https://creativecommons.org/licenses/by/3.0/it/)




