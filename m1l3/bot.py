import discord
import discord.ext.commands as commands
import random
from botlogic import gen_pass
from moderacao import verificar_mensagem
from voice import entrar_canal_voz
from memes import pegar_meme
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('A')  # Obtém o token do arquivo .env

# Permissões (intents)
intents = discord.Intents.default()
intents.message_content = True

# Criando o bot com prefixo !
bot = commands.Bot(command_prefix="bt ", intents=intents)

# Quando o bot ligar
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando !oi
@bot.command()
async def oi (ctx):
    
    await ctx.send("Oi 👋")
@bot.command()
async def tchau (ctx):

    await ctx.send("Tchau 👋")
@bot.command()
async def dia (ctx):

    await ctx.send("Bom dia 👋")
@bot.command()
async def tarde (ctx):

    await ctx.send("Boa tarde 👋")
@bot.command()
async def senha (ctx):

    await ctx.send("Sua senha é: " + gen_pass(10))
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Chama a função do outro arquivo
    await verificar_mensagem(message)

    if message.content.startswith("!"):
        await message.channel.send(message.content)

    await bot.process_commands(message)
@bot.command()
async def ficar(ctx):
    await entrar_canal_voz(ctx)
@bot.event
async def on_member_join(member):

    canal = None

    # procura canais comuns de boas-vindas
    for c in member.guild.text_channels:
        if c.name in ["geral", "general", "welcome", "boas-vindas"]:
            canal = c
            break

    # se não achar, pega o primeiro canal que o bot pode falar
    if canal is None:
        for c in member.guild.text_channels:
            if c.permissions_for(member.guild.me).send_messages:
                canal = c
                break

    if canal:
        await canal.send(f"oi esse é o meu server bom dia  {member.mention} 😁😀😁😂😂😂😁😀😎😎!")
@bot.command()
async def membros(ctx):
    await ctx.send(f"O servidor tem {ctx.guild.member_count} membros!")


# Coloque seu token aqui
bot.run(token)
