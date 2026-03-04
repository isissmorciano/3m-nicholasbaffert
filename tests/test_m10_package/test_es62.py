"""Test per l'Esercizio 62: Package Coordinate"""

import math

from src.m10_package.coordinate import punti, linee


def test_crea_punto():
    """Test creazione di un punto."""
    p = punti.crea_punto(3.0, 4.0)
    assert p["x"] == 3.0
    assert p["y"] == 4.0


def test_info_punto():
    """Test formattazione informazioni punto."""
    p = punti.crea_punto(2.5, 3.5)
    info = punti.info_punto(p)
    assert info == "(2.5, 3.5)"


def test_distanza_tra_punti():
    """Test calcolo distanza tra due punti."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(3.0, 4.0)
    
    # Triangle 3-4-5, distanza dovrebbe essere 5.0
    distanza = punti.distanza_tra_punti(p1, p2)
    assert distanza == 5.0


def test_distanza_tra_punti_stessi():
    """Test distanza quando i punti sono uguali."""
    p1 = punti.crea_punto(1.0, 1.0)
    p2 = punti.crea_punto(1.0, 1.0)
    
    distanza = punti.distanza_tra_punti(p1, p2)
    assert distanza == 0.0


def test_distanza_tra_punti_negativa():
    """Test distanza con coordinate negative."""
    p1 = punti.crea_punto(-3.0, -4.0)
    p2 = punti.crea_punto(0.0, 0.0)
    
    distanza = punti.distanza_tra_punti(p1, p2)
    assert distanza == 5.0


def test_crea_linea():
    """Test creazione di una linea."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(1.0, 1.0)
    
    linea = linee.crea_linea(p1, p2)
    assert linea["p1"] == p1
    assert linea["p2"] == p2


def test_lunghezza_linea():
    """Test calcolo lunghezza di una linea."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(3.0, 4.0)
    
    linea = linee.crea_linea(p1, p2)
    lungh = linee.lunghezza_linea(linea)
    assert lungh == 5.0


def test_punto_medio():
    """Test calcolo punto medio di una linea."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(4.0, 6.0)
    
    linea = linee.crea_linea(p1, p2)
    medio = linee.punto_medio(linea)
    
    assert medio["x"] == 2.0
    assert medio["y"] == 3.0


def test_punto_medio_negativi():
    """Test punto medio con coordinate negative."""
    p1 = punti.crea_punto(-2.0, -2.0)
    p2 = punti.crea_punto(2.0, 2.0)
    
    linea = linee.crea_linea(p1, p2)
    medio = linee.punto_medio(linea)
    
    assert medio["x"] == 0.0
    assert medio["y"] == 0.0


def test_info_linea():
    """Test formattazione informazioni linea."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(1.0, 1.0)
    
    linea = linee.crea_linea(p1, p2)
    info = linee.info_linea(linea)
    
    assert info == "Linea da (0.0, 0.0) a (1.0, 1.0)"


def test_linea_verticale():
    """Test linea verticale."""
    p1 = punti.crea_punto(0.0, 0.0)
    p2 = punti.crea_punto(0.0, 5.0)
    
    linea = linee.crea_linea(p1, p2)
    lungh = linee.lunghezza_linea(linea)
    
    assert lungh == 5.0


def test_linea_orizzontale():
    """Test linea orizzontale."""
    p1 = punti.crea_punto(0.0, 3.0)
    p2 = punti.crea_punto(4.0, 3.0)
    
    linea = linee.crea_linea(p1, p2)
    lungh = linee.lunghezza_linea(linea)
    
    assert lungh == 4.0
