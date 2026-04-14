# Esercizio 66: Grafici con Matplotlib

## Obiettivo
Creare un piccolo script Python che disegna diversi grafici usando la libreria esterna `matplotlib` e `numpy`.

## Requisiti preliminari
Prima di scrivere il codice, i ragazzi devono:

1. creare un ambiente virtuale con `python -m venv .venv` o equivalente
2. attivare l'ambiente virtuale con `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. installare la libreria necessaria con `pip install matplotlib`

> `matplotlib` installa anche `numpy` come dipendenza, quindi non serve installarlo separatamente.

## Istruzioni

1. Crea un file `es66_reference.py`.
2. Importa `matplotlib.pyplot` come `plt` e `numpy` come `np`.
3. Implementa quattro mini-esercizi diversi nel file:
   - Esercizio 1: un grafico a linea con due vettori di punti.
   - Esercizio 2: un grafico a linea con stile punteggiato.
   - Esercizio 3: un grafico a barre con categorie e valori.
   - Esercizio 4: una figura con `subplot` e due grafici affiancati.
4. Per ciascun grafico, aggiungi titolo, etichette e usa `plt.show()`.
5. Puoi mostrare i grafici uno dopo l'altro nello stesso script.

## Esercizi

### Esercizio 1: Linea semplice
Usa questi dati:
- `xpoints = np.array([0, 6])`
- `ypoints = np.array([0, 250])`

### Esercizio 2: Linea punteggiata
Usa questi dati:
- `ypoints = np.array([3, 8, 1, 10])`
- Imposta `linestyle='dotted'`

### Esercizio 3: Grafico a barre
Usa questi dati:
- `categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']`
- `valori = [10, 15, 7, 12]`

### Esercizio 4: Grafici con subplot
Usa questi dati:
- `xpoints = np.array([0, 6])`
- `ypoints = np.array([0, 250])`
- `categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']`
- `valori = [10, 15, 7, 12]`

Crea una figura con `plt.subplot(1, 2, 1)` e `plt.subplot(1, 2, 2)` per visualizzare due grafici affiancati.

## Output atteso
Il codice deve aprire quattro finestre (o aggiornare la stessa figura in sequenza) con i grafici:
- una linea semplice
- una linea punteggiata
- un grafico a barre
- una figura con due grafici affiancati usando subplot

## Suggerimenti
- Usa `plt.figure(figsize=(8, 5))` prima di ogni grafico.
- Per il grafico a barre, prova `plt.bar(categorie, valori, color='skyblue')`.
- Per aggiungere una griglia, usa `plt.grid(axis='y', linestyle='--', alpha=0.5)`.
