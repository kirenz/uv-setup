# Installation von uv
Deutsch | [English](../en/uv-installation.md)

1. Terminal (Mac) oder Git Bash (Windows) öffnen
2. Folgenden Befehl eingeben und Enter drücken:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Falls curl nicht vorhanden sein sollte, kann alternativ auch wget genutzt werden:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```


3. Warten, bis die Installation abgeschlossen ist

## Installation überprüfen

Nach der Installation sollte man überprüfen, ob uv korrekt installiert wurde:

1. Ein neues Terminal- bzw. Git-Bash-Fenster öffnen
2. Folgenden Befehl eingeben:

```bash
uv --version
```

3. Es sollte eine Versionsnummer angezeigt werden (z.B. `0.6.8`)


## Probleme bei der Installation

Für weitere Installationsoptionen besuchen Sie bitte die [offizielle Installationsanleitung](https://docs.astral.sh/uv/getting-started/installation/).


Falls der Befehl `uv --version` nicht gefunden wird, könnte es daran liegen, dass es Schwierigkeiten mit den Rechten gab. In diesem Fall bitte die Anleitungen zur Behebung von Permission denied Fehlern nutzen:

- [Permission denied Fehler unter macOS beheben](permission-mac.md)
