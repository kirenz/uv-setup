# Permission denied Fehler beheben (Windows)


Diese Anleitung beschreibt die **kurzeste und sicherste Methode**, um **uv** mit **Git Bash** zu installieren.  
Es sind keine Administratorrechte nötig und keine Änderungen am System.

---

## 🪄 Ziel

Am Ende soll im Terminal der Befehl  
```bash
uv --version
```  
eine Versionsnummer anzeigen.

---

## 1️⃣ Git Bash öffnen

- In der Windows-Suche „Git Bash“ eingeben  
- Git Bash starten (schwarzes Terminalfenster mit `$` am Anfang)

---

## 2️⃣ uv installieren

Diesen Befehl **komplett kopieren**, in Git Bash einfügen und **Enter** drücken:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> Der Installer lädt **uv** herunter und installiert es automatisch im Benutzerverzeichnis.

---

## 3️⃣ Shell neu laden

Damit uv sofort nutzbar ist:

```bash
source ~/.bashrc 2>/dev/null || source ~/.profile 2>/dev/null || true
```

> Falls keine Fehlermeldung erscheint, ist alles gut.  
> Dieser Befehl sorgt dafür, dass die Änderungen am `PATH` aktiv werden.

---

## 4️⃣ Installation prüfen

```bash
uv --version
```

Wenn eine Versionsnummer erscheint → **uv ist erfolgreich installiert 🎉**

---

## 💡 Wenn uv nicht gefunden wird

Falls die Meldung  
```
bash: uv: command not found
```
erscheint, liegt das meist daran, dass der Installationspfad noch nicht im `PATH` ist.

Dann diesen Befehl ausführen:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Danach Git Bash **neu starten** und nochmals testen:

```bash
uv --version
```

---

## 🧠 Erklärung

- uv wird im Ordner `~/.local/bin` installiert (das ist z. B. `C:\Users\<Name>\.local\bin`).  
- Keine Adminrechte nötig, kein Eingriff ins System.  
- Funktioniert zuverlässig in Git Bash, zsh oder WSL.

---

## 🧭 Zusammenfassung

| Schritt | Aufgabe |
|----------|----------|
| 1 | Git Bash öffnen |
| 2 | Installationsbefehl ausführen |
| 3 | Shell neu laden |
| 4 | Version prüfen |
| 5 | (Optional) PATH ergänzen, falls nötig |

Danach steht **uv** sofort zur Verfügung und kann verwendet werden.