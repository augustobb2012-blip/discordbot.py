import discord
from discord.ext import commands
import requests
import pyttsx3

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Inicializando a síntese de voz
engine = pyttsx3.init()


# Busca uma curiosidade na API
def get_fact():
    base_url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(base_url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data["text"]

        return "Desculpa, mas não consegui te enviar uma curiosidade."

    except requests.RequestException:
        return "Não foi possível conectar à API."


# Faz o bot falar uma mensagem
def speak(text: str):
    engine.stop()
    engine.say(text)
    engine.runAndWait()


# Comando para receber uma curiosidade
@bot.command()
async def fact(ctx):
    curiosity = get_fact()
    await ctx.send(curiosity)
    speak(curiosity)


# Comando para iniciar o bot
@bot.command()
async def start(ctx):
    await ctx.send("Tá pronto pra algumas curiosidades?")


# Inicia o bot
bot.run("")
