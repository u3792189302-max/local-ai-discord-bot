# Local AI Discord Bot (Ollama + Mistral + Python)

Ein lokal gehosteter Discord-Bot, der Nachrichten im Chat empfängt und mithilfe eines lokalen Sprachmodells (Mistral via Ollama) automatisiert beantwortet.

---

## Features
- 100 % Lokal & Datenschutzfreundlich: Alle KI-Berechnungen laufen lokal ab, es werden keine Daten an externe Cloud-Dienste (wie OpenAI) gesendet.
- Hardware-Beschleunigt: Die KI nutzt für schnelle Antwortzeiten direkt die lokale Grafikkarte (NVIDIA RTX GPU).
- Vollautomatisiert: Der Bot liest eingehende Chat-Nachrichten und antwortet in Echtzeit über das Discord Gateway Protocol.

---

## Technologien & Voraussetzungen

### Systemvoraussetzungen
- Betriebssystem: Windows 10/11 oder Linux
- Python: Version 3.10 oder neuer
- Ollama: Lokal installiert mit geladenem Modell mistral

### Verwendete Python-Bibliotheken
- discord.py – Schnittstelle zur Discord API
- requests – REST-API Kommunikation mit Ollama

---

## Schritt-für-Schritt Installation & Start

### 1. KI-Backend vorbereiten (Ollama)
Stelle sicher, dass Ollama installiert ist, und starte das Mistral-Modell in der Konsole:
```bash
ollama run mistral