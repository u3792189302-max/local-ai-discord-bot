import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f' Bot ist online und eingeloggt als {client.user}!')

@client.event
async def on_message(message):
    # Verhindere, dass der Bot sich selbst antwortet
    if message.author == client.user:
        return

    print(f"Empfangene Nachricht: {message.content}")

    # Sofortige Test-Antwort in Discord
    await message.channel.send(f" Nachricht empfangen! Sende an Ollama: {message.content}")

    try:
        # Anfrage an Ollama senden
        res = requests.post('http://127.0.0.1:11434/api/generate', json={
            "model": "mistral",
            "prompt": message.content,
            "stream": False
        })
        
        reply = res.json().get('response', 'Keine Antwort von KI erhalten.')
        await message.channel.send(reply)

    except Exception as e:
        print(f"Fehler bei Ollama: {e}")
        await message.channel.send(f" Fehler bei der KI-Anfrage: {e}")

client.run('DEIN_BOT_TOKEN_HIER')