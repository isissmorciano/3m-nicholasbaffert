"""Test per l'Esercizio 69: Grafico a bolle da file JSON"""

import unittest
import json
import tempfile
import os
from unittest.mock import patch, MagicMock

from src.m11_matplotlib.es69_reference import carica_dati, disegna_grafico_bolle


class TestEs69GraficoBolle(unittest.TestCase):
    """Test per il grafico a bolle."""

    def setUp(self):
        """Preparazione per i test."""
        self.dati_test = [
            {
                "nome": "Centro",
                "clienti": 220,
                "incasso": 820,
                "superficie": 120,
                "profitto": 19
            },
            {
                "nome": "Stazione",
                "clienti": 150,
                "incasso": 540,
                "superficie": 70,
                "profitto": 10
            },
            {
                "nome": "Quartiere",
                "clienti": 90,
                "incasso": 560,
                "superficie": 100,
                "profitto": 22
            }
        ]
        # Creare un file temporaneo con i dati
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        json.dump(self.dati_test, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        """Pulizia dopo i test."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_carica_dati_ritorna_lista(self):
        """Test che carica_dati ritorna una lista."""
        dati = carica_dati(self.temp_file.name)
        self.assertIsInstance(dati, list)

    def test_carica_dati_lunghezza_corretta(self):
        """Test che carica_dati ritorna il numero corretto di dati."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(len(dati), 3)

    def test_carica_dati_struttura_corretto(self):
        """Test che i dati hanno la struttura corretta."""
        dati = carica_dati(self.temp_file.name)
        negozio = dati[0]
        self.assertIn('nome', negozio)
        self.assertIn('clienti', negozio)
        self.assertIn('incasso', negozio)
        self.assertIn('superficie', negozio)
        self.assertIn('profitto', negozio)

    def test_carica_dati_primo_negozio(self):
        """Test che il primo negozio è caricato correttamente."""
        dati = carica_dati(self.temp_file.name)
        self.assertEqual(dati[0]['nome'], 'Centro')
        self.assertEqual(dati[0]['clienti'], 220)
        self.assertEqual(dati[0]['incasso'], 820)

    def test_carica_dati_da_file_reale(self):
        """Test caricamento da file reale."""
        try:
            dati = carica_dati('src/m11_matplotlib/es69_data.json')
            self.assertIsInstance(dati, list)
            self.assertGreater(len(dati), 0)
            # Verificare che ogni negozio ha i campi necessari
            for negozio in dati:
                self.assertIn('nome', negozio)
                self.assertIn('clienti', negozio)
                self.assertIn('incasso', negozio)
                self.assertIn('superficie', negozio)
                self.assertIn('profitto', negozio)
        except FileNotFoundError:
            self.skipTest("File es69_data.json non trovato")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.colorbar')
    @patch('matplotlib.pyplot.scatter')
    @patch('matplotlib.pyplot.figure')
    def test_disegna_grafico_bolle_esecuzione(self, mock_figure, mock_scatter, mock_colorbar, mock_savefig):
        """Test che disegna_grafico_bolle non genera errori."""
        try:
            # Mock il ritorno di scatter per evitare problemi con colorbar
            mock_scatter.return_value = MagicMock()
            disegna_grafico_bolle(self.dati_test)
            mock_figure.assert_called()
        except Exception as e:
            self.fail(f"disegna_grafico_bolle() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.show')
    def test_main_esecuzione(self, mock_show, mock_savefig):
        """Test che main non genera errori."""
        try:
            from src.m11_matplotlib.es69_reference import main
            main()
            mock_savefig.assert_called()
        except FileNotFoundError:
            self.skipTest("File es69_data.json non trovato")
        except Exception as e:
            self.fail(f"main() ha generato un'eccezione: {e}")


if __name__ == '__main__':
    unittest.main()
