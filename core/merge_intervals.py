# Beschreibung: Diese Funktion nimmt eine Liste von Intervallen als Eingabe und gibt eine Liste von zusammengeführten Intervallen zurück.
# Parameter:
# - intervals: Eine Liste von Intervallen, wobei jedes Intervall durch eine Liste von zwei Ganzzahlen dargestellt wird.
# Rückgabewert: Eine Liste von zusammengeführten Intervallen, wobei jedes Intervall durch eine Liste von zwei Ganzzahlen dargestellt wird.
#
# Beispiel:
# intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
# result = merge_intervals(intervals)
# print(result)  # Ausgabe: [[2, 23], [25, 30]]
#
# Hinweis: Die Funktion überprüft, ob die Eingabeintervalle gültig sind und wirft eine ValueError-Exception, wenn ein ungültiges Intervall gefunden wird.
# Hinweis: Die Intervalle werden nach ihrem Startpunkt sortiert, bevor sie zusammengeführt werden.
# Hinweis: Die Funktion verwendet eine Liste merged, um die zusammengeführten Intervalle zu speichern.
# Hinweis: Die Funktion verwendet eine Schleife, um die Intervalle zu überprüfen und zusammenzuführen.
# Hinweis: Die Funktion verwendet die Funktion max, um den Endpunkt der zusammengeführten Intervalle zu aktualisieren.
# Hinweis: Die Funktion gibt die Liste der zusammengeführten Intervalle zurück.


def merge_intervals(intervals):
    # Falls die Liste leer ist, gib einfach eine leere Liste zurück
    if not intervals:
        return []

    # Validierung: Überprüfe, ob alle Intervalle gültig sind
    for interval in intervals:
        if len(interval) != 2 or interval[0] > interval[1]:
            raise ValueError(f"Ungültiges Intervall: {interval}")

    # Sortiere die Intervalle nach ihrem Startpunkt
    intervals.sort(key=lambda x: x[0])

    # Initialisiere die Liste der zusammengeführten Intervalle
    merged = []

    for interval in intervals:
        # Falls die Liste leer ist oder kein Überlapp vorliegt, füge das Intervall hinzu
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Führe die Intervalle zusammen
            merged[-1][1] = max(merged[-1][1], interval[1])

    # Gib die Liste der zusammengeführten Intervalle zurück
    return merged
