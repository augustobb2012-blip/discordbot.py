import discord
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

engine = pyttsx3.init()


def get_fact():
    base_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data["text"]
    else:
        return "Desculpa, mas não consegui te enviar uma curiosidade."


@bot.command()
async def fact(ctx):
    fact = get_fact()
    await ctx.send(fact)
    speak(fact)


def speak(text: str):
    engine.stop()
    engine.say(text)
    engine.runAndWait()


@bot.command()
async def start(ctx):
    await ctx.send("Ta pronto pra algumas curiosidades?")

bot.run("")
