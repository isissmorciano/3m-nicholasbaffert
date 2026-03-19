# 1. Crea una playlist con nome a scelta
# 2. Crea almeno 3 canzoni
# 3. Aggiungile alla playlist
# 4. Stampa il contenuto con durata totale

# ## Concetti Chiave
# - **Package**: cartella con `__init__.py` e moduli
# - **Moduli correlati**: `canzoni.py` e `playlist.py` lavorano insieme
# - **Funzioni pure**: niente classi, solo funzioni che lavorano con dizionari
# - **Dizionari**: strutture dati per rappresentare dati

from musica_student import canzoni_student,playlist_student
def main(): 
    nome_playlist: str = input("Inserisci nome playlist")
    mia_playlist = playlist_student.crea__playlist(nome_playlist)
    for _ in range(3):
        nome_canzone_playlist: str = input("Inserisci nome canzone: ")
        artista_canzone_playlist: str = input("Inserisci nome artista")
        durata_canzone_playlist: int = int(input("Inserisci durata artista"))
        mia_canzone = canzoni_student.crea_canzone(nome_canzone_playlist,artista_canzone_playlist,durata_canzone_playlist)
        mia_playlist["canzoni"].append(mia_canzone)
    while True:
        print("=== AZIONI ===\n")
        print("1) Aggiungi Canzone: ")
        print("2) Rimuovi Canzone: ")
        print("3) Mostra Playlist: ")
        print("4) Mostra Durata: ")
        print("5) Esci: ")
        print("Che azione vuoi fare (1-5): ")
        
    


if __name__ == "__main__":
    main()