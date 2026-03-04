from src.m04_liste.es16_student import main

def test_range_normale(monkeypatch, capsys):
    inputs = iter(['3', '4', '7', '10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il range dei numeri inseriti è: 6" in captured.out