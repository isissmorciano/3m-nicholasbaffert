# Esercizio 67: Istogramma dei pesi da JSON

## Obiettivo
Leggere dati da un file JSON che contiene informazioni su persone e peso, quindi creare un istogramma dei pesi usando `matplotlib`.

## Requisiti preliminari
Prima di scrivere il codice, i ragazzi devono:

1. creare un ambiente virtuale con `python -m venv .venv` o equivalente
2. attivare l'ambiente virtuale con `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. installare la libreria necessaria con `pip install matplotlib`

> `matplotlib` installa anche `numpy` come dipendenza, quindi non serve installarlo separatamente.

## Istruzioni

1. Crea un file `es67_reference.py`.
2. Crea un file `es67_data.json` con dati su persone e peso.
3. Nel file Python importa `json`, `matplotlib.pyplot` come `plt` e `numpy` come `np`.
4. Leggi i dati JSON dal file e estrai i valori di peso.
5. Disegna un istogramma dei pesi con `plt.hist()`.
6. Aggiungi un titolo e etichette agli assi.
7. Mostra il grafico con `plt.show()`.

## Dati di esempio
Il file JSON deve avere una struttura simile a questa:

```json
[
  {"nome": "Luca", "peso": 72},
  {"nome": "Anna", "peso": 65},
  {"nome": "Marta", "peso": 58},
  {"nome": "Giorgio", "peso": 83},
  {"nome": "Sara", "peso": 69}
]
```

## Output atteso
Il codice deve aprire una finestra con un istogramma che mostra la distribuzione dei pesi delle persone.

## Suggerimenti
- Usa `with open('es67_data.json', 'r', encoding='utf-8') as file:` per leggere il JSON.
- Usa `plt.figure(figsize=(8, 5))` per creare la figura.
- Usa `plt.hist(pesi, bins=5, color='skyblue', edgecolor='black')`.
- Aggiungi `plt.title('Distribuzione dei pesi')`, `plt.xlabel('Peso (kg)')` e `plt.ylabel('Numero di persone')`.
