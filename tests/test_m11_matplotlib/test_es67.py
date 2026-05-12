"""Test per l'Esercizio 67: Istogramma dei pesi da JSON"""

import unittest
import json
import tempfile
import os
from unittest.mock import patch

from src.m11_matplotlib.es67_reference import carica_dati_json, estrai_pesi


class TestEs67Istogramma(unittest.TestCase):
    """Test per l'istogramma dei pesi."""

    def setUp(self):
        """Preparazione per i test."""
        self.dati_test = [
            {"nome": "Luca", "peso": 72},
            {"nome": "Anna", "peso": 65},
            {"nome": "Marta", "peso": 58},
            {"nome": "Giorgio", "peso": 83},
            {"nome": "Sara", "peso": 69}
        ]
        # Creare un file temporaneo con i dati
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        json.dump(self.dati_test, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        """Pulizia dopo i test."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_carica_dati_json_ritorna_lista(self):
        """Test che carica_dati_json ritorna una lista."""
        dati = carica_dati_json(self.temp_file.name)
        self.assertIsInstance(dati, list)

    def test_carica_dati_json_lunghezza_corretta(self):
        """Test che carica_dati_json ritorna i dati corretti."""
        dati = carica_dati_json(self.temp_file.name)
        self.assertEqual(len(dati), 5)

    def test_carica_dati_json_contenuto_corretto(self):
        """Test che il contenuto caricato è corretto."""
        dati = carica_dati_json(self.temp_file.name)
        self.assertEqual(dati[0]['nome'], 'Luca')
        self.assertEqual(dati[0]['peso'], 72)

    def test_estrai_pesi_ritorna_lista(self):
        """Test che estrai_pesi ritorna una lista."""
        pesi = estrai_pesi(self.dati_test)
        self.assertIsInstance(pesi, list)

    def test_estrai_pesi_lunghezza_corretta(self):
        """Test che estrai_pesi ritorna il numero corretto di pesi."""
        pesi = estrai_pesi(self.dati_test)
        self.assertEqual(len(pesi), 5)

    def test_estrai_pesi_valori_corretti(self):
        """Test che i pesi estratti sono corretti."""
        pesi = estrai_pesi(self.dati_test)
        pesi_attesi = [72, 65, 58, 83, 69]
        self.assertEqual(pesi, pesi_attesi)

    def test_estrai_pesi_tipo_elementi(self):
        """Test che gli elementi nella lista sono interi."""
        pesi = estrai_pesi(self.dati_test)
        for peso in pesi:
            self.assertIsInstance(peso, int)

    def test_estrai_pesi_lista_vuota(self):
        """Test estrai_pesi con lista vuota."""
        pesi = estrai_pesi([])
        self.assertEqual(pesi, [])

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_main_esecuzione(self, mock_savefig, mock_show):
        """Test che la funzione main non genera errori (con file reale)."""
        # Questo test usa il file reale es67_data.json se esiste
        try:
            from src.m11_matplotlib.es67_reference import main
            main()
            mock_savefig.assert_called()
        except FileNotFoundError:
            # Se il file non esiste, il test viene saltato
            self.skipTest("File es67_data.json non trovato")
        except Exception as e:
            self.fail(f"main() ha generato un'eccezione: {e}")


if __name__ == '__main__':
    unittest.main()
