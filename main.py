import discord
from discord.ext import commands

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Cześć")

@bot.command()
async def bye(ctx, id = 0):
    await ctx.send(bot.get_emoji(id).name)

@bot.command()
async def echo(ctx, messages):
    await ctx.send(messages)

bot.run("MTIzODgwMDY2NDI5Nzk5NjMwOA.GUi-jl.d1TDk2rodmQBiJTOf4obznKcTFNTfPPYzsONGA")
