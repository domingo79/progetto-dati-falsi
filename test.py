from generatore import genera_nomi, genera_strade, genera_telefono, generazione_comune

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
cellulari = [genera_telefono(3) for _ in range(3)]
print(" Genara 3 numeri di cellulari ".center(70, '#'))
for cellulare in cellulari:
    print(f"{cellulare['cellulare']}")
print()

################################## generazione_comune ##################################
# genera 10 comuni casuali con provincia e cap formato → {'comune': 'Neviglie', 'cap': 'CN', 'provincia': 'CN'}
lista_comuni = [generazione_comune() for _ in range(10)]
print(" Genera 10 comuni casuali ".center(70, '#'))
for comune in lista_comuni:
    print(f"{comune['comune']} {comune['cap']} {comune['provincia']}")
