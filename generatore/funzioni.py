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
