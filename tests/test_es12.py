from src.m03_cicli.es12_student import main

def test_intervallo_uguale(monkeypatch, capsys):
    inputs = iter(['5', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma dei numeri nell'intervallo [5, 5] è: 5" in captured.out

def test_intervallo_piccolo(monkeypatch, capsys):
    inputs = iter(['1', '3'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma dei numeri nell'intervallo [1, 3] è: 6" in captured.out

def test_intervallo_esempio(monkeypatch, capsys):
    inputs = iter(['5', '9'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La somma dei numeri nell'intervallo [5, 9] è: 35" in captured.out