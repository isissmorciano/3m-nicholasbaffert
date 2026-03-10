from src.m05_dizionari.es34_student import main

def test_hobby(monkeypatch, capsys):
    inputs = iter(['Mario', 'calcio', 'Luca', 'lettura', 'Anna', 'pittura'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Dizionario degli hobby:" in captured.out
    assert "Mario: calcio" in captured.out
    assert "Luca: lettura" in captured.out
    assert "Anna: pittura" in captured.out