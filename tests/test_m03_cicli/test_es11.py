from src.m03_cicli.es11_student import main

def test_somma_zero_numeri(monkeypatch, capsys):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma totale è: 0" in captured.out

def test_somma_un_numero(monkeypatch, capsys):
    inputs = iter(['1', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma totale è: 5" in captured.out

def test_somma_più_numeri(monkeypatch, capsys):
    inputs = iter(['3', '1', '2', '3'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma totale è: 6" in captured.out