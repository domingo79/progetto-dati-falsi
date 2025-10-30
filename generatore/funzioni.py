
import random
from . import dati


def genera_nomi(numero: int = 10, titoli: bool = True, seed: int | None = None):
    """
    Genera una lista di nomi, cognomi e titoli completamente casuale.

    Args:
        numero (int, opzionale): Numero di nomi completi da generare (default 10).
        titoli (bool, opzionale): Se True, aggiunge titoli casuali (default True).
        seed (int | None, opzionale): Numero per inizializzare il generatore casuale (default None).
            Se fornito un numero la generazione sarà sempre uguale per lo stesso seed.
            Se None, ogni esecuzione produrrà risultati diversi.

    Returns:
        list[str]: Lista di nomi completi casuali.

    Example:
        >>> genera_nomi(3)
        ['Dott. Andrea Rossi', 'Sofia Bruno', 'Ing. Tommaso Moretti']

    """
    if seed is not None:
        random.seed(seed)

    nomi_completi = []
    for _ in range(numero):
        # casualità per la scelta dei nomi maschili e femminili con relativo titolo
        if random.choice([True, False]):
            nome = random.choice(dati.NOMI_MASCHILI)
            titolo = random.choice(dati.TITOLI_MASCHILI)
        else:
            nome = random.choice(dati.NOMI_FEMMINILI)
            titolo = random.choice(dati.TITOLI_FEMMINILI)
        cognome = random.choice(dati.COGNOMI)

        # imposto un 60% di probabilità per la scelta del titolo se è richiesto
        if titoli and random.random() < 0.60:
            nomi_completi.append(f"{titolo} {nome} {cognome}")
        else:
            nomi_completi.append(f"{nome} {cognome}")

    return nomi_completi


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


def generazione_comune(seed: int | None = None):
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
