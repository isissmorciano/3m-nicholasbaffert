"""Modulo per la gestione dei punti in 2D."""

import math


def crea_punto(x: float, y: float) -> dict:
    """
    Crea un punto rappresentato come dizionario.
    
    Args:
        x: Coordinata x
        y: Coordinata y
        
    Returns:
        Un dizionario con chiavi: x, y
    """
    return {
        "x": x,
        "y": y
    }


def distanza_tra_punti(p1: dict, p2: dict) -> float:
    """
    Calcola la distanza euclidea tra due punti.
    
    Formula: √((x2-x1)² + (y2-y1)²)
    """
    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    return math.sqrt(dx**2 + dy**2)


def info_punto(punto: dict) -> str:
    """
    Restituisce una stringa formattata del punto.
    
    Formato: "(x, y)"
    """
    return f"({punto['x']}, {punto['y']})"
