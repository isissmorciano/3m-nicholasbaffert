PASSWORD_COMUNI = ["password", "123456", "qwerty", "admin", "letmein"]


def conta_caratteri(password: str) -> dict[str, int]:
    maiuscole = 0
    minuscole = 0
    numeri = 0

    for ch in password:
        if ch.isupper():
            maiuscole += 1
        elif ch.islower():
            minuscole += 1
        elif ch.isdigit():
            numeri += 1

    return {"maiuscole": maiuscole, "minuscole": minuscole, "numeri": numeri}


def valida_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if password[0].isupper() is False:
        return False

    if password.lower() in PASSWORD_COMUNI:
        return False

    conteggi = conta_caratteri(password)
    if conteggi["maiuscole"] < 1 or conteggi["minuscole"] < 1 or conteggi["numeri"] < 1:
        return False

    return True


def livello_sicurezza(password: str) -> int:
    if not valida_password(password):
        return 0

    livello = 1
    if len(password) >= 10:
        livello += 1

    conteggi = conta_caratteri(password)
    if conteggi["maiuscole"] > 1 or conteggi["numeri"] > 1:
        livello += 1

    return min(livello, 3)


def esercizio1_main() -> None:
    pw = input("Inserisci password: ").strip()
    if valida_password(pw):
        print(f"Valida (Livello {livello_sicurezza(pw)})")
    else:
        print("Non valida")


def aggiungi_ingrediente() -> dict[str, float | str]:
    nome = input("Nome ingrediente: ").strip()
    quantita = float(input("Quantità: "))
    prezzo_unitario = float(input("Prezzo unitario: "))
    return {"nome": nome, "quantita": quantita, "prezzo_unitario": prezzo_unitario}


def calcola_costo_totale(ricetta: list[dict[str, float]]) -> float:
    return sum(item["quantita"] * item["prezzo_unitario"] for item in ricetta)


def visualizza_ricetta(ricetta: list[dict[str, float]]) -> None:
    for ingrediente in ricetta:
        nome = ingrediente["nome"]
        q = ingrediente["quantita"]
        prezzo = ingrediente["prezzo_unitario"]
        costo = q * prezzo
        print(f"{nome}: {q} x {prezzo} = {costo}")
    print(f"Totale: {calcola_costo_totale(ricetta)} €")


def esercizio2_main() -> None:
    ricetta: list[dict[str, float]] = []
    while True:
        print("\nMenu ricetta:\n1. Aggiungi\n2. Visualizza\n3. Totale\n4. Esci")
        scelta = input("Scelta: ").strip()
        if scelta == "1":
            ricetta.append(aggiungi_ingrediente())
        elif scelta == "2":
            visualizza_ricetta(ricetta)
        elif scelta == "3":
            print(f"Totale: {calcola_costo_totale(ricetta)} €")
        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")


def main() -> None:
    print("--- Verifica v3 ---")
    esercizio1_main()
    esercizio2_main()


if __name__ == "__main__":
    main()
