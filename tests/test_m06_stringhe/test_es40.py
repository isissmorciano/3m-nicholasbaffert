from src.m06_stringhe.es40_student import main

def test_formattazione_prodotti(capsys):
    main()
    captured = capsys.readouterr()
    assert "Prodotto: Mela, Totale: 13.50 € (sconto 10%), Inizia con 'M': True, Conteggio 'a': 1" in captured.out
    assert "Prodotto: Banana, Totale: 10.00 € (nessuno sconto), Inizia con 'M': False, Conteggio 'a': 3" in captured.out
    assert "Prodotto: Arancia, Totale: 9.60 € (nessuno sconto), Inizia con 'M': False, Conteggio 'a': 3" in captured.out