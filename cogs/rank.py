import discord
from PIL import Image, ImageOps, ImageDraw, ImageFont
import requests
import io
from io import BytesIO
import json
from discord.ext import commands

import random

quotes = [
    "C4n y0u pwn th4 m4chin3?",
    "Hacker man 0x1 0x0 0x1",
    "The quieter you become the more you are able to hear",
    "\*Morpheus\*: Red or Blue pill?",
    "Access security... Access security grid... YOU DIDN'T SAY THE MAGIC WORD!",
    "Just hack the mainframe.",
    "Z2VsdW5weHpyLnBieg==",
    "The Matrix is real",
    "No place like 127.0.0.1",
    "Hack the planet",
    "Just obfuscate it...",
    "Armitage + Hail Mary",
    "WEP, WPA, WAH?",
    "admin:password",
    "rockyou.txt",
    "tmux > screens",
    "tabs or spaces?",
    "Leeerrrroy Jeekinnnns...",
    "Enumeration is key",
    "Try harder..",
    "https://discord.gg/zGdzUad",
    "Satoshi Nakamoto",
    "Mining Bitcoin...",
    "Configuring neural network"
    ]

font1 = ImageFont.truetype("fonts/Ubuntu-Light.ttf", 75)
font2 = ImageFont.truetype("fonts/Ubuntu-Light.ttf", 50)
font3 = ImageFont.truetype("fonts/Ubuntu-Bold.ttf", 30)
red = (162,6,6)
gray = (52,60,66)
green = (136,204,20)
white = (255, 255, 255)

def getMoto():
    return quotes[random.randint(0, len(quotes) - 1)]

def getUsernames(page):

    pages = {1:5,2:10,3:15,4:20,5:25,6:30,7:35,8:40,9:45,10:50}
    response = requests.get("https://tryhackme.com/api/leaderboards")
    data = response.text
    data = json.loads(data)["topUsers"]
    num = pages[page]-5
    r_num = num+1
    usernames = []
    for e,i in enumerate(data[num:pages[page]]):
        usernames.append(i["username"])
    return usernames

def getAvatars(page):

    pages = {1:5,2:10,3:15,4:20,5:25,6:30,7:35,8:40,9:45,10:50}
    response = requests.get("https://tryhackme.com/api/leaderboards")
    data = response.text
    data = json.loads(data)["topUsers"]
    num = pages[page]-5
    r_num = num+1
    avatars = []
    for e,i in enumerate(data[num:pages[page]]):
        avatars.append(i["avatar"])
    return avatars

def getPoints(page):

    pages = {1:5,2:10,3:15,4:20,5:25,6:30,7:35,8:40,9:45,10:50}
    response = requests.get("https://tryhackme.com/api/leaderboards")
    data = response.text
    data = json.loads(data)["topUsers"]
    num = pages[page]-5
    r_num = num+1
    points = []
    for e,i in enumerate(data[num:pages[page]]):
        points.append(i["points"])
    return points

'''
def image_gen(page):
        img = Image.new('RGB', (1000, 1000), color=gray)
        logo = Image.open("THMlogo.png")
        logo.thumbnail((logo.size[0]/4, logo.size[1]/4), Image.ANTIALIAS)
        img.paste(logo, (775, 15), logo)
        d = ImageDraw.Draw(img)
        d.text((12, 20), "Leaderboard:", font=font1, fill=white)
        d.text((865-len(str(page))*25, 920), "Page {}".format(page), font=font2, fill=white)
        d.text((12, 925), "Made with love by the TryHackMe Discord Bot", font=font3, fill=white)
        d.text((12, 955), "discord.gg/GzVZtGX", font=font3, fill=white)
        size = (128, 128)
        mask = Image.new("L", size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0) + size, fill=255)
        avatars = getAvatars(page)
        usernames = getUsernames(page)
        points = getPoints(page)
        base = 150
        index = 0
        pos = (8, base)
        edge = 975
        for x in usernames:
                response = requests.get(avatars[index])
                temp_img = Image.open(BytesIO(response.content))
                temp_img.save('temp{}.png'.format(index))
                output = ImageOps.fit(temp_img, mask.size, centering=(0.5, 0.5))
                img.paste(output, (83, base), mask)
                d.text((222, base+32), "{}".format(usernames[index]), font=font2, fill=white)
                d.text((8, base+32), "{}.".format(index+1+(page-1)*5), font=font2, fill=white)

                d.text((970-(len(str(points[index]))*25), base+32), str(points[index]), font=font2, fill=green)
                base += 160
                pos = (8, base)
                index += 1


        large_img = img.resize((img.size[0]*4, img.size[1]*4))
        large_img.save('images/image.png')
'''
class Rank(commands.Cog,name="Rank Commands"):
        def __init__(self,bot):
                self.bot = bot

        @commands.command()
        async def leaderboard(self,ctx,*,page: int=1):
                #image_gen(page)
                print("generating...")
                emoji = "\N{Waving White Flag}"
                await ctx.message.add_reaction(emoji)
                img = Image.new('RGB', (1000, 1000), color=gray)
                logo = Image.open("images/THMlogo.png")
                logo.thumbnail((logo.size[0]/4, logo.size[1]/4), Image.ANTIALIAS)
                img.paste(logo, (775, 15), logo)
                d = ImageDraw.Draw(img)
                d.text((12, 20), "Leaderboard:", font=font1, fill=white)
                d.text((865-len(str(page))*25, 920), "Page {}".format(page), font=font2, fill=white)
                d.text((12, 925), "Made with love by the TryHackMe Discord Bot", font=font3, fill=white)
                d.text((12, 955), "discord.gg/GzVZtGX", font=font3, fill=white)
                size = (128, 128)
                mask = Image.new("L", size, 0)
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse((0, 0) + size, fill=255)
                avatars = getAvatars(page)
                usernames = getUsernames(page)
                points = getPoints(page)
                base = 150
                index = 0
                pos = (8, base)
                edge = 975
                for x in usernames:
                        response = requests.get(avatars[index])
                        temp_img = Image.open(BytesIO(response.content))
                        temp_img.save('temp{}.png'.format(index))
                        output = ImageOps.fit(temp_img, mask.size, centering=(0.5, 0.5))
                        img.paste(output, (83, base), mask)
                        d.text((222, base+32), "{}".format(usernames[index]), font=font2, fill=white)
                        d.text((8, base+32), "{}.".format(index+1+(page-1)*5), font=font2, fill=white)

                        d.text((970-(len(str(points[index]))*25), base+32), str(points[index]), font=font2, fill=green)
                        base += 160
                        pos = (8, base)
                        index += 1


                large_img = img.resize((img.size[0]*4, img.size[1]*4))
                large_img.save('images/image.png')
                await ctx.send(file=discord.File('images/image.png'))
            

def setup(bot):
	bot.add_cog(Rank(bot))
				

        