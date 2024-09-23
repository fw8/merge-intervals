def merge_intervals(intervals):
    # Sortiere die Intervalle nach ihrem Startpunkt
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # Falls die Liste leer ist oder kein Überlapp vorliegt, füge das Intervall hinzu
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Führe die Intervalle zusammen
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Beispiel
intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
result = merge_intervals(intervals)
print(result)  # Ausgabe: [[2, 23], [25, 30]]
