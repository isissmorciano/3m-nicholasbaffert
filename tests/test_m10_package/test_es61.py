"""Test per l'Esercizio 61: Package Musicale"""

from src.m10_package.musica import canzoni, playlist


def test_crea_canzone():
    """Test creazione di una canzone."""
    canzone = canzoni.crea_canzone("Bohemian Rhapsody", "Queen", 355)
    assert canzone["titolo"] == "Bohemian Rhapsody"
    assert canzone["artista"] == "Queen"
    assert canzone["durata"] == 355


def test_info_canzone():
    """Test formattazione informazioni canzone."""
    canzone = canzoni.crea_canzone("Bohemian Rhapsody", "Queen", 355)
    info = canzoni.info_canzone(canzone)
    assert info == "Bohemian Rhapsody - Queen (5:55)"


def test_info_canzone_con_secondi_zero():
    """Test formattazione con secondi < 10."""
    canzone = canzoni.crea_canzone("Test", "Artist", 605)  # 10:05
    info = canzoni.info_canzone(canzone)
    assert info == "Test - Artist (10:05)"


def test_crea_playlist_vuota():
    """Test creazione di una playlist vuota."""
    p = playlist.crea_playlist("My Playlist")
    assert p["nome"] == "My Playlist"
    assert p["canzoni"] == []


def test_aggiungi_canzone():
    """Test aggiunta di canzoni alla playlist."""
    p = playlist.crea_playlist("Test Playlist")
    canzone = canzoni.crea_canzone("Song 1", "Artist 1", 200)
    
    playlist.aggiungi_canzone(p, canzone)
    assert len(p["canzoni"]) == 1
    assert p["canzoni"][0] == canzone


def test_aggiungi_multiple_canzoni():
    """Test aggiunta di multiple canzoni."""
    p = playlist.crea_playlist("Test Playlist")
    c1 = canzoni.crea_canzone("Song 1", "Artist 1", 200)
    c2 = canzoni.crea_canzone("Song 2", "Artist 2", 300)
    c3 = canzoni.crea_canzone("Song 3", "Artist 3", 250)
    
    playlist.aggiungi_canzone(p, c1)
    playlist.aggiungi_canzone(p, c2)
    playlist.aggiungi_canzone(p, c3)
    
    assert len(p["canzoni"]) == 3


def test_rimuovi_canzone():
    """Test rimozione di una canzone per indice."""
    p = playlist.crea_playlist("Test Playlist")
    c1 = canzoni.crea_canzone("Song 1", "Artist 1", 200)
    c2 = canzoni.crea_canzone("Song 2", "Artist 2", 300)
    c3 = canzoni.crea_canzone("Song 3", "Artist 3", 250)
    
    playlist.aggiungi_canzone(p, c1)
    playlist.aggiungi_canzone(p, c2)
    playlist.aggiungi_canzone(p, c3)
    
    playlist.rimuovi_canzone(p, 1)  # Rimuovi Song 2
    
    assert len(p["canzoni"]) == 2
    assert p["canzoni"][0]["titolo"] == "Song 1"
    assert p["canzoni"][1]["titolo"] == "Song 3"


def test_rimuovi_canzone_indice_non_valido():
    """Test rimozione con indice non valido."""
    p = playlist.crea_playlist("Test Playlist")
    c1 = canzoni.crea_canzone("Song 1", "Artist 1", 200)
    playlist.aggiungi_canzone(p, c1)
    
    # Non dovrebbe fare nulla con indice non valido
    playlist.rimuovi_canzone(p, 5)
    assert len(p["canzoni"]) == 1


def test_durata_totale_vuota():
    """Test durata totale per playlist vuota."""
    p = playlist.crea_playlist("Empty Playlist")
    assert playlist.durata_totale(p) == 0


def test_durata_totale():
    """Test calcolo durata totale della playlist."""
    p = playlist.crea_playlist("Test Playlist")
    c1 = canzoni.crea_canzone("Song 1", "Artist 1", 200)  # 3:20
    c2 = canzoni.crea_canzone("Song 2", "Artist 2", 300)  # 5:00
    c3 = canzoni.crea_canzone("Song 3", "Artist 3", 250)  # 4:10
    
    playlist.aggiungi_canzone(p, c1)
    playlist.aggiungi_canzone(p, c2)
    playlist.aggiungi_canzone(p, c3)
    
    # 200 + 300 + 250 = 750 secondi
    assert playlist.durata_totale(p) == 750


def test_mostra_playlist_vuota():
    """Test visualizzazione playlist vuota."""
    p = playlist.crea_playlist("Empty")
    output = playlist.mostra_playlist(p)
    assert "Empty" in output
    assert "Vuota" in output


def test_mostra_playlist():
    """Test visualizzazione playlist con canzoni."""
    p = playlist.crea_playlist("Rock Classics")
    c1 = canzoni.crea_canzone("Bohemian Rhapsody", "Queen", 355)
    c2 = canzoni.crea_canzone("Stairway to Heaven", "Led Zeppelin", 482)
    
    playlist.aggiungi_canzone(p, c1)
    playlist.aggiungi_canzone(p, c2)
    
    output = playlist.mostra_playlist(p)
    
    assert "Rock Classics" in output
    assert "Bohemian Rhapsody" in output
    assert "Queen" in output
    assert "5:55" in output
    assert "Stairway to Heaven" in output
    assert "Led Zeppelin" in output
    assert "8:02" in output
    assert "Durata totale: 13:57" in output
