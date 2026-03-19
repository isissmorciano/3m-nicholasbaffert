# Esercizio 64: Package "Quiz" - Domande e Risultati

## Obiettivo
Creare un package `quiz` che gestisca domande a scelta multipla e persista i risultati su file.

## Istruzioni

### Parte 1: Struttura del package
Crea una cartella `quiz/` con:
```
quiz/
├── __init__.py
├── domande.py
└── risultati.py
```

### Parte 2: Modulo `domande.py`
Funzioni per gestire le domande (rappresentate come dizionari):
- `crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:`
  - `risposta` è l'indice 0-based dell'opzione corretta
- `info_domanda(domanda: dict) -> str:`
  - Restituisce una stringa leggibile con domanda + opzioni numerate
- `risposta_valida(domanda: dict, scelta: int) -> bool:`
  - Verifica se la scelta (1-based) è valida
- `verifica_risposta(domanda: dict, scelta: int) -> bool:`
  - Restituisce True se la scelta (1-based) è corretta

### Parte 3: Modulo `risultati.py`
Funzioni per gestire i risultati del quiz e per salvarli/caricarli su file JSON:
- `crea_risultati() -> dict:`
  - Restituisce un dizionario con chiavi: `totale`, `corretti`
- `registra_risposta(risultati: dict, corretta: bool) -> None:`
  - Aggiorna i totali
- `percentuale_corrette(risultati: dict) -> float:`
  - Restituisce la percentuale di risposte corrette (1 decimale)
- `mostra_risultati(risultati: dict) -> str:`
  - Restituisce una stringa leggibile del riepilogo
- `salva_risultati(risultati: dict, nome_file: str) -> None:`
  - Salva i risultati in un file JSON
- `carica_risultati(nome_file: str) -> dict:`
  - Carica i risultati da un file JSON

### Parte 4: Utilizzo del package in `es64_reference.py`
1. Crea alcune domande (almeno 3)
2. Simula alcune risposte dell'utente
3. Registra i risultati
4. Stampa il riepilogo
5. Salva su file e ricarica dall'archivio

## Concetti Chiave
- **Package**: cartella con `__init__.py` e moduli
- **Moduli collegati**: `risultati.py` usa `json` per la persistenza
- **Funzioni pure**: funzioni che lavorano solo con dizionari e restituiscono risultati
- **Gestione file**: lettura/scrittura JSON con gestione degli errori

## Esempio di Output
```
Domanda: Qual è il linguaggio usato in questo corso?
1. Python
2. Java
3. C++

Risultati:
Risposte corrette: 3/4 (75.0%)

Risultati salvati in 'quiz_risultati.json'
Risultati caricati: Risposte corrette: 3/4 (75.0%)
```
