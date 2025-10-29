# Permission denied Fehler beheben 

Diese Anleitung beschreibt Schritt für Schritt, wie die Installation von **uv** auf einem Mac gelingt, wenn im Terminal eine Meldung wie  `Permission denied` oder  
`unable to create receipt directory at ~/.config/uv`  
erscheint.


---

## 1️⃣ Terminal öffnen

Kurzweg:
- Spotlight mit `⌘ + Leertaste` öffnen  
- „Terminal“ tippen  
- **Return** drücken

---

## 2️⃣ Installation von uv starten

**Zweck:** Installer herunterladen und ausführen.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Wenn keine Fehlermeldung erscheint, ist die Installation abgeschlossen (später noch Schritt 6 „Prüfen“ ausführen).  
Bei **„Permission denied“** weiter mit Schritt 3.

---

## 3️⃣ Häufigste Ursache: fehlende Rechte in `.zshrc` oder `.config`

Im Folgenden werden Rechte für **`~/.zshrc`** und **`~/.config`** repariert.  

### 3a) `.zshrc` gehört wieder dem aktuellen Account

**Zweck:** Eigentum der Datei `~/.zshrc` auf den aktuellen Account setzen, damit der Installer sie anpassen darf.

```bash
chown $(whoami) ~/.zshrc 2>/dev/null || true
```

> Hinweis: Wenn die Datei nicht existiert, ist das unkritisch – dann eine leere Datei anlegen (siehe nächster Befehl).

**Zweck:** Sicherstellen, dass `~/.zshrc` existiert (leere Datei anlegen, falls nicht vorhanden).

```bash
touch ~/.zshrc
```

**Zweck:** Lese- und Schreibrechte für die Datei setzen.

```bash
chmod u+rw ~/.zshrc
```

---

### 3b) `.config` ist nicht gesperrt und betretbar

**Zweck:** Status des Konfigurationsordners prüfen (Owner, Flags, Rechte).

```bash
ls -ldO ~/.config ~/.config/uv 2>/dev/null
```

> In der Spalte „Owner“ sollte der eigene Benutzername stehen.  
> In der Spalte „Flags“ darf **kein** `uchg` stehen (Schreibschutz).

**Zweck:** Möglichen macOS-Schreibschutz (Flag `uchg`) entfernen.

```bash
chflags -R nouchg ~/.config 2>/dev/null || true
```

**Zweck:** Sicherstellen, dass im Ordner gelesen/geschrieben/„hineingegangen“ werden kann.  
(Wichtig: ohne **x** auf dem Ordner schlägt `mkdir` fehl.)

```bash
chmod u+rwx ~/.config
```

**Zweck:** Zielordner für uv anlegen (falls nicht vorhanden).

```bash
mkdir -p ~/.config/uv
```

---

## 4️⃣ Installer erneut ausführen

**Zweck:** Installation mit reparierten Rechten wiederholen.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 5️⃣ Shell-Konfiguration neu laden

**Zweck:** Änderungen sofort aktivieren.

```bash
source ~/.zshrc
```

---

## 6️⃣ Installation prüfen

**Zweck:** Kontrolle, ob uv verfügbar ist.

```bash
uv --version
```

> Erscheint eine Versionsnummer, ist die Installation erfolgreich abgeschlossen. 🎉

---

# 🆘 Wenn es trotz alledem **weiterhin** scheitert

Mitunter werden alle Schritte korrekt befolgt – und **`mkdir` scheitert trotzdem**.  
Dann liegt meist **eine der folgenden Sonderursachen** vor. Für jede Ursache gibt es einen **einzelnen** Prüf- oder Reparaturschritt.

---

### A) Eigentümer ist nicht der aktuelle Account (ohne Adminrechte nicht änderbar)

**Zweck:** Eigentümer von `~/.config` eindeutig prüfen.

```bash
stat -f "%Su %N" ~/.config
```

- Gibt der Befehl **nicht** den aktuellen Benutzernamen zurück, gehört der Ordner einem anderen Account.  
- Ohne Adminrechte lässt sich das **nicht** umstellen. In Lehr- bzw. Campusumgebungen ist das ein typischer IT-Policy-Fall.

**Workaround ohne Rechteänderung:** uv auf einen **benutzer­eigenen Konfigurationspfad** umleiten.

**Zweck:** Eigenen Config-Pfad definieren (dauerhaft).

```bash
echo 'export XDG_CONFIG_HOME="$HOME/.config-user"' >> ~/.zshrc
```

**Zweck:** Zielordner anlegen.

```bash
mkdir -p ~/.config-user/uv
```

**Zweck:** Shell neu laden und Installer erneut ausführen.

```bash
source ~/.zshrc
```

**Zweck:** Installation mit neuem Config-Pfad durchführen.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> Damit werden **alle** Konfigurationsdateien in `~/.config-user` abgelegt – völlig ohne Eingriffe in den gesperrten `~/.config`.

---

### B) `.zshrc` ist ein Ordner oder Link statt einer Datei

**Zweck:** Typ der Ressource feststellen.

```bash
file ~/.zshrc
```

- Meldet der Befehl „directory“ oder „symbolic link“, kann der Installer die „Datei“ nicht bearbeiten.  
- In diesem Fall muss die Struktur korrigiert werden (z. B. Ordner umbenennen).  

**Zweck:** (Nur wenn `.zshrc` fälschlich ein Ordner ist) Sichern und leere Datei anlegen.

```bash
mv ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d-%H%M%S)
```

**Zweck:** Leere Konfigurationsdatei erstellen.

```bash
touch ~/.zshrc
```

**Zweck:** Rechte setzen.

```bash
chmod u+rw ~/.zshrc
```

Anschließend erneut zu **Schritt 4** (Installer ausführen).

---

### C) Fehlendes Ausführungsrecht auf dem Home-Ordner selbst

Ohne **x** auf dem Home-Ordner kann kein Unterordner betreten werden.

**Zweck:** Rechte des Home-Ordners prüfen.

```bash
ls -ld ~
```

- In der ersten Spalte sollte bei den **user-Rechten** ein **x** enthalten sein (z. B. `drwx------`).  
- Fehlt dieses **x**, ist „Durchschreiten“ nicht erlaubt.

**Zweck:** Ausführungsrecht für den Benutzer setzen (nur falls das **x** fehlt).

```bash
chmod u+x ~
```

Danach erneut zu **Schritt 4** (Installer ausführen).

---

## 💡 Hintergrundwissen

- **uv** installiert in `~/.local/bin` und nutzt `~/.config/uv` für interne Dateien.  
- `mkdir` schlägt fehl, wenn:
  - der **Parent-Ordner** nicht dem aktuellen Account gehört,  
  - ein **Schreibschutz-Flag (`uchg`)** gesetzt ist,  
  - dem Ordner das **Ausführungsrecht (x)** fehlt,  
  - die erwartete **Datei** (`~/.zshrc`) in Wirklichkeit ein **Ordner/Link** ist.  
- Der Abschnitt „🆘 Wenn es weiterhin scheitert“ deckt diese Sonderfälle ab – ohne Administratorrechte.

---

## 🧭 Zusammenfassung

| Schritt | Aufgabe |
|---|---|
| 1 | Terminal öffnen |
| 2 | uv installieren |
| 3 | Rechte in `.zshrc` und `.config` reparieren |
| 4 | Installer erneut ausführen |
| 5 | Shell neu laden |
| 6 | Version prüfen |
| 🆘 | Bei hartnäckigen Fehlern: A/B/C prüfen und die jeweils **einzelnen** Befehle ausführen |

Nach diesen Schritten sollte die Installation auch in den gezeigten Problemfällen funktionieren.