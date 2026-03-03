"""Esercizio 62: Utilizzo del package coordinate con punti e linee."""

from coordinate import punti, linee


def main() -> None:
    # Crea i punti
    punto_a = punti.crea_punto(0.0, 0.0)
    punto_b = punti.crea_punto(3.0, 4.0)
    punto_c = punti.crea_punto(6.0, 0.0)
    
    # Mostra i punti
    print("=== Coordinate e Linee ===\n")
    print("Punti:")
    print(f"- Punto A: {punti.info_punto(punto_a)}")
    print(f"- Punto B: {punti.info_punto(punto_b)}")
    print(f"- Punto C: {punti.info_punto(punto_c)}")
    
    # Crea le linee
    linea_ab = linee.crea_linea(punto_a, punto_b)
    linea_bc = linee.crea_linea(punto_b, punto_c)
    linea_ca = linee.crea_linea(punto_c, punto_a)
    
    # Mostra le linee con dettagli
    print("\nLinee:")
    for linea in [linea_ab, linea_bc, linea_ca]:
        lungh = round(linee.lunghezza_linea(linea), 2)
        medio = linee.punto_medio(linea)
        print(
            f"- {linee.info_linea(linea)} | "
            f"Lunghezza: {lungh} | "
            f"Punto medio: {punti.info_punto(medio)}"
        )
    
    # Calcola distanza tra tutti i punti
    print("\nDistanze:")
    print(f"- A a B: {round(punti.distanza_tra_punti(punto_a, punto_b), 2)}")
    print(f"- B a C: {round(punti.distanza_tra_punti(punto_b, punto_c), 2)}")
    print(f"- C a A: {round(punti.distanza_tra_punti(punto_c, punto_a), 2)}")


if __name__ == "__main__":
    main()
