# Local AI Discord Bot (Ollama + Mistral + Python)

Ein vollautomatischer, lokal gehosteter Discord-Bot für Windows, der Nachrichten im Chat empfängt und mithilfe eines lokalen Open-Source-Sprachmodells datenschutzfreundlich und in Echtzeit beantwortet.

---

## 1. Über das Projekt

Dieses Projekt ermöglicht es, einen eigenen KI-gesteuerten Discord-Bot zu betreiben, der vollständig lokal auf der eigenen Hardware läuft. Es werden keine kostenpflichtigen oder datenschutzrechtlich bedenklichen Cloud-APIs (wie OpenAI) benötigt. Alle Anfragen werden direkt von der lokalen Grafikkarte und dem Open-Source-Modell *Mistral* verarbeitet.

---

## 2. Voraussetzungen & Downloads

Bevor du startest, lade dir folgende Programme für Windows herunter und installiere sie:

**Python (Version 3.10 oder neuer):**
[Python für Windows herunterladen](https://www.python.org/downloads/)

**Ollama (Die lokale KI-Engine):**
[Ollama für Windows herunterladen](https://ollama.com/download/windows)
(Klicke auf "Manual install")

---

## 3. Schritt-für-Schritt Installation

### Schritt 1: KI-Modell (Mistral) herunterladen und starten

1. Öffne die Windows-Eingabeaufforderung (Drücke die Windows-Taste + R, tippe `cmd` ein und drücke Enter).
2. Gib folgenden Befehl in einem neuen Terminal-Fenster ein, um das Mistral-Modell herunterzuladen und zu starten:

   ```bash
   ollama run mistral
   ```

3. Warte, bis der Download komplett abgeschlossen ist und die KI bereit ist.
4. **Wichtig:** Lass dieses Konsolenfenster geöffnet (du kannst es minimieren). Ollama muss im Hintergrund laufen, damit der Bot Anfragen an die KI senden kann.

---

## 4. Discord Bot & Server erstellen

### Schritt A: Einen eigenen Discord-Server erstellen

Falls du noch keinen eigenen Test-Server hast, auf dem du den Bot testen kannst:

1. Öffne Discord und klicke ganz links in der Server-Leiste auf das **+** Symbol (Server hinzufügen).
2. Wähle "Einen eigenen erstellen" und dann "Für mich und meine Freunde".
3. Gib deinem Server einen Namen (z. B. *KI Test Server*) und klicke auf **Erstellen**.

### Schritt B: Den Bot im Developer Portal einrichten

1. Gehe auf das [Discord Developer Portal](https://discord.com/developers/applications) und logge dich mit deinem Discord-Account ein.
2. Klicke oben rechts auf den blauen Button "Neue Anwendung" (New Application), gib einen Namen ein (z. B. `LocalAIBot`) und klicke auf **Create**.
3. Gehe im linken Menü auf den Reiter **"Bot"**:
   - Klicke rechts auf **"Reset Token"** und kopiere dir den generierten **Token** (eine lange Reihe aus Buchstaben und Zahlen). Gib diesen Token niemals an andere weiter!
   - **Wichtig - Nachrichten-Berechtigungen erlauben:** Scrolle auf dieser Seite etwas nach unten zum Bereich **"Privileged Gateway Intents"**. Setze dort unbedingt das Häkchen bei **"Message Content Intent"**! (Ohne dieses Kästchen darf der Bot den Text von Nachrichten in Chats nicht lesen).
   - Klicke unten auf **"Save Changes"**.
4. **Bot zum eigenen Server einladen:**
   - Gehe links im Menü auf **OAuth2** und dann auf **URL Generator**.
   - Wähle bei *Scopes* das Häkchen bei **bot** aus.
   - Scrolle weiter nach unten zu *Bot Permissions* und wähle **Send Messages** und **Read Message History** aus.
   - Kopiere den generierten Link ganz unten in der Zeile, füge ihn oben in deinen Browser ein, wähle deinen eben erstellten Test-Server aus und klicke auf **Autorisieren**.

---

## 5. Bot-Token in die bot.py eintragen

1. Öffne die Datei `bot.py` mit einem Texteditor (z. B. Notepad).
2. Trage ganz unten im Code deinen in Schritt B kopierten Discord-Token ein:

   ```python
   client.run('DEIN_DISCORD_BOT_TOKEN_HIER')
   ```

3. Speichere die Datei ab.

---

## 6. Projektordner anlegen und Abhängigkeiten installieren

1. Lege auf deinem PC einen Projektordner an und speichere darin die Dateien `requirements.txt` und `bot.py`.
2. Öffne ein **zweites** Konsolenfenster und navigiere in deinen Projektordner. Tipp: Tippe im Windows Explorer oben in die Adresszeile `cmd` ein und drücke Enter, dann öffnet sich ein Terminal im richtigen Ordner.
3. Installiere die benötigten Bibliotheken (`discord.py` für die Discord-Schnittstelle und `requests` für die Kommunikation mit Ollama) mit folgendem Befehl:

   ```bash
   pip install -r requirements.txt
   ```

---

## 7. Den Bot starten (Wichtig: Zwei Konsolen!)

Damit der Bot reibungslos funktioniert, müssen zwei Konsolenfenster parallel laufen:

**Konsole 1 (Das KI-Backend):** Hier läuft dauerhaft Ollama mit dem Befehl:

```bash
ollama run mistral
```

**Konsole 2 (Der Discord-Bot):** Öffne im Windows Explorer den Projektordner, tippe oben in die Adresszeile `cmd` ein, drücke Enter und starte den Bot mit:

```bash
python bot.py
```

Sobald in Konsole 2 die Meldung erscheint (z. B. "Bot ist online und eingeloggt als..."), ist der Bot einsatzbereit.
Gehe in deinen Discord-Server, schreibe dem Bot eine Nachricht oder erwähne ihn. Die lokale KI wird dir direkt antworten!