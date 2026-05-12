# # Esercizio 57: Conteggio Parole in un File
# ## Obiettivo
# Leggere un file di testo e contare le occorrenze di ogni parola (case-insensitive, ignorando punteggiatura semplice).
# ## Dati forniti
# Un paragrafo hardcoded da scrivere su file:
# ```python
# testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
# ```
# ## Istruzioni
# 1. **Definire `conta_parole(nome_file)`**: Accetta un nome file, legge il contenuto, splitta in parole (ignorando maiuscole e punteggiatura come virgole e punti), e restituisce un dizionario {parola: conteggio}.
# 2. **Definire `stampa_conteggio(dizionario)`**: Accetta il dizionario e lo stampa in ordine alfabetico delle chiavi.
# 3. **Definire `main()`**: 
#    - Definisce `testo` (dati hardcoded)
#    - Scrive `testo` su "esercizio57.txt"
#    - Chiama `conta_parole` e `stampa_conteggio`
# ## Suggerimenti
# - Per scrivere il file iniziale: usa `with open("esercizio57.txt", "w") as f: f.write(testo)`
# - Per contare: converti tutto in lowercase, rimuovi "." e ",", poi `.split()`
# - Usa un dizionario per accumulare conteggi
# - Per ordinare: `sorted(dizionario.items())`
# ## Esempio di output atteso
# ```
# Conteggio parole:
# di: 1
# e: 1
# linguaggio: 1
# potente: 1
# programmazione: 1
# python: 2
# semplice: 1
# un: 1
# è: 2
# ```

# 1. **Definire `conta_parole(nome_file)`**: Accetta un nome file, legge il contenuto, splitta in parole (ignorando maiuscole e punteggiatura come virgole e punti), e restituisce un dizionario {parola: conteggio}.
def conta_parole(nome_file: str) -> dict[str, int]:
    conteggio = {}
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            parole = 0
            contenuto = file.read().lower()
            contenuto = contenuto.replace(".", ",")
            parola = contenuto.split()
            if parola in conteggio:
                conteggio[parole] += 1
            else:
                parola = 1
    except FileNotFoundError as e:
        print("File non trovato")
    except IOError as e:
        print("Errore durante la lettura del file")
    return conteggio[nome_file, parola]
        
# 2. **Definire `stampa_conteggio(dizionario)`**: Accetta il dizionario e lo stampa in ordine alfabetico delle chiavi.
def stampa_conteggio(conteggio: dict[str, int]) -> None:
    print(f"{conteggio}")

def main():
    testo: str = "Python è un linguaggio di programmazione. Python è semplice e potente."
    nome_file = "esercizio57.txt"
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(testo)
        print(f"File '{nome_file}' creato con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")
        return
    
    dizionario_conteggio = conta_parole(nome_file)
    stampa_conteggio(dizionario_conteggio)


    
if __name__ == "__main__":
    main()


# 3. **Definire `main()`**: 
#    - Definisce `testo` (dati hardcoded)
#    - Scrive `testo` su "esercizio57.txt"
#    - Chiama `conta_parole` e `stampa_conteggio`