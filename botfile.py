import discord
from discord.ext import commands
import os
import random
import asyncio
from discord.utils import get
import sqlite3
connection = sqlite3.connect('server.db')
cursor = connection.cursor()

@client.event
async def on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    id INT,
    rep INT,
    cash BIGINT,
    xp INT,
    lvl INT
    
)""")
    

client = commands.Bot( command_prefix = '=')
client.remove_command('help')

@client.event
async def on_redy():
    print( 'Bot connected')
    

                    
@client.command()
async def load(ctx, extensions):
    client.load_extensions(f'cogs.{extensions}')
    await ctx.send("loaded")

@client.command()
async def unload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')
    await ctx.send('unloaded')
    
    
@client.command()
async def reload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')# отгружаем ког
    client.load_extension(f'cogs.{extensions}')# загружаем 
    await ctx.send('reloaded')

text = ['']    
@commands.command()
@commands.has_permissions( administrator = True )
async def rew(self, ctx , * , arg = None):
        global text
        await ctx.channel.purge( limit = 1 ) 
        text = text + arg
        await ctx.send(f" {arg} ") 
        await ctx.send(f"{text}")
        await ctx.message.add_reaction('👍')  

        
        
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 745689538608758806: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '1️⃣': # Emoji для реакций
            role = guild.get_role(745685081489801246) # ID Ролей для выдачи
        elif str(payload.emoji) == '2️⃣':
            role = guild.get_role(745685081506709674)
        elif str(payload.emoji) == '3️⃣':
            role = guild.get_role(745685081548652594)
        elif str(payload.emoji) == '4️⃣':
            role = guild.get_role(745687846576455832)
            
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)          
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
