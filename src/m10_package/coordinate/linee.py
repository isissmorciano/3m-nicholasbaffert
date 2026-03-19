"""Modulo per la gestione delle linee in 2D."""

from .punti import distanza_tra_punti, info_punto, crea_punto


def crea_linea(p1: dict, p2: dict) -> dict:
    """
    Crea una linea rappresentata come dizionario.
    
    Args:
        p1: Punto di partenza
        p2: Punto di arrivo
        
    Returns:
        Un dizionario con chiavi: p1, p2
    """
    return {
        "p1": p1,
        "p2": p2
    }


def lunghezza_linea(linea: dict) -> float:
    """Calcola la lunghezza della linea usando la distanza tra i due punti."""
    return distanza_tra_punti(linea["p1"], linea["p2"])


def punto_medio(linea: dict) -> dict:
    """
    Calcola il punto medio tra i due estremi della linea.
    
    Coordinate: ((x1+x2)/2, (y1+y2)/2)
    """
    x_medio = (linea["p1"]["x"] + linea["p2"]["x"]) / 2
    y_medio = (linea["p1"]["y"] + linea["p2"]["y"]) / 2
    return crea_punto(x_medio, y_medio)


def info_linea(linea: dict) -> str:
    """
    Restituisce una stringa formattata della linea.
    
    Formato: "Linea da (x1, y1) a (x2, y2)"
    """
    return f"Linea da {info_punto(linea['p1'])} a {info_punto(linea['p2'])}"
