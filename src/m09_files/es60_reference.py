#!/usr/bin/env python3
"""Simple interactive menu for managing students (JSON storage).

No UUID, no argparse, no CSV. Pure menu-driven with for loops.
Separates logic (return values) from presentation (print in main).
"""

import json
import os

STORAGE_FILE = "studenti.json"


def load_studenti(path: str = STORAGE_FILE) -> list[dict[str, str | float]]:
    """Load students from JSON file. Return empty list if not found."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []


def save_studenti(studenti: list[dict[str, str | float]], path: str = STORAGE_FILE) -> None:
    """Save students to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, ensure_ascii=False, indent=4)


def valida_voto(voto_str: str) -> tuple[bool, str | float]:
    """Validate vote string. Returns (is_valid, value_or_error)."""
    try:
        voto = float(voto_str)
        if voto < 0 or voto > 10:
            return False, "Voto deve essere tra 0 e 10."
        return True, voto
    except ValueError:
        return False, "Voto deve essere un numero."


def formatta_lista(studenti: list[dict[str, str | float]]) -> str:
    """Format student list as string. Returns formatted output."""
    if not studenti:
        return "Nessuno studente."

    righe = []
    for i in range(len(studenti)):
        s = studenti[i]
        righe.append(f"{i}. {s['nome']} - Voto: {s['voto']}")
    return "\n".join(righe)


def mostra_dettaglio(
    studenti: list[dict[str, str | float]], indice: int
) -> tuple[bool, str, dict[str, str | float] | None]:
    """Show detail for one student by index. Returns (success, message, data)."""
    if indice < 0 or indice >= len(studenti):
        return False, f"Indice non valido: {indice}", None

    s = studenti[indice]
    messaggio = f"Nome: {s['nome']}\nVoto: {s['voto']}"
    return True, messaggio, s


def aggiungi_studente(studenti: list[dict[str, str | float]]) -> tuple[bool, str, dict[str, str | float] | None]:
    """Add a new student. Returns (success, message, new_student)."""
    nome = input("Nome studente: ").strip()
    if not nome:
        return False, "Errore: nome non può essere vuoto.", None

    voto_str = input("Voto (0-10): ")
    is_valid, result = valida_voto(voto_str)
    if not is_valid:
        return False, f"Errore: {result}", None

    voto = result
    studente = {"nome": nome, "voto": voto}
    studenti.append(studente)
    return True, f"Aggiunto: {nome} con voto {voto}", studente


def cancella_studente(studenti: list[dict[str, str | float]]) -> tuple[bool, str]:
    """Delete a student by index. Returns (success, message)."""
    if not studenti:
        return False, "Nessuno studente da cancellare."

    indice_str = input("Indice da cancellare: ")
    try:
        indice = int(indice_str)
    except ValueError:
        return False, "Errore: indice deve essere un numero."

    if indice < 0 or indice >= len(studenti):
        return False, "Errore: indice non valido."

    nome = studenti[indice]["nome"]
    studenti.pop(indice)
    return True, f"Cancellato: {nome}"


def aggiorna_studente(studenti: list[dict[str, str | float]]) -> tuple[bool, str]:
    """Update a student's voto by index. Returns (success, message)."""
    if not studenti:
        return False, "Nessuno studente da aggiornare."

    indice_str = input("Indice da aggiornare: ")
    try:
        indice = int(indice_str)
    except ValueError:
        return False, "Errore: indice deve essere un numero."

    if indice < 0 or indice >= len(studenti):
        return False, "Errore: indice non valido."

    voto_str = input("Nuovo voto (0-10): ")
    is_valid, result = valida_voto(voto_str)
    if not is_valid:
        return False, f"Errore: {result}"

    voto = result
    studenti[indice]["voto"] = voto
    return True, f"Aggiornato: {studenti[indice]['nome']} con voto {voto}"


def ricerca_per_nome(
    studenti: list[dict[str, str | float]], termine: str | None = None
) -> list[dict[str, str | float]]:
    """Search students by name. Returns list of results."""
    if termine is None:
        termine = input("Termine di ricerca: ").strip().lower()
    else:
        termine = termine.lower()

    if not termine:
        return []

    risultati = []
    for s in studenti:
        nome_lower = s["nome"].lower()
        if termine in nome_lower:
            risultati.append(s)

    return risultati


def filtra_per_voto(
    studenti: list[dict[str, str | float]], min_voto: float | None = None, max_voto: float | None = None
) -> list[dict[str, str | float]]:
    """Filter students by voto range. Returns list of results."""
    if min_voto is None:
        min_str = input("Voto minimo (0-10): ")
        is_valid, result = valida_voto(min_str)
        if not is_valid:
            return []
        min_voto = result

    if max_voto is None:
        max_str = input("Voto massimo (0-10): ")
        is_valid, result = valida_voto(max_str)
        if not is_valid:
            return []
        max_voto = result

    if min_voto > max_voto:
        return []

    risultati = []
    for s in studenti:
        if min_voto <= s["voto"] <= max_voto:
            risultati.append(s)

    return risultati


def calcola_media(studenti: list[dict[str, str | float]]) -> float:
    """Calculate average grade. Returns float or 0 if no students."""
    if not studenti:
        return 0.0

    total = 0.0
    for s in studenti:
        total += s["voto"]
    return total / len(studenti)


def trova_migliore(studenti: list[dict[str, str | float]]) -> dict[str, str | float] | None:
    """Find student with highest grade. Returns student dict or None."""
    if not studenti:
        return None

    migliore = studenti[0]
    for s in studenti:
        if s["voto"] > migliore["voto"]:
            migliore = s
    return migliore


def trova_peggiore(studenti: list[dict[str, str | float]]) -> dict[str, str | float] | None:
    """Find student with lowest grade. Returns student dict or None."""
    if not studenti:
        return None

    peggiore = studenti[0]
    for s in studenti:
        if s["voto"] < peggiore["voto"]:
            peggiore = s
    return peggiore


def main() -> None:
    """Main menu loop - handles all output."""
    studenti = load_studenti()

    while True:
        print("\n=== GESTIONE STUDENTI ===")
        print("1. Aggiungi studente")
        print("2. Visualizza lista")
        print("3. Visualizza dettaglio")
        print("4. Aggiorna voto")
        print("5. Cancella studente")
        print("6. Ricerca per nome")
        print("7. Filtra per voto")
        print("8. Statistiche")
        print("9. Esci")

        scelta = input("\nScelta (1-9): ").strip()

        if scelta == "1":
            success, msg, _ = aggiungi_studente(studenti)
            print(msg)

        elif scelta == "2":
            output = formatta_lista(studenti)
            print(output)

        elif scelta == "3":
            output = formatta_lista(studenti)
            print(output)
            indice_str = input("Indice: ")
            try:
                indice = int(indice_str)
                success, msg, _ = mostra_dettaglio(studenti, indice)
                print(msg)
            except ValueError:
                print("Errore: indice deve essere un numero.")

        elif scelta == "4":
            output = formatta_lista(studenti)
            print(output)
            success, msg = aggiorna_studente(studenti)
            print(msg)

        elif scelta == "5":
            output = formatta_lista(studenti)
            print(output)
            success, msg = cancella_studente(studenti)
            print(msg)

        elif scelta == "6":
            risultati = ricerca_per_nome(studenti)
            if risultati:
                print(f"Trovato(i) {len(risultati)} risultato(i):")
                for s in risultati:
                    print(f"  {s['nome']} - Voto: {s['voto']}")
            else:
                print("Nessuno studente trovato.")

        elif scelta == "7":
            risultati = filtra_per_voto(studenti)
            if risultati:
                print(f"Trovato(i) {len(risultati)} risultato(i):")
                for s in risultati:
                    print(f"  {s['nome']} - Voto: {s['voto']}")
            else:
                print("Nessuno studente in questo range.")

        elif scelta == "8":
            media = calcola_media(studenti)
            migliore = trova_migliore(studenti)
            peggiore = trova_peggiore(studenti)

            print("\n--- Statistiche ---")
            print(f"Numero studenti: {len(studenti)}")
            print(f"Media voti: {media:.2f}")
            if migliore:
                print(f"Voto più alto: {migliore['nome']} ({migliore['voto']})")
            if peggiore:
                print(f"Voto più basso: {peggiore['nome']} ({peggiore['voto']})")

        elif scelta == "9":
            save_studenti(studenti)
            print("Salvato. Arrivederci!")
            break

        else:
            print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()
