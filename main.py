# Beispiel-Code für die Verwendung der Funktion merge_intervals
from core.merge_intervals import merge_intervals

# Beispiel-Intervalle
intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
print(f"Input Intervalle: {intervals}")

# Intervalle sortieren und zusammenführen
result = merge_intervals(intervals)
print(f"Output Intervalle: {result}")  # Ausgabe: [[2, 23], [25, 30]]
