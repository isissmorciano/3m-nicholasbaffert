from src.m08_funzioni.es54_student import main, calcola_voto_medio, trova_film_migliore

def test_calcola_voto_medio():
    film = [{"voto": 9}, {"voto": 8}, {"voto": 8}]
    assert calcola_voto_medio(film) == (9 + 8 + 8) / 3

def test_trova_film_migliore():
    film = [{"titolo": "A", "voto": 8}, {"titolo": "B", "voto": 9}]
    assert trova_film_migliore(film)["titolo"] == "B"

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "TRACKER FILM VISTI" in captured.out
    assert "The Shawshank Redemption" in captured.out
    assert "Film visti: 8" in captured.out