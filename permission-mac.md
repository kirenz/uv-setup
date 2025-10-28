# Permission denied Fehler beheben (macOS)


## 1️⃣ Terminal öffnen

- Spotlight öffnen mit `⌘ + Leertaste`  
- „Terminal“ eingeben  
- **Return** drücken

---

## 2️⃣ uv installieren

Diesen Befehl **kopieren**, ins Terminal einfügen und **Return** drücken:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 3️⃣ Wenn eine „Permission denied“-Fehlermeldung erscheint

Dann fehlt nur die Berechtigung, damit der Installer die richtigen Ordner und Dateien anlegen darf.  
In diesem Fall bitte nacheinander diese Befehle ausführen (jeweils einzeln mit **Return** bestätigen):

```bash
mkdir -p ~/.config/fish/conf.d
```

```bash
chown $(whoami) ~/.zshrc 2>/dev/null || true
```

```bash
chown -R $(whoami) ~/.config/fish
```

Danach einfach den Installationsbefehl **noch einmal** ausführen:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 4️⃣ Shell neu laden

Damit die Änderungen aktiv werden:

```bash
source ~/.zshrc
```

---

## 5️⃣ Installation testen

```bash
uv --version
```

Wenn eine Versionsnummer erscheint → **alles funktioniert! 🎉**

---

## 💡 Kurz erklärt

- **uv** wird automatisch im Benutzerverzeichnis installiert (`~/.local/bin`).  
- Die Befehle oben stellen sicher, dass das Installationsprogramm in die richtigen Dateien schreiben darf.  
- Es ist **kein Administrator-Zugriff** nötig.  

---

### 🧭 Zusammenfassung

| Schritt | Aufgabe |
|----------|----------|
| 1 | Terminal öffnen |
| 2 | Installationsbefehl ausführen |
| 3 | Falls nötig: kurze Rechtekorrektur |
| 4 | Shell neu laden |
| 5 | Version prüfen |

Fertig ✅  
uv ist nun installiert und kann verwendet werden.