from src.m09_files.es59_student import salva_inventario, carica_inventario, filtra_per_categoria, calcola_totale_categoria, main
import os

def test_salva_inventario():
    prodotti = [{"nome": "Test", "categoria": "Test", "prezzo": 1.0, "quantita": 5}]
    nome_file = "test59.json"
    salva_inventario(prodotti, nome_file)
    assert os.path.exists(nome_file)
    os.remove(nome_file)

def test_carica_inventario():
    prodotti = [{"nome": "Test", "categoria": "Test", "prezzo": 1.0, "quantita": 5}]
    nome_file = "test59.json"
    salva_inventario(prodotti, nome_file)
    result = carica_inventario(nome_file)
    assert result == prodotti
    os.remove(nome_file)

def test_filtra_per_categoria():
    prodotti = [
        {"nome": "A", "categoria": "Frutta", "prezzo": 1.0, "quantita": 10},
        {"nome": "B", "categoria": "Pane", "prezzo": 2.0, "quantita": 5}
    ]
    result = filtra_per_categoria(prodotti, "Frutta")
    assert len(result) == 1
    assert result[0]["nome"] == "A"

def test_calcola_totale_categoria():
    prodotti = [
        {"nome": "A", "categoria": "Frutta", "prezzo": 1.0, "quantita": 10},
        {"nome": "B", "categoria": "Pane", "prezzo": 2.0, "quantita": 5}
    ]
    result = calcola_totale_categoria(prodotti, "Frutta")
    assert result == 10.0

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "File 'inventario.json' salvato con successo." in captured.out
    assert "Prodotti Frutta:" in captured.out
    assert "Totale valore Frutta: 39.4" in captured.out
    # Cleanup
    if os.path.exists("inventario.json"):
        os.remove("inventario.json")