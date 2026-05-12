# 1. Crea un file `es66_reference.py`.
# 2. Importa `matplotlib.pyplot` come `plt` e `numpy` come `np`.
# 3. Implementa quattro mini-esercizi diversi nel file:
#    - Esercizio 1: un grafico a linea con due vettori di punti.
#    - Esercizio 2: un grafico a linea con stile punteggiato.
#    - Esercizio 3: un grafico a barre con categorie e valori.
#    - Esercizio 4: una figura con `subplot` e due grafici affiancati.
# 4. Per ciascun grafico, aggiungi titolo, etichette e usa `plt.show()`.
# 5. Puoi mostrare i grafici uno dopo l'altro nello stesso script.

import matplotlib.pyplot as plt
import numpy as np

### Esercizio 1: Linea semplice
def foto1() -> None:
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    plt.figure(figsize=(8, 5))
    plt.plot(xpoints, ypoints)
    plt.savefig('my_lot.png')

# ### Esercizio 2: Linea punteggiata
def foto2()-> None:
    ypoints = np.array([3, 8, 1, 10])
    plt.figure(figsize=(8, 5))
    plt.plot(ypoints, linestyle = 'dotted')
    plt.savefig('my_lot2.png')

# ### Esercizio 3: Grafico a barre
def foto3()-> None:
    categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']
    valori = [10, 15, 7, 12]
    plt.figure(figsize=(8, 5))
    plt.bar(categorie, valori, color='skyblue')
    plt.savefig('my_lot3.png')

# ### Esercizio 4: Grafici con subplot
def foto4()-> None:
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']
    valori = [10, 15, 7, 12]
    plt.figure(figsize=(8, 5))
    plt.plot(xpoints, ypoints, categorie, valori)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.savefig('my_lot4.png')

# Crea una figura con `plt.subplot(1, 2, 1)` e `plt.subplot(1, 2, 2)` per visualizzare due grafici affiancati.


def main()-> None:
    foto1()
    foto2()
    foto3()
    foto4()
if __name__ == "__main__":
    main()
