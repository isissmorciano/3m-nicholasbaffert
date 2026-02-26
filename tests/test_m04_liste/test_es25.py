from src.m04_liste.es25_student import main

def test_tabella_somme(monkeypatch, capsys):
    inputs = iter(['3', '4'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 3
    assert lines[0] == "0 1 2 3 "
    assert lines[1] == "1 2 3 4 "
    assert lines[2] == "2 3 4 5"