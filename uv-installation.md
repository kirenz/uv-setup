

## Installation von uv

1. Terminal oder Git Bash öffnen
2. Folgenden Befehl eingeben und Enter drücken:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

:::{.callout-important title="Falls curl nicht installiert ist" collapse="true"}
Falls curl nicht vorhanden sein sollte, kann alternativ auch wget genutzt werden:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```
:::

3. Warten, bis die Installation abgeschlossen ist

### Installation überprüfen

Nach der Installation sollte man überprüfen, ob uv korrekt installiert wurde:

1. Ein neues Terminal- bzw. Git-Bash-Fenster öffnen
2. Folgenden Befehl eingeben:
```bash
uv --version
```
3. Es sollte eine Versionsnummer angezeigt werden (z.B. `0.6.8`)

::: {.callout-important}
Falls die Meldung "Command not found" erscheint, sollte die Kommandozeile neu gestartet werden.
:::
