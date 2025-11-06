from generatore import (genera_anagrafica, genera_strade, genera_telefono,
                        genera_comune, genera_persona, genera_eta_e_data_nascita)

#################################   genera_strade   #################################
# genera indirizzo casuale in formato → {'odonimo': 'Via', 'nome': 'Garibaldi', 'civico': 100}
indirizzo = genera_strade()
print(" Genara un indirizzo completo (casuale) ".center(70, '#'))
print(
    f"Indirizzo: {indirizzo["odonimo"]} {indirizzo["nome"]}, {indirizzo['civico']}")
print()

# genera n indirizzi casuali in formato → {'odonimo': 'Via', 'nome': 'Garibaldi', 'civico': 100}
print(" Genara 5 indirizzi completi (casuali) ".center(70, '#'))
indirizzi = [genera_strade() for _ in range(5)]
for indirizzo in indirizzi:
    print(
        f"Indirizzo: {indirizzo["odonimo"]} {indirizzo["nome"]}, {indirizzo['civico']}")
print()

################################   genera_telefono     ################################
# genera 3 numeri di cellulari casuali nel formato → {'prefisso': '336', 'numero': '9825979', 'cellulare': '336 9825979'}
cellulari = [genera_telefono() for _ in range(3)]
print(" Genara 3 numeri di cellulari ".center(70, '#'))
for cellulare in cellulari:
    print(f"{cellulare['cellulare']} oppure possiamo avere doppio formato prefisso: {cellulare['prefisso']} numero: {cellulare['numero']}")
print()

################################## generazione_comune ##################################
# genera 10 comuni casuali con provincia e cap formato → {'comune': 'Neviglie', 'cap': 'CN', 'provincia': 'CN'}
lista_comuni = [genera_comune() for _ in range(10)]
print(" Genera 10 comuni casuali ".center(70, '#'))
for comune in lista_comuni:
    print(f"{comune['comune']} {comune['cap']} {comune['provincia']}")
print()

################################### genera_anafragica ###################################
# genera un anagrafica di base con la possibilità di avere anche un 'titolo' titoli=True
# formato → {'nome': 'Alessia', 'cognome': 'Martini', 'sesso': 'F'}
anfragica = genera_anagrafica()
print(" genera un'anagrafica di base ".center(70, '#'))
print(
    f"Nome: {anfragica['nome']} Cognome: {anfragica['cognome']} Sesso: {anfragica['sesso']}")
print()

# genera 4 anagrafiche casuali con formato titolo, nome e cognome
# formato → {'nome': 'Guido', 'cognome': 'Mancini', 'sesso': 'M', 'titolo': 'Sig.'}
lista_anagrafica = [genera_anagrafica(titoli=True) for _ in range(4)]
print(" Genera 4 anagrafiche con formato titolo nome cognome".center(70, '#'))
for p in lista_anagrafica:
    print(f"{p['titolo']} {p['nome']} {p['cognome']}")
print()

################################# genera_eta_e_data_nascita ###################################
# Genera una data di nascita casuale e l'età corrispondente, vincolate da un intervallo di
# età minimo e massimo.
# formato → {'eta': 50, 'data_nascita': ''}
data_di_nascita = genera_eta_e_data_nascita(18, 90)
print(
    f"età: {data_di_nascita['eta']}, nato il: {data_di_nascita['data_nascita']}")
print()
################################### genera_persona  #######################################
# Genera un dizionario di una persona fittizia contenente dati anagrafici, di contatto e residenza.
# formato → {'nome': 'Gioia', 'cognome': 'Rizzo', 'sesso': 'F', "cellulare": "349 1113597",
# 'codice_fiscale': 'RZZGIO80R61B590W', 'eta': 45,
# 'data_nascita': '21/10/1980', "indirizzo": "Piazza Mazzini 115", "comune": "Candida 83040 AV"}
persone = [genera_persona() for _ in range(4)]
for persona in persone:
    indirizzo_formattato = " ".join((persona["indirizzo"]))
    comune_formattato = " ".join(persona["comune"])
    msg = ""
    if persona["sesso"] == "M":
        msg = "nato"
    else:
        msg = "nata"
    print(
        f"{persona["nome"]} {persona["cognome"]} {persona["sesso"]} {persona["cellulare"]}"
        f" codice fiscale: {persona["codice_fiscale"]}"
        f" età: {persona["eta"]} {msg} il {persona["data_nascita"]}"
        f" indirizzo: {indirizzo_formattato} - {comune_formattato}"
    )
