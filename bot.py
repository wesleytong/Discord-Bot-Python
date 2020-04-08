import discord
import asyncio
import random
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='-', description=description)
print(discord.__version__)
disc = discord.Client


on = False
f = 0
inHouseStatus = 0
poolOpenStatus = False
inHousePool = []
inHouseQueue =[]
inHouseTeam1 = []
inHouseTeam2 = []
uwuFile = open("uwuCount.txt", "r")
uwuDict = {}
for x in uwuFile:
    str1 = x.split(', ')
    uwuDict[str(str1[0])] = str(str1[1])

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# @bot.event
# async def on_typing(channel,msg, when):
#     await channel.send('Stop typing')

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

@bot.command()
async def superhere(ctx):
    membersListId = ctx.channel.members
    for i in membersListId:
        await ctx.channel.send('<@' + str(i.id) + '>')

@bot.command()
async def inhouse(ctx, status=1):
    global inHouseStatus
    global poolOpenStatus
    if(inHouseStatus == 0 and status==1):
        await ctx.channel.send('Starting in house session...')
        poolOpenStatus = True
    elif(status==0):
        await ctx.channel.send('Ending in house session...')
    elif(inHouseStatus == 1 and status != 0):
        await ctx.channel.send('In house in progress...')
    elif (inHouseStatus != 1 and status != 1):
        await ctx.channel.send('No in house in progress...')
    inHouseStatus = status

@bot.command()
async def forcejoin(ctx):
    for i in ctx.message.mentions:
        addPlayerPool(i.id)


@bot.command()
async def join(ctx):
    global poolOpenStatus
    userIn = checkIfIn(ctx.message.author.id)
    await ctx.channel.purge(limit=1)
    if (inHouseStatus == 1):
        if(poolOpenStatus == False):
            await ctx.channel.send('No players can join at the moment')
        if(userIn == True):
            await ctx.channel.send('You\'re already in dummy')
        elif ctx.message.author != bot.user and len(inHousePool) <= 9 and ctx.message.author.id not in inHousePool:
            await ctx.channel.send('Adding ' + '<@' + str(ctx.message.author.id) + '> to user pool')
            addPlayerPool(ctx.message.author.id)
            if(len(inHousePool) == 10):
                poolOpenStatus = False
                ctx.channel.send('The user pool is now closed, adding ' + '<@' + str(ctx.message.author.id) + '> to the queue')
                addPlayerQueue(ctx.message.author.id)
                await ctx.channel.send('Adding ' + '<@' + str(ctx.message.author.id) + '> to queue')
    else:
        await ctx.channel.send('No in house in progress')

@bot.command()
async def forceleave(ctx):
    for i in ctx.message.mentions:
        removePlayerPool(i.id)
        removePlayerTeam1(i.id)
        removePlayerTeam2(i.id)

@bot.command()
async def leave(ctx):
    await ctx.channel.purge(limit=1)
    if(inHouseStatus == 1):
        removePlayerPool(ctx.message.author.id)
        removePlayerTeam1(ctx.message.author.id)
        removePlayerTeam2(ctx.message.author.id)
        await ctx.channel.send('Removing ' + '<@' + str(ctx.message.author.id) + '>')

    else:
        await ctx.channel.send('No in house in progress')

@bot.command()
async def players(ctx):
    if(inHouseStatus == 1):
        await ctx.channel.send('Players in pool: ')
        for i in inHousePool:
            await ctx.channel.send('<@' + str(i) + '>')

        await ctx.channel.send('Players in team 1: ')
        for i in inHouseTeam1:
            await ctx.channel.send('<@' + str(i) + '>')

        await ctx.channel.send('Players in team 2: ')
        for i in inHouseTeam2:
            await ctx.channel.send('<@' + str(i) + '>')

        await ctx.channel.send('Players in queue:')
        for i in inHouseQueue:
            await ctx.channel.send('<@' + str(i) + '>')
    else:
        await ctx.channel.send('No in house in progress')

@bot.command()
async def captains(ctx):
    captains = ctx.message.mentions

    if(len(captains) > 2):
        await ctx.channel.send('You included too many captains, only the first two will be assigned')
    elif(len(captains) < 2):
        await ctx.channel.send('You didn\'t include enough captains')
    elif(captains[0].id in inHousePool and captains[1].id in inHousePool):
        addPlayerTeam1(captains[0].id)
        addPlayerTeam2(captains[1].id)
        removePlayerPool(captains[0].id)
        removePlayerPool(captains[1].id)
    else:
        await ctx.channel.send('One or more of the captains you selected are not part of the pool and therefore were not added')

def checkIfIn(id:int):
    if(id in inHouseQueue or id in inHousePool or id in inHouseTeam1 or id in inHouseTeam2):
        return True
    else:
        return False

def addPlayerTeam1(id:int):
    inHouseTeam1.append(id)

def addPlayerTeam2(id:int):
    inHouseTeam2.append(id)

def addPlayerPool(id:int):
    inHousePool.append(id)

def addPlayerQueue(id: int):
    inHouseQueue.append(id)

def removePlayerTeam1(id: int):
    if(id in inHouseTeam1):
        inHouseTeam1.remove(id)

def removePlayerTeam2(id: int):
    if (id in inHouseTeam2):
        inHouseTeam2.remove(id)

def removePlayerPool(id: int):
    if (id in inHousePool):
        inHousePool.remove(id)

def removePlayerQueue(id: int):
    if (id in inHouseQueue):
        inHouseQueue.remove(id)











bot.run('Njc2MzM0MTA4Nzc4OTU0Nzcx.XowYnQ.PBNyQQ6z_fgwbmTlei7d8174njY')
