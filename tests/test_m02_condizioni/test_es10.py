from src.m02_condizioni.es10_student import main

def test_inverno(monkeypatch, capsys):
    inputs = iter(['gen'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il mese GEN appartiene alla stagione: inverno." in captured.out

def test_primavera(monkeypatch, capsys):
    inputs = iter(['apr'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il mese APR appartiene alla stagione: primavera." in captured.out

def test_estate(monkeypatch, capsys):
    inputs = iter(['lug'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il mese LUG appartiene alla stagione: estate." in captured.out

def test_autunno(monkeypatch, capsys):
    inputs = iter(['ott'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il mese OTT appartiene alla stagione: autunno." in captured.out

def test_mese_inesistente(monkeypatch, capsys):
    inputs = iter(['xyz'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Sigla mese inesistente." in captured.out