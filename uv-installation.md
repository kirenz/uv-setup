# Installation von uv

## Hinweise für Windows

Unter Windows wird empfohlen, **Git Bash** zu verwenden, um uv zu installieren und zu nutzen. Git Bash bietet eine Unix-ähnliche Umgebung, die gut mit uv harmoniert.

Falls Git Bash noch nicht installiert ist, kann dies wie folgt nachgeholt werden:

1.  **Git for Windows** herunterladen: [git-scm.com/download/win](https://git-scm.com/download/win)
2.  Die heruntergeladene Installationsdatei wird ausgeführt. Bei allen Installationsschritten können die Standardeinstellungen beibehalten werden. Es genügt, sich mit "Next" durch den Installer zu klicken.
3.  Nach der Installation findet sich im Windows-Startmenü ein neues Programm namens **Git Bash**. Dieses wird geöffnet.

## Installation unter macOS/Linux

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

- Falls der Befehl `uv --version` nicht gefunden wird, könnte es daran liegen, dass es Schwierigkeiten mit den Rechten gab. In diesem Fall bitte die Anleitungen zur Behebung von Permission denied Fehlern nutzen:

- [Permission denied Fehler unter Windows beheben](permission-windows.md)

- [Permission denied Fehler unter macOS/Linux beheben](permission-mac.md)
