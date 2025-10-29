from generatore import genera_nomi

# genera 5 Nomi e Cognomi con Titoli
nomi_completi = genera_nomi(5)
print("")
print(" Nomi e Cognomi con Titoli ".center(70, '#'))
print(nomi_completi)
print("")


# genera 5 studenti con solo nome e cognome
studenti = genera_nomi(5, titoli=False)
print(" Studenti con solo Nome e Cognome ".center(70, '#'))
print(studenti)
print()


# genera 5 persone statiche con l'uso del seed
nomi_completi_statici = genera_nomi(5, seed=(79))
print(" Nomi e Cognomi con Titoli (dati STATICI) ".center(70, '#'))
print(nomi_completi_statici)
