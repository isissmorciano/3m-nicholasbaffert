from src.m02_condizioni.es05_student import main

def test_due_soluzioni(monkeypatch, capsys):
    inputs = iter(['1', '0', '-4'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Le soluzioni sono x1 = 2.0 e x2 = -2.0" in captured.out

def test_soluzione_doppia(monkeypatch, capsys):
    inputs = iter(['1', '2', '1'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La soluzione doppia è x = -1.0" in captured.out

def test_nessuna_soluzione(monkeypatch, capsys):
    inputs = iter(['1', '0', '4'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Non ci sono soluzioni reali." in captured.out