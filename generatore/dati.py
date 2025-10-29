import random


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

    nomi_maschili = [
        "Alessandro", "Andrea", "Matteo", "Luca", "Lorenzo", "Gabriele", "Leonardo", "Francesco", "Emanuele", "Davide",
        "Giuseppe", "Antonio", "Simone", "Riccardo", "Federico", "Giovanni", "Marco", "Stefano", "Nicola", "Angelo",
        "Michele", "Tommaso", "Filippo", "Alberto", "Paolo", "Giulio", "Carlo", "Pietro", "Claudio", "Daniele",
        "Salvatore", "Roberto", "Vincenzo", "Adriano", "Giorgio", "Massimo", "Christian", "Samuele", "Fabio", "Enrico",
        "Amedeo", "Raffaele", "Alessio", "Cristian", "Mario", "Sergio", "Maurizio", "Valerio", "Guido", "Giovanni"
    ]

    nomi_femminili = [
        "Sofia", "Aurora", "Giulia", "Ginevra", "Vittoria", "Beatrice", "Alice", "Ludovica", "Emma", "Matilde",
        "Anna", "Camilla", "Chiara", "Giorgia", "Martina", "Sara", "Arianna", "Noemi", "Rebecca", "Mia",
        "Isabel", "Adele", "Chloe", "Elena", "Francesca", "Gioia", "Ambra", "Viola", "Abigail", "Ada",
        "Adelaide", "Agata", "Agnese", "Alessandra", "Alessia", "Angela", "Angelica", "Anita", "Debora", "Federica"
    ]

    cognomi = [
        "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Bruno", "Ricci", "Marino", "Costa", "Franco",
        "Gallo", "Conti", "Greco", "Martino", "Giordano", "Rizzo", "Mancini", "Villa", "Mauro", "Lombardi", "Fontana", "Barbieri",
        "Moretti", "Bianco", "Martini", "Mariani", "Rinaldi", "Amato"]

    titoli_maschili = ["Sig.", "Dott.", "Avv.",
                       "Ing.", "Rag.", "Geom.", "Prof.", "Comm."]

    titoli_femminili = ["Sig.ra", "Dott.ssa", "Avv.sa",
                        "Ing.", "Rag.", "Geom.", "Prof.ssa", "Comm."]

    nomi_completi = []
    for _ in range(numero):
        # casualità per la scelta dei nomi maschili e femminili con relativo titolo
        if random.choice([True, False]):
            nome = random.choice(nomi_maschili)
            titolo = random.choice(titoli_maschili)
        else:
            nome = random.choice(nomi_femminili)
            titolo = random.choice(titoli_femminili)
        cognome = random.choice(cognomi)

        # imposto un 60% di probabilità per la scelta del titolo se è richiesto
        if titoli and random.random() < 0.60:
            nomi_completi.append(f"{titolo} {nome} {cognome}")
        else:
            nomi_completi.append(f"{nome} {cognome}")

    return nomi_completi
