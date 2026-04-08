### Parte 3: Modulo `persistenza.py`
#Implementa le funzioni per salvare e caricare il diario su file JSON:
#- `salva_diario(diario: dict, nome_file: str) -> None`
#- `carica_diario(nome_file: str) -> dict`

import json
def salva_diario(diario: dict, nome_file: str) -> None:
    try:
            with open(nome_file, "w", encoding="utf-8") as file:
                json.dump(diario, file, indent=4)
            print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
            print(f"Errore durante il salvataggio del file: {e}")

def carica_diario(nome_file: str) -> list[dict]:
    """Carica la lista di prodotti da un file JSON."""
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            diario = json.load(file)
        return diario
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []
