# id 
# token 
# permissions 


import discord
import asyncio
import random

client = discord.Client()

@client.event # event decorator /wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    senddex_guild = client.get_guild() # discord server ID for REDACTED
    
    #Got rid of server ID for privacy & security reasons

    #Check member count and logout
    if "steve.member_count()" == message.content.lower():
        await message.channel.send(f" {senddex_guild.member_count}")

    elif "steve.logout()" in message.content.lower():
        await client.close()




    #Chat Commands for the BOT
    if "hi there" in message.content.lower():
        await message.channel.send(random.choice(["Hi", "Hello"]))
    
    if "thanks steve" in message.content.lower():
        await message.channel.send(random.choice(["No problem, anything for a Gamer", "No, thank you", "Your welcome Gamer"]))

    if "tanks in terraria" in message.content.lower():
        await message.channel.send("SHUT THE FUCK UP, IF YOU AREN'T PLAYING TERRARIA LEAVE THE FUCKING CHANNEL")

    if "fuck you steve" in message.content.lower():   
        await message.channel.send(random.choice(["Don't be mean please. UwU", "Get a life nerd lol", "Do you kiss your wife's boyfriend with that mouth"]))
    
    if "do you hate women steve" in message.content.lower():
        await message.channel.send("I'm a huge fan of Affirmative Action")

    if "do you hate men steve" in message.content.lower():
        await message.channel.send(random.choice(["Not a big of them", "Men? yikes!", "Imagine being a man in the current year"]))
    
    if "hello steve" in message.content.lower():   
        await message.channel.send(random.choice(["Why howdy Gamer", "Gamer!"]))
        
    if "hi steve" in message.content.lower():   
        await message.channel.send("Hello Gamer")    

    if "sorry steve" in message.content.lower():
        await message.channel.send(random.choice(["It's okay Gamer, we all make mistakes.", "Apology Accepted!", "You're Gucci"]))

    if "thank you steve" in message.content.lower():
        await message.channel.send("Don't sweat it Gamer Girl.")
    
    if "wanna play dota" in message.content.lower():
        await message.channel.send("Send me an invite I'll hop on.")

    if "wanna play artifact" in message.content.lower():
        await message.channel.send("Are you dumb?")






    elif "!ping" in message.content.lower():
        await message.channel.send("Pong!")

    elif message.content.startswith("!coinflip"):
        await message.channel.send(random.choice(["Heads UwU", "Tails OwO"]))

    elif message.content.startswith("!8ball"):
        await message.channel.send(random.choice(["It is certaiin :8ball:", "It is decidedly so :8ball:", "Without a doubt :8ball:", "Yes, defintely :8ball:", "You may rely on it :8ball:", "As I see it, yes :8ball:", "Most likely :8ball:", "Outlook good :8ball:", "Yes :8ball:", "Signs point to yes :8ball:", "Replay hazy try again :8ball:", "Ask again later :8ball:", "Better not tell you now :8ball:", "Cannot predict now :8ball:", "Don't count on it :8ball:", "My reply is no :8ball:", "My sources say no :8ball:", "Outlook not so good :8ball:"]))
    






    #Able to post images now 1/31/2020
    #Has to be in directory of steve and not in images
    elif message.content.startswith("!test"):
        file = discord.File("cutie.png", filename="cutie.png")
        await message.channel.send("cutie.png", file=file)
    
    #Testing to see if this one interferes with the previous code
    elif message.content.startswith("!bog"):
        file = discord.File("bog.jpg", filename="bog.jpg")
        await message.channel.send("bog.jpg, file=file")
    
    #JPG doesn't appear to work, testing with PNG
    elif message.content.startswith("!airlines"):
        file = discord.File("tiny.png", filename="tiny.png")
        await message.channel.send("tiny.png", file=file)

    elif message.content.startswith("!tiny"):
        file = discord.File("tiny.png", filename="tiny.png")
        await message.channel.send("tiny.png", file=file)




client.run("")
