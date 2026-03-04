"""Test per l'Esercizio 63: Package Streaming"""

from src.m10_package.streaming import video, playlist


def test_crea_video():
    """Test creazione di un video."""
    v = video.crea_video("Test Video", 1200, "1080p", 5000)
    assert v["titolo"] == "Test Video"
    assert v["durata"] == 1200
    assert v["risoluzione"] == "1080p"
    assert v["bitrate"] == 5000


def test_info_video():
    """Test formattazione informazioni video."""
    v = video.crea_video("Movie", 135, "720p", 3000)
    info = video.info_video(v)
    assert info == "Movie - 2:15 - 720p - 3000 kbps"


def test_info_video_con_secondi_zero():
    """Test formattazione con secondi < 10."""
    v = video.crea_video("Test", 605, "1080p", 5000)  # 10:05
    info = video.info_video(v)
    assert info == "Test - 10:05 - 1080p - 5000 kbps"


def test_dimensione_video():
    """Test calcolo dimensione video."""
    # Formula: (durata * bitrate) / (8 * 1024)
    # (600 * 5000) / (8 * 1024) = 3000000 / 8192 ≈ 366.21 MB
    v = video.crea_video("Test", 600, "1080p", 5000)
    dim = video.dimensione_video(v)
    assert dim == 366.21


def test_dimensione_video_piccolo():
    """Test calcolo dimensione per video piccolo."""
    v = video.crea_video("Short", 60, "360p", 500)
    dim = video.dimensione_video(v)
    assert dim == 3.66


def test_crea_playlist_vuota():
    """Test creazione di una playlist vuota."""
    p = playlist.crea_playlist("My Streaming")
    assert p["nome"] == "My Streaming"
    assert p["video"] == []


def test_aggiungi_video():
    """Test aggiunta di video alla playlist."""
    p = playlist.crea_playlist("Test Playlist")
    v = video.crea_video("Video 1", 1200, "1080p", 5000)

    playlist.aggiungi_video(p, v)
    assert len(p["video"]) == 1
    assert p["video"][0] == v


def test_aggiungi_multiple_video():
    """Test aggiunta di multiple video."""
    p = playlist.crea_playlist("Test Playlist")
    v1 = video.crea_video("Video 1", 1200, "1080p", 5000)
    v2 = video.crea_video("Video 2", 900, "720p", 3000)
    v3 = video.crea_video("Video 3", 1500, "480p", 2000)

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)
    playlist.aggiungi_video(p, v3)

    assert len(p["video"]) == 3


def test_rimuovi_video():
    """Test rimozione di un video."""
    p = playlist.crea_playlist("Test Playlist")
    v1 = video.crea_video("Video 1", 1200, "1080p", 5000)
    v2 = video.crea_video("Video 2", 900, "720p", 3000)

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)

    playlist.rimuovi_video(p, 0)
    assert len(p["video"]) == 1
    assert p["video"][0]["titolo"] == "Video 2"


def test_rimuovi_video_indice_invalido():
    """Test rimozione con indice non valido."""
    p = playlist.crea_playlist("Test Playlist")
    v = video.crea_video("Video 1", 1200, "1080p", 5000)
    playlist.aggiungi_video(p, v)

    # Non deve aggiustare nulla con indice invalido
    playlist.rimuovi_video(p, 10)
    assert len(p["video"]) == 1


def test_durata_totale():
    """Test calcolo durata totale."""
    p = playlist.crea_playlist("Test")
    v1 = video.crea_video("V1", 600, "1080p", 5000)  # 600s
    v2 = video.crea_video("V2", 900, "720p", 3000)  # 900s
    v3 = video.crea_video("V3", 300, "480p", 2000)  # 300s

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)
    playlist.aggiungi_video(p, v3)

    # Totale: 1800s
    durata = playlist.durata_totale(p)
    assert durata == 1800


def test_durata_totale_vuota():
    """Test durata di playlist vuota."""
    p = playlist.crea_playlist("Empty")
    assert playlist.durata_totale(p) == 0


def test_dimensione_totale():
    """Test calcolo dimensione totale."""
    p = playlist.crea_playlist("Test")
    v1 = video.crea_video("V1", 600, "1080p", 5000)  # 366.21 MB
    v2 = video.crea_video("V2", 300, "720p", 3000)  # 109.86 MB

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)

    dim = playlist.dimensione_totale(p)
    # 366.21 + 109.86 = 476.07 MB
    assert dim == 476.07


def test_ordina_per_durata():
    """Test ordinamento per durata."""
    p = playlist.crea_playlist("Test")
    v1 = video.crea_video("V1", 1200, "1080p", 5000)
    v2 = video.crea_video("V2", 600, "720p", 3000)
    v3 = video.crea_video("V3", 900, "480p", 2000)

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)
    playlist.aggiungi_video(p, v3)

    ordinati = playlist.ordina_per_durata(p)

    assert ordinati[0]["durata"] == 600  # V2
    assert ordinati[1]["durata"] == 900  # V3
    assert ordinati[2]["durata"] == 1200  # V1


def test_mostra_playlist():
    """Test formattazione della playlist."""
    p = playlist.crea_playlist("My Streaming")
    v1 = video.crea_video("Video 1", 120, "1080p", 5000)
    v2 = video.crea_video("Video 2", 90, "720p", 3000)

    playlist.aggiungi_video(p, v1)
    playlist.aggiungi_video(p, v2)

    info = playlist.mostra_playlist(p)
    assert "My Streaming" in info
    assert "Video 1" in info
    assert "Video 2" in info
    assert "1080p" in info
    assert "720p" in info


def test_mostra_playlist_vuota():
    """Test formattazione playlist vuota."""
    p = playlist.crea_playlist("Empty")
    info = playlist.mostra_playlist(p)
    assert "Empty" in info
