from src.exams.v1.v1_student_s1 import main as main_s1
from src.exams.v1.v1_student_s2 import main as main_s2
from src.exams.v1.v1_student_s3 import main as main_s3


def main() -> None:
    print("Verifica v1: scegli esercizio")
    print("1. Esercizio 1")
    print("2. Esercizio 2")
    print("3. Esercizio 3")
    scelta = input("Scelta: ").strip()

    if scelta == "1":
        main_s1()
    elif scelta == "2":
        main_s2()
    elif scelta == "3":
        main_s3()
    else:
        print("Scelta non valida")


if __name__ == "__main__":
    main()
