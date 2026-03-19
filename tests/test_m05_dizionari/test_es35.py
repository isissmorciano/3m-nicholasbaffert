from src.m05_dizionari.es35_student import main

def test_frequenze(capsys):
    main()
    captured = capsys.readouterr()
    assert "rosso: 2" in captured.out
    assert "blu: 2" in captured.out
    assert "verde: 1" in captured.out