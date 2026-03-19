# Funzioni per gestire le playlist (liste di canzoni):
# - `crea_playlist(nome: str) -> dict:` 
#   - Restituisce un dizionario con `nome` e `canzoni` (lista vuota)
# - `aggiungi_canzone(playlist: dict, canzone: dict) -> None:` 
#   - Aggiunge una canzone alla playlist
# - `rimuovi_canzone(playlist: dict, indice: int) -> None:` 
#   - Rimuove una canzone per indice (0-based)
# - `durata_totale(playlist: dict) -> int:` 
#   - Restituisce durata totale in secondi
# - `mostra_playlist(playlist: dict) -> str:` 
#   - Restituisce stringa formattata con tutte le canzoni

def crea__playlist(nome: str) -> dict:
    return {"nome": nome, "canzone": []}

def aggiungi_canzone(playlist: dict, canzone_da_aggiungere: dict) -> None:
    for canzone in playlist:
        playlist["canzone"].append(canzone_da_aggiungere)

def rimuovi_canzone(playlist: dict, indice: int) -> None:
    try:
        #if 0 <= indice < len(playlist["canzone"]):
        for canzone in playlist:
            if canzone == indice:
                playlist["canzone"].pop(indice)
    except IndexError as e:
        print(f"Indice non valido: {e}")


def durata_totale(playlist: dict) -> int:
    durata_complessiva: int = 0
    for canzone in playlist:
        durata_complessiva += canzone["durata"]
    return durata_complessiva

def mostra_playlist(playlist: dict) -> str:
    output = f"=== Playlist: {playlist["nome"]} ===\n"
    for indice, canzone in enumerate(playlist["nome"], start=1):
        output += f"{indice}. {canzone["titolo"]} - {canzone["artista"]} - {canzone["durata"]}"
    return output
    