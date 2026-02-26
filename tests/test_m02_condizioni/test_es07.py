from src.m02_condizioni.es07_student import main

def test_rettangolo(monkeypatch, capsys):
    inputs = iter(['3', '4', '5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il triangolo è rettangolo." in captured.out

def test_non_rettangolo(monkeypatch, capsys):
    inputs = iter(['3', '4', '6'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il triangolo non è rettangolo." in captured.out