from src.m04_liste.es13_student import main

def test_media_normale(monkeypatch, capsys):
    inputs = iter(['3', '4', '7', '10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La media vale: 7.00" in captured.out

def test_lista_vuota(monkeypatch, capsys):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "la lista e' vuota" in captured.out