from src.m08_funzioni.es55_student import main, calcola_gol_fatti, conta_risultati

def test_calcola_gol_fatti():
    partite = [
        {"squadra_casa": "Milan", "gol_casa": 2, "squadra_trasferta": "Juventus", "gol_trasferta": 1},
        {"squadra_casa": "Juventus", "gol_casa": 1, "squadra_trasferta": "Milan", "gol_trasferta": 0}
    ]
    assert calcola_gol_fatti(partite, "Milan") == (2 + 0) / 2

def test_conta_risultati():
    partite = [
        {"squadra_casa": "Milan", "gol_casa": 2, "squadra_trasferta": "Juventus", "gol_trasferta": 1},
        {"squadra_casa": "Juventus", "gol_casa": 1, "squadra_trasferta": "Milan", "gol_trasferta": 0}
    ]
    result = conta_risultati(partite, "Milan")
    assert result["vittorie"] == 1
    assert result["pareggi"] == 0
    assert result["sconfitte"] == 1

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "ANALYZER PARTITE CALCIO" in captured.out
    assert "Milan" in captured.out
    assert "Partite: 3" in captured.out