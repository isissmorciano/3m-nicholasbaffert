from src.m07_cicli_while.es44_student import main

def test_input_valido(monkeypatch, capsys):
    inputs = iter(['-5', 'abc', '10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Errore: il numero deve essere positivo." in captured.out
    assert "Errore: inserisci un numero intero valido." in captured.out
    assert "Numero valido: 10" in captured.out