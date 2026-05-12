"""Test per l'Esercizio 65: Package Diario."""

from src.m10_package.diario import entrate, persistenza


def test_crea_entrata():
    voce = entrate.crea_entrata("2026-04-08", "Ho studiato Python.", "studio", 60)
    assert voce["data"] == "2026-04-08"
    assert voce["testo"] == "Ho studiato Python."
    assert voce["categoria"] == "studio"
    assert voce["durata"] == 60


def test_info_entrata():
    voce = entrate.crea_entrata("2026-04-09", "Passeggiata.", "tempo libero", 30)
    info = entrate.info_entrata(voce)
    assert "2026-04-09" in info
    assert "tempo libero" in info
    assert "30 min" in info
    assert "Passeggiata." in info


def test_crea_diario_e_aggiungi_entrata():
    diario = entrate.crea_diario()
    assert diario["entrate"] == []

    voce = entrate.crea_entrata("2026-04-08", "Scrittura.", "lavoro", 45)
    entrate.aggiungi_entrata(diario, voce)
    assert len(diario["entrate"]) == 1
    assert diario["entrate"][0]["categoria"] == "lavoro"


def test_rimuovi_entrata():
    diario = entrate.crea_diario()
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-08", "A", "studio", 30))
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-09", "B", "tempo libero", 20))

    entrate.rimuovi_entrata(diario, 0)
    assert len(diario["entrate"]) == 1
    assert diario["entrate"][0]["testo"] == "B"


def test_tempo_totale_e_per_categoria():
    diario = entrate.crea_diario()
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-08", "A", "studio", 60))
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-08", "B", "studio", 30))
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-09", "C", "tempo libero", 15))

    assert entrate.tempo_totale(diario) == 105
    totali = entrate.tempo_per_categoria(diario)
    assert totali["studio"] == 90
    assert totali["tempo libero"] == 15


def test_trova_entrate_per_data():
    diario = entrate.crea_diario()
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-08", "A", "studio", 60))
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-09", "B", "tempo libero", 30))

    trovate = entrate.trova_entrate_per_data(diario, "2026-04-08")
    assert len(trovate) == 1
    assert trovate[0]["testo"] == "A"


def test_salva_e_carica_diario(tmp_path):
    diario = entrate.crea_diario()
    entrate.aggiungi_entrata(diario, entrate.crea_entrata("2026-04-08", "A", "studio", 60))
    file_path = tmp_path / "diario.json"

    persistenza.salva_diario(diario, str(file_path))
    caricati = persistenza.carica_diario(str(file_path))

    assert caricati["entrate"][0]["data"] == "2026-04-08"
    assert caricati["entrate"][0]["categoria"] == "studio"
    assert caricati["entrate"][0]["durata"] == 60
