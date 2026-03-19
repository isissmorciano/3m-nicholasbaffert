"""Test per l'Esercizio 64: Package Quiz."""

from src.m10_package.quiz import domande, risultati


def test_crea_domanda():
    q = domande.crea_domanda("Test?", ["A", "B", "C"], 1)
    assert q["testo"] == "Test?"
    assert q["opzioni"] == ["A", "B", "C"]
    assert q["risposta"] == 1


def test_info_domanda():
    q = domande.crea_domanda("Domanda?", ["A", "B"], 0)
    info = domande.info_domanda(q)
    assert "Domanda?" in info
    assert "1. A" in info
    assert "2. B" in info


def test_risposta_valida():
    q = domande.crea_domanda("Domanda?", ["A", "B"], 0)
    assert domande.risposta_valida(q, 1)
    assert domande.risposta_valida(q, 2)
    assert not domande.risposta_valida(q, 0)
    assert not domande.risposta_valida(q, 3)


def test_verifica_risposta():
    q = domande.crea_domanda("Domanda?", ["A", "B"], 1)
    assert domande.verifica_risposta(q, 2)
    assert not domande.verifica_risposta(q, 1)


def test_crea_risultati():
    r = risultati.crea_risultati()
    assert r["totale"] == 0
    assert r["corretti"] == 0


def test_registra_risposta():
    r = risultati.crea_risultati()
    risultati.registra_risposta(r, True)
    risultati.registra_risposta(r, False)
    assert r["totale"] == 2
    assert r["corretti"] == 1


def test_percentuale_corrette():
    r = risultati.crea_risultati()
    risultati.registra_risposta(r, True)
    risultati.registra_risposta(r, True)
    risultati.registra_risposta(r, False)
    assert risultati.percentuale_corrette(r) == 66.7


def test_mostra_risultati():
    r = risultati.crea_risultati()
    risultati.registra_risposta(r, True)
    risultati.registra_risposta(r, False)
    output = risultati.mostra_risultati(r)
    assert "1/2" in output
    assert "50.0" in output


def test_salva_e_carica_risultati(tmp_path):
    r = risultati.crea_risultati()
    risultati.registra_risposta(r, True)
    risultati.registra_risposta(r, False)

    file_path = tmp_path / "risultati.json"
    risultati.salva_risultati(r, str(file_path))

    caricati = risultati.carica_risultati(str(file_path))
    assert caricati["totale"] == 2
    assert caricati["corretti"] == 1
