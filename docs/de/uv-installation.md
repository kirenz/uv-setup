# uv installieren

1. Terminal (macOS) oder Git Bash (Windows) öffnen.
2. Folgenden Befehl ausführen:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Falls `curl` nicht verfügbar ist, stattdessen `wget` verwenden:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

3. Installation abwarten, bis sie abgeschlossen ist.

Nach der Installation prüfen, ob uv verfügbar ist:

4. Aktuelles Terminalfenster schließen.
5. Neues Terminal- oder Git-Bash-Fenster öffnen.
6. Diesen Befehl eingeben:

```bash
uv --version
```

Es sollte eine Versionsnummer erscheinen (z. B. `0.6.8`).

Bei fehlgeschlagener Installation die Schritte unter Problembehebung ausprobieren.

## Problembehebung

### Windows

PowerShell statt Git Bash verwenden und folgenden Befehl ausführen:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS

Zuerst den Paketmanager Homebrew installieren (falls noch nicht vorhanden):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Anschließend uv installieren mit:

```bash
brew install uv
```

Bei Fehlermeldungen vom Typ „Permission denied“ den Schritten in dieser Anleitung folgen:

- [Berechtigungsfehler unter macOS beheben](permission-mac.md)
