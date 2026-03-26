"""Modulo per la gestione delle domande del quiz."""


def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    """Crea una domanda con opzioni e indice della risposta corretta.

    La risposta corretta è un indice 0-based nella lista delle opzioni.
    """
    return {"testo": testo, "opzioni": opzioni, "risposta": risposta}


def info_domanda(domanda: dict) -> str:
    """Restituisce una rappresentazione testuale della domanda.

    Il formato è:
        <testo>
        1. <opzione1>
        2. <opzione2>
        ...
    """
    linee = [domanda["testo"]]
    for i, opzione in enumerate(domanda["opzioni"], 1):
        linee.append(f"{i}. {opzione}")
    return "\n".join(linee)


def risposta_valida(domanda: dict, scelta: int) -> bool:
    """Verifica se una scelta (1-based) è valida per la domanda."""
    return 1 <= scelta <= len(domanda["opzioni"])


def verifica_risposta(domanda: dict, scelta: int) -> bool:
    """Verifica se la scelta (1-based) corrisponde alla risposta corretta."""
    if not risposta_valida(domanda, scelta):
        return False
    return (scelta - 1) == domanda["risposta"]
