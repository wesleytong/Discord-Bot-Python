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
first = 0
second = 0
inHouseStatus = 0
poolOpenStatus = False
inHousePool = []
inHouseQueue =[]
inHouseTeam1 = []
inHouseTeam2 = []
picking = False
team1Pick = False
team2Pick = False
teamPicks = [team1Pick, team2Pick]
teams = [inHouseTeam1, inHouseTeam2]
# draftingBans1 = False
# draftingBans1Inc = 2
team1Champs = ''
team1Bans = ''
team2Champs = ''
team2Bans = ''
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
    global team1Pick
    global team2Pick
    global picking
    # global draftingBans1
    # global draftingBans1Inc
    # global team1Champs
    # global team1Bans
    # global team2Champs
    # global team2Bans
    facts = ["tru","facts","fact","fax","factual information","ngl","true","truth","on god","no cap","right blake","right blake?","tru?"]
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

    if message.content.lower() in facts:
        await message.channel.send("on god no cap")


    # if message.content.startswith('<@'):
    #     await message.channel.send(message.content)
    #     await message.channel.send(message.content)

    if picking == True and message.content.startswith('<@'):
        playerId = int(message.content[3:len(message.content) - 1])
        if(message.author.id == teams[first][0] and teamPicks[first] == True):
            if(playerId in inHousePool):
                addPlayerToTeam(playerId, first)
                removePlayerPool(playerId)
                teamPicks[first] = False
                teamPicks[second] = True
                await message.channel.send('Team ' + str(second+1) + ' Captain please pick a player')
            else:
                await message.channel.send('Player is not part of the pool, please pick again')
        if (message.author.id == teams[second][0] and teamPicks[second] == True):
            if (int(playerId) in inHousePool):
                addPlayerToTeam(playerId, second)
                removePlayerPool(playerId)
                teamPicks[second] = False
                teamPicks[first] = True
                await message.channel.send('Team ' + str(first+1) + ' Captain please pick a player')
            else:
                await message.channel.send('Player is not part of the pool, please pick again')
        if(len(inHouseTeam1) + len(inHouseTeam2) == 10):
            picking = False
            teamPicks[first] = False
            teamPicks[second] = False

    # if draftingBans1 == True:
    #     if(message.author.id == teams[draftingBans1Inc % 2][0]):
    #         if draftingBans1Inc % 2 == 0:
    #             team1Bans += message.content + ' '
    #         else:
    #             team2Bans += message.content + ' '
    #         if(len(team2Bans.split(' ', 2)) >= 3):
    #             draftingBans1 = False
    #         else:
    #             message.channel.send('Team ' + str(draftingBans1Inc % 2 + 1) + 'please your ban')


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
    await ctx.send('```Commands go here```', delete_after=30)

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
async def spam(ctx, msg='', amount=0, userId=101389477888430080,):
    # await ctx.channel.purge(limit=1)
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
    await ctx.channel.purge(limit=1)
    if (inHouseStatus == 1):
        if(poolOpenStatus == False):
            await ctx.channel.send('No players can join at the moment')
        if(checkIfIn(ctx.message.author.id) == True):
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
        if(len(inHouseQueue) > 0):
            addPlayerPool(inHouseQueue[0])
            removePlayerQueue(inHouseQueue[0])

    else:
        await ctx.channel.send('No in house in progress')

@bot.command()
async def players(ctx):
    if(inHouseStatus == 1):
        await ctx.channel.send('Players in pool: ')
        for i in inHousePool:
            await ctx.channel.send('<@' + str(i) + '>')
            await asyncio.sleep(1)

        await ctx.channel.send('Players in team 1: ')
        for i in inHouseTeam1:
            await ctx.channel.send('<@' + str(i) + '>')
            await asyncio.sleep(1)

        await ctx.channel.send('Players in team 2: ')
        for i in inHouseTeam2:
            await ctx.channel.send('<@' + str(i) + '>')
            await asyncio.sleep(1)

        await ctx.channel.send('Players in queue:')
        for i in inHouseQueue:
            await ctx.channel.send('<@' + str(i) + '>')
            await asyncio.sleep(1)
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

@bot.command()
async def startPicks(ctx):
    global first
    global second
    global picking
    if(len(inHouseTeam1) == 0 and len(inHouseTeam2) == 0):
        await ctx.channel.send('You have not selected any team captains')
    # first = random.randint(0,1)
    # if(first == 0):
    #     second = 1
    # else:
    #     first = 1
    first = 0
    second = 1
    await ctx.channel.send('Team ' + str(first + 1) + ' is picking first')
    teamPicks[first] = True
    picking = True

@bot.command()
async def draft(ctx):
    # global draftingBans1
    # draftingBans1 = True

    await ctx.channel.send(
        '```Team 1 Bans: ' + team1Bans + '\n \n'
                                         'Team 2 Bans: ' + team2Bans + '\n \n'
                                                                       'Team 1 Picks: ' + team1Champs + '\n \n'
                                                                                                        'Team 2 Picks: ' + team2Champs + '```'

    )

    # ctx.channel.send('Team 1 please type the name of your first champion ban')
    
@bot.command()
async def pick(ctx, pick = ''):
    global team1Champs
    global team2Champs
    if(ctx.message.author.id == inHouseTeam1[0]):
        team1Champs += pick + ' '
    if (ctx.message.author.id == inHouseTeam2[0]):
        team2Champs += pick + ' '
    await ctx.channel.send(
        '```Team 1 Bans: ' + team1Bans + '\n \n'
                                         'Team 2 Bans: ' + team2Bans + '\n \n'
                                                                       'Team 1 Picks: ' + team1Champs + '\n \n'
                                                                                                        'Team 2 Picks: ' + team2Champs + '```'

    )

@bot.command()
async def ban(ctx, pick = ''):
    global team1Bans
    global team2Bans
    if (ctx.message.author.id == inHouseTeam1[0]):
        team1Bans += pick + ' '
    if (ctx.message.author.id == inHouseTeam2[0]):
        team2Bans += pick + ' '
    await ctx.channel.send(
        '```Team 1 Bans: ' + team1Bans + '\n \n'
                                         'Team 2 Bans: ' + team2Bans + '\n \n'
                                                                       'Team 1 Picks: ' + team1Champs + '\n \n'
                                                                                                        'Team 2 Picks: ' + team2Champs + '```'

    )

@bot.command()
async def reset(ctx, reset=0):
    global inHousePool
    global inHouseTeam1
    global inHouseTeam2
    global team1Bans
    global team1Champs
    global team2Bans
    global team2Champs
    if(reset == 0):
        resetSoft()
    else:
        inHousePool = []
        inHouseQueue = []
        inHouseTeam1 = []
        inHouseTeam2 = []
        team1Champs = ''
        team1Bans = ''
        team2Champs = ''
        team2Bans = ''

def checkIfIn(id:int):
    if(id in inHouseQueue or id in inHousePool or id in inHouseTeam1 or id in inHouseTeam2):
        return True
    else:
        return False


def resetSoft():
    global inHousePool
    global inHouseTeam1
    global inHouseTeam2
    global team1Bans
    global team1Champs
    global team2Bans
    global team2Champs

    for i in inHouseTeam1:
        addPlayerPool(i)
        removePlayerTeam1(i)
    for i in inHouseTeam2:
        addPlayerPool(i)
        removePlayerTeam2(i)
    team1Champs = ''
    team2Champs = ''
    team1Bans = ''
    team2Bans = ''

def addPlayerToTeam(id:int, team:int):
    if(team == 0):
        addPlayerTeam1(id)
    else:
        addPlayerTeam2(id)

def addPlayerTeam1(id:int):
    inHouseTeam1.append(id)

def addPlayerTeam2(id:int):
    inHouseTeam2.append(id)

def addPlayerPool(id:int):
    inHousePool.append(id)
    # for i in range(len(inHousePool)):
    #     if(inHousePool[i] == ''):
    #         inHousePool.pop(i)
    #         inHousePool.insert(i, id)
    #         break

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











bot.run(botToken.token)
