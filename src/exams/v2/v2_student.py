def esercizio1_calcoli(n: int, numeri: list[int]) -> tuple[int, int, float]:
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    if len(numeri) != n:
        raise ValueError("numero di valori diverso da n")

    somma_quadrati_pari = 0
    count_dispari_negativi = 0
    somma_assoluti = 0

    for num in numeri:
        if num % 2 == 0:
            somma_quadrati_pari += num ** 2
        if num % 2 != 0 and num < 0:
            count_dispari_negativi += 1
        somma_assoluti += abs(num)

    media_assoluta = somma_assoluti / n
    return somma_quadrati_pari, count_dispari_negativi, media_assoluta


def esercizio2_filtri(n: int, numeri: list[int]) -> tuple[list[int], int, int, int]:
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")
    if len(numeri) != n:
        raise ValueError("numero di valori diverso da n")

    filtrati = [x for x in numeri if x > 0 and x % 3 == 0]
    non_filtrati = n - len(filtrati)
    somma_filtrati = sum(filtrati)

    return filtrati, len(filtrati), non_filtrati, somma_filtrati


def esercizio3_prodotti(
    prodotti: list[str],
    prezzi: list[float],
    quantita: list[int]
) -> tuple[list[float], str, int]:
    if not (len(prodotti) == len(prezzi) == len(quantita)):
        raise ValueError("Le liste devono avere la stessa lunghezza")

    valori = []
    for i in range(len(prodotti)):
        valori.append(prezzi[i] * quantita[i])

    max_index = max(range(len(valori)), key=lambda i: valori[i])
    prodotto_max = prodotti[max_index]
    count_prezzobasso_quantita_alta = sum(1 for i in range(len(prodotti)) if prezzi[i] < 10 and quantita[i] > 5)

    return valori, prodotto_max, count_prezzobasso_quantita_alta


def main() -> None:
    print("-- Esercizio 1: Cicli Senza Liste con Calcoli --")
    n = int(input("Quanti numeri inserire? "))
    numeri = []
    for i in range(n):
        numeri.append(int(input(f"Numero {i + 1}: ")))
    s1, c1, m1 = esercizio1_calcoli(n, numeri)
    print(f"Somma quadrati pari: {s1}")
    print(f"Conteggio dispari negativi: {c1}")
    print(f"Media assoluta: {m1}")

    print("\n-- Esercizio 2: Liste con Filtri e Statistiche --")
    n2 = int(input("Quanti numeri inserire per l'esercizio 2? "))
    numeri2 = []
    for i in range(n2):
        numeri2.append(int(input(f"Numero {i + 1}: ")))
    l2, filtri_cnt, non_filtri_cnt, somma_filtri = esercizio2_filtri(n2, numeri2)
    print(f"Lista filtrata: {l2}")
    print(f"Filtrati: {filtri_cnt}")
    print(f"Non filtrati: {non_filtri_cnt}")
    print(f"Somma filtrati: {somma_filtri}")

    print("\n-- Esercizio 3: Liste Parallele con Calcoli --")
    prodotti = ["Pane", "Latte", "Uova"]
    prezzi = [2.5, 1.2, 12.0]
    quantita = [10, 20, 15]
    valori, prodotto_max, count_cond = esercizio3_prodotti(prodotti, prezzi, quantita)

    print("Prodotti:")
    for p, v in zip(prodotti, valori):
        print(f"{p}: {v} €")
    print(f"Prodotto con valore massimo: {prodotto_max}")
    print(f"Prodotti con prezzo <10 e quantità >5: {count_cond}")


if __name__ == "__main__":
    main()
