# Esercizio 61: Package "Musicale" - Canzoni e Playlist

## Obiettivo
Creare un package `musica` che gestisca canzoni e playlist con funzioni pure.

## Istruzioni

### Parte 1: Creazione della struttura del package
Crea una cartella `musica/` con:
```
musica/
├── __init__.py
├── canzoni.py
└── playlist.py
```

### Parte 2: Implementazione di `musica/canzoni.py`
Funzioni per gestire le canzoni (rappresentate come dizionari):
- `crea_canzone(titolo: str, artista: str, durata: int) -> dict:` 
  - Restituisce un dizionario con chiavi: `titolo`, `artista`, `durata`
- `info_canzone(canzone: dict) -> str:` 
  - Restituisce formato: `"Titolo - Artista (M:SS)"`
  - Esempio: `"Bohemian Rhapsody - Queen (5:55)"`

### Parte 3: Implementazione di `musica/playlist.py`
Funzioni per gestire le playlist (liste di canzoni):
- `crea_playlist(nome: str) -> dict:` 
  - Restituisce un dizionario con `nome` e `canzoni` (lista vuota)
- `aggiungi_canzone(playlist: dict, canzone: dict) -> None:` 
  - Aggiunge una canzone alla playlist
- `rimuovi_canzone(playlist: dict, indice: int) -> None:` 
  - Rimuove una canzone per indice (0-based)
- `durata_totale(playlist: dict) -> int:` 
  - Restituisce durata totale in secondi
- `mostra_playlist(playlist: dict) -> str:` 
  - Restituisce stringa formattata con tutte le canzoni

### Parte 4: Utilizzo del package in `es51_main.py`
1. Crea una playlist con nome a scelta
2. Crea almeno 3 canzoni
3. Aggiungile alla playlist
4. Stampa il contenuto con durata totale

## Concetti Chiave
- **Package**: cartella con `__init__.py` e moduli
- **Moduli correlati**: `canzoni.py` e `playlist.py` lavorano insieme
- **Funzioni pure**: niente classi, solo funzioni che lavorano con dizionari
- **Dizionari**: strutture dati per rappresentare dati

## Esempio di Output
```
=== Playlist: Le mie canzoni preferite ===
1. Bohemian Rhapsody - Queen (5:55)
2. Stairway to Heaven - Led Zeppelin (8:02)
3. Hotel California - Eagles (6:30)

Durata totale: 20:27
```

## Suggerimenti
- Rappresenta una canzone con: `{"titolo": "...", "artista": "...", "durata": 355}`
- Rappresenta una playlist con: `{"nome": "...", "canzoni": [...]}`
- Converti secondi in M:SS con: `minuti = durata // 60`, `secondi = durata % 60`
