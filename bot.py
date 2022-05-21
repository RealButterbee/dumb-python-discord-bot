# Your code here
# bot.py
import os
import discord
import time
import asyncio
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''
GUILD = ""
CHANNEL = ""
intents = discord.Intents.default()
intents.members = True
client = discord.Client(command_prefix=',',intents=intents)
voice = discord.VoiceChannel


@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        server = client.get_guild(GUILD)
        roles = member.roles
        voice_channel = member.voice.channel.id
        channel = server.get_channel(voice_channel)
        for t in roles:
            print(t.name)
            print(t.id)
            if Sauron == t.id:
                await playSound("sauron.mp3", channel)
                return
            if Gandalf == t.id:
                await playSound("gandalf.mp3", channel)
                return
            if Nazgul == t.id:
                await playSound("nazgul.mp3", channel)
                return
            if Orc == t.id:
                await playSound("orc.mp3", channel)
                return
            if hobbit == t.id:
                await playSound("shire.mp3", channel)
                return

                

async def playSound(name, channel):
    vc = await channel.connect()
    time.sleep(1)
    vc.play(discord.FFmpegPCMAudio(name), after=lambda e: print('done', e))
    while True:
        if vc.is_playing() == False:
            await vc.disconnect()
            break
    return



@client.event
async def on_ready():
    server = client.get_guild(GUILD)
    channel = server.get_channel(CHANNEL)
    users = server.members
    for channelz in server.channels:
        print(channelz, channel.id)
    userlist = ""
    for user in users:
        if str(user.nick) != 'None':
            userlist = userlist + str(user.nick) + "\n"
        else:
            userlist = userlist + str(user.name) + "\n"
    #print(userlist)
    #voice = await channel.connect()

    print(f'{client.user} has connected to Discord!')
    print(server.roles)
    files = []
    for file in os.listdir("."):
        if file.endswith(".mp3"):
            files.append(file)

    while True:
        await asyncio.sleep(1)
        number = random.randint(0,3600)
        if number == 0:
            number2 = random.randint(0,len(files)-1)
            fileToPlay = files[number2]
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(fileToPlay), after=lambda e: print('done', e))
            while True:
                if vc.is_playing() == False:
                    await vc.disconnect()
                    break

@client.event
async def on_message(message):
    songList = []
    for file in os.listdir("."):
        if file.endswith(".mp3"):
            songList.append(file)


    messageString = str(message.content).lower()
    messageString = messageString + ".mp3"
    server = client.get_guild(GUILD)
    users = server.members
    userlist = ""
    for user in users:
        if str(user.nick) != 'None':
            userlist = userlist + str(user.nick) + ", "
        else:
            userlist = userlist + str(user.name) + ", "
    question = ['?']
    incel = ['incel']
    exclamation = ['!']
    helplist = ['hjälp','help']
    user = message.author

    # don't respond to ourselves
    if message.author.bot:
        return
    if message.content == "":
        return
    messageContent = str(message.content).lower()
    if len(messageContent) > 0:
        for word in question:
            if word in messageContent:
                await message.channel.send('Ja och/eller nej')
        for word in exclamation:
            if word in messageContent:
                await message.channel.send('Nej')
        if messageString in songList:
            voice_channel = user.voice.channel.id
            channel = server.get_channel(voice_channel)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(messageString), after=lambda e: print('done', e))
            while True:
                if vc.is_playing() == False:
                    await vc.disconnect()
                    break
            return
        
        for word in helplist:
            if word in messageContent:
                helpCommands = ""
                for song in songList:
                    song = song[:-4]
                    helpCommands = helpCommands + song + ", "
                await message.channel.send('följande voice commands funkar: ')
                await message.channel.send(helpCommands)
     
