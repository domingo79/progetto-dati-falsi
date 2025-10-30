
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


def genera_strade(numero: int = 1, seed: int | None = None):
    """
    Genera una lista di indirizzi stradali casuali (Via, Nome, Civico).

    Args:
        numero (int, opzionale): Numero di indirizzi da generare (default 1).
        seed (int | None, opzionale): Seed per il generatore casuale.

    Returns:
        list[str]: Lista di indirizzi casuali.
    """
    if seed is not None:
        random.seed(seed)

    lista_indirizzi = []
    for _ in range(numero):
        tipo = random.choice(dati.TIPI_STRADE)
        nome = random.choice(dati.NOMI_STRADE)
        civico = random.randint(1, 200)

        indirizzo_completo = f"{tipo} {nome}, {civico}"
        lista_indirizzi.append(indirizzo_completo)

    return lista_indirizzi


def genera_telefono(numero: int = 1, seed: int | None = None):
    """
    Genera una lista di numeri di cellulari casuali (330 3032478).

    Args:
        numero (int, opzionale): Numero di cellulari da generare (default 1).
        seed (int | None, opzionale): Seed per il generatore casuale.

    Returns:
        list[str]: Lista di numeri di cellulari casuali.
    """
    if seed is not None:
        random.seed(seed)

    lista_cellulari = []
    for _ in range(numero):
        prefisso = random.choice(dati.PREFISSI_TELEFONICI)
        cifre_numero = [str(random.randint(0, 9)) for _ in range(7)]
        # unisco le cifre
        numero_cellulare = "".join(cifre_numero)

        cellulare_completo = f"{prefisso} {numero_cellulare}"
        lista_cellulari.append(cellulare_completo)
    return lista_cellulari


def generazione_comune():

    if not dati.LISTA_COMUNI:
        return "N/D", "N/D", "N/D",
    comune_scelto = random.choice(dati.LISTA_COMUNI)

    comune = comune_scelto["nome"]
    provincia = comune_scelto["sigla"]
    cap = comune_scelto["cap"][0]

    return comune, cap, provincia
