from src.exams.v6.v6_student import es2_filtra_e_metriche, valuta_studente


def test_es2_filtra_e_metriche_base():
    result = es2_filtra_e_metriche(6, [3, 12, -5, 22, 7, -9])
    assert result["pari_positivi"] == [12, 22]
    assert result["dispari_negativi"] == [-5, -9]
    assert result["somma_maggiore_10"] == 34  # 12 + 22
    assert abs(result["media_assoluta"] - (3 + 12 + 5 + 22 + 7 + 9) / 6) < 1e-9


def test_es2_filtra_e_metriche_error_n_nonpositivo():
    import pytest
    with pytest.raises(ValueError):
        es2_filtra_e_metriche(0, [])


def test_valuta_studente_ammesso():
    result = valuta_studente([24, 23, 21])
    assert result["esito"] == "Ammesso"


def test_valuta_studente_recupero():
    result = valuta_studente([17, 16, 15])
    assert result["esito"] == "Recupero"


def test_valuta_studente_bocciato():
    result = valuta_studente([12, 10, 14])
    assert result["esito"] == "Bocciato"
