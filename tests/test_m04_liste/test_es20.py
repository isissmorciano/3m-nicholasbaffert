from src.m04_liste.es20_student import main

def test_numeri_filtrati(monkeypatch, capsys):
    inputs = iter(['5', '2', '1', '10', '2', '4', '6', '8', '12'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Numero di numeri: 4" in captured.out
    assert "Media: 5.0" in captured.out