from src.m04_liste.es17_student import main

def test_stringa_lunga(monkeypatch, capsys):
    inputs = iter(['3', 'ciao', 'buongiorno', 'ok'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La stringa più lunga è: 'buongiorno' con 10 caratteri" in captured.out