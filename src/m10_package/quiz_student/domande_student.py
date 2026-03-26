# Funzioni per gestire le domande (rappresentate come dizionari):
# - `crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:`
#   - `risposta` è l'indice 0-based dell'opzione corretta
# - `info_domanda(domanda: dict) -> str:`
#   - Restituisce una stringa leggibile con domanda + opzioni numerate
# - `risposta_valida(domanda: dict, scelta: int) -> bool:`
#   - Verifica se la scelta (1-based) è valida
# - `verifica_risposta(domanda: dict, scelta: int) -> bool:`
#   - Restituisce True se la scelta (1-based) è corretta


def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    