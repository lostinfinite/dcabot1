import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='Kick', help='Kicks the mentioned user')
async def kick(ctx, member: discord.Member):
    await ctx.guild.kick(member)
    await ctx.send(f'{member} has been kicked')

@bot.command(name='Ban', help='Bans the mentioned user')
async def ban(ctx, member: discord.Member):
    await ctx.guild.ban(member)
    await ctx.send(f'{member} has been banned')

@bot.command(name='Mute', help='Mutes the mentioned user')
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(mute_role)
    await ctx.send(f'{member} has been muted')

@bot.command(name='Purge', help='Deletes a specified number of messages')
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages have been deleted')

bot = discord.Bot()
bot.run(os.environ['BOT_TOKEN'])