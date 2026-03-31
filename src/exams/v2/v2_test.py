from src.exams.v2.v2_student import (
    esercizio1_calcoli, esercizio2_filtri, esercizio3_prodotti
)


def test_esercizio1_calcoli():
    s1, c1, m1 = esercizio1_calcoli(5, [2, -3, 4, -5, 6])
    assert s1 == 56
    assert c1 == 2
    assert m1 == 4.0


def test_esercizio2_filtri():
    l2, nfil, nnon, somma = esercizio2_filtri(6, [3, 6, -9, 12, 5, 15])
    assert l2 == [3, 6, 12, 15]
    assert nfil == 4
    assert nnon == 2
    assert somma == 36


def test_esercizio3_prodotti():
    prodotti = ["Pane", "Latte", "Uova"]
    prezzi = [2.5, 1.2, 12.0]
    quantita = [10, 20, 15]
    valori, prodotto_max, count_cond = esercizio3_prodotti(prodotti, prezzi, quantita)
    assert valori == [25.0, 24.0, 180.0]
    assert prodotto_max == "Uova"
    assert count_cond == 2
