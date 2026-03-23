import discord
from discord.ext import commands

async def entrar_canal_voz(ctx):
    if ctx.author.voice:
        canal = ctx.author.voice.channel

        if ctx.voice_client is None:
            await canal.connect()
            await ctx.send("Entrei no canal de voz 🎧")
        else:
            await ctx.voice_client.move_to(canal)
            await ctx.send("Mudei para o canal de voz 🎧")
    else:
        await ctx.send("Você precisa estar em um canal de voz.")