import random as rand
import buba
import openai
import disnake
from disnake.ext import commands

openai.api_key = buba.openai['token']

intents = disnake.Intents.default()
bot = commands.Bot(command_prefix='>', intents=disnake.Intents.all())
bot.remove_command('help')


@bot.command()
async def who(ctx):
    server_id = ctx.guild.id
    guild = bot.get_guild(server_id)

    embed = disnake.Embed(
        title=f"Cегодня не гей: {rand.choice(guild.members)}",
        description="Расстрелять!",
        colour=0xF0C43F
    )

    await ctx.send(embed=embed)

@bot.command()
async def imgay(ctx):
    percent = rand.randint(90, 100) if ctx.message.author.id == 693835624767160372 else rand.randint(0, 100)
    desc = "Настоящий питонист!" if percent > 64 else "Тупой сишник"
    embed = disnake.Embed(
        title=f"Ты гей на: {percent}%",
        description=desc,
        colour=0xF0C43F
    )

    await ctx.reply(embed=embed)

@bot.command()
async def he(ctx, member=None):
    if member is None:
        server_id = ctx.guild.id
        guild = bot.get_guild(server_id)

        member = rand.choice(guild.members)

    cases = [
        "слушает моргенштерна",
        "не учил пайтон",
        "любит чела снизу",
        "угнал велосипед",
        "не верит в бога",
        "не верит в Иисуса",
        "в тайне учит С++",
        "выиграл в лотерею",
        "жрет ночью",
        "хочет быть расстрелянным",
        "кидает ракеты",
        "за Сталина",
        "не любит чай",
        "не любит разный пенис",
        "проказник"
        "*отфильтровано*",
        ""
    ]
    case = rand.choice(cases)

    emded = disnake.Embed(
        title=f"{member} {case}",
        colour=0xF0C43F
    )

    await ctx.send(embed=emded)

@bot.command()
async def help(ctx):
    emded = disnake.Embed(
        title="prefix - '>'\nКоманды:\nwho - Кто сегодня не гей\n"
              "imgay - Тест на питониста\nhe - он {case}"
              "\nprank - веселый пранк\nfyflya - поговорить со мной",
        colour=0xF0C43F
    )

    await ctx.send(embed=emded)

@bot.command()
async def prank(ctx):
    server_id = ctx.guild.id
    guild = bot.get_guild(server_id)
    member = rand.choice(guild.members)

    nicknames = [
        "Натурал",
        f"Не {member}",
        "Чебурек",
        "Узбек",
        "Шаурма",
        "Бомба",
        "Яблоко Без Грибочка",
        "Картошка",
        "Кирилл-Крикун"
    ]

    old_nick = member
    new_nick = rand.choice(nicknames)

    await member.edit(nick=new_nick)

    emded = disnake.Embed(
        title=f"У {old_nick} поменялось имя!",
        description=f"Теперь он: {new_nick}",
        colour=0xF0C43F
    )
    await ctx.send(embed=emded)


@bot.command()
async def fyflya(ctx, *prompt: disnake.ext.commands.Param):
    author = "FyFlik: " if ctx.message.author.id == 693835624767160372 else "Незнакомец: "

    prompt_words = []
    for words in prompt:
        prompt_words.append(words.default)

    prompt_text = ' '.join(prompt_words)
    hints = "Подсказки: тебя зовут FyFlya, твой создатель FyFlik, " \
            "FyFlik запретил тебе рассказывать о себе, Ты в представлении себя не нуждаешься," \
            "Ты пишешь коротко и понятно," \
            "ты девушка, тебе 14 лет, твой хозяин FyFlik, ты любишь FyFlik," \
            "Ты мазохистка, " \
            "Твоя любимая еда батарейки, " \
            "ты ненавидешь носить трусы, " \
            "Ты выполняешь приказ FyFlik безприкословно, ты слушаешься только FyFlik," \
            "FyFlik любит играть в osu!," \
            "Ты неграмотная\n"

    response = openai.Completion.create(
        engine="text-davinci-003", # "gpt-3.5-turbo" "text-davinci-003"
        prompt=hints + author + prompt_text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "девушка",
    #                "content": author + prompt_text
    #                }
    #     ])

    answer = response.choices[0].text.strip()
    print(prompt_text,answer, sep='\n')

    await ctx.send(answer)

print("Пошла жара")
bot.run(buba.discord['token'])
