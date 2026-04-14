from biblioteca.libri import (
    crea_libro,
    info_libro,
    filtra_per_genere,
    libri_disponibili,
    cerca_per_autore,
)
from biblioteca.prestiti import (
    crea_utente,
    crea_biblioteca,
    aggiungi_libro,
    presta_libro,
    restituisci_libro,
    libri_prestati,
)


def main() -> None:
    libri = [
        crea_libro("1984", "George Orwell", "Fantascienza", 1),
        crea_libro("Dune", "Frank Herbert", "Fantascienza", 2),
        crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1),
        crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3),
    ]

    biblioteca = crea_biblioteca()
    for libro in libri:
        aggiungi_libro(biblioteca, libro)

    utenti = [
        crea_utente("Mario", "Rossi"),
        crea_utente("Laura", "Bianchi"),
        crea_utente("Carlo", "Verdi"),
    ]

    for libro in libri:
        print(info_libro(libro))

    print()

    fantascienza = filtra_per_genere(libri, "Fantascienza")
    print(f"Libri di Fantascienza: {len(fantascienza)}")
    for libro in fantascienza:
        print(f"- {libro['titolo']}")

    disponibili = libri_disponibili(libri)
    print(f"Libri disponibili: {', '.join(libro['titolo'] for libro in disponibili)}")

    orwell = cerca_per_autore(libri, "George Orwell")
    print(f"Libri di George Orwell: {', '.join(libro['titolo'] for libro in orwell)}")

    print()

    risultato = presta_libro(biblioteca, libri[0])
    print(f"Prestito di {utenti[0]['nome']} {utenti[0]['cognome']} per {libri[0]['titolo']}: {risultato}")
    risultato = presta_libro(biblioteca, libri[0])
    print(f"Prestito di {utenti[1]['nome']} {utenti[1]['cognome']} per {libri[0]['titolo']}: {risultato}")

    print(info_libro(libri[0]))

    print()

    prestiti = libri_prestati(biblioteca)
    print(f"Libri prestati: {', '.join(libro['titolo'] for libro in prestiti)}")

    print()

    restituito = restituisci_libro(biblioteca, libri[0])
    print(f"Restituzione del libro {libri[0]['titolo']}: {restituito}")
    print(info_libro(libri[0]))


if __name__ == "__main__":
    main()
