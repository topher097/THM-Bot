import discord
import aiohttp
import asyncio
import json
from discord.utils import get
from discord.ext import commands
from discord import guild
from discord.channel import DMChannel


rolesF = json.loads(open("config/roles.json", "r").read())

devLeadID = rolesF["devLead"]
devID = rolesF["dev"]


# Role managment
def hasRole(member, id):
        for role in member.roles:
                if id == role.id:
                        return True
        return False

# Actual command
class DevRole(commands.Cog,name="BOT Dev"):
        def __init__(self,bot):
                self.bot = bot

        @commands.command()
        async def botdev(self, ctx, member: discord.Member):

                devRole = ctx.guild.get_role(devID)
                
                if (hasRole(ctx.author, devLeadID) and not (hasRole(member, devID))):
                        await member.add_roles(devRole)
                        await ctx.send("Welcome on the BOT Dev team, " + member.mention + "!")
                elif (hasRole(ctx.author, devLeadID) and (hasRole(member, devID))):
                        await member.remove_roles(devRole)
                        await ctx.send(member.mention + " left the BOT Dev team!")
            

def setup(bot):
        bot.add_cog(DevRole(bot))
