"""Esercizio 63: Utilizzo del package streaming con video e playlist."""

from streaming import video, playlist


def main() -> None:
    # Crea una playlist
    mia_playlist = playlist.crea_playlist("Corso Python 2026")

    # Crea i video con diverse risoluzioni e bitrate
    v1 = video.crea_video("Introduzione a Python", 930, "1080p", 5000)
    v2 = video.crea_video("Variabili e Tipi", 1335, "720p", 3000)
    v3 = video.crea_video("Funzioni e Moduli", 1080, "1080p", 5000)
    v4 = video.crea_video("Liste e Dizionari", 1560, "480p", 2000)
    v5 = video.crea_video("Introduzione OOP", 1350, "720p", 3000)

    # Aggiungi i video alla playlist
    playlist.aggiungi_video(mia_playlist, v1)
    playlist.aggiungi_video(mia_playlist, v2)
    playlist.aggiungi_video(mia_playlist, v3)
    playlist.aggiungi_video(mia_playlist, v4)
    playlist.aggiungi_video(mia_playlist, v5)

    # Stampa la playlist originale
    print("=" * 60)
    print("PLAYLIST ORIGINALE")
    print("=" * 60)
    print(playlist.mostra_playlist(mia_playlist))

    # Calcola statistiche
    durata_tot = playlist.durata_totale(mia_playlist)
    minuti_tot = durata_tot // 60
    secondi_tot = durata_tot % 60
    dimensione_tot = playlist.dimensione_totale(mia_playlist)

    print(f"\nDurata totale: {minuti_tot}:{secondi_tot:02d}")
    print(f"Dimensione totale: {dimensione_tot} MB")

    # Mostra i dimensioni di ogni video
    print("\nDimensioni dei video:")
    for v in mia_playlist["video"]:
        dim = video.dimensione_video(v)
        print(f"- {v['titolo']}: {dim} MB")

    # Ordina per durata
    print("\n" + "=" * 60)
    print("ORDINATI PER DURATA (crescente)")
    print("=" * 60)
    video_ordinati = playlist.ordina_per_durata(mia_playlist)
    print(playlist.mostra_playlist({"nome": "Ordinati per durata", "video": video_ordinati}))


if __name__ == "__main__":
    main()
