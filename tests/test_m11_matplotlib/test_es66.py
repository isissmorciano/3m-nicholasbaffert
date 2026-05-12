"""Test per l'Esercizio 66: Grafici con Matplotlib"""

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import matplotlib.pyplot as plt

from src.m11_matplotlib.es66_reference import (
    plot_linea_semplice,
    plot_linea_punteggiata,
    plot_barre,
    plot_subplot,
)


class TestEs66Grafici(unittest.TestCase):
    """Test per i grafici del modulo matplotlib."""

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_plot_linea_semplice_esecuzione(self, mock_savefig, mock_show):
        """Test che il grafico a linea semplice non genera errori."""
        try:
            plot_linea_semplice()
            mock_savefig.assert_called()
        except Exception as e:
            self.fail(f"plot_linea_semplice() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_plot_linea_punteggiata_esecuzione(self, mock_savefig, mock_show):
        """Test che il grafico a linea punteggiata non genera errori."""
        try:
            plot_linea_punteggiata()
            mock_savefig.assert_called()
        except Exception as e:
            self.fail(f"plot_linea_punteggiata() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_plot_barre_esecuzione(self, mock_savefig, mock_show):
        """Test che il grafico a barre non genera errori."""
        try:
            plot_barre()
            mock_savefig.assert_called()
        except Exception as e:
            self.fail(f"plot_barre() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_plot_subplot_esecuzione(self, mock_savefig, mock_show):
        """Test che il grafico con subplot non genera errori."""
        try:
            plot_subplot()
            mock_savefig.assert_called()
        except Exception as e:
            self.fail(f"plot_subplot() ha generato un'eccezione: {e}")

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.savefig')
    def test_tutti_i_grafici_esecuzione(self, mock_savefig, mock_show):
        """Test che tutti i grafici vengono creati senza errori."""
        try:
            plot_linea_semplice()
            plot_linea_punteggiata()
            plot_barre()
            plot_subplot()
            # Controllare che savefig è stato chiamato almeno 4 volte (una per ogni grafico)
            self.assertGreaterEqual(mock_savefig.call_count, 4)
        except Exception as e:
            self.fail(f"La creazione dei grafici ha generato un'eccezione: {e}")


if __name__ == '__main__':
    unittest.main()
