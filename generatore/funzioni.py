import random
import datetime
from codicefiscale import codice_fiscale as cf
from . import dati


def genera_persona(seed: int | None = None):
    """
    Genera un dizionario completo contenente dati anagrafici, di contatto e residenza per una 
    persona fittizia.

    Args:
        seed (int | None, optional): Un valore seed opzionale per l'inizializzazione 
                                    del generatore di numeri casuali. Questo assicura
                                    che, se fornito, chiamate consecutive alla funzione 
                                    con lo stesso seed producano lo stesso output. 
                                    Il valore predefinito è None.

    Returns:
        dict: Un dizionario contenente le seguenti chiavi e i relativi dati generati:
            - "nome" (str): Il nome di battesimo.
            - "cognome" (str): Il cognome.
            - "sesso" (str): Il sesso ('M' o 'F').
            - "cellulare" (str): Un numero di telefono cellulare.
            - "data_nascita" (str): data_nascita (DD/MM/YYY),
            - "eta": (int)eta,
            - "codice_fiscale"(str): codice_fiscale,
            - "indirizzo" (list[str]): Una lista con [Odonomio, Nome strada, Numero civico].
            - "comune" (list[str]): Una lista con [Nome Comune, CAP, Provincia].

    Esempi:
        >>> persona = genera_persona()
        >>> print(persona['nome'])
        'Marco'
        >>> print(persona['indirizzo'][1])
        'Via Roma'

        >>> # Generazione ripetibile
        >>> persona_A = genera_persona(seed=42)
        >>> persona_B = genera_persona(seed=42)
        >>> persona_A == persona_B
        True
    """
    # popolamento da genera_anagrafica()
    anagrafica = genera_anagrafica()
    nome = anagrafica['nome']
    cognome = anagrafica['cognome']
    sesso = anagrafica['sesso']

    # popolamento da genera_telefono()
    cellulare = genera_telefono()
    cellulare = cellulare['cellulare']

    # popolamento da genera_strade()
    indirizzo = genera_strade()
    indirizzo = [indirizzo['odonimo'], indirizzo['nome'], indirizzo["civico"]]

    # popolamento da genera_comune()
    comune = genera_comune()
    comune = [comune["comune"], comune["cap"], comune["provincia"]]

    # popolamento da genera_eta_e_data_nascita()
    data_di_nascita = genera_eta_e_data_nascita()
    eta = data_di_nascita["eta"]
    data_nascita = data_di_nascita["data_nascita"]

    codice_fiscale = cf.genera_codice_fiscale(
        nome=nome,
        cognome=cognome,
        sesso=sesso,
        data_nascita=data_nascita,
        comune=comune[0].upper()
    )
    return {
        "nome": nome,
        "cognome": cognome,
        "sesso": sesso,
        "cellulare": cellulare,
        "indirizzo": indirizzo,
        "comune": comune,
        "data_nascita": data_nascita,
        "eta": eta,
        "codice_fiscale": codice_fiscale,
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
        "civico": str(civico)
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


def genera_eta_e_data_nascita(min_age=18, max_age=90, seed: int | None = None):
    """
    Genera una data di nascita casuale e l'età corrispondente, vincolate da un intervallo di età 
    minimo e massimo.

    La data di nascita viene scelta in modo casuale all'interno del range di anni specificato da 
    'min_age' e 'max_age'.

    Args:
        min_age (int, optional): L'età minima (in anni) della persona da generare. 
                                Il valore predefinito è 18.
        max_age (int, optional): L'età massima (in anni) della persona da generare. 
                                Il valore predefinito è 90.
        seed (int | None, optional): Un valore seed opzionale per l'inizializzazione del generatore 
                                    di numeri casuali, utile per la riproducibilità. 
                                Il valore predefinito è None.

    Returns:
        dict: Un dizionario contenente:
            - "data_nascita" (str): La data di nascita generata, formattata come "DD/MM/YYYY".
            - "eta" (int): L'età calcolata con precisione in base alla data odierna.

    Esempi:
        >>> risultati = genera_eta_e_data_nascita(min_age=20, max_age=30)
        >>> print(risultati['eta'])
        25 
        >>> print(risultati['data_nascita'])
        '15/07/2000'
    """
    data_odierna = datetime.date.today()

    # Calcola l'anno minimo e massimo in base al range di età
    anno_min = data_odierna.year - max_age  # 1940
    anno_max = data_odierna.year - min_age  # 2007

    # Sceglie una data casuale nell'intervallo
    data_inizio = datetime.date(anno_min, 1, 1)  # 1940, gen, 01
    data_fine = datetime.date(anno_max, 12, 31)  # 2027, dic, 31

    giorni_totali = (data_fine - data_inizio).days  # 24836

    data_nascita = data_inizio + \
        datetime.timedelta(days=random.randint(0, giorni_totali))

    # Calcola età
    eta = data_odierna.year - data_nascita.year - ((data_odierna.month,
                                                    data_odierna.day) < (data_nascita.month, data_nascita.day))
    return {
        # Formattato come stringa DD/MM/YYYY
        "data_nascita": data_nascita.strftime("%d/%m/%Y"),
        "eta": eta
    }
