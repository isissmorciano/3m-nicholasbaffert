def crea_libro(titolo: str, autore: str, genere: str, copie_disponibili: int) -> dict:
    return {
        "titolo": titolo,
        "autore": autore,
        "genere": genere,
        "copie_disponibili": copie_disponibili,
    }


def info_libro(libro: dict) -> str:
    return (
        f"{libro['titolo']} di {libro['autore']} ({libro['genere']}) - "
        f"Copie disponibili: {libro['copie_disponibili']}"
    )


def libro_disponibile(libro: dict) -> bool:
    return libro["copie_disponibili"] > 0


def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    return [libro for libro in libri if libro["genere"] == genere]


def libri_disponibili(libri: list[dict]) -> list[dict]:
    return [libro for libro in libri if libro_disponibile(libro)]


def cerca_per_autore(libri: list[dict], autore: str) -> list[dict]:
    return [libro for libro in libri if libro["autore"] == autore]
