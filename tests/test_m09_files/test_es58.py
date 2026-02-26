from src.m09_files.es58_student import salva_studenti, carica_studenti, calcola_media, main
import os

def test_salva_studenti():
    studenti = [{"nome": "Test", "voto": 8}]
    nome_file = "test58.json"
    salva_studenti(studenti, nome_file)
    assert os.path.exists(nome_file)
    os.remove(nome_file)

def test_carica_studenti():
    studenti = [{"nome": "Test", "voto": 8}]
    nome_file = "test58.json"
    salva_studenti(studenti, nome_file)
    result = carica_studenti(nome_file)
    assert result == studenti
    os.remove(nome_file)

def test_calcola_media():
    studenti = [{"nome": "A", "voto": 8}, {"nome": "B", "voto": 7}]
    assert calcola_media(studenti) == 7.5

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "File 'studenti.json' salvato con successo." in captured.out
    assert "Studenti caricati:" in captured.out
    assert "Media voti: 8.0" in captured.out
    # Cleanup
    if os.path.exists("studenti.json"):
        os.remove("studenti.json")