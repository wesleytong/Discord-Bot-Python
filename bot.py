import discord
import asyncio
import random
import botToken
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='-', description=description)
print(discord.__version__)
disc = discord.Client


on = False
f = 0
uwuFile = open("uwuCount.txt", "r")
uwuDict = {}
for x in uwuFile:
    str1 = x.split(', ')
    uwuDict[str(str1[0])] = str(str1[1])


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    global on
    str2 = message.content.lower()
    global uwuDict

    if str2.find('uwu') >= 0 and message.author != bot.user:
        print(message.content)
        if(str(message.author.id) in uwuDict):
            uwuDict[str(message.author.id)] = str(int(uwuDict.get(str(message.author.id))) + 1)
        else:
            uwuDict[str(message.author.id)] = str(1)

        print(uwuDict)
        f = open("uwuCount.txt", "w")
        for i in uwuDict:
            f.write(i + ', ' + uwuDict[i] + '\n')
        f.close()

    if message.author == bot.user:
        return

    if message.content.startswith('<@'):
        await message.channel.send(message.content)
        await message.channel.send(message.content)
    await bot.process_commands(message)


@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=1)
    f = open('deletedTxts.txt', 'a')
    async for message in ctx.channel.history(limit=amount):
        f.write(message.content)
        f.write('\n')
    f.close()
    await ctx.channel.purge(limit=amount)
    await ctx.send('Done!', delete_after=5)


@bot.command()
async def commands(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('```ur gay```', delete_after=30)


@bot.command()
async def p(ctx, name: str, amount=3.0):
    await ctx.channel.purge(limit=1)
    if(amount < 1.0):
        amount = 1.0
    if(amount > 10.0):
        amount = 1000.0
    for i in range(0, int(amount)):
        await ctx.send(name)
        await asyncio.sleep(.5,2)

@bot.command()
async def k(ctx):
    await ctx.channel.purge(limit=1)
    async with ctx.typing():
        await asyncio.sleep(600)
        await ctx.send('k.', delete_after=60)

@bot.command()
async def pp(ctx):
    await ctx.channel.purge(limit=1)
    global on
    on = not on


@bot.command()
async def summon(ctx):
    await ctx.send('In progress...', delete_after=10)
    # voice_client = bot.get_channel()
    # try:
    #     voice_client = await ctx.message.author.voice.channel.connect()
    # except discord.ext.commands.errors.CommandInvokeError:
    #     print('Connect')
    # except discord.errors.ClientException:
    #     voice_client.disconnect()
    #     voice_client = await ctx.message.author.voice.channel.connect()

@bot.command()
async def move(ctx, amount: int, userId=221417504944160770):
    await ctx.channel.purge(limit=1)
    global f
    voicechannels = ctx.guild.voice_channels

    f = 0
    while f != 1:
        count = random.randint(0,amount-1)
        print('Moving!')
        print(count)
        await ctx.guild.get_member(userId).edit(voice_channel=voicechannels[count])
        await asyncio.sleep(1)


@bot.command()
async def stoppls(ctx):
    await ctx.channel.purge(limit=1)
    global f
    f = 1

@bot.command()
async def spam(ctx, userId=101389477888430080, msg='', amount=0):
    await ctx.channel.purge(limit=1)
    messagesSent = 0;
    user = ctx.guild.get_member(userId)
    if(user.dm_channel == None):
        await user.create_dm()
    dm= user.dm_channel
    while messagesSent < amount:
        await asyncio.sleep(.5)
        await dm.send(msg)
        messagesSent += 1

@bot.command()
async def banish(ctx, userId=221417504944160770):
    await ctx.channel.purge(limit=1)
    voicechannels = ctx.guild.voice_channels
    await ctx.guild.get_member(userId).edit(voice_channel=voicechannels[8])
    f = 0
    while f != 1:
        # print(await ctx.guild.get_member(userId).voice.channel.id)
        # if(await ctx.guild.get_member(userId).voice.channel.id != 564578778077069312):
        #     print('true')
        #     await ctx.guild.get_member(userId).edit(voice_channel=voicechannels[8])
        print('Banished!')
        await ctx.guild.get_member(userId).edit(voice_channel=voicechannels[8])
        await asyncio.sleep(1)

@bot.command()
async def uwuCount(ctx):
    await ctx.channel.purge(limit=1)
    global uwuDict
    for i in uwuDict:
        await ctx.channel.send('<@' + i + '>' + ' : ' + uwuDict[i] + ' degen messages')




bot.run(botToken.YOUR_TOKEN)
