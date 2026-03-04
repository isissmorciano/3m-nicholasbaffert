from musica import canzoni, playlist
from musica.playlist import Playlist
from musica.canzoni import Canzone


def main() -> None:
    # Crea una playlist
    mia_playlist: Playlist = playlist.crea_playlist("Le mie canzoni preferite")

    # Crea le canzoni
    canzone1: Canzone = canzoni.crea_canzone("Bohemian Rhapsody", "Queen", 355)
    canzone2: Canzone = canzoni.crea_canzone("Stairway to Heaven", "Led Zeppelin", 482)
    canzone3: Canzone = canzoni.crea_canzone("Hotel California", "Eagles", 390)

    # Aggiungi le canzoni alla playlist
    playlist.aggiungi_canzone(mia_playlist, canzone1)
    playlist.aggiungi_canzone(mia_playlist, canzone2)
    playlist.aggiungi_canzone(mia_playlist, canzone3)

    # Mostra la playlist
    print(playlist.mostra_playlist(mia_playlist))


if __name__ == "__main__":
    main()
