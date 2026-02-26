from src.m04_liste.es19_student import main

def test_stringhe_con_c(monkeypatch, capsys):
    inputs = iter(['3', 'a', '3', 'ciao', 'test', 'palla'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Numero di stringhe che contengono 'a' e sono più lunghe di 3: 2" in captured.out
    assert "Lunghezza minima delle stringhe che contengono 'a' e sono più lunghe di 3: 4" in captured.out