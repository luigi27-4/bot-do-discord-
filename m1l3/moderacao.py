import re
from datetime import timedelta

# 👑 Seu ID (não será punido, mas será censurado)
DONO_ID = 412347257233604609

# 📜 Lista de palavrões
palavras_proibidas = [
    "porra", "caralho", "fdp", "filho da puta", "filha da puta",
    "puta", "puto", "putinha", "putaria",
    "vagabundo", "vagabunda",
    "otario", "otária", "idiota", "imbecil",
    "babaca", "trouxa", "arrombado", "arrombada",
    "corno", "corna","cu", "buceta", "xereca", "xota",
    "piroca", "rola", "pau", "pinto",
    "viado", "viadinho",
    "retardado", "lixo", "escroto", "escrota",
    "vai se foder",
    "vai tomar no cu",
    "vai pra puta que pariu",
    "tomar no cu",
    "se foder"
]

infrações = {}

def censurar(texto):
    texto_censurado = texto
    for palavra in palavras_proibidas:
        padrao = re.compile(re.escape(palavra), re.IGNORECASE)
        texto_censurado = padrao.sub("*" * len(palavra), texto_censurado)
    return texto_censurado

async def verificar_mensagem(message):
    global infrações

    if message.author.bot:
        return

    mensagem_original = message.content
    mensagem_censurada = censurar(mensagem_original)

    if mensagem_original != mensagem_censurada:
        await message.delete()

        await message.channel.send(
            f"{message.author.mention}: {mensagem_censurada}"
        )

        user_id = message.author.id

        # 👑 Se for você, para aqui (não conta infração)
        if user_id == DONO_ID:
            return

        if user_id not in infrações:
            infrações[user_id] = 0

        infrações[user_id] += 1

        if infrações[user_id] >= 2:
            await message.author.timeout(
                timedelta(hours=1),
                reason="2 mensagens impróprias"
            )

            await message.channel.send(
                f"{message.author.mention} foi suspenso por 1 hora 🚫"
            )

            infrações[user_id] = 0