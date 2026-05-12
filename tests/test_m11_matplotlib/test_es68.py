"""Test per l'Esercizio 68: Parabole e rette da file JSON"""

import unittest
import numpy as np
from unittest.mock import patch

from src.m11_matplotlib.es68_reference import (
    carica_dati_json,
    calcola_parabola,
    calcola_retta,
)


class TestEs68ParaboleRette(unittest.TestCase):
    """Test per il calcolo di parabole e rette."""

    def test_calcola_parabola_punto_singolo(self):
        """Test calcolo di una parabola in un punto."""
        x = np.array([0])
        y = calcola_parabola(1, 0, 0, x)
        np.testing.assert_array_almost_equal(y, [0])

    def test_calcola_parabola_y_eq_x_quadrato(self):
        """Test y = x^2."""
        x = np.array([0, 1, 2, 3])
        y = calcola_parabola(1, 0, 0, x)
        np.testing.assert_array_almost_equal(y, [0, 1, 4, 9])

    def test_calcola_parabola_con_shift(self):
        """Test y = x^2 + 1."""
        x = np.array([0, 1, 2])
        y = calcola_parabola(1, 0, 1, x)
        np.testing.assert_array_almost_equal(y, [1, 2, 5])

    def test_calcola_parabola_coefficienti_diversi(self):
        """Test y = 2x^2 - 3x + 1."""
        x = np.array([0, 1, 2])
        y = calcola_parabola(2, -3, 1, x)
        # x=0: 0 - 0 + 1 = 1
        # x=1: 2 - 3 + 1 = 0
        # x=2: 8 - 6 + 1 = 3
        np.testing.assert_array_almost_equal(y, [1, 0, 3])

    def test_calcola_parabola_negativa(self):
        """Test parabola con coefficiente negativo."""
        x = np.array([0, 1, 2])
        y = calcola_parabola(-1, 0, 0, x)
        np.testing.assert_array_almost_equal(y, [0, -1, -4])

    def test_calcola_retta_origine(self):
        """Test retta y = x passante per l'origine."""
        x = np.array([0, 1, 2, 3])
        y = calcola_retta(1, 0, x)
        np.testing.assert_array_almost_equal(y, [0, 1, 2, 3])

    def test_calcola_retta_con_intercetta(self):
        """Test retta y = x + 2."""
        x = np.array([0, 1, 2])
        y = calcola_retta(1, 2, x)
        np.testing.assert_array_almost_equal(y, [2, 3, 4])

    def test_calcola_retta_pendenza_negativa(self):
        """Test retta y = -2x + 5."""
        x = np.array([0, 1, 2])
        y = calcola_retta(-2, 5, x)
        np.testing.assert_array_almost_equal(y, [5, 3, 1])

    def test_calcola_retta_orizzontale(self):
        """Test retta orizzontale y = 3."""
        x = np.array([0, 1, 2, 3])
        y = calcola_retta(0, 3, x)
        np.testing.assert_array_almost_equal(y, [3, 3, 3, 3])

    def test_carica_dati_json_struttura(self):
        """Test che carica_dati_json ritorna un dizionario."""
        try:
            dati = carica_dati_json('src/m11_matplotlib/es68_data.json')
            self.assertIsInstance(dati, dict)
            self.assertIn('parabole', dati)
            self.assertIn('rette', dati)
        except FileNotFoundError:
            self.skipTest("File es68_data.json non trovato")

    def test_carica_dati_json_parabole(self):
        """Test che le parabole sono caricate correttamente."""
        try:
            dati = carica_dati_json('src/m11_matplotlib/es68_data.json')
            parabole = dati['parabole']
            self.assertIsInstance(parabole, list)
            if len(parabole) > 0:
                self.assertIn('a', parabole[0])
                self.assertIn('b', parabole[0])
                self.assertIn('c', parabole[0])
        except FileNotFoundError:
            self.skipTest("File es68_data.json non trovato")

    def test_carica_dati_json_rette(self):
        """Test che le rette sono caricate correttamente."""
        try:
            dati = carica_dati_json('src/m11_matplotlib/es68_data.json')
            rette = dati['rette']
            self.assertIsInstance(rette, list)
            if len(rette) > 0:
                self.assertIn('m', rette[0])
                self.assertIn('q', rette[0])
        except FileNotFoundError:
            self.skipTest("File es68_data.json non trovato")

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_main_esecuzione(self, mock_savefig, mock_show):
        """Test che main non genera errori."""
        try:
            from src.m11_matplotlib.es68_reference import main
            main()
        except FileNotFoundError:
            self.skipTest("File es68_data.json non trovato")
        except Exception as e:
            self.fail(f"main() ha generato un'eccezione: {e}")


if __name__ == '__main__':
    unittest.main()
