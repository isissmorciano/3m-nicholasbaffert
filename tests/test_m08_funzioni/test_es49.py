from src.m08_funzioni.es49_student import genera_numero, verifica_tentativo, aggiorna_contatore
import random

def test_genera_numero():
    random.seed(42)
    result = genera_numero()
    assert 1 <= result <= 100

def test_verifica_tentativo():
    assert verifica_tentativo(50, 50) == "corretto"
    assert verifica_tentativo(40, 50) == "basso"
    assert verifica_tentativo(60, 50) == "alto"

def test_aggiorna_contatore():
    assert aggiorna_contatore(0) == 1
    assert aggiorna_contatore(5) == 6