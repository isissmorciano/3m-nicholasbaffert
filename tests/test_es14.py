from src.m04_liste.es14_student import main

def test_massimo_normale(monkeypatch, capsys):
    inputs = iter(['3', '4', '7', '10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il massimo dei numeri inseriti è: 10" in captured.out

def test_input_non_valido(monkeypatch, capsys):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Errore: numero di valori deve essere positivo." in captured.out