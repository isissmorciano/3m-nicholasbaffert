from src.m05_dizionari.es27_student import main

def test_dizionario(monkeypatch, capsys):
    inputs = iter(['Mario', '30', 'Milano'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Nome: Mario" in captured.out
    assert "Età: 30" in captured.out
    assert "Città: Milano" in captured.out