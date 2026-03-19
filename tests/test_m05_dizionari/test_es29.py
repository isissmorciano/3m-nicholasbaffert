from src.m05_dizionari.es29_student import main

def test_vincitore(capsys):
    main()
    captured = capsys.readouterr()
    assert "Il giocatore con il punteggio più alto è Giulia con 95 punti." in captured.out