from src.m05_dizionari.es28_student import main

def test_medie(capsys):
    main()
    captured = capsys.readouterr()
    assert "Mario: Media voti = 8.3" in captured.out
    assert "Luca: Media voti = 7.0" in captured.out
    assert "Anna: Media voti = 9.0" in captured.out