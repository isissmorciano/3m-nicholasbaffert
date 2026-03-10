from src.m08_funzioni.es50_student import aggiungi_elemento, rimuovi_elemento, visualizza_lista, calcola_totale

def test_aggiungi_elemento(monkeypatch):
    lista = []
    inputs = iter(['pane', '2.5'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    result = aggiungi_elemento(lista)
    assert result is True
    assert lista == [{"nome": "pane", "prezzo": 2.5}]

def test_rimuovi_elemento(monkeypatch):
    lista = [{"nome": "pane", "prezzo": 2.5}]
    inputs = iter(['pane'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    rimuovi_elemento(lista)
    assert lista == []

def test_calcola_totale():
    lista = [{"nome": "pane", "prezzo": 2.5}, {"nome": "latte", "prezzo": 1.5}]
    assert calcola_totale(lista) == 4.0