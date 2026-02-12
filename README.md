# 2526_3M

## Come eseguire i test per un singolo esercizio

### Dove trovare il testo dell'esercizio
Il testo dell'esercizio si trova nel file `esXX_description.md` nella cartella del modulo corrispondente, ad esempio `src/m01_input_output/es01_description.md`.

### Dove trovare la soluzione del docente (se pubblicata)
La soluzione del docente è nel file `esXX_reference.py` nella stessa cartella del modulo, ad esempio `src/m01_input_output/es01_reference.py`.

### Come chiamare il file dello studente
Lo studente deve scrivere la soluzione nel file `esXX_student.py` nella cartella del modulo, ad esempio `src/m01_input_output/es01_student.py`. Il file deve definire una funzione `main()` che sarà testata.

### Come eseguire i test
Per eseguire i test di un singolo esercizio, usa il comando:

```bash
pytest tests/test_esXX.py
```

Sostituisci `XX` con il numero dell'esercizio, ad esempio `pytest tests/test_es01.py`.