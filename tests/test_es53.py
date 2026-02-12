from src.m08_funzioni.es53_student import main, calcola_media, analizza_studente

def test_calcola_media():
    assert calcola_media([8.5, 7.8, 9.0, 8.2]) == 8.375

def test_analizza_studente():
    result = analizza_studente("Alice", [8.5, 7.8, 9.0, 8.2])
    assert result["nome"] == "Alice"
    assert result["media"] == 8.375
    assert result["min"] == 7.8
    assert result["max"] == 9.0

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "REPORT VOTI - CLASSE" in captured.out
    assert "Alice" in captured.out
    assert "Media classe:" in captured.out