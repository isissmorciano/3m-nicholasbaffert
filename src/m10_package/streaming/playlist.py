"""Modulo playlist per gestire collezioni di video in uno streaming package."""

from .video import dimensione_video


def crea_playlist(nome: str) -> dict:
    """Crea una playlist vuota.

    Args:
        nome: Nome della playlist

    Returns:
        Dizionario con nome e lista video vuota
    """
    return {"nome": nome, "video": []}


def aggiungi_video(playlist: dict, video: dict) -> None:
    """Aggiunge un video alla playlist.

    Args:
        playlist: Dizionario della playlist
        video: Dizionario del video da aggiungere
    """
    playlist["video"].append(video)


def rimuovi_video(playlist: dict, indice: int) -> None:
    """Rimuove un video dalla playlist per indice.

    Args:
        playlist: Dizionario della playlist
        indice: Indice 0-based del video da rimuovere
    """
    if 0 <= indice < len(playlist["video"]):
        playlist["video"].pop(indice)


def durata_totale(playlist: dict) -> int:
    """Calcola la durata totale della playlist in secondi.

    Args:
        playlist: Dizionario della playlist

    Returns:
        Durata totale in secondi
    """
    # return sum(video["durata"] for video in playlist["video"])
    durata_totale = 0
    for video in playlist["video"]:
        durata_totale += video["durata"]
    return durata_totale


def dimensione_totale(playlist: dict) -> float:
    """Calcola la dimensione totale della playlist in MB.

    Args:
        playlist: Dizionario della playlist

    Returns:
        Dimensione totale in MB arrotondata a 2 decimali
    """
    # total = sum(dimensione_video(video) for video in playlist["video"])
    total = 0
    for video in playlist["video"]:
        total += dimensione_video(video)
    return round(total, 2)


def ordina_per_durata(playlist: dict) -> list:
    """Restituisce lista di video ordinati per durata crescente.

    Args:
        playlist: Dizionario della playlist

    Returns:
        Lista di video ordinati per durata
    """
    return playlist["video"].sort(key=lambda video: video["durata"])


def mostra_playlist(playlist: dict) -> str:
    """Restituisce stringa formattata con tutti i video della playlist.

    Args:
        playlist: Dizionario della playlist

    Returns:
        Stringa formattata con i dettagli della playlist
    """
    from .video import info_video

    linee = [f"Playlist: {playlist['nome']}"]
    for video in playlist["video"]:
        linee.append(f"- {info_video(video)}")

    return "\n".join(linee)
