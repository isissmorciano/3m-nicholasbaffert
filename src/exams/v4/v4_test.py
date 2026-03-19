from src.exams.v4.v4_student import (
    salva_biblioteca, carica_biblioteca,
    filtra_per_genere, calcola_media_anno, trova_libro_piu_recente,
    conta_per_genere, modifica_anno_libro, main
)
import os


# --- Punto A: Salvataggio e Caricamento JSON ---

def test_salva_biblioteca():
    """Test salvataggio biblioteca in JSON."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943}
    ]
    nome_file = "test_biblioteca.json"
    salva_biblioteca(libri, nome_file)
    assert os.path.exists(nome_file)
    os.remove(nome_file)


def test_carica_biblioteca():
    """Test caricamento biblioteca da JSON."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949}
    ]
    nome_file = "test_biblioteca.json"
    salva_biblioteca(libri, nome_file)
    result = carica_biblioteca(nome_file)
    assert result == libri
    os.remove(nome_file)


def test_carica_biblioteca_file_non_esiste():
    """Test caricamento da file inesistente."""
    result = carica_biblioteca("nonexistent.json")
    assert result == []


# --- Punto B: Filtro per Genere ---

def test_filtra_per_genere():
    """Test filtro per genere."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965}
    ]
    result = filtra_per_genere(libri, "Fantascienza")
    assert len(result) == 2
    assert result[0]["titolo"] == "1984"
    assert result[1]["titolo"] == "Dune"


def test_filtra_per_genere_vuoto():
    """Test filtro con genere non presente."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943}
    ]
    result = filtra_per_genere(libri, "Horror")
    assert result == []


# --- Punto C: Statistiche ---

def test_calcola_media_anno():
    """Test calcolo media anno."""
    libri = [
        {"titolo": "A", "genere": "Romanzo", "anno": 1940},
        {"titolo": "B", "genere": "Romanzo", "anno": 1950},
        {"titolo": "C", "genere": "Romanzo", "anno": 1960}
    ]
    result = calcola_media_anno(libri)
    assert result == 1950.0


def test_calcola_media_anno_lista_vuota():
    """Test media su lista vuota."""
    result = calcola_media_anno([])
    assert result == 0.0


def test_calcola_media_anno_4_libri():
    """Test media anno con 4 libri."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    result = calcola_media_anno(libri)
    assert result == 1963.5


def test_trova_libro_piu_recente():
    """Test ricerca libro più recente."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    result = trova_libro_piu_recente(libri)
    assert result is not None
    assert result["titolo"] == "Harry Potter"
    assert result["anno"] == 1997


def test_trova_libro_piu_recente_lista_vuota():
    """Test con lista vuota."""
    result = trova_libro_piu_recente([])
    assert result is None


# --- Punto D: Conta per Genere ---

def test_conta_per_genere():
    """Test conteggio libri per genere."""
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    result = conta_per_genere(libri)
    assert result["Romanzo"] == 1
    assert result["Fantascienza"] == 2
    assert result["Fantasy"] == 1


def test_conta_per_genere_singolo():
    """Test conteggio con un solo genere."""
    libri = [
        {"titolo": "A", "genere": "Avventura", "anno": 2000},
        {"titolo": "B", "genere": "Avventura", "anno": 2001}
    ]
    result = conta_per_genere(libri)
    assert result == {"Avventura": 2}


def test_conta_per_genere_lista_vuota():
    """Test conteggio su lista vuota."""
    result = conta_per_genere([])
    assert result == {}


# --- Punto E: Modifica Libro ---

def test_modifica_anno_libro_success():
    """Test modifica anno di un libro esistente."""
    libri = [
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949}
    ]
    success, messaggio, libri_modificati = modifica_anno_libro(libri, "1984", 1950)
    assert success is True
    assert "1984" in messaggio
    assert "1950" in messaggio
    assert libri_modificati[0]["anno"] == 1950


def test_modifica_anno_libro_non_trovato():
    """Test modifica con libro non trovato."""
    libri = [
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949}
    ]
    success, messaggio, libri_modificati = modifica_anno_libro(libri, "Titanic", 2000)
    assert success is False
    assert "Titanic" in messaggio
    assert "non trovato" in messaggio
    assert len(libri_modificati) == 1


# --- Main ---

def test_main(monkeypatch, capsys):
    """Test della funzione main completa."""
    inputs = iter(["1984", "1950"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    captured = capsys.readouterr()
    
    # Verifica output Punto A
    assert "File 'biblioteca.json' salvato con successo." in captured.out
    assert "Libri in archivio: 4" in captured.out
    
    # Verifica output Punto B
    assert "Libri di Fantascienza: 2" in captured.out
    assert "1984" in captured.out
    assert "Dune" in captured.out
    
    # Verifica output Punto C
    assert "Media anno di pubblicazione: 1963.5" in captured.out
    assert "Libro più recente: Harry Potter (1997)" in captured.out
    
    # Verifica output Punto D
    assert "Libri per genere:" in captured.out
    assert "Fantasy: 1" in captured.out
    assert "Fantascienza: 2" in captured.out
    assert "Romanzo: 1" in captured.out
    
    # Verifica output Punto E
    assert "1984" in captured.out
    assert "1950" in captured.out
    
    # Cleanup
    if os.path.exists("biblioteca.json"):
        os.remove("biblioteca.json")
