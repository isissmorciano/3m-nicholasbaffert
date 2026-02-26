"""Modulo per la gestione delle canzoni."""


def crea_canzone(titolo: str, artista: str, durata: int) -> dict:
    """
    Crea una canzone rappresentata come dizionario.
    
    Args:
        titolo: Il titolo della canzone
        artista: Il nome dell'artista
        durata: La durata in secondi
        
    Returns:
        Un dizionario con chiavi: titolo, artista, durata
    """
    return {
        "titolo": titolo,
        "artista": artista,
        "durata": durata
    }


def info_canzone(canzone: dict) -> str:
    """
    Restituisce una stringa formattata della canzone.
    
    Formato: "Titolo - Artista (M:SS)"
    Esempio: "Bohemian Rhapsody - Queen (5:55)"
    """
    minuti = canzone["durata"] // 60
    secondi = canzone["durata"] % 60
    return f"{canzone['titolo']} - {canzone['artista']} ({minuti}:{secondi:02d})"
