from src.m07_cicli_while.es45_student import main
import random

def test_gioco_rpg(monkeypatch, capsys):
    # Mock random per prevedibilità
    original_choice = random.choice
    original_randint = random.randint
    random.choice = lambda lst: lst[0]  # Sempre Spada
    random.randint = lambda a, b: 50  # Sempre 50 per mostro

    inputs = iter(['1', '3', '4', '5'])  # Esplora, Inventario, Statistiche, Esci
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Hai trovato: Spada (arma, valore: 20)" in captured.out
    assert "Nome: Spada, Tipo: arma, Valore: 20, Usato: False" in captured.out
    assert "Nome: Eroe, Livello: 1, HP: 100, Attacco: 10" in captured.out
    assert "Totale oggetti: 1" in captured.out
    assert "Arrivederci!" in captured.out

    # Restore
    random.choice = original_choice
    random.randint = original_randint