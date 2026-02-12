from src.m06_stringhe.es43_student import main

def test_conversione_binario(monkeypatch, capsys):
    inputs = iter(['1010'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Numero decimale: 10" in captured.out