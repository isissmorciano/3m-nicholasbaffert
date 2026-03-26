"""Esercizio 64: Utilizzo del package quiz con domande e risultati."""

from quiz import domande, risultati


def main() -> None:
    # Definisci alcune domande
    q1 = domande.crea_domanda(
        "Qual è il linguaggio usato in questo corso?",
        ["Python", "Java", "C++"],
        0,
    )
    q2 = domande.crea_domanda(
        "Quale struttura dati Python usa parentesi quadre?",
        ["Dizionario", "Lista", "Tupla"],
        1,
    )
    q3 = domande.crea_domanda(
        "Quale comando usi per stampare in Python?",
        ["print", "echo", "console.log"],
        0,
    )

    domande_quiz = [q1, q2, q3]

    # Simula un utente che risponde
    risposte_utente = [1, 2, 1]  # 1-based: prima opzione, seconda, prima

    risultati_quiz = risultati.crea_risultati()

    for domanda, scelta in zip(domande_quiz, risposte_utente):
        corretta = domande.verifica_risposta(domanda, scelta)
        risultati.registra_risposta(risultati_quiz, corretta)

    print("Risultati:")
    print(risultati.mostra_risultati(risultati_quiz))

    nome_file = "quiz_risultati.json"
    risultati.salva_risultati(risultati_quiz, nome_file)
    print(f"\nRisultati salvati in '{nome_file}'")

    caricati = risultati.carica_risultati(nome_file)
    print(f"Risultati caricati: {risultati.mostra_risultati(caricati)}")


if __name__ == "__main__":
    main()
