import random
from . import dati


def genera_persona(seed: int | None = None):
    anagrafica = genera_anagrafica()
    cellulare = genera_telefono()
    indirizzo = genera_strade()
    comune = genera_comune()

    return {
        "nome": anagrafica['nome'],
        "cognome": anagrafica['cognome'],
        "sesso": anagrafica['sesso'],
        "cellulare": cellulare['cellulare'],
        "indirizzo": [indirizzo['odonimo'], indirizzo['nome'], str(indirizzo['civico'])],
        "comune": [comune["comune"], comune["cap"], comune["provincia"]]
    }


def genera_anagrafica(titoli: bool = False, seed: int | None = None):
    """
    Genera nome, cognome e sesso di una persona.
    Se richiesto, aggiunge un titolo.

    Esempio di output (con titolo):
    {'nome': 'Mario', 'cognome': 'Rossi', 'sesso': 'M', 'titolo': 'Dott.'}

    Esempio di output (senza titolo):
    {'nome': 'Anna', 'cognome': 'Verdi', 'sesso': 'F'}

    Args:
        titoli (bool, optional): Se True, viene aggiunto un titolo. 
        Se False, il titolo non viene mai aggiunto. Default a False.
        seed (int | None, optional): Seed per il generatore casuale
            per risultati riproducibili. Default a None.

    Returns:
        dict: Un dizionario contenente "nome", "cognome", "sesso"
              e, opzionalmente, "titolo".
    """
    if seed is not None:
        random.seed(seed)

    # Determina sesso e nome
    sesso = random.choice(["M", "F"])
    if sesso == 'M':
        nome = random.choice(dati.NOMI_MASCHILI)
    else:
        nome = random.choice(dati.NOMI_FEMMINILI)

    cognome = random.choice(dati.COGNOMI)

    # Dizionario di base
    output = {
        "nome": nome,
        "cognome": cognome,
        "sesso": sesso,
    }

    # Controlla la condizione per aggiungere il titolo
    if titoli:  # and random.random() < 0.60:
        if sesso == 'M':
            titolo = random.choice(dati.TITOLI_MASCHILI)
        else:
            titolo = random.choice(dati.TITOLI_FEMMINILI)

        output["titolo"] = titolo

    return output


def genera_strade(seed: int | None = None):
    """
    Genera un indirizzo stradale fittizio con odonimo, nome e n.civico.

    Esempio di output:
    {'odonimo': 'Via', 'nome': 'Garibaldi', 'civico': 100}

    Args:
        seed (int | None, optional): Un seme (seed) opzionale per il
            generatore casuale, per ottenere risultati riproducibili.
            Default a None (casuale).

    Returns:
        dict: Un dizionario contenente:
              - "odonimo" (str): Il tipo di strada (es. "Via", "Piazza").
              - "nome" (str): Il nome della strada (es. "Garibaldi").
              - "civico" (int): Un numero civico casuale.
    """
    if seed is not None:
        random.seed(seed)

    odonimo = random.choice(dati.TIPI_STRADE)
    nome = random.choice(dati.NOMI_STRADE)
    civico = random.randint(1, 200)
    return {
        "odonimo": odonimo,
        "nome": nome,
        "civico": civico
    }


def genera_comune(seed: int | None = None):
    """
    Genera un Comune fittizio con nome, CAP e provincia.

    Esempio di output:
    {'comune': 'Andria', 'cap': '76123', 'provincia': 'BT'}

    Args:
        seed (int | None, optional): Un seme (seed) opzionale per il
            generatore casuale, per ottenere risultati riproducibili.
            Default a None (casuale).

    Returns:
        dict: Un dizionario contenente:
              - "comune" (str): Il nome del comune (es. "Andria").
              - "cap" (str): Il Codice di Avviamento Postale (es. "76123").
              - "provincia" (str): La sigla della provincia (es. "BT").
    """
    if seed is not None:
        random.seed(seed)

    if not dati.LISTA_COMUNI:
        # --- CORREZIONE LOGICA QUI ---
        # Deve restituire un dict, non una tupla, per coerenza
        return {
            "comune": "N/D",
            "cap": "N/D",
            "provincia": "N/D"
        }

    comune_scelto = random.choice(dati.LISTA_COMUNI)

    comune = comune_scelto["nome"]
    provincia = comune_scelto["sigla"]
    cap = comune_scelto["cap"][0]

    return {
        "comune": comune,
        "cap": cap,
        "provincia": provincia
    }


def genera_telefono(seed: int | None = None):
    """
    Genera un numero di cellulare fittizio (es. 330 3032478).

    Esempio di output:
    {'prefisso': '330', 'numero': '3032478', 'completo': '330 3032478'}

    Args:
        seed (int | None, opzionale): Seed per il generatore casuale
            per risultati riproducibili. Default a None.

    Returns:
        dict: Un dizionario contenente:
              - "prefisso" (str): Il prefisso del cellulare (es. "330").
              - "numero" (str): Il corpo del numero (7 cifre).
              - "completo" (str): Il numero formattato "prefisso numero".
    """
    if seed is not None:
        random.seed(seed)

    prefisso = random.choice(dati.PREFISSI_TELEFONICI)

    cifre_numero = [str(random.randint(0, 9)) for _ in range(7)]

    numero_cellulare = "".join(cifre_numero)

    return {
        "prefisso": prefisso,
        "numero": numero_cellulare,
        "cellulare": f"{prefisso} {numero_cellulare}"
    }
