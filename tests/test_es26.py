from src.m04_liste.es26_student import main

def test_ordinamento(monkeypatch, capsys):
    inputs = iter(['4', '3', '1', '4', '2'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Lista originale: [3, 1, 4, 2]" in captured.out
    assert "Lista ordinata: [1, 2, 3, 4]" in captured.out