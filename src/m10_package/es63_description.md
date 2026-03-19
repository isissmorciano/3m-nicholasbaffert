# Esercizio 63: Package "Streaming" - Video e Playlist

## Obiettivo
Creare un package `streaming` che gestisca video in una piattaforma di streaming. Imparerai a:
- Organizzare funzioni correlate in moduli
- Usare dizionari per rappresentare dati
- Ordinare dati con criteri personalizzati usando `sorted()` e `key`

## Istruzioni

### Parte 1: Struttura del Package
Crea una cartella `streaming/` con tre file:
- `__init__.py` (vuoto o con commento)
- `video.py` - funzioni per i video singoli
- `playlist.py` - funzioni per gestire collezioni di video

### Parte 2: Modulo `video.py`
Implementa funzioni per rappresentare e manipolare video come dizionari.

**Funzioni richieste:**
- `crea_video()` - crea un dizionario video con: titolo, durata (secondi), risoluzione, bitrate (kbps)
- `info_video()` - formatta i dettagli del video in una stringa leggibile (es. "Titolo - M:SS - Risoluzione - Bitrate kbps")
- `dimensione_video()` - calcola la dimensione del file

**Approfondimento: Calcolo della dimensione**
Il bitrate è la quantità di dati trasmessi al secondo, misurata in kilobit per secondo (kbps).
Per calcolare la dimensione di un file:
1. Moltiplica la durata (in secondi) per il bitrate (in kbps) → ottieni kilobit totali
2. Dividi per 8 per convertire kilobit in kilobyte
3. Dividi per 1024 per convertire kilobyte in megabyte
4. Arrotonda a 2 decimali

Esempio: un video di 600 secondi a 5000 kbps occupa circa 366 MB

### Parte 3: Modulo `playlist.py`
Implementa funzioni per gestire collezioni di video.

**Funzioni di base:**
- `crea_playlist()` - crea un dizionario con nome e lista vuota di video
- `aggiungi_video()` - aggiunge un video alla playlist
- `rimuovi_video()` - rimuove un video per indice
- `durata_totale()` - somma le durate di tutti i video
- `dimensione_totale()` - somma le dimensioni di tutti i video
- `mostra_playlist()` - formatta la playlist in una stringa leggibile

**Funzioni di ordinamento (con sorted):**
- `ordina_per_durata()` - ordina i video dal più breve al più lungo
  - Usa `sorted()` con `key` per specificare quale attributo usare per l'ordinamento

**Approfondimento: sorted() con key**
`sorted()` ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con `key`, puoi dire esattamente come confrontare gli elementi:
- `key=lambda v: v["durata"]` ordina usando il valore della chiave "durata"

### Parte 4: Dati da usare

**Nome playlist:** `"Corso Python Base"`

**Video da aggiungere (nell'ordine):**

| Titolo | Durata (s) | Risoluzione | Bitrate (kbps) |
|--------|-----------|-------------|---|
| Introduzione a Python | 930 | 1080p | 5000 |
| Variabili e Tipi | 1335 | 720p | 3000 |
| Funzioni e Moduli | 1080 | 1080p | 5000 |
| Liste e Dizionari | 1560 | 480p | 2000 |

### Parte 5: Utilizzo del Package
Scrivi uno script che:
1. Importa il package
2. Crea una playlist con il nome specificato
3. Aggiunge i 4 video con i dati della tabella sopra
4. Stampa la playlist originale
5. Stampa la playlist ordinata per durata
6. Stampa statistiche totali (durata e dimensione)
