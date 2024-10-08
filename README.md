![Python tests](https://github.com/FW8/merge-intervals/actions/workflows/python-tests.yaml/badge.svg)

# Implementierung einer Merge-Funktion für Intervalle

## Funktionsbeschreibung

Die Funktion `merge_intervals` nimmt eine Liste von Intervallen entgegen und gibt als Ergebnis wiederum eine Liste von Intervallen zurück. Überlappende Intervalle werden gemerged, und nicht überlappende Intervalle bleiben unberührt.

### Beispiel:

Input: `[25,30]`, `[2,19]`, `[14,23]`, `[4,8]`  
Output: `[2,23]`, `[25,30]`

## Implementierung

Beschreibung des verwendeten Algorithmus:

- Die Intervalle werden zuerst nach ihrem Startpunkt sortiert.
- Dann durchlaufen wir die sortierte Liste und prüfen, ob das aktuelle Intervall mit dem letzten Intervall der Ergebnisliste überlappt.
- Wenn eine Überlappung vorliegt, werden die beiden Intervalle zusammengeführt, indem wir den Endpunkt aktualisieren.
- Wenn keine Überlappung vorliegt, wird das Intervall direkt zur Ergebnisliste hinzugefügt.

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
pip install -r requirements.txt
```

3. **Ausführen der Funktion**:

Ein beispielhafter Aufruf der Funktion kann mit `main.py` erfolgen:

```bash {"id":"01J8MCS8YWEK42TE4FKTDMFP54"}
python main.py
```

4. **Unit-Tests ausführen**:

Um die Unit-Tests zu starten, kann `pytest` verwendet werden. Es müssen allerdings vorher noch zusetzliche Pakete installiert werden.

```bash {"id":"01J8N5M41BMSVR2FQYMEW6EYET"}
pip install -r tests/requirements.txt
```

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

## Entwicklung

### Projektstruktur

Die wichtigsten Verzeichnisse und Dateien im Projekt:

```txt {"id":"01J8Q344AA92SWHK2Y1KC732A6"}
├── README.md
├── core
│   └── merge_intervals.py
├── dev-requirements.txt
├── main.py
├── models
│   └── custom_types.py
├── requirements.txt
└── tests
    ├── requirements.txt
    └── test_merge_intervals.py
```

* `core` enthält die eigentliche Anwendung bzw. Funktion
* `models`enthält die Pydantic-Modelle
* `tests`enthält die Unit-Tests

Beim Entwickeln sollten die `dev-requirements.txt` installiert werden, um alle benötigten Entwicklungstools zu bekommen:

```bash {"id":"01J8Q344AA92SWHK2Y1P7FVYSM"}
pip install -r dev-requirements.txt
```

### Tools und Methoden

Die Anwendung verschiedener Tools und Vorgehensweisen können helfen, den Code robuster, besser lesbar, besser wartbar und damit weniger fehleranfällig zu machen.
Es folgt eine Liste von Tools, die beim Entwickeln, aber auch in der automatischen Code-Prüfung verwendet werden.

#### Ruff: Schneller und Leichtgewichtiger Linter

**Ruff** ist ein sehr schneller Linter und Code-Formatter, der entwickelt wurde, um große Codebasen effizient zu handhaben. Er ist in Rust geschrieben und zielt darauf ab, Echtzeit-Feedback zu liefern, ohne Geschwindigkeit oder Genauigkeit zu opfern. **Ruff** wurde entwickelt, um Werkzeuge wie Flake8 zu ersetzen, und unterstützt eine breite Palette von Linting-Regeln.

Wichtige Funktionen:

* 10- bis 100-mal schneller als herkömmliche Linter.
* Unterstützt eine Vielzahl von Linting-Regeln.
* Benötigt minimale Konfiguration.
* Bietet schnelles Feedback während der Entwicklung.

Um den Code zu formatieren und die Importe in einem einheitlichen Schema zu sortieren, sollten folgende Kommandos vor jedem Commit mit Code-Änderungen ausgeführt werden:

```bash {"id":"01J8Q344AA92SWHK2Y1R93S5YA"}
ruff check --select I --fix .
ruff format .
```

#### Pydantic: Datenvalidierung und Verwaltung von Einstellungen

**Pydantic** ist eine Bibliothek zur Datenvalidierung und Einstellungenverwaltung, die Python-Typannotationen verwendet. Sie stellt die Datenintegrität sicher, indem sie Daten validiert und analysiert, was sie ideal für die Handhabung komplexer Konfigurationen und Datenstrukturen macht. **Pydantic** funktioniert hervorragend mit FastAPI und anderen Frameworks und bietet eine nahtlose Validierung von Anfragen- und Antwortdaten.

Wichtige Funktionen:

* Verwendet Typannotationen zur Datenvalidierung.
* Parst und konvertiert Daten automatisch.
* Funktioniert mit FastAPI für die API-Entwicklung.
* Bietet effiziente und benutzerfreundliche Fehlerbehandlung.

#### MyPy: Statische Typüberprüfung

**MyPy** bringt statische Typüberprüfung in Python. Durch das Erzwingen von Typ-Hinweisen hilft **MyPy**, typbezogene Fehler früh im Entwicklungsprozess zu erkennen, was die Robustheit und Lesbarkeit des Codes verbessert. Es ist besonders nützlich für große Codebasen, bei denen dynamische Typisierung zu Laufzeitfehlern führen kann.

Wichtige Funktionen:

* Bietet statische Typüberprüfung für Python-Code.
* Hilft, typbezogene Fehler zu erkennen und zu verhindern.
* Verbessert die Lesbarkeit und Wartbarkeit des Codes.
* Funktioniert mit Pydantic für eine nahtlose Datenvalidierung.

Um eine Typüberprüfung durchzuführen, kann folgendes Kommando ausgeführt werden:

```bash {"id":"01J8Q2YF3T5ZBJ5TNSDTTJEY27"}
mypy .
```

## Weitere Anmerkungen

### Performance:

Die Leistung der Funktion wird vor allem durch das Sortieren der Intervalle bestimmt. Das Sortieren erfolgt mit einer Zeitkomplexität von **O(n log n)**. Das anschließende Zusammenführen der Intervalle erfolgt in **O(n)**, wobei `n` die Anzahl der Intervalle ist.

### Speicherverbrauch:

1. **Sortieren**:  
   Die Python-Methode `list.sort()` führt eine "in-place"-Sortierung durch, was bedeutet, dass der Speicherbedarf minimal ist, da lediglich Platz für ein temporäres Element zusätzlich gebraucht wird.
2. **Merging-Phase**:  
   Im schlimmsten Fall kann die Speicheranforderung für die Ergebnisliste genauso groß sein wie die Eingabeliste, da eine neue Liste `merged` erstellt wird, in die die gemergten Intervalle eingefügt werden.

### Verbesserungsmöglichkeiten und Herausforderungen bei großen Datenmengen

#### Fehlerbehandlung

Weitere Fehlerbehandlung, um ungültige Eingaben abzufangen und aussagekräftige Fehlermeldungen zu liefern.

#### Logging

Logging kann sinnvoll sein, um zu überwachen, wie die Eingabe verarbeitet wird und wo Engpässe oder Fehler auftreten.

#### Metriken

Metriken bereitstellen (z.B. für Prometheus).

- Anzahl der verarbeiteten Intervalle:
   Anzahl der Intervalle, die verarbeitet werden, um Engpässe oder steigende Arbeitslast zu erkennen.
- Dauer der Merge-Operation:
   Zeit (Latenz), die benötigt wird, um die Merge-Operation durchzuführen (Durchschnittszeit, maximale Zeit, etc.).
- Speichernutzung:
   Überwachung des Speichers, der durch die Merge-Operation verbraucht wird, besonders in Bezug auf große Datenmengen.
- Anzahl der Fehler:
   Anzahl der auftretenden Fehler, z. B. wenn ungültige Daten (falsche Typen oder Werte) übergeben werden.
- Systemressourcen:
   CPU-Auslastung und Speicherverbrauch während der Ausführung der Merge-Operation.

#### Unit-Tests

Tests, die sowohl normale als auch Grenzfälle abdecken (z. B. überlappende Intervalle, identische Intervalle, keine Überlappung).

#### Benchmarking

Durchführen von Benchmarks mit verschiedenen Eingabegrößen, um die Leistung der Funktion bei steigender Eingabegröße zu überwachen.

#### Speicheroptimierung:

Falls die ursprüngliche Liste nach dem Merge nicht mehr benötigt wird, könnte die Funktion die Eingabeliste direkt modifizieren (in-place), anstatt eine neue Liste zu erzeugen. Dies spart Speicher, da keine Kopien angelegt werden müssen. Die neue Länge der Liste kann dann als Rückgabewert geliefert werden. Dieser Ansatz erhöht die Komplexität der Funktion deutlich und muß auch vom Nutzer der Funktion berücksichtigt werden, da die übergebene Liste manipuliert wird.

#### Chunking

Wenn die Eingabeliste so groß ist, dass sie nicht in den Speicher passt, sollte die Liste in **Chunks** verarbeitet werden. Zwischenstände können auf die Festplatte oder in eine Datenbank ausgelagert werden (Streaming-Verarbeitung).

#### Nutzung von Datenbanken:

Datenbanken sind auf die Verarbeitung großer Datenmengen spezialisiert und bieten fortschrittliche Mechanismen zum Sortieren und Mergen von Daten. Statt die Verarbeitung selbst zu implementieren, kann eine relationale oder NoSQL-Datenbank verwendet werden, um die Intervalldaten zu speichern und zu verarbeiten.

#### Performance-Optimierung durch verteilte Verarbeitung:

Für sehr große Datensätze kann das **Teile-und-Herrsche-Prinzip** auch in einer verteilten Architektur angewendet werden. Die Intervall-Daten können in kleinere Teile (Chunks) aufgeteilt und parallel verarbeitet werden, z. B. durch verteilte Systeme wie **Apache Spark** oder mit Microservices-Plattformen wie **Kubernetes**. Die Teilresultate können anschließend in einer abschließenden Phase zusammengeführt werden, um das endgültige Ergebnis zu erhalten.

---

Durch die oben genannten Techniken lässt sich die Performance und Skalierbarkeit der Merge-Funktion für verschiedene Anwendungsfälle optimieren.
