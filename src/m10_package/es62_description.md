# Esercizio 62: Package "Coordinate" - Punti e Linee

## Obiettivo
Creare un package `coordinate` che gestisca punti e linee in uno spazio 2D con funzioni pure.

## Istruzioni

### Parte 1: Creazione della struttura del package
Crea una cartella `coordinate/` con:
```
coordinate/
├── __init__.py
├── punti.py
└── linee.py
```

### Parte 2: Implementazione di `coordinate/punti.py`
Funzioni per gestire i punti (rappresentati come dizionari):
- `crea_punto(x: float, y: float) -> dict:` 
  - Restituisce un dizionario con chiavi: `x`, `y`
- `distanza_tra_punti(p1: dict, p2: dict) -> float:` 
  - Calcola la distanza euclidea tra due punti
  - Formula: √((x2-x1)² + (y2-y1)²)
- `info_punto(punto: dict) -> str:` 
  - Restituisce formato: `"(x, y)"`
  - Esempio: `"(3.5, 2.0)"`

### Parte 3: Implementazione di `coordinate/linee.py`
Funzioni per gestire le linee (definite da due punti):
- `crea_linea(p1: dict, p2: dict) -> dict:` 
  - Restituisce un dizionario con chiavi: `p1`, `p2`
- `lunghezza_linea(linea: dict) -> float:` 
  - Calcola la lunghezza using `distanza_tra_punti`
  - Importa `from .punti import distanza_tra_punti`
- `punto_medio(linea: dict) -> dict:` 
  - Restituisce il punto medio tra p1 e p2
  - Coordinate: ((x1+x2)/2, (y1+y2)/2)
- `info_linea(linea: dict) -> str:` 
  - Restituisce formato: `"Linea da (x1, y1) a (x2, y2)"`

### Parte 4: Utilizzo del package in `es62_reference.py`
1. Importa il package: `from coordinate import punti, linee`
2. Crea almeno 3 punti
3. Crea 2-3 linee dai punti
4. Calcola lunghezze e punti medi
5. Stampa risultati formattati

## Concetti Chiave
- **Package**: cartella con `__init__.py` e moduli
- **Moduli correlati**: `linee.py` importa da `punti.py` (import relativo)
- **Funzioni pure**: niente classi, solo funzioni che lavorano con dizionari
- **Dizionari**: strutture dati per rappresentare punti e linee
- **Import relativi**: `from .punti import ...`

## Esempio di Output
```
=== Coordinate e Linee ===

Punti:
- Punto A: (0.0, 0.0)
- Punto B: (3.0, 4.0)
- Punto C: (6.0, 0.0)

Linee:
- Linea da (0.0, 0.0) a (3.0, 4.0) | Lunghezza: 5.00 | Punto medio: (1.5, 2.0)
- Linea da (3.0, 4.0) a (6.0, 0.0) | Lunghezza: 7.21 | Punto medio: (4.5, 2.0)
```

## Suggerimenti
- Rappresenta un punto con: `{"x": 0.0, "y": 5.0}`
- Rappresenta una linea con: `{"p1": {...}, "p2": {...}}`
- Usa `math.sqrt()` per calcolare la radice quadrata
- Arrotonda i risultati a 2 decimali con `round(valore, 2)`
