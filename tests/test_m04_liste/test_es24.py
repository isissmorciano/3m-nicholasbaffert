from src.m04_liste.es24_student import main

def test_tabella(monkeypatch, capsys):
    inputs = iter(['2', '3'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 2
    assert lines[0] == "1 1 1 "
    assert lines[1] == "1 1 1"