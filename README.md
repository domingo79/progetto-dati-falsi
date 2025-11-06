# generatore — 'progetto-dati-falsi' 🇮🇹

Un pacchetto leggero e semplice per generare **dati anagrafici italiani fittizi completi** (inclusi Codice Fiscale, data di nascita e dati di residenza). Utile per popolamento di database, testing o per uso didattico.

---

## Contenuto del pacchetto

Il pacchetto espone (import diretto da `generatore`) le seguenti funzioni principali:

### 👤 `genera_persona(seed: int | None = None)`
Genera un dizionario completo contenente tutti i dati aggregati di una persona fittizia. Accetta un `seed` per la riproducibilità.

**Output (dict) e Chiavi Generati:**
* `"nome"` (str): Il nome di battesimo.
* `"cognome"` (str): Il cognome.
* `"sesso"` (str): Il sesso ('M' o 'F').
* `"cellulare"` (str): Un numero di telefono cellulare.
* **`"codice_fiscale"` (str): Il Codice Fiscale calcolato sulla base degli altri dati. (NUOVO!)**
* **`"data_nascita"` (str): Data di nascita, formattata come "DD/MM/YYYY". (NUOVO!)**
* **`"eta"` (int): Età calcolata in anni. (NUOVO!)**
* `"indirizzo"` (list[str]): Una lista con [Odonomio, Nome strada, Numero civico].
* `"comune"` (list[str]): Una lista con [Nome Comune, CAP, Provincia].

---

### Altre Funzioni Utili

* `genera_anagrafica(titoli: bool = False, seed: int | None = None)`: Genera un dizionario con `nome`, `cognome`, `sesso` e opzionalmente `titolo`.
* **`genera_eta_e_data_nascita(min_age=18, max_age=90, seed: int | None = None)`:** Genera un dizionario con `"data_nascita"` e `"eta"`, vincolati da un range di età.
* `genera_strade(seed: int | None = None)`: Genera un indirizzo casuale (es.: odonimo, nome, civico).
* `genera_telefono(seed: int | None = None)`: Genera un numero telefonico casuale.
* `genera_comune(seed: int | None = None)`: Restituisce dati relativi a un comune italiano (Comune, CAP, Provincia).

... `molte altre in arrivo.....`

---

## Requisiti
- Python 3.9+ (il codice usa annotazioni di tipo moderne)


## Installazione

**Nota:** Per installare il pacchetto è necessario che tu abbia `pip` e `git` installati sul tuo sistema.

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

Questo progetto si basa su dati e librerie di terze parti per garantire la precisione.

### Database Comuni Italiani (JSON)
* **Autore:** Matteo Contrini
* **Fonte Originale:** [github.com/matteocontrini/comuni-italiani](https://github.com/matteocontrini/comuni-json)
* **Licenza Dati:** [Creative Commons BY 3.0 IT](https://creativecommons.org/licenses/by/3.0/it/)

### Calcolo Codice Fiscale
* **Libreria:** codicefiscale-ita
* **Autore:** Filippo Casadei
* **Licenza:** [MIT License](https://opensource.org/licenses/MIT) 
* **Requisiti:** Python >=3.7