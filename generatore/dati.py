from pathlib import Path
import json

# Path(__file__) è il file corrente .parent è la cartella che lo contiene
CARTELLA_PROGETTO = Path(__file__).parent
JSON_COMUNI = CARTELLA_PROGETTO / "comuni_italiani.json"


def carica_dati_json(file_path):
    """Funzione helper per caricare un file JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            dati = json.load(f)
            return dati
    except FileNotFoundError:
        print(f"ERRORE: File non trovato a questo percorso: {file_path}")
        return []
    except json.JSONDecodeError:
        print(
            f"ERRORE: Il file JSON non è formattato correttamente: {file_path}")
        return []


# --- CARICAMENTO DATI UNA SOLA VOLTA ---
LISTA_COMUNI = carica_dati_json(JSON_COMUNI)

NOMI_MASCHILI = [
    "Alessandro", "Andrea", "Matteo", "Luca", "Lorenzo", "Gabriele", "Leonardo", "Francesco", "Emanuele", "Davide",
    "Giuseppe", "Antonio", "Simone", "Riccardo", "Federico", "Giovanni", "Marco", "Stefano", "Nicola", "Angelo",
    "Michele", "Tommaso", "Filippo", "Alberto", "Paolo", "Giulio", "Carlo", "Pietro", "Claudio", "Daniele",
    "Salvatore", "Roberto", "Vincenzo", "Adriano", "Giorgio", "Massimo", "Christian", "Samuele", "Fabio", "Enrico",
    "Amedeo", "Raffaele", "Alessio", "Cristian", "Mario", "Sergio", "Maurizio", "Valerio", "Guido", "Giovanni"
]

NOMI_FEMMINILI = [
    "Sofia", "Aurora", "Giulia", "Ginevra", "Vittoria", "Beatrice", "Alice", "Ludovica", "Emma", "Matilde",
    "Anna", "Camilla", "Chiara", "Giorgia", "Martina", "Sara", "Arianna", "Noemi", "Rebecca", "Mia",
    "Isabel", "Adele", "Chloe", "Elena", "Francesca", "Gioia", "Ambra", "Viola", "Abigail", "Ada",
    "Adelaide", "Agata", "Agnese", "Alessandra", "Alessia", "Angela", "Angelica", "Anita", "Debora", "Federica"
]

COGNOMI = [
    "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Bruno", "Ricci", "Marino", "Costa", "Franco",
    "Gallo", "Conti", "Greco", "Martino", "Giordano", "Rizzo", "Mancini", "Villa", "Mauro", "Lombardi", "Fontana", "Barbieri",
    "Moretti", "Bianco", "Martini", "Mariani", "Rinaldi", "Amato"]

TITOLI_MASCHILI = ["Sig.", "Dott.", "Avv.",
                   "Ing.", "Rag.", "Geom.", "Prof.", "Comm."]

TITOLI_FEMMINILI = ["Sig.ra", "Dott.ssa", "Avv.sa",
                    "Ing.", "Rag.", "Geom.", "Prof.ssa", "Comm."]

# "Via" e "Piazza" ripetuti apposta per renderli più probabili
TIPI_STRADE = ["Via", "Corso", "Piazza", "Viale", "Vicolo",
               "Largo", "Via", "Via", "Piazza", "Via", "Piazza"]

NOMI_STRADE = [
    # Eroi e Personaggi
    "Garibaldi", "Mazzini", "Cavour", "Verdi", "Dante Alighieri", "Manzoni", "Leopardi",
    "Giotto", "Marconi", "Leonardo Da Vinci", "Galilei", "Colombo", "Matteotti", "Gramsci",
    "Pascoli", "Carducci", "Petrarca", "Boccaccio", "Michelangelo", "Raffaello",

    # Città e Luoghi
    "Roma", "Milano", "Napoli", "Torino", "Firenze", "Venezia", "Bologna", "Genova",
    "Palermo", "Bari", "Europa", "Italia",

    # Concetti e Natura
    "della Repubblica", "dell'Indipendenza", "della Libertà", "della Pace", "XX Settembre",
    "IV Novembre", "della Vittoria", "Stazione", "Mercato", "Duomo",
    "dei Fiori", "degli Ulivi", "dei Pini", "delle Rose", "dei Mille", "Nuova",
]

# Dentro a generatore_dati/dati.py

PREFISSI_TELEFONICI = [
    "333", "347", "338", "335", "366", "339", "348", "349", "340", "334",
    "320", "328", "329", "330", "331", "336", "337", "342", "345", "346",
    "350", "351", "360", "368", "370", "371", "373", "377", "379",
    "380", "388", "389", "390", "391", "392", "393"
]
