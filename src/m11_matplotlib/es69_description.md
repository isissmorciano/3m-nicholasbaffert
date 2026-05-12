# Esercizio 69: Grafico a bolle da file JSON

## Obiettivo
Leggere un file JSON con i dati di diversi negozi e disegnare un grafico a bolle usando `matplotlib`.

## Perché serve
Un grafico a bolle permette di visualizzare contemporaneamente tre variabili:
- `x`: una variabile orizzontale,
- `y`: una variabile verticale,
- `s`: la dimensione della bolla.

Questo tipo di grafico è utile quando vuoi confrontare elementi in base a due valori e aggiungere una terza informazione visiva con l’area delle bolle.

## Esempio reale
Immagina una catena di negozi. Per ogni negozio conosciamo:
- numero di clienti medi al giorno,
- incasso medio giornaliero,
- superficie del negozio in metri quadrati.

Il grafico a bolle aiuta a rispondere a domande come:
- Quale negozio ha più clienti?
- Quale negozio guadagna di più?
- Quale negozio usa meglio lo spazio disponibile?

## Istruzioni

1. Crea un file `es69_reference.py`.
2. Crea un file `es69_data.json` con i dati dei negozi.
3. Nel file Python importa `json`, `matplotlib.pyplot as plt` e `numpy as np`.
4. Leggi il file JSON e estrai i valori di `clienti`, `incasso`, `superficie` e `nome`.
5. Disegna un grafico a bolle con `plt.scatter()`.
6. Usa `s` per la dimensione della bolla e `c` per aggiungere un colore basato sul profitto.
7. Aggiungi titolo, etichette degli assi, griglia e annotazioni con `plt.text()`.
8. Mostra il grafico con `plt.show()`.

## Suggerimenti
- Usa `plt.figure(figsize=(10, 6))`.
- Usa una scala per `s` come `area * 8` per rendere le bolle visibili.
- Aggiungi `plt.colorbar()` per mostrare cosa rappresenta il colore.
- Puoi posizionare le etichette con un piccolo offset in `plt.text()`.

## Dati attesi
Il codice deve aprire una finestra con un grafico a bolle che mostra i negozi con:
- asse X = clienti al giorno,
- asse Y = incasso medio (€),
- dimensione bolla = area del negozio (mq),
- colore = profitto percentuale.
