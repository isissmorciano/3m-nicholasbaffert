"""Modulo per la gestione delle playlist."""

from .canzoni import info_canzone


def crea_playlist(nome: str) -> dict:
    """
    Crea una playlist rappresentata come dizionario.
    
    Args:
        nome: Il nome della playlist
        
    Returns:
        Un dizionario con chiavi: nome, canzoni (lista vuota)
    """
    return {
        "nome": nome,
        "canzoni": []
    }


def aggiungi_canzone(playlist: dict, canzone: dict) -> None:
    """Aggiunge una canzone alla playlist."""
    playlist["canzoni"].append(canzone)


def rimuovi_canzone(playlist: dict, indice: int) -> None:
    """Rimuove una canzone dalla playlist per indice (0-based)."""
    if 0 <= indice < len(playlist["canzoni"]):
        playlist["canzoni"].pop(indice)
    else:
        print(f"Errore: indice {indice} non valido")


def durata_totale(playlist: dict) -> int:
    """Restituisce la durata totale della playlist in secondi."""
    return sum(canzone["durata"] for canzone in playlist["canzoni"])


def mostra_playlist(playlist: dict) -> str:
    """Restituisce una rappresentazione formattata della playlist."""
    if not playlist["canzoni"]:
        return f"=== Playlist: {playlist['nome']} ===\n(Vuota)"
    
    linee = [f"=== Playlist: {playlist['nome']} ==="]
    for i, canzone in enumerate(playlist["canzoni"], 1):
        linee.append(f"{i}. {info_canzone(canzone)}")
    
    # Aggiungi durata totale
    total = durata_totale(playlist)
    minuti = total // 60
    secondi = total % 60
    linee.append(f"\nDurata totale: {minuti}:{secondi:02d}")
    
    return "\n".join(linee)
