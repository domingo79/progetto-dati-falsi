# Librerie Standard di Python (Built-in)
import random
import string
from datetime import datetime, date, timedelta
# Librerie di Terze Parti
from codicefiscale import codice_fiscale as cf
# Mio Moduli
from . import dati


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
    data_odierna = date.today()

    # Calcola l'anno minimo e massimo in base al range di età
    anno_min = data_odierna.year - max_age  # 1940
    anno_max = data_odierna.year - min_age  # 2007

    # Sceglie una data casuale nell'intervallo
    data_inizio = date(anno_min, 1, 1)  # 1940, gen, 01
    data_fine = date(anno_max, 12, 31)  # 2027, dic, 31

    giorni_totali = (data_fine - data_inizio).days  # 24836

    data_nascita = data_inizio + \
        timedelta(days=random.randint(0, giorni_totali))

    # Calcola età
    eta = data_odierna.year - data_nascita.year - ((data_odierna.month,
                                                    data_odierna.day) < (data_nascita.month, data_nascita.day))
    return {
        # Formattato come stringa DD/MM/YYYY
        "data_nascita": data_nascita.strftime("%d/%m/%Y"),
        "eta": eta
    }


def genera_lavoro(sesso: str = 'M', eta: int = 30, seed: int | None = None) -> dict:
    """
    Genera un titolo di lavoro/professione casuale, declinato in base al sesso ed età.
    Se il sesso non è valido, restituisce 'Non specificato'.
    Se l'età è superiore a 65 la professione sarà disoccupato/a

    Args:
        sesso (str): Il sesso della persona ('M' o 'F'). Default a M.
        eta (int): L'eta della persona. Default a 30
        seed (int | None, optional): Seed per la riproducibilità. Default a None.

    Returns:
        dict: Un dizionario contenente la chiave 'professione' (str).
    """

    if seed is not None:
        random.seed(seed)

    # Standarizzazione del sesso per evitare ripetizioni
    sesso_std = sesso.upper()

    if eta > 64:
        if sesso_std == "M":
            professione_scelta = "Pensionato"
        elif sesso_std == "F":
            professione_scelta = "Pensionata"
        else:
            return {"professione": 'Non specificato'}
    else:
        lista_professioni = (dati.PROFESSIONI_MASCHILI if sesso_std == 'M'
                             else dati.PROFESSIONI_FEMMINILI if sesso_std == "F"
                             else None)

        if lista_professioni is None:
            return {"professione": "Non specificato"}

        professione_scelta = random.choice(lista_professioni)

    return {
        "professione": professione_scelta,
    }


def genera_email(nome: str = 'pinco', cognome: str = 'pallino', seed: int | None = None) -> dict:
    """
    Genera un indirizzo email fittizio (username@dominio) basato su nome e cognome.

    Args:
        nome (str): Il nome della persona.
        cognome (str): Il cognome della persona.
        seed (int | None, optional): Seed per la riproducibilità.

    Returns:
        dict: Un dizionario contenente la chiave 'email' (str).
    """
    if seed is not None:
        random.seed(seed)

    # Pulizia e normalizzazione di nome e cognome
    nome_pulito = nome.lower().strip().replace(' ', '')
    cognome_pulito = cognome.lower().strip().replace(' ', '')

    formati_username = [
        f"{nome_pulito}.{cognome_pulito}",
        f"{cognome_pulito}-{nome_pulito}",
        f"{nome_pulito}{random.randint(1, 99)}{cognome_pulito}",
        f"{nome_pulito[0]}.{cognome_pulito}{random.randint(1, 9)}"
    ]
    username = random.choice(formati_username)
    dominio = random.choice(dati.DOMINI_EMAIL)
    return {"email": f"{username}@{dominio}"}


def genera_stato_civile(sesso: str = 'M', seed: int | None = None) -> dict:
    """
    Genera uno stato civile casuale, declinato in base al sesso della persona.

    La funzione utilizza liste separate per l'assegnazione al maschile (Celibe/Sposato/Divorziato/Vedovo) 
    e al femminile (Nubile/Sposata/Divorziata/Vedova).

    Args:
        sesso (str): Il sesso della persona ('M' o 'F'). Default a M.
        seed (int | None, optional): Un valore seed opzionale per la riproducibilità. 
                                    Il valore predefinito è None.

    Returns:
        dict: Un dizionario contenente la chiave 'stato_civile' (str).
            Restituisce "Non specificato" se il parametro 'sesso' non è valido.

    Esempi:
        >>> genera_stato_civile(sesso='M')['stato_civile']
        'Celibe'
        >>> genera_stato_civile(sesso='F')['stato_civile']
        'Nubile'
    """

    if seed is not None:
        random.seed(seed)

    # Standarizzazione del sesso per evitare ripetizioni
    sesso_std = sesso.upper()

    if sesso_std == 'M':
        stato = dati.STATO_CIVILE_M
    elif sesso_std == 'F':
        stato = dati.STATO_CIVILE_F
    else:
        return {"stato_civile": "Non specificato"}

    stato_civile = random.choice(stato)

    return {"stato_civile": stato_civile}


def genera_patente(data_nascita: str = "14/07/1979", eta: int = 40, rilasciato: str = "MIT-UCO", seed: int | None = None) -> dict:
    """
    Simula la generazione dei dati di una patente di guida (numero, rilascio, scadenza).

    La funzione applica logiche di rinnovo basate sull'età e calcola date di rilascio/scadenza casuali 
    ma coerenti, allineando la scadenza al giorno e mese di nascita. Genera un numero di patente 
    alfanumerico di 10 caratteri (schema: LLNNLNNNNN).

    Args:
        data_nascita (str): Data di nascita del titolare ('GG/MM/AAAA').
        eta (int): Età corrente del titolare.
        rilasciato (str): Ente di rilascio simulato (default 'MIT-UCO').
        seed (int | None): Seed per il generatore casuale.

    Returns:
        dict: Dizionario contenente i dettagli della patente simulata.
              'stato_patente' sarà 'MAI POSSEDUTA' se età < 18 o per probabilità casuale(15%).
    """
    FORMATO_DATA = "%d/%m/%Y"
    CARATTERI = string.ascii_uppercase
    NUMERI = string.digits

    if seed is not None:
        random.seed(seed)

    if random.random() < 0.15 or eta < 18:
        return {
            "stato_patente": "MAI POSSEDUTA",
            "numero_patente": '',
            "categoria": '',
            "data_rilascio": '',
            "data_scadenza": '',
            "rilasciato_da": ''
        }

    idoneo_guida = 18 <= eta <= 90

    rinnovo = 0
    if idoneo_guida:
        if 18 <= eta < 50:
            rinnovo = 10
        elif 50 <= eta < 70:
            rinnovo = 5
        elif 70 <= eta < 80:
            rinnovo = 3
        elif 80 <= eta <= 90:
            rinnovo = 2

    oggi = datetime.now().date()  # 2025-11-08
    data_di_nascita = datetime.strptime(
        data_nascita, FORMATO_DATA).date()  # 1968-09-17

    giorno_nascita = data_di_nascita.day
    mese_nascita = data_di_nascita.month

    PERIODO = [0.10, 0.25, 0.35, 0.45, 0.65, 0.75, 0.85]
    scelta = random.choice(PERIODO)

    x_passato = rinnovo * scelta
    x_futuro = rinnovo - x_passato

    anno_rinnovo = int(oggi.year + x_futuro)

    giorno_rilascio = random.randint(1, 28)
    mese_rilascio = random.randint(1, 12)

    anno_rilascio = int(oggi.year - x_passato)

    match eta:
        case _ if 18 <= eta < 25:
            # casistica di neo patentato
            data_rilascio = oggi.replace(
                day=giorno_rilascio, month=(mese_nascita + 2), year=oggi.year)
            data_scadenza = oggi.replace(
                day=giorno_nascita, month=mese_nascita, year=anno_rinnovo)
        case _:
            data_rilascio = oggi.replace(
                day=giorno_rilascio, month=mese_rilascio, year=anno_rilascio)
            data_scadenza = oggi.replace(
                day=giorno_nascita, month=mese_nascita, year=anno_rinnovo)

    numero_patente = None

    # 2 Lettere + 2 Numeri + 1 Lettera + 5 Numeri = 10 caratteri
    numero_patente = "".join(random.choices(CARATTERI, k=2)) + \
        "".join(random.choices(NUMERI, k=2)) + \
        "".join(random.choices(CARATTERI, k=1)) + \
        "".join(random.choices(NUMERI, k=5))

    return {"stato_patente": "ATTIVO",
            "numero_patente": numero_patente,
            "categoria": 'B',
            "data_rilascio": data_rilascio.strftime(FORMATO_DATA),
            "data_scadenza": data_scadenza.strftime(FORMATO_DATA),
            "rilasciato_da": rilasciato
            }


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
    if seed is not None:
        random.seed(seed)

    # popolamento da anagrafica da genera_anagrafica()
    anagrafica = genera_anagrafica()
    nome = anagrafica['nome']
    cognome = anagrafica['cognome']
    sesso = anagrafica['sesso']

    # popolamento stato civile da genera_stato_civile()
    st_civ = genera_stato_civile(sesso=sesso)
    stato_civile = st_civ['stato_civile']

    # popolamento e-mail da genera_email()
    mail = genera_email(nome=nome, cognome=cognome)
    email = mail['email']

    # popolamento cellulare da genera_telefono()
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

    # popolamento professione
    lavoro = genera_lavoro(sesso=sesso, eta=eta)
    professione = lavoro['professione']

    # popolamento patente
    patente = genera_patente(data_nascita=data_nascita, eta=eta)
    stato_patente = patente["stato_patente"]
    numero_patente = patente["numero_patente"]
    categoria_patente = patente["categoria"]
    data_rilascio_patente = patente["data_rilascio"]
    data_scadenza_patente = patente["data_scadenza"]
    rilasciata = patente["rilasciato_da"]

    try:
        codice_fiscale = cf.genera_codice_fiscale(
            nome=nome,
            cognome=cognome,
            sesso=sesso,
            data_nascita=data_nascita,
            comune=comune[0]
        )
    except ValueError as e:
        print(
            "------------------------- ERRORE DI GENERAZIONE CF -------------------------")
        print(f"⚠️ ERRORE CATTURATO: {e}")
        print(
            f"DATI DI INPUT: Nome={nome}, Cognome={cognome}, Sesso={sesso}, Comune fornito={comune}")
        print(
            "----------------------------------------------------------------------------")
        codice_fiscale = "CF_NON_VALIDO"

    return {
        "nome": nome,
        "cognome": cognome,
        "sesso": sesso,
        "stato_civile": stato_civile,
        "professione": professione,
        "email": email,
        "cellulare": cellulare,
        "indirizzo": indirizzo,
        "comune": comune,
        "data_nascita": data_nascita,
        "eta": eta,
        "codice_fiscale": codice_fiscale,
        "patente": {
            "stato": stato_patente,
            "numero": numero_patente,
            "categoria": categoria_patente,
            "data_rilascio": data_rilascio_patente,
            "data_scadenza": data_scadenza_patente,
            "rilasciata": rilasciata
        }
    }
