from src.m06_stringhe.es39_student import main

def test_manipolazione_stringhe(monkeypatch, capsys):
    inputs = iter(['ciao hi mondo python'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Parola 'hi' troppo corta per slicing." in captured.out
    assert "Parola: ciao -> Primi 3: cia, Ultimi 3: iao, Modificata: CIAO" in captured.out
    assert "Parola: mondo -> Primi 3: mon, Ultimi 3: ndo, Modificata: MONDO" in captured.out
    assert "Parola: python -> Primi 3: pyt, Ultimi 3: hon, Modificata: PYTHON" in captured.out
    assert "Frase concatenata: CIAO MONDO PYTHON" in captured.out