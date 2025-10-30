from generatore import genera_nomi, genera_strade, genera_telefono, generazione_comune

#################################  genera_nomi     ###################################
# genera 5 Nomi e Cognomi con Titoli Formato → ['Ing. Arianna Rinaldi']
nomi_completi = genera_nomi(5)
print("")
print(" Nomi e Cognomi con Titoli ".center(70, '#'))
print(nomi_completi)
print("")

# genera 5 studenti con solo nome e cognome Formato → ['Pietro Bruno']
studenti = genera_nomi(5, titoli=False)
print(" Studenti con solo Nome e Cognome ".center(70, '#'))
print(studenti)
print()

# genera 5 persone statiche con l'uso del seed
nomi_completi_statici = genera_nomi(5, seed=(79))
print(" Nomi e Cognomi con Titoli (dati STATICI) ".center(70, '#'))
print(nomi_completi_statici)
print()


#################################   genera_strade   #################################
# genera 2 indirizzi casuali in formato → [Largo dei Mille, 190']
indirizzo = genera_strade(2)
print(" Genara due indirizzi completi (casuali) ".center(70, '#'))
print(indirizzo)
print()

indirizzo_statico = genera_strade(2, seed=False)
print(" Genara due indirizzi completi (STATICI) ".center(70, '#'))
print(indirizzo_statico)
print()

################################   genera_telefono     ################################
# genera 3 numeri di telefono casuali nel formato → ['371 4759382']
cellulari = genera_telefono(3)
print(" Genara 3 numeri di cellulari ".center(70, '#'))
print(cellulari)
print()

################################## generazione_comune ##################################
# genera 10 comuni casuali
print("\n--- Esempio di 10 luoghi casuali ---")
for _ in range(10):
    comune, prov, cap = generazione_comune()
    print(f"Comune: {comune}, Provincia: {prov}, CAP: {cap}")
