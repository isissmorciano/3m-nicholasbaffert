"""Test per l'Esercizio 70: Grafico a linee multiple - Vendite per prodotto"""

import unittest
import json
import tempfile
import os
from unittest.mock import patch

from src.m11_matplotlib.es70_reference import carica_dati, disegna_grafico_linee


class TestEs70GraficoLinee(unittest.TestCase):
    """Test per il grafico a linee multiple."""

    def setUp(self):
        """Preparazione per i test."""
        self.dati_test = {
            "mesi": ["Gennaio", "Febbraio", "Marzo"],
            "prodotti": [
                {"nome": "Cuffie", "vendite": [45, 52, 48]},
                {"nome": "Tastiera", "vendite": [30, 35, 38]},
                {"nome": "Mouse", "vendite": [25, 28, 32]}
            ]
        }
        # Creare un file temporaneo con i dati
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        json.dump(self.dati_test, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        """Pulizia dopo i test."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_carica_dati_ritorna_dizionario(self):
        """Test che carica_dati ritorna un dizionario."""
        dati = carica_dati(self.temp_file.name)
        self.assertIsInstance(dati, dict)

    def test_carica_dati_contiene_mesi(self):
        """Test che il dizionario contiene 'mesi'."""
        dati = carica_dati(self.temp_file.name)
        self.assertIn('mesi', dati)

    def test_carica_dati_contiene_prodotti(self):
        """Test che il dizionario contiene 'prodotti'."""
        dati = carica_dati(self.temp_file.name)
        self.assertIn('prodotti', dati)

    def test_carica_dati_mesi_lunghezza(self):
        """Test che mesi ha la lunghezza corretta."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(len(dati['mesi']), 3)

    def test_carica_dati_prodotti_lunghezza(self):
        """Test che prodotti ha la lunghezza corretta."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(len(dati['prodotti']), 3)

    def test_carica_dati_primo_mese(self):
        """Test che il primo mese è corretto."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(dati['mesi'][0], 'Gennaio')

    def test_carica_dati_primo_prodotto(self):
        """Test che il primo prodotto è corretto."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(dati['prodotti'][0]['nome'], 'Cuffie')
        self.assertEqual(dati['prodotti'][0]['vendite'][0], 45)

    def test_carica_dati_da_file_reale(self):
        """Test caricamento da file reale."""
        try:
            dati = carica_dati('src/m11_matplotlib/es70_data.json')
            self.assertIsInstance(dati, dict)
            self.assertIn('mesi', dati)
            self.assertIn('prodotti', dati)
            # Verificare che ci sono 12 mesi
            self.assertEqual(len(dati['mesi']), 12)
            # Verificare la struttura di ogni prodotto
            for prodotto in dati['prodotti']:
                self.assertIn('nome', prodotto)
                self.assertIn('vendite', prodotto)
                self.assertEqual(len(prodotto['vendite']), 12)
        except FileNotFoundError:
            self.skipTest("File es70_data.json non trovato")

    def test_mesi_non_vuoti(self):
        """Test che i mesi non sono vuoti."""
        dati = carica_dati(self.temp_file.name)
        for mese in dati['mesi']:
            self.assertIsInstance(mese, str)
            self.assertGreater(len(mese), 0)

    def test_prodotti_hanno_vendite(self):
        """Test che ogni prodotto ha vendite."""
        dati = carica_dati(self.temp_file.name)
        for prodotto in dati['prodotti']:
            self.assertIn('nome', prodotto)
            self.assertIn('vendite', prodotto)
            self.assertIsInstance(prodotto['vendite'], list)
            self.assertGreater(len(prodotto['vendite']), 0)

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.plot')
    @patch('matplotlib.pyplot.figure')
    def test_disegna_grafico_linee_esecuzione(self, mock_figure, mock_plot, mock_savefig):
        """Test che disegna_grafico_linee non genera errori."""
        try:
            disegna_grafico_linee(self.dati_test)
            mock_figure.assert_called()
        except Exception as e:
            self.fail(f"disegna_grafico_linee() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.show')
    def test_main_esecuzione(self, mock_show, mock_savefig):
        """Test che main non genera errori."""
        try:
            from src.m11_matplotlib.es70_reference import main
            main()
            mock_savefig.assert_called()
        except FileNotFoundError:
            self.skipTest("File es70_data.json non trovato")
        except Exception as e:
            self.fail(f"main() ha generato un'eccezione: {e}")


if __name__ == '__main__':
    unittest.main()
