from src.m09_files.es56_student import scrivi_file, leggi_file, main
import os

def test_scrivi_file():
    frasi = ["Test 1", "Test 2"]
    nome_file = "test56.txt"
    scrivi_file(frasi, nome_file)
    assert os.path.exists(nome_file)
    with open(nome_file, "r") as f:
        content = f.read()
    assert content == "Test 1\nTest 2\n"
    os.remove(nome_file)

def test_leggi_file():
    nome_file = "test56.txt"
    with open(nome_file, "w") as f:
        f.write("Line 1\nLine 2\n")
    result = leggi_file(nome_file)
    assert result == ["Line 1", "Line 2"]
    os.remove(nome_file)

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "File 'esercizio56.txt' scritto con successo." in captured.out
    assert "Contenuto del file:" in captured.out
    assert "Ciao mondo" in captured.out
    assert "Python è divertente" in captured.out
    assert "File handling" in captured.out
    # Cleanup
    if os.path.exists("esercizio56.txt"):
        os.remove("esercizio56.txt")