import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.messages = True

GUILD_ID = GUILD  # Replace this with your actual guild ID

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="guildinfo")
async def guildinfo(ctx):
    guild = bot.get_guild(GUILD)

    if guild is not None:
        await ctx.send(f'Guild name: {guild.name}\nGuild ID: {guild.id}\nMember count: {guild.member_count}')
    else:
        await ctx.send(f'Could not find the guild with ID: {GUILD_ID}')

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

bot.run('TOKEN')