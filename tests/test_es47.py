from src.m08_funzioni.es47_student import chiedi_numeri, scegli_operazione, calcola

def test_chiedi_numeri(monkeypatch):
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    result = chiedi_numeri()
    assert result == [5.0, 3.0]

def test_scegli_operazione(monkeypatch):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    result = scegli_operazione()
    assert result == "+"

def test_calcola():
    assert calcola(5.0, 3.0, "+") == 8.0
    assert calcola(5.0, 3.0, "-") == 2.0
    assert calcola(5.0, 3.0, "*") == 15.0
    assert calcola(6.0, 2.0, "/") == 3.0
    assert calcola(5.0, 0.0, "/") is None