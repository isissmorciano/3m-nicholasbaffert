from src.m05_dizionari.es31_student import main

def test_titoli(capsys):
    main()
    captured = capsys.readouterr()
    assert "Titoli dei libri:" in captured.out
    assert "1984" in captured.out
    assert "Il Signore degli Anelli" in captured.out
    assert "Harry Potter" in captured.out