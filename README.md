# Implementierung einer Merge-Funktion für Intervalle

## Funktionsbeschreibung

Die Funktion `merge_intervals` nimmt eine Liste von Intervallen entgegen und gibt als Ergebnis wiederum eine Liste von Intervallen zurück. Überlappende Intervalle werden gemerged, und nicht überlappende Intervalle bleiben unberührt.

### Beispiel:

Input: `[25,30]`, `[2,19]`, `[14,23]`, `[4,8]`  
Output: `[2,23]`, `[25,30]`

Die Funktion eignet sich insbesondere für die Verarbeitung von Intervall-Daten wie Zeiträume oder Bereichsangaben, bei denen eine Konsolidierung notwendig ist.

## Installation und Test

### Voraussetzung: Python

Um die Funktion auszuführen, wird Python benötigt. Alternativ kann die Umgebung auch in einem Docker-Container bereitgestellt werden.

### Installation

#### Lokale Python-Installation:

1. **Virtuelle Umgebung erstellen und aktivieren**:

```bash {"id":"01J8M4NMWB3FKYDEG1P2WRW38R"}
python3.12 -m venv .venv && source .venv/bin/activate
```

2. **Benötigte Pakete installieren**:

```bash {"id":"01J8MCS8YWEK42TE4FKSD1CR06"}
pip install -r tests/requirements.txt
```

3. **Ausführen der Funktion**:

Ein beispielhafter Aufruf der Funktion kann mit `main.py` erfolgen:

```bash {"id":"01J8MCS8YWEK42TE4FKTDMFP54"}
python main.py
```

4. **Unit-Tests ausführen**:

Um die Unit-Tests zu starten, kann `pytest` verwendet werden:

```bash {"id":"01J8MCS8YWEK42TE4FKXZ40KV5"}
pytest
```

#### Docker-Installation:

Falls du kein lokales Python-Setup verwenden möchtest, kannst du die Funktion in einem Docker-Container ausführen:

1. **Interaktiven Docker-Container erstellen**:

In einer `bash`:

```bash {"id":"01J8MCS8YWEK42TE4FM1RDRHWC"}
docker run --rm -it -v $(pwd):/work -w /work python:3.12 bash
```

In einer Powershell

```powershell {"id":"01J8MCS8YWEK42TE4FM30K6385"}
docker run --rm -it -v ${pwd}:/work -w /work python:3.12 bash
```

2. **Weiter wie oben**:  
   Innerhalb des Containers kannst du die gleichen Schritte ausführen, um die Umgebung zu installieren und die Funktion bzw. Tests auszuführen.

## Anmerkungen

### Performance:

Die Leistung der Funktion wird vor allem durch das Sortieren der Intervalle bestimmt. Das Sortieren erfolgt mit einer Laufzeit von **O(n log n)**. Das anschließende Zusammenführen der Intervalle erfolgt in **O(n)**, wobei `n` die Anzahl der Intervalle ist.

### Speicherverbrauch:

1. **Sortieren**:  
   Die Python-Methode `list.sort()` führt eine "in-place"-Sortierung durch, was bedeutet, dass der Speicherbedarf minimal ist, da kein zusätzlicher Speicher für die Liste selbst benötigt wird. Lediglich Platz für ein temporäres Element wird zusätzlich gebraucht.
2. **Merging-Phase**:  
   Im schlimmsten Fall kann die Speicheranforderung für die Ergebnisliste genauso groß sein wie die Eingabeliste, da eine neue Liste `merged` erstellt wird, in die die gemergten Intervalle eingefügt werden.

### Verbesserungsmöglichkeiten und Herausforderungen bei großen Datenmengen

#### Speicheroptimierung:

Falls die ursprüngliche Liste nach dem Merge nicht mehr benötigt wird, könnte die Funktion die Eingabeliste direkt modifizieren (in-place), anstatt eine neue Liste zu erzeugen. Dies spart Speicher, da keine Kopien angelegt werden müssen. Die neue Länge der Liste kann dann als Rückgabewert geliefert werden. Dieser Ansatz erhöht die Komplexität der Funktion deutlich und muß auch vom Nutzer der Funktion berücksichtigt werden, da die übergebene Liste manipuliert wird.

#### Teile-und-Herrsche-Ansatz:

Wenn die Eingabeliste so groß ist, dass sie nicht in den Speicher passt, sollte die Liste in **Chunks** verarbeitet werden. Zwischenstände können auf die Festplatte oder in eine Datenbank ausgelagert werden (Streaming-Verarbeitung).

#### Nutzung von Datenbanken:

Datenbanken sind auf die Verarbeitung großer Datenmengen spezialisiert und bieten fortschrittliche Mechanismen zum Sortieren und Mergen von Daten. Statt die Verarbeitung selbst zu implementieren, kann eine relationale oder NoSQL-Datenbank verwendet werden, um die Intervalldaten zu speichern und zu verarbeiten.

#### Performance-Optimierung durch verteilte Verarbeitung:

Für sehr große Datensätze kann das **Teile-und-Herrsche-Prinzip** auch in einer verteilten Architektur angewendet werden. Die Intervall-Daten können in kleinere Teile (Chunks) aufgeteilt und parallel verarbeitet werden, z. B. durch verteilte Systeme wie **Apache Spark** oder mit Microservices-Plattformen wie **Kubernetes**. Die Teilresultate können anschließend in einer abschließenden Phase zusammengeführt werden, um das endgültige Ergebnis zu erhalten.

---
Durch die oben genannten Techniken lässt sich die Performance und Skalierbarkeit der Merge-Funktion für verschiedene Anwendungsfälle optimieren.
