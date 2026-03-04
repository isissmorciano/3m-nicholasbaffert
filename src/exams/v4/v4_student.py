import json


def salva_biblioteca(libri: list[dict], nome_file: str) -> None:
    """Salva la lista di libri in un file JSON."""
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(libri, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_biblioteca(nome_file: str) -> list[dict]:
    """Carica la lista di libri da un file JSON."""
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            libri = json.load(file)
        return libri
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []


def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    """Restituisce i libri di un genere specifico."""
    filtrati = []
    for libro in libri:
        if libro["genere"] == genere:
            filtrati.append(libro)
    return filtrati


def calcola_media_anno(libri: list[dict]) -> float:
    """Calcola la media degli anni di pubblicazione."""
    if not libri:
        return 0.0
    somma = 0
    for libro in libri:
        somma = somma + libro["anno"]
    media = somma / len(libri)
    return media


def trova_libro_piu_recente(libri: list[dict]) -> dict | None:
    """Restituisce il libro con l'anno più alto."""
    if not libri:
        return None
    piu_recente = libri[0]
    for libro in libri:
        if libro["anno"] > piu_recente["anno"]:
            piu_recente = libro
    return piu_recente


def conta_per_genere(libri: list[dict]) -> dict[str, int]:
    """Restituisce un dizionario con il conteggio dei libri per genere."""
    conteggio: dict[str, int] = {}
    for libro in libri:
        genere = libro["genere"]
        if genere in conteggio:
            conteggio[genere] += 1
        else:
            conteggio[genere] = 1
    return conteggio


def modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]:
    """Modifica l'anno di un libro dato il titolo. Restituisce (success, messaggio, libri_modificati)."""
    for libro in libri:
        if libro["titolo"] == titolo:
            libro["anno"] = nuovo_anno
            return (True, f"Libro '{titolo}' aggiornato con anno {nuovo_anno}. Totale libri: {len(libri)}", libri)
    return (False, f"Libro '{titolo}' non trovato.", libri)


def main() -> None:
    """Funzione principale."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    
    # Punto A: Salvataggio e caricamento JSON
    nome_file_json = "biblioteca.json"
    salva_biblioteca(libri, nome_file_json)
    
    libri_caricati = carica_biblioteca(nome_file_json)
    print(f"Libri in archivio: {len(libri_caricati)}")
    
    print()
    
    # Punto B: Filtro per genere
    fantascienza = filtra_per_genere(libri_caricati, "Fantascienza")
    print(f"Libri di Fantascienza: {len(fantascienza)}")
    for libro in fantascienza:
        print(f"- {libro['titolo']}")
    
    print()
    
    # Punto C: Statistiche
    media_anno = calcola_media_anno(libri_caricati)
    print(f"Media anno di pubblicazione: {media_anno}")
    
    piu_recente = trova_libro_piu_recente(libri_caricati)
    if piu_recente:
        print(f"Libro più recente: {piu_recente['titolo']} ({piu_recente['anno']})")
    
    print()
    
    # Punto D: Conta libri per genere
    conteggio = conta_per_genere(libri_caricati)
    print("Libri per genere:")
    for genere in sorted(conteggio.keys()):
        print(f"{genere}: {conteggio[genere]}")
    
    print()
    
    # Punto E: Bonus - Modifica anno di un libro
    titolo = input("Inserisci titolo da modificare: ").strip()
    nuovo_anno = int(input("Inserisci nuovo anno: "))
    
    success, messaggio, libri_caricati = modifica_anno_libro(libri_caricati, titolo, nuovo_anno)
    print(messaggio)

    print(libri_caricati)
    
    if success:
        salva_biblioteca(libri_caricati, nome_file_json)


if __name__ == "__main__":
    main()
