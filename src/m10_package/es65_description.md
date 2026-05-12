# Esercizio 65: Package "Diario" - Entrate giornaliere

## Obiettivo
Creare un package `diario` che gestisca un elenco di entrate quotidiane e salvi il diario su file JSON.

## Istruzioni

### Parte 1: Struttura del package
Crea una cartella `diario/` con:
```
diario/
├── __init__.py
├── entrate.py
└── persistenza.py
```

### Parte 2: Modulo `entrate.py`
Implementa funzioni per lavorare con le entrate del diario:
- `crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict`
  - `data` è una stringa nel formato `YYYY-MM-DD`
  - `durata` è il tempo trascorso in minuti
- `info_entrata(entrata: dict) -> str`
  - Restituisce una stringa leggibile con data, categoria, durata e testo
- `crea_diario() -> dict`
  - Restituisce un dizionario con chiave `entrate` e lista vuota
- `aggiungi_entrata(diario: dict, entrata: dict) -> None`
- `rimuovi_entrata(diario: dict, indice: int) -> None`
- `tempo_totale(diario: dict) -> int`
  - Somma tutte le durate in minuti
- `tempo_per_categoria(diario: dict) -> dict[str, int]`
  - Restituisce il tempo totale speso per categoria
- `trova_entrate_per_data(diario: dict, data: str) -> list[dict]`

### Parte 3: Modulo `persistenza.py`
Implementa le funzioni per salvare e caricare il diario su file JSON:
- `salva_diario(diario: dict, nome_file: str) -> None`
- `carica_diario(nome_file: str) -> dict`

### Parte 4: Dati di esempio
Usa queste entrate nel file di riferimento o come base per il testing:

| Data | Categoria | Durata (minuti) | Testo |
|------|-----------|-----------------|-------|
| 2026-04-08 | studio | 60 | Ho iniziato un nuovo corso di Python. |
| 2026-04-08 | studio | 45 | Ho scritto un esercizio sul package diario. |
| 2026-04-09 | tempo libero | 30 | Sono andato a fare una passeggiata nel parco. |

### Parte 5: Utilizzo del package in `es65_reference.py`
1. Importa il package con `from diario import entrate, persistenza`
2. Crea alcune entrate di esempio
3. Aggiungile al diario
4. Stampa il diario e le statistiche sul tempo totale
5. Salva su file e ricarica il diario

## Esempio di output
```
=== Diario ===
2026-04-08 [studio] (60 min): Ho iniziato un nuovo corso di Python.
2026-04-08 [studio] (45 min): Ho scritto un esercizio sul package diario.
2026-04-09 [tempo libero] (30 min): Sono andato a fare una passeggiata nel parco.

Tempo totale: 135 minuti

Tempo per categoria:
- studio: 105 minuti
- tempo libero: 30 minuti

Diario salvato in 'diario.json'

Diario caricato:
2026-04-08 [studio] (60 min): Ho iniziato un nuovo corso di Python.
2026-04-08 [studio] (45 min): Ho scritto un esercizio sul package diario.
2026-04-09 [tempo libero] (30 min): Sono andato a fare una passeggiata nel parco.
```

## Concetti Chiave
- package Python con `__init__.py`
- moduli separati per logica e persistenza
- dizionari e liste per rappresentare dati
- lettura/scrittura JSON
