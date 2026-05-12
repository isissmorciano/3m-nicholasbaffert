# Esercizio 70: Grafico a linee multiple - Vendite per prodotto

## Obiettivo
Leggere un file JSON con i dati di vendite mensili di diversi prodotti e disegnare un grafico a linee multiple usando `matplotlib`.

## Perché serve
Un grafico a linee è utile per visualizzare trend nel tempo. Disegnando più linee sullo stesso grafico puoi confrontare l'andamento di diversi prodotti nel tempo e rispondere a domande come:
- Quale prodotto vende di più?
- Come cambiano le vendite mese per mese?
- Qual è il mese migliore per ogni prodotto?
- Quale prodotto cresce più velocemente?

## Esempio reale
Immagina un'azienda che vende tre prodotti: Cuffie, Tastiera e Mouse. Ogni mese registra le vendite di ogni prodotto. Un grafico a linee multiple ti aiuta a:
- Vedere quale prodotto vende di più ogni mese
- Identificare stagionalità (mesi con più vendite)
- Confrontare le prestazioni tra prodotti

## Istruzioni

1. Crea un file `es70_reference.py`.
2. Crea un file `es70_data.json` con i dati delle vendite mensili.
3. Nel file Python importa `json`, `matplotlib.pyplot as plt` e `numpy as np` (se necessario).
4. Leggi il file JSON e estrai i mesi e le vendite per ogni prodotto.
5. Disegna linee multiple con `plt.plot()`, una per ogni prodotto.
6. Usa colori e stili di linea diversi per distinguere i prodotti.
7. Aggiungi titolo, etichette degli assi, legenda e griglia.
8. Salva il grafico con `plt.savefig()` e mostra con `plt.show()`.

## Suggerimenti
- Usa `plt.figure(figsize=(10, 6))`.
- Usa `plt.plot()` più volte per ogni linea (una per prodotto).
- Usa `marker='o'` per aggiungere punti sulle linee.
- Usa `plt.legend()` per identificare ogni linea.
- Usa colori come `'red'`, `'blue'`, `'green'` oppure abbreviazioni `'r'`, `'b'`, `'g'`.

## Dati attesi
Il codice deve aprire una finestra con un grafico a linee che mostra tre linee:
- Una linea per le vendite di Cuffie (rosso)
- Una linea per le vendite di Tastiera (blu)
- Una linea per le vendite di Mouse (verde)
Ogni linea mostra l'andamento delle vendite nei 12 mesi dell'anno.
