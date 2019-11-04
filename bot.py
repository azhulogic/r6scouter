import discord
import main
import ball

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

client = discord.Client()
statslink = 'https://docs.google.com/spreadsheets/d/1fp0PyB2qnfwi9qT0g5Bbr_O0StlnQML-u7OF9iMWSj8/edit?usp=sharing'
gamelink ='https://battlefy.com/collegiater6-collegiate-rainbow-six-siege/collegiater6-fall-2019-phase-1/5d7b085b3243c828f709553f/stage/5db69a087e3a1361f7b0e43c/match/5dc06d0d839bce0eab027b19'

#verifies log in and set game status
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("with Spencer's emotions")
    await client.change_presence(activity = game)
    


@client.event

#prevents bot from reading it's own messages
async def on_message(message):
    if message.author == client.user:
        return
    
#Help command
    if message.content.startswith('$HMO help'):
        print('Help Command Registered')
        await message.channel.send(\
"Welcome to SHMOBOT the R6S bot for the UMN Siege Discord Server! \n \
The following commands are available now: \n \
$HMO lookup [UserName] - will lookup a player's siege stats\n \
$HMO scout - pulls up Piv's scouting sheet.\n\
$HMO nextgame - pulls up our next match on Battlefy")

 
#Stat Lookup Command
    if message.content.startswith('$HMO lookup'):
        print('Looking up a user')
        channel = message.channel   
        print(message.content[12:])
        name = message.content[12:]
        player = main.playerClass(name)
        player.getPlayerID()
        player.getTabData()
        player.setStats()
        await message.channel.send('MMR is: {} \n\
Rank is: {} \n\
KD this season is: {} \n\
WL this season is: {} \n\
Overall KD is: {} \n\
Overall WL is: {}'.format(player.seasMMR, player.seasRank, truncate(player.seasKD, 2), truncate(player.seasWL, 2), truncate((player.ovrKD / 100), 2), truncate(player.ovrWL, 2)))

   
#gamestats command
    if message.content.startswith('$HMO scout'):
        print('pulling up game stats')
        await message.channel.send('Pulling up the scouting report')
        await message.channel.send(statslink)

#next game
    if message.content.startswith('$HMO nextgame'):
        print('pulling up our next game')
        await message.channel.send('pulling up the next CR6 match')
        await message.channel.send(gamelink)
 
#yeg
    if 'y e g' in message.content:
        print('somebody said yeg')
        await message.channel.send('yeg')
    if 'yeg' in message.content:
        print('somebody said yeg')
        await message.channel.send('yeg')
    if 'Yeg' in message.content:
        print('somebody said yeg')
        await message.channel.send('yeg')
#8ball
#    if message.content.startswith('$HMO ask'):
#        print('consulting with $HMOBOT')
#        response = ball.gen
#        await message.channel.send(response)
        
client.run('NjM4MTIxNzA3NTUwNTM5Nzc4.XbkGVQ.vuuuYGzzR5Fa-M730J2Lp4bb7dM')

