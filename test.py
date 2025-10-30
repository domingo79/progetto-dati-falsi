from generatore import genera_anafragica, genera_strade, genera_telefono, generazione_comune

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
lista_comuni = [generazione_comune() for _ in range(10)]
print(" Genera 10 comuni casuali ".center(70, '#'))
for comune in lista_comuni:
    print(f"{comune['comune']} {comune['cap']} {comune['provincia']}")
print()

################################### genera_anafragica ###################################
# genera un anagrafica di base con la possibilità di avere anche un 'titolo' titoli=True
# formato → {'nome': 'Alessia', 'cognome': 'Martini', 'sesso': 'F'}
anfragica = genera_anafragica()
print(" genera un'anagrafica di base ".center(70, '#'))
print(
    f"Nome: {anfragica['nome']} Cognome: {anfragica['cognome']} Sesso: {anfragica['sesso']}")
print()

# genera 4 anagrafiche casuali con formato titolo, nome e cognome
# formato → {'nome': 'Guido', 'cognome': 'Mancini', 'sesso': 'M', 'titolo': 'Sig.'}
lista_anagrafica = [genera_anafragica(titoli=True) for _ in range(4)]
print(" Genera 4 anagrafiche con formato titolo nome cognome".center(70, '#'))
for p in lista_anagrafica:
    print(f"{p['titolo']} {p['nome']} {p['cognome']}")
print()
