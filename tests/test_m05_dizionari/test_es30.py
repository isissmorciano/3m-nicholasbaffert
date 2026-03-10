from src.m05_dizionari.es30_student import main

def test_conteggio(capsys):
    main()
    captured = capsys.readouterr()
    assert "Numero di prodotti che costano più di 1.7 euro: 2" in captured.out