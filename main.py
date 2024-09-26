# Beispiel-Code für die Verwendung der Funktion merge_intervals
from core.merge_intervals import merge_intervals
from models.custom_types import Interval

try:
    # Beispiel-Intervalle
    input_intervals = [
        Interval(start=25, end=30),
        Interval(start=2, end=19),
        Interval(start=14, end=23),
        Interval(start=4, end=8),
    ]

    print("Input Intervalle:")
    for interval in input_intervals:
        print(f"[{interval.start}, {interval.end}]")

    # Intervalle sortieren und zusammenführen
    merged_intervals = merge_intervals(input_intervals)

    # Ergebnis anzeigen
    print("Output Intervalle:")
    for interval in merged_intervals:
        print(f"[{interval.start}, {interval.end}]")

except ValueError as e:
    print("Eingabefehler:", e)
