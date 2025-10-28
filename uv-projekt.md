# Erstellung eines Projekts mit uv

uv macht die Python-Projektinitialisierung zu einem einfachen Prozess. Mit wenigen Befehlen erhalten wir eine vollständig konfigurierte Entwicklungsumgebung mit der richtigen Python-Version. 

## Projekterstellung mit uv init

Zunächst erstellen wir ein neues Projekt in der Kommandozeile (Terminal bzw. Git Bash). Wir erstellen das Projekt wieder im Home-Verzeichnis.

Um das Projekt in einem anderen Ordner zu installieren, einfach zuerst in das gewünschte Verzeichnis navigieren, (z. B. `cd Documents`).

 Wir nutzen den Befehl `uv init` und geben den gewünschten Namen (hier: `mein-projekt`) und die Python-Version (hier `3.11`) an:


```bash
uv init mein-projekt --python 3.11
```

Damit wird ein neuer Ordner mit der Bezeichnung "mein-projekt" angelegt. 

Wir navigieren nun in diesen Ordner:

```bash
cd mein-projekt
```

Und verwenden `ls -a` um alle darin enthaltenen Dateien anzuzeigen (auch versteckte Ordner und Dateien)

```bash
ls -a
```

Hier einige Hinweise zu den Inhalten:

```
mein-projekt/
├── README.md         # Projektdokumentation
└── pyproject.toml    # Projektkonfiguration
├── main.py           # Python-Beispieldatei
├── .python-version   # Python-Versionsangabe
├── .gitignore        # Git-Ausschlussliste
└── .git/             # Git-Metadate
```

`README.md` dient der Dokumentation, die `pyproject.toml` enthält die Projektkonfiguration und `main.py` ist eine Beispieldatei zum Einstieg.


Eine **TOML-Datei** ist ein Konfigurationsdateiformat, das für "Tom’s Obvious, Minimal Language" steht. Es wurde entwickelt, um menschenlesbar und einfach zu bearbeiten zu sein, während es gleichzeitig strukturiert und maschinenlesbar ist. TOML wird oft in Projekten verwendet, die eine unkomplizierte und klare Konfigurationsdatei benötigen.


uv erstellt auch einige verborgene Dateien (sogenannte "dotfiles"), die wichtige Funktionen erfüllen. Diese Dateien beginnen mit einem Punkt und sind in normalen Verzeichnisansichten oft ausgeblendet. 

Die `.gitignore`-Datei ist eine wichtige Datei für die Arbeit mit Git. Sie enthält Regeln, welche Dateien nicht unter Versionskontrolle gestellt werden sollen. Zudem wurde ein .git-Ordner erstellt (mehr zu Git in einem anderen Kapitel). Eine weitere verborgene Datei ist die `.python-version`. Sie enthält nur eine einzige Zeile, die verwendete Python-Version. 


## Virtuelle Umgebung mit uv sync

Damit eine virtuelle Python-Umgebung für unser Projekt erstellt wird, initialisieren wir das Projekt mit dem Befehl `uv sync` (wir könnten stattdessen auch `uv run` nutzen) :

```bash
uv sync
```

Dadurch wird ein Ordner mit der Bezeichnung `.venv` (für virtual environment) in dem Projekt erzeugt. 


Das `.venv`-Verzeichnis enthält eine isolierte Python-Umgebung speziell für unser Projekt. uv richtet diese automatisch mit der angegebenen Python-Version ein. 

Dies bedeutet:

- Die gewünschte Python-Version wird automatisch heruntergeladen und installiert
- Die Umgebung ist sofort einsatzbereit für die Paketinstallation
- Andere Projekte bleiben von unseren Paketinstallationen unberührt

Ohne aktivierte virtuelle Umgebung werden Pakete weiterhin "global" installiert, d.h. in die allgemeine Python-Umgebung. Mit aktivierter virtueller Umgebung werden Pakete nur in diese spezifische Umgebung installiert. 



Außerdem hat uv eine `uv.lock`-Datei erstellt. Dies ist eine TOML-Datei, wird jedoch von uv verwaltet und sollte nicht manuell bearbeitet werden. 

Die Datei `uv.lock` ist eine *universelle* bzw. *plattformübergreifende* Lockfile, die alle Pakete erfasst, die installiert wurden. Eine Lockfile stellt sicher, dass Personen, die mit verschiedenen Geräten an einem Projekt arbeiten, immer die gleichen Paketversionen nutzen. 

Die Lockfile wird während uv-Aufrufen erstellt und aktualisiert, die die Projektumgebung nutzen, d.h. `uv sync` und `uv run`. Die Lockfile kann auch explizit über `uv lock` aktualisiert werden.

Im Gegensatz zur `pyproject.toml`, die zur Spezifikation der allgemeinen Projektanforderungen dient, enthält die Lockfile die exakten Paket-Versionen, die in der Projektumgebung installiert sind. Diese Datei sollte in die Versionskontrolle aufgenommen werden, um konsistente und reproduzierbare Installationen über verschiedene Systeme hinweg zu ermöglichen.


Damit wir die virtuelle Umgebung nutzen können, muss sie zunächst aktiviert werden: 

```bash
source .venv/bin/activate
```

Wir können nun prüfen, ob tatsächlich die Python-Version 3.11 installiert wurde. Dafür nutzen mir den Befehl `uv run` (damit wird immer unsere uv-Python-Umgebung genutzt, selbst wenn wir vergessen haben sollten, die Umgebung zuvor zu aktivieren) 

```bash
uv run python --version
```

Führen wir außerdem die Beispieldatei main.py aus, um sicherzustellen, dass alles funktioniert:


```bash
uv run python main.py
```

Es sollte eine "Hello from mein-projekt!" Nachricht angezeigt werden


## Pakete installieren

Nach der Initialisierung können wir mit der Entwicklung beginnen. Da uv bereits die virtuelle Umgebung eingerichtet hat, können wir nun Pakete hinzufügen.

In diesem Beispiel nutzen wir `uv add` um die Pakete pandas und openai zu installieren:

```bash
uv add pandas openai 
```


uv aktualisiert bei jedem `uv add`-Befehl automatisch die `pyproject.toml` und uv.lock-Datei und installiert die Pakete in die bereits vorhandene virtuelle Umgebung.



## uv in VS Code

Zur Arbeit in Visual Studio Code (VS Code) das Projekt öffnen.

1. VS Code starten
2. Im Menü oben links „Datei“ wählen
3. „Ordner öffnen…“ auswählen
4. Ordner `mein-projekt` wählen

### Python-Interpreter auswählen

Damit VS Code die richtige Python-Umgebung nutzt, den Interpreter der virtuellen Umgebung auswählen:

- Befehlspalette öffnen: `Strg`+`Shift`+`P` (Windows/Linux) bzw. `Cmd`+`Shift`+`P` (macOS)
- „Python: Interpreter auswählen“ eingeben
- Interpreter wählen (Python 3.11.xx (mein-projekt)):
    - macOS/Linux: `.venv/bin/python`
    - Windows: `.venv\Scripts\python.exe`
- Falls nicht sichtbar: „Interpreter durchsuchen…“ wählen und den Pfad manuell angeben


### Nutzung des integrierten Terminals


Zuerst wird der Terminal-Bereich geöffnet, falls dieser noch nicht sichtbar ist.

- Über das Menü: "Terminal" auswählen und "Neues Terminal" anklicken.

Im nun sichtbaren Terminal-Bereich befindet sich rechts eine Leiste mit Symbolen. Mit der Maus in den Terminal-Bereich navigieren und:

- Ein Klick auf den kleinen **Pfeil nach unten (`v`)** neben dem Plus-Symbol (`+`) öffnet eine Liste aller verfügbaren Terminal-Profile.
  * Aus dieser Liste wird **Git Bash** (Windows) oder **zsh** (macOS) ausgewählt.

Daraufhin wird ein neuer Tab im Terminal-Bereich geöffnet.

Beispieldatei mit uv ausführen (dadurch wird garantiert die Projektumgebung verwendet):

```bash
uv run python main.py
```