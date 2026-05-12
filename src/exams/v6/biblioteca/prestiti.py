from .libri import libro_disponibile


def crea_utente(nome: str, cognome: str) -> dict:
    return {"nome": nome, "cognome": cognome}


def crea_biblioteca() -> dict:
    return {"libri": []}


def aggiungi_libro(biblioteca: dict, libro: dict) -> None:
    libro["copie_iniziali"] = libro["copie_disponibili"]
    biblioteca["libri"].append(libro)


def presta_libro(biblioteca: dict, libro: dict) -> bool:
    if not libro_disponibile(libro):
        return False

    libro["copie_disponibili"] -= 1
    return True


def restituisci_libro(biblioteca: dict, libro: dict) -> bool:
    if libro["copie_disponibili"] < libro["copie_iniziali"]:
        libro["copie_disponibili"] += 1
        return True
    return False


def libri_prestati(biblioteca: dict) -> list[dict]:
    return [
        libro
        for libro in biblioteca["libri"]
        if libro["copie_disponibili"] < libro["copie_iniziali"]
    ]
