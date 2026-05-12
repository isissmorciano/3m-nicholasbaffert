from src.m04_liste.es21_student import main

def test_studenti(capsys):
    main()
    captured = capsys.readouterr()
    assert "Media: 8.0" in captured.out
    assert "Massimo: 9" in captured.out
    assert "Minimo: 7" in captured.out