# Funktion: merge_intervals
# Beschreibung: Diese Funktion nimmt eine Liste von Intervallen und gibt eine Liste von zusammengeführten Intervallen zurück.
# Die Intervalle werden nach ihrem Startpunkt sortiert und dann zusammengeführt, wenn sie sich überlappen.
# Parameter:
# - intervals: Eine Liste von Intervallen, die zusammengeführt werden sollen.
# Rückgabewert:
# - Eine Liste von zusammengeführten Intervallen.
# Hinweis: Die Funktion verwendet das Modell Interval aus models/types.py.


from typing import List

from models.types import Interval


def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    # Falls die Liste leer ist, gib einfach eine leere Liste zurück
    if not intervals:
        return []

    # Sortiere die Intervalle nach ihrem Startpunkt
    intervals.sort(key=lambda interval: interval.start)

    # Initialisiere die Liste der zusammengeführten Intervalle
    merged = [intervals[0]]  # Starte mit dem ersten Intervall

    # Starte bei Index 1, da das erste Intervall bereits in merged ist
    for current in intervals[1:]:
        # Hole das zuletzt zusammengeführte Intervall
        last_merged = merged[-1]

        # Überprüfe, ob das aktuelle Intervall mit dem letzten zusammengeführten Intervall überlappt
        if last_merged.end < current.start:
            # Kein Überlappen, füge das aktuelle Intervall hinzu
            merged.append(current)
        else:
            # Überlappen, vereine die Intervalle
            last_merged.end = max(last_merged.end, current.end)

    # Gib die Liste der zusammengeführten Intervalle zurück
    return merged
