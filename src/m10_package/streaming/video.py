"""Modulo video per gestire video singoli in uno streaming package."""


def crea_video(titolo: str, durata: int, risoluzione: str, bitrate: int) -> dict:
    """Crea un video con metadati.

    Args:
        titolo: Titolo del video
        durata: Durata in secondi
        risoluzione: Risoluzione (es. "1080p", "720p", "480p", "360p")
        bitrate: Bitrate in kbps

    Returns:
        Dizionario con le proprietà del video
    """
    return {"titolo": titolo, "durata": durata, "risoluzione": risoluzione, "bitrate": bitrate}


def info_video(video: dict) -> str:
    """Restituisce informazioni formattate di un video.

    Args:
        video: Dizionario del video

    Returns:
        Stringa formattata: "Titolo - M:SS - Risoluzione - Bitrate kbps"
    """

    minuti = video["durata"] // 60
    secondi = video["durata"] % 60
    tempo_formattato = f"{minuti}:{secondi:02d}"

    return f"{video['titolo']} - {tempo_formattato} - {video['risoluzione']} - {video['bitrate']} kbps"


def dimensione_video(video: dict) -> float:
    """Calcola la dimensione approssimativa del video in MB.

    Formula: (durata_secondi * bitrate) / (8 * 1024)

    Args:
        video: Dizionario del video

    Returns:
        Dimensione in MB arrotondata a 2 decimali
    """
    dimensione_mb = (video["durata"] * video["bitrate"]) / (8 * 1024)
    return round(dimensione_mb, 2)
