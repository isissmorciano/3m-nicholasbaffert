from src.m06_stringhe.es41_student import main

def test_analizzatore_testo(monkeypatch, capsys):
    inputs = iter(['Ciao mondo. Python è fantastico.'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Analisi testo:" in captured.out
    assert "\tCaratteri: 32" in captured.out
    assert "\tParole: 5" in captured.out
    assert "\tFrasi: 3" in captured.out