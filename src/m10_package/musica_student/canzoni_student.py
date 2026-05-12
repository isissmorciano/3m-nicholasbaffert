# musica/canzoni.py`
# Funzioni per gestire le canzoni (rappresentate come dizionari):
# - `crea_canzone(titolo: str, artista: str, durata: int) -> dict:` 
#   - Restituisce un dizionario con chiavi: `titolo`, `artista`, `durata`
# - `info_canzone(canzone: dict) -> str:` 
#   - Restituisce formato: `"Titolo - Artista (M:SS)"`
#   - Esempio: `"Bohemian Rhapsody - Queen (5:55)"`

def crea_canzone(titolo: str, artista: str, durata: int) -> dict:
    return {"titolo": titolo, "artista":artista, "durata":durata}

def info_canzone(canzone:dict) -> str:
    minuti = canzone["durata"] // 60
    secondi = canzone["durata"] % 60
    return {f"{canzone['durata']} - {canzone["artista"]} {minuti}{secondi:02d}"} #mette uno zero dietro il 02d