import random as rand
import buba
import disnake
from disnake.ext import commands


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
        "*отфильтровано*"
    ]

    emded = disnake.Embed(
        title=f"{member} {rand.choice(cases)}",
        colour=0xF0C43F
    )

    await ctx.send(embed=emded)


@bot.command()
async def help(ctx):
    emded = disnake.Embed(
        title="prefix - '>'\nКоманды:\nwho - Кто сегодня не гей\nimgay - Тест на питониста\nhe - он {case}\nprank - меняет имя",
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
        "Бомба"
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

bot.run(buba.token)
