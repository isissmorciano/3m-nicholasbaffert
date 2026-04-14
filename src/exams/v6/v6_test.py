from src.exams.v6.biblioteca.libri import (
    crea_libro,
    info_libro,
    libro_disponibile,
    filtra_per_genere,
    libri_disponibili,
    cerca_per_autore,
)
from src.exams.v6.biblioteca.prestiti import (
    crea_utente,
    crea_biblioteca,
    aggiungi_libro,
    presta_libro,
    restituisci_libro,
    libri_prestati,
)


def test_crea_libro():
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    assert libro["titolo"] == "1984"
    assert libro["autore"] == "George Orwell"
    assert libro["genere"] == "Fantascienza"
    assert libro["copie_disponibili"] == 1


def test_info_libro():
    libro = crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
    assert info_libro(libro) == "Dune di Frank Herbert (Fantascienza) - Copie disponibili: 2"


def test_libro_disponibile():
    assert libro_disponibile(crea_libro("Dune", "Frank Herbert", "Fantascienza", 2))
    assert not libro_disponibile(crea_libro("1984", "George Orwell", "Fantascienza", 0))


def test_filtra_per_genere():
    libri = [
        crea_libro("1984", "George Orwell", "Fantascienza", 1),
        crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1),
    ]
    result = filtra_per_genere(libri, "Fantascienza")
    assert len(result) == 1
    assert result[0]["titolo"] == "1984"


def test_libri_disponibili():
    libri = [
        crea_libro("1984", "George Orwell", "Fantascienza", 0),
        crea_libro("Dune", "Frank Herbert", "Fantascienza", 2),
    ]
    result = libri_disponibili(libri)
    assert len(result) == 1
    assert result[0]["titolo"] == "Dune"


def test_cerca_per_autore():
    libri = [
        crea_libro("1984", "George Orwell", "Fantascienza", 1),
        crea_libro("Dune", "Frank Herbert", "Fantascienza", 2),
    ]
    result = cerca_per_autore(libri, "George Orwell")
    assert len(result) == 1
    assert result[0]["titolo"] == "1984"


def test_crea_utente():
    utente = crea_utente("Mario", "Rossi")
    assert utente == {"nome": "Mario", "cognome": "Rossi"}


def test_crea_biblioteca_e_aggiungi_libro():
    biblioteca = crea_biblioteca()
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    aggiungi_libro(biblioteca, libro)
    assert biblioteca["libri"] == [libro]
    assert libro["copie_iniziali"] == 1


def test_presta_libro_successo():
    biblioteca = crea_biblioteca()
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    aggiungi_libro(biblioteca, libro)
    assert presta_libro(biblioteca, libro)
    assert libro["copie_disponibili"] == 0
    result = libri_prestati(biblioteca)
    assert len(result) == 1
    assert result[0]["titolo"] == "1984"


def test_presta_libro_esaurito():
    biblioteca = crea_biblioteca()
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 0)
    aggiungi_libro(biblioteca, libro)
    assert not presta_libro(biblioteca, libro)
    assert libri_prestati(biblioteca) == []


def test_restituisci_libro_successo():
    biblioteca = crea_biblioteca()
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    aggiungi_libro(biblioteca, libro)
    presta_libro(biblioteca, libro)
    assert restituisci_libro(biblioteca, libro)
    assert libro["copie_disponibili"] == 1
    assert libri_prestati(biblioteca) == []


def test_restituisci_libro_non_prestato():
    biblioteca = crea_biblioteca()
    libro = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    aggiungi_libro(biblioteca, libro)
    assert not restituisci_libro(biblioteca, libro)
