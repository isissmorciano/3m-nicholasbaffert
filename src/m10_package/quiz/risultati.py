"""Modulo per la gestione e la persistenza dei risultati del quiz."""

import json

Risultati = dict[str, int]


def crea_risultati() -> Risultati:
    """Crea una struttura vuota per salvare i risultati."""
    return {"totale": 0, "corretti": 0}


def registra_risposta(risultati: Risultati, corretta: bool) -> None:
    """Registra una nuova risposta (corretta o meno)."""
    risultati["totale"] += 1
    if corretta:
        risultati["corretti"] += 1


def percentuale_corrette(risultati: Risultati) -> float:
    """Restituisce la percentuale di risposte corrette (1 decimale)."""
    totale = risultati.get("totale", 0)
    if totale == 0:
        return 0.0
    return round(risultati.get("corretti", 0) / totale * 100, 1)


def mostra_risultati(risultati: Risultati) -> str:
    """Restituisce una stringa con il riepilogo dei risultati."""
    percentuale = percentuale_corrette(risultati)
    return (
        f"Risposte corrette: {risultati.get('corretti', 0)}/" 
        f"{risultati.get('totale', 0)} ({percentuale}%)"
    )


def salva_risultati(risultati: Risultati, nome_file: str) -> None:
    """Salva i risultati in un file JSON."""
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(risultati, file, indent=4)
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_risultati(nome_file: str) -> Risultati:
    """Carica i risultati da un file JSON. Se fallisce, restituisce risultati vuoti."""
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            dati = json.load(file)
        return {"totale": int(dati.get("totale", 0)), "corretti": int(dati.get("corretti", 0))}
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return crea_risultati()
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Errore nel parsing del file: {e}")
        return crea_risultati()
