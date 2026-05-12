from src.exams.v3.v3_student import (
    PASSWORD_COMUNI,
    conta_caratteri, valida_password, livello_sicurezza,
    calcola_costo_totale, visualizza_ricetta
)


def test_conta_caratteri():
    assert conta_caratteri("MyPass123") == {"maiuscole": 2, "minuscole": 4, "numeri": 3}


def test_valida_password_valida():
    assert valida_password("MyPass123") is True


def test_valida_password_non_valida_ragione():
    assert valida_password("password") is False
    assert valida_password("mypassword") is False
    assert valida_password("Mypa1") is False


def test_livello_sicurezza():
    assert livello_sicurezza("MyPass123") == 2
    assert livello_sicurezza("MySuperPass123") == 3


def test_calcola_costo_totale():
    ricetta = [
        {"nome": "farina", "quantita": 500.0, "prezzo_unitario": 0.01},
        {"nome": "uova", "quantita": 2.0, "prezzo_unitario": 0.3}
    ]
    assert calcola_costo_totale(ricetta) == 5.6


def test_visualizza_ricetta(capsys):
    ricetta = [
        {"nome": "farina", "quantita": 500.0, "prezzo_unitario": 0.01},
        {"nome": "uova", "quantita": 2.0, "prezzo_unitario": 0.3}
    ]
    visualizza_ricetta(ricetta)
    captured = capsys.readouterr()
    assert "farina: 500.0 x 0.01 = 5.0" in captured.out
    assert "Totale: 5.6 €" in captured.out
