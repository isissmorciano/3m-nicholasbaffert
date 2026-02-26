from src.m04_liste.es18_student import main

def test_stringhe_filtrate(monkeypatch, capsys):
    inputs = iter(['3', '3', 'a', 'abcd', 'efghi'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Numero di stringhe più lunghe di 3: 2" in captured.out
    assert "Lunghezza media delle stringhe più lunghe di 3: 4.5" in captured.out