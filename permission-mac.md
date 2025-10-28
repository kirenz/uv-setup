# Permission denied Fehler beheben (macOS, zsh)

Diese Anleitung zeigt, wie die Installation von **uv** auf einem Mac funktioniert, wenn im Terminal eine Meldung wie `Permission denied` erscheint.  


---

## 1️⃣ Terminal öffnen

- Spotlight öffnen mit `⌘ + Leertaste`  
- „Terminal“ eingeben  
- **Return** drücken

---

## 2️⃣ uv installieren

Diesen Befehl **komplett kopieren**, im Terminal einfügen und **Return** drücken:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 3️⃣ Wenn eine „Permission denied“-Fehlermeldung erscheint

Das bedeutet, dass der Installer keine Schreibrechte für bestimmte Konfigurationsdateien hat (meist `~/.zshrc`).  
In diesem Fall nacheinander diese Befehle ausführen (jeweils einzeln mit **Return** bestätigen):

```bash
chown $(whoami) ~/.zshrc 2>/dev/null || true
```

```bash
chmod u+rw ~/.zshrc
```

Dann den Installationsbefehl **noch einmal** ausführen:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 4️⃣ Shell neu laden

Damit die Änderungen sofort wirksam werden:

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
- Die kurzen Befehle oben stellen sicher, dass das Installationsprogramm in `~/.zshrc` schreiben darf.  
