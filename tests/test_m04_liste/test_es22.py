from src.m04_liste.es22_student import main

def test_squadre(capsys):
    main()
    captured = capsys.readouterr()
    assert "Vincente: Juventus" in captured.out
    assert "Differenza con seconda: 5" in captured.out