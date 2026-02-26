from src.m08_funzioni.es52_student import calcola_bmi, classifica_bmi, get_colore_categoria

def test_calcola_bmi():
    assert calcola_bmi(70, 1.75) == 70 / (1.75 ** 2)

def test_classifica_bmi():
    assert classifica_bmi(16) == "Sottopeso"
    assert classifica_bmi(22) == "Peso normale"
    assert classifica_bmi(27) == "Sovrappeso"
    assert classifica_bmi(32) == "Obeso"

def test_get_colore_categoria():
    assert get_colore_categoria(16) == "🔵 Sottopeso"
    assert get_colore_categoria(22) == "🟢 Peso normale"
    assert get_colore_categoria(27) == "🟡 Sovrappeso"
    assert get_colore_categoria(32) == "🔴 Obeso"