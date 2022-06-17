#joeker made in lesson
import random , os , discord , subprocess,asyncio
from subprocess import run
from discord.utils import get
TOKEN = ""

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
#detect the reactions to a message and check its not from the bot
#save messages to text document to be added to training dataset
@client.event
async def on_reaction_add(reaction, user):
    print(reaction.message.content)
    if user != client.user:
        if reaction.emoji == '\N{UPWARDS BLACK ARROW}':
            print("emoji up")
            file = open("funny.txt","a+")
            file.write("\n"+str(reaction.message.content))
            file.close()
        elif reaction.emoji == "\N{DOWNWARDS BLACK ARROW}":
            file = open("unfunny.txt","a+")
            file.write("\n" +str(reaction.message.content))
            file.close()
        else:
            print("emoji added")
#respond to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Debug":
        emoji = '\N{NEUTRAL FACE}'
        await message.channel.send(emoji)
    #initialize variables    
    swiftmsg = ""
    debug = False #Set True for Fun
    usrname = str(message.author.name)
    chan = str(message.channel.name)
    pid = str(message.author.id)
    parsemsg = message.content
    parsemsg = parsemsg.lower()
    
    #user = client.get_user(user_id) or await client.fetch_user(user_id)
    #await user.send(usrname + " in " + chan + " wrote: " + parsemsg)

    print(usrname + " in " + chan + " wrote: " + parsemsg)
    parsemsg = str(message.clean_content)
# clean a message so that it doesnt break the swift code
    for x in parsemsg:
        if x == " " or x == ")":
            y = "_"
        else:
            y = x
        swiftmsg = swiftmsg + y
    #remove banned terms
    if parsemsg.__contains__("among us"):
            await message.delete()
    #dont react to short messages as it gets annoying
    if "_" not in swiftmsg and debug != True:
        print("too short")
    else:
        #pass the fixed message string to the swift program to see if ai thinks its a joke
        output = subprocess.Popen( "./joke " + swiftmsg , stdout=subprocess.PIPE , shell=True ).communicate()[0]
        print(output)
        if "True" in str(output.decode("utf-8")):
            print("funni")
            if parsemsg.__contains__("test"):
                emoji = '\N{NEUTRAL FACE}'
            else:
                emoji = '\N{FACE WITH TEARS OF JOY}'
            #add reactions to see if people agree
            await message.add_reaction(emoji)
            emoji = '\N{UPWARDS BLACK ARROW}'
            await message.add_reaction(emoji)
            emoji = '\N{DOWNWARDS BLACK ARROW}'
            await message.add_reaction(emoji)
        else:
            print("un funny")
            emoji = '\N{UPWARDS BLACK ARROW}'
            await message.add_reaction(emoji)
            emoji = '\N{DOWNWARDS BLACK ARROW}'
            await message.add_reaction(emoji)

client.run(TOKEN)
