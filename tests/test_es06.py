from src.m02_condizioni.es06_student import main

def test_insufficiente(monkeypatch, capsys):
    inputs = iter(['4'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Giudizio: insufficiente" in captured.out

def test_sufficiente(monkeypatch, capsys):
    inputs = iter(['6'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Giudizio: sufficiente" in captured.out

def test_buono(monkeypatch, capsys):
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Giudizio: buono" in captured.out

def test_ottimo(monkeypatch, capsys):
    inputs = iter(['8'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Giudizio: ottimo" in captured.out

def test_uscita(monkeypatch, capsys):
    inputs = iter(['-1'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Uscita dal programma." in captured.out

def test_fuori_range(monkeypatch, capsys):
    inputs = iter(['11'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Errore: voto fuori range." in captured.out