from src.m02_condizioni.es09_student import main

def test_multa_36(monkeypatch, capsys):
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La sanzione amministrativa è di euro 36." in captured.out

def test_multa_148(monkeypatch, capsys):
    inputs = iter(['25'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La sanzione amministrativa è di euro 148." in captured.out

def test_multa_370(monkeypatch, capsys):
    inputs = iter(['50'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La sanzione amministrativa è di euro 370." in captured.out

def test_multa_500(monkeypatch, capsys):
    inputs = iter(['70'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "La sanzione amministrativa è di euro 500." in captured.out