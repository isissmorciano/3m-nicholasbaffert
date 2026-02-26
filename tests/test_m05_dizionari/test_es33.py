from src.m05_dizionari.es33_student import main

def test_colore_presente(monkeypatch, capsys):
    inputs = iter(['rosso'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Colore presente" in captured.out

def test_colore_non_trovato(monkeypatch, capsys):
    inputs = iter(['giallo'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Colore non trovato" in captured.out