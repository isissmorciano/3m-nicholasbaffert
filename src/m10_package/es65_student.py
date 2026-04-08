# 1. Importa il package con `from diario import entrate, persistenza`
# 2. Crea alcune entrate di esempio
# 3. Aggiungile al diario
# 4. Stampa il diario e le statistiche sul tempo totale
# 5. Salva su file e ricarica il diario
from diario_student import entrate_student,persistenza_student
e1 = entrate_student.crea_diario("2026-04-08","studio",60,"Ho iniziato un nuovo corso di Python.")
e2 = entrate_student.crea_diario("2026-04-08","studio",45," Ho scritto un esercizio sul package diario.")
e3 = 