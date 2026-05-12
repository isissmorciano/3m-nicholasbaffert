from src.m09_files.es57_student import conta_parole, main
import os

def test_conta_parole():
    nome_file = "test57.txt"
    with open(nome_file, "w") as f:
        f.write("Python è un linguaggio. Python è potente.")
    result = conta_parole(nome_file)
    expected = {"python": 2, "è": 2, "un": 1, "linguaggio": 1, "potente": 1}
    assert result == expected
    os.remove(nome_file)

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "File 'esercizio57.txt' creato con successo." in captured.out
    assert "Conteggio parole:" in captured.out
    assert "python: 2" in captured.out
    assert "è: 2" in captured.out
    # Cleanup
    if os.path.exists("esercizio57.txt"):
        os.remove("esercizio57.txt")