from src.m02_condizioni.es04_student import main

def test_soluzione_normale(monkeypatch, capsys):
    inputs = iter(['2', '4'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La soluzione è x = -2.0" in captured.out

def test_indeterminata(monkeypatch, capsys):
    inputs = iter(['0', '0'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "L'equazione è indeterminata (infinite soluzioni)." in captured.out

def test_impossibile(monkeypatch, capsys):
    inputs = iter(['0', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "L'equazione è impossibile (nessuna soluzione)." in captured.out