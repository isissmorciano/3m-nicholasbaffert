# Esercizio 68: Parabole e rette da file JSON

## Obiettivo
Leggere un file JSON che contiene i coefficienti delle parabole (`a`, `b`, `c`) e delle rette (`m`, `q`), quindi disegnare tutti i grafici su una singola figura usando `matplotlib`.

## Requisiti preliminari
1. Creare un ambiente virtuale con `python -m venv .venv` o equivalente
2. Attivare l'ambiente virtuale con `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. Installare la libreria necessaria con `pip install matplotlib`

## Istruzioni

1. Crea un file `es68_reference.py`.
2. Crea un file `es68_data.json` con i coefficienti delle parabole e delle rette.
3. Nel file Python importa `json`, `matplotlib.pyplot` come `plt` e `numpy` come `np`.
4. Leggi i dati JSON dal file e estrai le liste di parabole e rette.
5. Calcola i valori `y` di ogni parabola usando `y = a*x**2 + b*x + c`.
6. Calcola i valori `y` di ogni retta usando `y = m*x + q`.
7. Disegna tutte le curve sulla stessa figura, usando colori diversi e una legenda.
8. Aggiungi titolo, etichette degli assi e griglia.
9. Mostra il grafico con `plt.show()`.

## Struttura JSON di esempio

```json
{
  "parabole": [
    {"a": 1, "b": -2, "c": 1},
    {"a": 0.5, "b": 0, "c": -1}
  ],
  "rette": [
    {"m": 1, "q": 0},
    {"m": -0.5, "q": 2}
  ]
}
```

## Output atteso
Il codice deve aprire una finestra con un grafico che mostra le parabole e le rette disegnate nello stesso sistema di assi. Le curve devono avere una legenda chiara e un titolo descrittivo.

## Suggerimenti
- Usa `np.linspace(-10, 10, 400)` per generare i valori di `x`.
- Usa diversi stili di linea per distinguere parabole e rette.
- Aggiungi `plt.legend()` per identificare ogni curva.
