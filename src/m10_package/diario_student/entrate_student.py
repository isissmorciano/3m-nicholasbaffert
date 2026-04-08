# ### Parte 2: Modulo `entrate.py`
# Implementa funzioni per lavorare con le entrate del diario:
# - `crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict`
#   - `data` è una stringa nel formato `YYYY-MM-DD`
#   - `durata` è il tempo trascorso in minuti
# - `info_entrata(entrata: dict) -> str`
#   - Restituisce una stringa leggibile con data, categoria, durata e testo
# - `crea_diario() -> dict`
#   - Restituisce un dizionario con chiave `entrate` e lista vuota
# - `aggiungi_entrata(diario: dict, entrata: dict) -> None`
# - `rimuovi_entrata(diario: dict, indice: int) -> None`
# - `tempo_totale(diario: dict) -> int`
#   - Somma tutte le durate in minuti
# - `tempo_per_categoria(diario: dict) -> dict[str, int]`
#   - Restituisce il tempo totale speso per categoria
# - `trova_entrate_per_data(diario: dict, data: str) -> list[dict]`

def crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict:
    return {"data": data, "testo": testo, "categoria": categoria, "durata": durata}

def info_entrata(entrata: dict) -> str:

# | Data | Categoria | Durata (minuti) | Testo |
# |------|-----------|-----------------|-------|
# | 2026-04-08 | studio | 60 | Ho iniziato un nuovo corso di Python. |
# | 2026-04-08 | studio | 45 | Ho scritto un esercizio sul package diario. |
# | 2026-04-09 | tempo libero | 30 | Sono andato a fare una passeggiata nel parco. |
    informazioni_entrata = info_entrata(entrata)
    return (
        " | Data | Categoria | Durata (minuti) | Testo |"
        f"|------|-----------|-----------------|-------|"
        f"|{entrata["data"]}|{entrata["categoria"]}|{entrata["durata"]}|{entrata["testo"]}|"
    )

def crea_diario() -> dict:
    return {"entrate": []}

def aggiungi_entrata(diario: dict, entrata_da_aggiungere: dict) -> None:
    diario["entrate"].append(entrata_da_aggiungere)
    print("Aggiunta entrata...")

def rimuovi_entrata(diario: dict, indice: int) -> None:
    if 0 <= indice < len(diario["entrate"]):
        diario["entrate"].pop(indice)
        print("Entrata rimossa...")
    else:
        print("Indice non valido")
    
def tempo_totale(diario: dict) -> int:
    tempo_complessivo: int = 0
    for entrata in diario["entrate"]:
        tempo_complessivo += entrata["durata"]
    return tempo_complessivo

def tempo_per_categoria(diario: dict) -> dict[str, int]:
    #Resdef tempo_per_categoria(diario: dict) -> dict[str, int]:
    categoria_di_tempo = {}

    for entrata in diario["entrate"]:
        categoria = entrata["categoria"]
        durata = entrata["durata"]

        if categoria in categoria_di_tempo:
            categoria_di_tempo[categoria] += durata
        else:
            categoria_di_tempo[categoria] = durata

    return categoria_di_tempo

def trova_entrate_per_data(diario: dict, data: str) -> list[dict]:
    risultato = []

    for entrata in diario["entrate"]:
        if entrata["data"] == data:
            risultato.append(entrata)

    return risultato