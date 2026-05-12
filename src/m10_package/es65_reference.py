"""Esercizio 65: Utilizzo del package diario con entrate e persistenza."""

from diario import entrate, persistenza


def main() -> None:
    diario = entrate.crea_diario()

    e1 = entrate.crea_entrata(
        "2026-04-08",
        "Ho iniziato un nuovo corso di Python.",
        "studio",
        60,
    )
    e2 = entrate.crea_entrata(
        "2026-04-08",
        "Ho scritto un esercizio sul package diario.",
        "studio",
        45,
    )
    e3 = entrate.crea_entrata(
        "2026-04-09",
        "Sono andato a fare una passeggiata nel parco.",
        "tempo libero",
        30,
    )

    entrate.aggiungi_entrata(diario, e1)
    entrate.aggiungi_entrata(diario, e2)
    entrate.aggiungi_entrata(diario, e3)

    print("=== Diario ===")
    for voce in diario["entrate"]:
        print(entrate.info_entrata(voce))

    totale = entrate.tempo_totale(diario)
    print(f"\nTempo totale: {totale} minuti")

    per_categoria = entrate.tempo_per_categoria(diario)
    print("\nTempo per categoria:")
    for categoria, minuti in per_categoria.items():
        print(f"- {categoria}: {minuti} minuti")

    nome_file = "diario.json"
    persistenza.salva_diario(diario, nome_file)
    print(f"\nDiario salvato in '{nome_file}'")

    caricati = persistenza.carica_diario(nome_file)
    print("\nDiario caricato:")
    for voce in caricati["entrate"]:
        print(entrate.info_entrata(voce))


if __name__ == "__main__":
    main()
