import discord
import main

client = discord.Client()

#verifies log in
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
@client.event
#prevents bot from reading it's own messages
async def on_message(message):
    if message.author == client.user:
        return
#Help command
    if message.content.startswith('$HMO help'):
        await message.channel.send('Welcome to SHMOBOT the R6S bot for the UMN Siege Discord Server! \n \
The following commands will be implemented soon: \n \
$HMO lookup [UserName] \n \
')
#Stat Lookup Command
    if message.content.startswith('$HMO lookup'):
        channel = message.channel   
        print(message.content[12:])
        name = message.content[12:]
        player = main.playerClass(name)
        player.getPlayerID()
        player.getTabData()
        await message.channel.send()
#yeg
    if message.content.startswith('yeg'):
            await message.channel.send('yeg')
client.run('*insert client string*')

