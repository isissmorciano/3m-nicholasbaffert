from src.m08_funzioni.es46_student import calcola_area_triangolo

def test_calcola_area_triangolo():
    assert calcola_area_triangolo(3.0, 4.0) == 6.0
    assert calcola_area_triangolo(5.0, 2.0) == 5.0
    assert calcola_area_triangolo(0.0, 10.0) == 0.0