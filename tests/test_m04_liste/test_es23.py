from src.m04_liste.es23_student import main

def test_citta(capsys):
    main()
    captured = capsys.readouterr()
    assert "Città con densità massima: Napoli" in captured.out
    assert "Città con densità >1000: 3" in captured.out