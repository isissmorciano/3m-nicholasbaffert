from src.m04_liste.es15_student import main

def test_conteggio_pari(monkeypatch, capsys):
    inputs = iter(['3', '4', '7', '10'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Il numero di numeri pari inseriti è: 2" in captured.out