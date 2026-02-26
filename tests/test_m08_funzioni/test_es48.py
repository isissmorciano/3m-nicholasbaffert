from src.m08_funzioni.es48_student import fattoriale

def test_fattoriale():
    assert fattoriale(0) == 1
    assert fattoriale(1) == 1
    assert fattoriale(5) == 120
    assert fattoriale(6) == 720