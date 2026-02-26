from src.m06_stringhe.es42_student import main

def test_analisi_testo(monkeypatch, capsys):
    inputs = iter(['Ciao mondo'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Conteggi vocali: {'Ciao': 3, 'mondo': 2}" in captured.out
    assert "Parola con più vocali: Ciao (3 vocali)" in captured.out