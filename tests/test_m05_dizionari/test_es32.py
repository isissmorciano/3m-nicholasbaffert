from src.m05_dizionari.es32_student import main

def test_citta(capsys):
    main()
    captured = capsys.readouterr()
    assert "Roma: 2870000 abitanti" in captured.out
    assert "Milano: 1350000 abitanti" in captured.out
    assert "Napoli: 975000 abitanti" in captured.out