# Projektmanagement mit uv

uv ist ein schneller, in Rust geschriebener Paket- und Projektmanager für Python. Er bündelt Installation, virtuelle Umgebungen und Dependency-Management in einem einzigen Werkzeug und ist damit eine moderne Alternative zu `pip`, `virtualenv` oder `pip-tools`.

## Inhalt
- [Warum uv?](#warum-uv)
- [Schnellstart](#schnellstart)
- [Dokumentation in diesem Ordner](#dokumentation-in-diesem-ordner)
- [Weiterführende Ressourcen](#weiterführende-ressourcen)

## Warum uv?
- Installiert Python-Versionen, Pakete und virtuelle Umgebungen in einem Schritt
- Erstellt reproduzierbare Umgebungen durch `uv.lock`
- Läuft 10–100x schneller als klassische `pip`-Workflows
- Verfügt über eine `pip`-kompatible Oberfläche und lässt sich schrittweise einführen

## Schnellstart
1. **Terminal öffnen**  
   - Windows: Git Bash  
   - macOS/Linux: Terminal bzw. zsh
2. **uv installieren**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Alternativ `wget -qO- … | sh`. Hinweise zu Berechtigungen siehe unten.
3. **Neues Projekt anlegen**
   ```bash
   uv init mein-projekt --python 3.11
   cd mein-projekt
   ```
4. **Umgebung synchronisieren**
   ```bash
   uv sync
   ```
   Dadurch entstehen `.venv/`, `pyproject.toml` und `uv.lock`.
5. **Code ausführen oder Pakete ergänzen**
   ```bash
   uv run python main.py
   uv add pandas openai
   ```
6. **VS Code nutzen**  
   Projektordner öffnen, anschließend in der Befehls­palette den Interpreter aus `.venv` auswählen.

Bei `permission denied`-Fehlern helfen die Anleitungen weiter unten.

## Dokumentation in diesem Ordner
- [uv-hinweise.md](uv-hinweise.md): Überblick, Funktionsumfang und Begriffe rund um uv
- [uv-installation.md](uv-installation.md): Installationsanleitung inkl. Fehlerbehebung
- [uv-projekt.md](uv-projekt.md): Schritt-für-Schritt-Anleitung zum Aufbau eines Projekts
- [permission-windows.md](permission-windows.md): Rechteprobleme in Git Bash unter Windows lösen
- [permission-mac.md](permission-mac.md): Rechteprobleme unter macOS (zsh/fish) beheben

## Weiterführende Ressourcen
- Offizielle Website: [https://astral.sh/uv](https://astral.sh/uv)
- GitHub-Repository: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- Einführungsvideo (englisch): [uv in 5 minutes](https://www.youtube.com/watch?v=gIqGC1kf9_Y)

Feedback oder Ergänzungswünsche gerne direkt in diesem Repository festhalten.
