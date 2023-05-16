import os
import asyncio
from gtts import gTTS  
import ast
import random
import datetime as td
from datetime import timedelta, datetime
from disnake import TextInputStyle
import psutil
import disnake
from disnake.ext import commands,  tasks
from simpledemotivators import Demotivator

import json


import aiohttp
from googleapiclient.discovery import build


api_key = "AIzaSyBu0AuxzCw45Em77YQDV-3eU6pWTRvvldw"
Current = "+"
bans=[]


test_guilds=[1032733965695582228]
intents = disnake.Intents.default()

token = ""
intents.message_content=True
Bot = commands.Bot(command_prefix="+",intents=intents)
Bot.remove_command('help')
folder = 'music_files'
@Bot.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):     
        error=f"{error}"
        errorne=error.replace(" permission(s) to run this command.", "")
        errorne=errorne.replace("You are missing ", "")
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Для выполнения этой команды требуется права: ``{errorne}``", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        print(error)
# @Bot.slash_command(test_guilds=[1047132110391095407])
# async def gmute(ctx: disnake.ApplicationCommandInteraction ,id):
#     abcd=False
#     a=True
#     gu= await Bot.fetch_guild(1047132110391095407)
    
#     for b in [1047243772263665784,1047243783030448158,1047244301572243556,1047243615971311619]:
#         ro=  disnake.utils.get(gu.roles, id=b)
#         if ro in ctx.author.roles:
#             abcd=True

#     if abcd==True:
#         try:
#             member=await Bot.fetch_user(int(id))
#         except:
#             member=None
#             print("Иди от сюда")
#         if member!=None:
        
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", 'r') as f:
#                 prefix = json.load(f)
#                 sex=prefix[str("Ban")]
#             for ab in sex:
#                 print(ab)
#                 if ab==member.id:
#                     a=False
#             if a==True:
#                 sex.append(member.id)
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", 'w') as f:
#                     json.dump(prefix, f, indent=4)
#                 await ctx.send("Клоун в муте", ephemeral=True)
#                 print(f"успешно ")
#             else:
#                 print("ses")
            


#     else:
#         print("прав нема")

# @Bot.event
# async def on_message(msg:disnake.Message):
#     bababoy=False
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", "r") as f:
#         nig=json.load(f)
#         banesd=nig[str("Ban")]
#     for susyy in banesd:
#         if susyy==msg.author.id:
#             bababoy=True
         
#     if bababoy==False:
#         try:
#             if msg.author.bot==False:
            
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(msg.guild.id), "r") as f:
#                     nig=json.load(f)
#                     chaid=nig[str("servchannel")]
#         except:
#             chaid=None
#         ban=False
#         if msg.author.bot==False:
#             if msg.channel.id == chaid:
#                 for bebra in Bot.guilds:

#                     work=True
#                     try:
#                         with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                             nig=json.load(f)
#                     except:
#                         work=False
#                     if work==True and "https" not in msg.content and "invite" not in msg.content and "discord.gg" not in msg.content:
#                         try:
#                             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                 nig=json.load(f)
#                                 chaid=nig[str("servchannel")]
#                         except:
#                             chaid=None
        
#                         if chaid==None:
#                             print(f"{bebra.name} да, ")
                    
#                         else:
                
#                             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                 nig=json.load(f)
#                             try:
#                                 bans=nig[str("muted")]
#                                 for mem in bans:
#                                     if msg.author.id ==mem:
#                                         ban=True
#                             except:
#                                 ban=False

#                             if ban==False:
#                                 print(f"{bebra.name}нигер")
#                                 if msg.guild.id != bebra.id:
#                                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                         nig=json.load(f)
#                                         try:
#                                             chaid=nig[str("servchannel")]
#                                         except:
#                                             chaid=None
                                            
#                                     try:
#                                         channel=await Bot.fetch_channel(int(chaid))
                                        
#                                         print(f"{bebra.name} спиздуй шлюха")
#                                         mywh=None
#                                         for wh in nig:
#                                             if wh=="webhook":
#                                                 mywh=nig[str("webhook")]
#                                         if mywh!=None:
                                            
#                                             webhook= await Bot.fetch_webhook(int(mywh))

#                                         else:
#                                             print(f"{bebra.name}мать твоя")
#                                             webhook=await channel.create_webhook(name="Vable Chat")
#                                             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                                     nig=json.load(f)
#                                                     nig[str("webhook")]=webhook.id
#                                             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "w") as f:
#                                                     json.dump(nig, f, indent=4)
#                                         newcontent=msg.content.replace("@everyone", "")
#                                         newcontent=newcontent.replace("@here", "")
#                                         await webhook.send(content=newcontent, username=f"{msg.author.id}", avatar_url=msg.author.avatar)
#                                         print(bebra)
#                                     except:
#                                         pass


#         with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(msg.guild.id), "r") as f:
#             try:
#                 nig=json.load(f)
#                 aprim=nig["prime"]
#             except:
#                 aprim=False

#         if aprim==True:
#             if msg.author.bot==False:
#                 try:
#                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(msg.guild.id), "r") as f:
#                         nig=json.load(f)
#                         srv=nig[str("private")]
#                         chaid=nig[str("privatechannel")]
#                 except:
#                     chaid=None
#                 ban=False
#                 if msg.author.bot==False:
#                     if msg.channel.id == chaid:
#                         for bebra in srv:
#                             bebra=await Bot.fetch_guild(int(bebra))

#                             work=True
#                             try:
#                                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                     nig=json.load(f)
#                             except:
#                                 work=False
#                             if work==True and "https" not in msg.content and "invite" not in msg.content and "discord.gg" not in msg.content:
#                                 try:
#                                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                         nig=json.load(f)
#                                         chaid=nig[str("privatechannel")]
#                                 except:
#                                     chaid=None
                
#                                 if chaid==None:
#                                     pass
#                                 else:
                        
#                                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                         nig=json.load(f)
#                                     try:
#                                         bans=nig[str("muted")]
#                                         for mem in bans:
#                                             if msg.author.id ==mem:
#                                                 ban=True
#                                     except:
#                                         ban=False

#                                     if ban==False:
#                                         if msg.guild.id != bebra.id:
#                                             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                                 nig=json.load(f)
#                                                 try:
#                                                     chaid=nig[str("privatechannel")]
#                                                 except:
#                                                     pass
#                                             try:
#                                                 channel=await Bot.fetch_channel(int(chaid))
#                                                 mywh=None
#                                                 for wh in nig:
#                                                     if wh=="privatewebhook":
#                                                         mywh=nig[str("privatewebhook")]
#                                                 if mywh!=None:
#                                                     webhook= await Bot.fetch_webhook(int(mywh))

#                                                 else:
#                                                     webhook=await channel.create_webhook(name="Vable Private Chat")
#                                                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "r") as f:
#                                                             nig=json.load(f)
#                                                             nig[str("privatewebhook")]=webhook.id
#                                                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(bebra.id), "w") as f:
#                                                             json.dump(nig, f, indent=4)
#                                                 newcontent=msg.content.replace("@everyone", "")
#                                                 newcontent=newcontent.replace("@here", "")
#                                                 print(bebra)
#                                                 await webhook.send(content=newcontent, username=f"{msg.author.name}#{msg.author.tag}", avatar_url=msg.author.avatar)
#                                                 print(bebra)
#                                             except:
#                                                 pass

# @Bot.slash_command(name="remove-private-guild", description="Отключить сервер от вашего приватного чата")
# @commands.is_owner()
# async def rpg(ctx: disnake.ApplicationCommandInteraction, id:str=commands.Param(description="Айди сервера, который вы хотите отключить")):

#     zuk=True
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:

#         try:
#             prefix = json.load(f)
#             alword = prefix[str("prime")]
#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#             pass

#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:
#         zopa=json.load(f)
#         try:
#             zas=zopa[str("private")]
#         except:
#             zopa[str("private")]=[]
#             zas=zopa[str("private")]
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                 json.dump(zopa, f, indent=4)
#     for a in zas:
#         if int(a) ==int(id):
#             zuk=False
#     if zuk==True:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Такого сервера нету в вашем межсерверном чате", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
#     else:
#         if alword==True:
    
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(id), "r") as f:
#                 try:
#                     prefix = json.load(f)
#                     alwored = prefix[str("prime")]
#                 except:
#                     embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#                     embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                     await ctx.send(embed=embed, ephemeral=True)
#                     pass
#             if alwored==True:
#                 try:
#                     l=prefix[str("private")]
#                     l.remove(int(ctx.guild.id))
#                 except:
#                     prefix[str("private")]=[]
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(id), "w") as f:
#                     json.dump(prefix, f, indent=4)
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#                     nig=json.load(f)
#                 try:
#                     l=nig[str("private")]
#                     l.remove(int(id))
#                 except:
#                     nig[str("private")]=[]
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                     json.dump(nig, f, indent=4)
#                 owner=await Bot.fetch_guild(id)
#                 owner=await Bot.fetch_user(int(owner.owner_id))
#                 p=disnake.utils.format_dt(datetime.now(), "D")

#                 embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Сервер: {ctx.guild.name}``({ctx.guild.id})``\n От имени: ``{ctx.author.name}`` \n Дата: {p} \nПодключился в ваш приватный межсерверный чат.", color=0x42aaff)
#                 embed.set_thumbnail(url=Bot.user.avatar)
#                 await ctx.send(embed=embed, ephemeral=True)

#                 try:
#                     embed = disnake.Embed(title = "**Внимание! ⚠️**", description = f"Сервер: {ctx.guild.name}``({ctx.guild.id})``\n От имени: ``{ctx.author.name}`` \n Дата: {p} \nПодключился в новый приватный-межсерверный чат.", color=0x42aaff)
#                     embed.set_thumbnail(url=Bot.user.avatar)
#                     await owner.send(embed=embed)
#                 except:
#                     pass
#             else:
#                 embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У данного сервера нету premium.", color=0x42aaff)
#                 embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                 await ctx.send(embed=embed, ephemeral=True)
#         else:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У вашего сервера нету premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True) 


# @Bot.slash_command(name="add-private-guild", description="Подключить/подключиться сервер к приватному межсерверному чату")
# @commands.is_owner()
# async def apg(ctx, id:str=commands.Param(description="Айди сервера, к которому вы хотите подключиться")):

#     zuk=True
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:

#         try:
#             prefix = json.load(f)
#             alword = prefix[str("prime")]
#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#             pass

#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:
#         zopa=json.load(f)
#         try:
#             zas=zopa[str("private")]
#         except:
#             zopa[str("private")]=[]
#             zas=zopa[str("private")]
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                 json.dump(zopa, f, indent=4)
#     for a in zas:
#         if int(a) ==int(id):
#             zuk=False
#     if zuk==False:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы уже добавили этот сервер..", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
#     else:
#         if alword==True:
    
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(id), "r") as f:
#                 try:
#                     prefix = json.load(f)
#                     alwored = prefix[str("prime")]
#                 except:
#                     embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#                     embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                     await ctx.send(embed=embed, ephemeral=True)
#                     pass
#             if alwored==True:
#                 try:
#                     l=prefix[str("private")]
#                     l.append(int(ctx.guild.id))
#                 except:
#                     prefix[str("private")]=[int(ctx.guild.id)]
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(id), "w") as f:
#                     json.dump(prefix, f, indent=4)
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#                     nig=json.load(f)
#                 try:
#                     l=nig[str("private")]
#                     l.append(int(id))
#                 except:
#                     nig[str("private")]=[int(id)]
#                 with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                     json.dump(nig, f, indent=4)
#                 owner=await Bot.fetch_guild(id)
#                 owner=await Bot.fetch_user(int(owner.owner_id))
#                 p=disnake.utils.format_dt(datetime.now(), "D")

#                 embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Сервер: {ctx.guild.name}``({ctx.guild.id})``\n От имени: ``{ctx.author.name}`` \n Дата: {p} \nПодключился в новый приватный межсерверный чат.", color=0x42aaff)
#                 embed.set_thumbnail(url=Bot.user.avatar)
#                 await ctx.send(embed=embed, ephemeral=True)

#                 try:
#                     embed = disnake.Embed(title = "**Внимание! ⚠️**", description = f"Сервер: {ctx.guild.name}``({ctx.guild.id})``\n От имени: ``{ctx.author.name}`` \n Дата: {p} \nПодключился в ваш приватный-межсерверный чат.", color=0x42aaff)
#                     embed.set_thumbnail(url=Bot.user.avatar)
#                     embed.set_footer(text=f"От {ctx.guild.name}", icon_url=ctx.guild.icon)

#                     await owner.send(embed=embed)
#                 except:
#                     pass
#             else:
#                 embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У данного сервера нету premium.", color=0x42aaff)
#                 embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                 await ctx.send(embed=embed, ephemeral=True)
#         else:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У вашего сервера нету premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True) 




                

# @Bot.slash_command(description="Установить приватный-межсерверный канал")
# @commands.has_guild_permissions(administrator=True)

# async def privchannel(ctx):
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:

#         try:
#             prefix = json.load(f)
#             alword = prefix[str("prime")]
#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#             pass
#     if alword==True:
#         with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#             prefix = json.load(f)
#         try:
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#                     prefix = json.load(f)
#                     prefix[str("privatechannel")] = ctx.channel.id 
#                     niger=prefix[str("privatewebhook")]
#                     aberb=await Bot.fetch_webhook(int(niger))
#                     a=aberb.edit(name="Vable Private Chat", channel=ctx.channel)
#                     await aberb.delete()
#                     prefix[str("privatewebhook")]=a.id
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
#                     json.dump(prefix, f, indent=4)
#         except:
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#                 prefix = json.load(f)
#                 prefix[str("privatechannel")] = ctx.channel.id 
#                 a=await ctx.channel.create_webhook(name="Vable Private Chat")
#                 prefix[str("privatewebhook")]= a.id
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
#                     json.dump(prefix, f, indent=4)

                    
#             embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы установили межсерверный канал - <#{ctx.channel.id}>", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"``{ctx.guild.name}`` не имеет ``premium``.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True) 

                     
            
# @Bot.slash_command(name="private-guilds",description="Список серверов в приватном чате.")
# @commands.has_guild_permissions(administrator=True)

# async def privateguilds(ctx):
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:

#         try:
#             prefix = json.load(f)
#             alword = prefix[str("prime")]
#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#             pass
#     if alword==True:
#         try:
#             embed=disnake.Embed(title="Успешно! ✅", description="Вы получили список приватных серверов в чате.", color=0x42aaff)
#             embed.set_thumbnail(url=ctx.guild.icon)
#             embed.set_footer(text=f"Запросил {ctx.author}", icon_url=ctx.author.avatar)
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#                 nig=json.load(f)
#                 mutes=nig[str("private")]
            
#             for mute in mutes:
                
#                 memb=await Bot.fetch_guild(int(mute))
#                 niger=await Bot.fetch_user(int(memb.owner_id))
#                 embed.add_field(name=f"{memb.name}", value=f"Создатель: ``{niger.name}``\nАйди: ``{memb.id}``",inline=False)    
#             await ctx.send(embed=embed, ephemeral=True)

#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось обнаружить сервера в приватном чате.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True) 
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"``{ctx.guild.name}`` не имеет ``premium``.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True) 

    
            
    
            




# @Bot.slash_command(description="Замутить пользователя на сервере")
# @commands.has_guild_permissions(administrator=True)

# async def mute(ctx, id:str=commands.Param(description="Айди пользователя")):
#     use=None
#     member=None
#     try:
#         member= await Bot.fetch_user(int(id))
#     except:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось найти пользователя.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
#         pass
        
#     print(member)
#     if member!=None:
#         with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#                 nig=json.load(f)
#                 try:
                    
#                     liste=nig[str("muted")]
#                     for us in liste:
#                         if use==member.id:
#                             use=us
#                     if use!=None:
#                         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы уже замутили ``{member.name}`` на своем сервере.", color=0x42aaff)
#                         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                         await ctx.send(embed=embed, ephemeral=True)
#                     else:
#                         embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы замутили ``{member.name}``, на своем сервере.", color=0x42aaff)
#                         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                         await ctx.send(embed=embed, ephemeral=True)
#                         liste.append(member.id)
        
#                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                             json.dump(nig, f, indent=4)
#                 except:
#                     nig[str("muted")] = [member.id]
#                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                         json.dump(nig, f, indent=4)
#                     embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы замутили ``{member.name}``, на своем сервере.", color=0x42aaff)
#                     embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                     await ctx.send(embed=embed, ephemeral=True)
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось найти пользователя.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
                     
            
# @Bot.slash_command(description="Список заткнутых участников")
# @commands.has_guild_permissions(administrator=True)

# async def muted(ctx):
#     embed=disnake.Embed(title="Успешно! ✅", description="Вы получили список заткнутых участников.", color=0x42aaff)
#     embed.set_thumbnail(url=ctx.guild.icon)
#     embed.set_footer(text=f"Запросил {ctx.author}", icon_url=ctx.author.avatar)
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#         nig=json.load(f)
#         mutes=nig[str("muted")]
    
#     for mute in mutes:
#         memb=await Bot.fetch_user(int(mute))
#         embed.add_field(name=f"{memb.name}#{memb.discriminator}", value=f"``{memb.id}``",inline=False)    
#     await ctx.send(embed=embed, ephemeral=True)
    
            


            
# @Bot.slash_command(description="Установить межсерверный канал")
# @commands.has_guild_permissions(administrator=True)

# async def servchannel(ctx):
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#         prefix = json.load(f)
#         try:
#             a=prefix[str("ban")]
#         except:
#             a=False
#     if a==False:
#         try:
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#                     prefix = json.load(f)
#                     prefix[str("servchannel")] = ctx.channel.id 
#                     niger=prefix[str("webhook")]
#                     aberb=await Bot.fetch_webhook(int(niger))
#                     a=aberb.edit(name="Vable Chat", channel=ctx.channel)
#                     await aberb.delete()

#                     prefix[str("webhook")]=a.id
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
#                     json.dump(prefix, f, indent=4)
#         except:
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
#                 prefix = json.load(f)
#                 prefix[str("servchannel")] = ctx.channel.id 
#                 a=await ctx.channel.create_webhook(name="Vable chat")
#                 prefix[str("webhook")]= a.id
#             with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
#                     json.dump(prefix, f, indent=4)

                    
#             embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы установили межсерверный канал - <#{ctx.channel.id}>", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Ваш сервер был заблокирован в межсерверном чате.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
            
# @Bot.slash_command(description="Размутить пользователя на сервере")
# @commands.has_guild_permissions(administrator=True)

# async def unmute(ctx, id:str=commands.Param(description="Никнейм пользователя.")):
#     try:
#         member=await Bot.fetch_user(int(id))
#     except:
#         member=None
#     if member!=None:
#         with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
#                 nig=json.load(f)
#                 try:
                    
#                     liste=nig[str("muted")]
#                     for use in liste:
#                         if use==member.id:
#                             a=use
#                     if use==None:
#                         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не мутили ``{member.name}`` на своем сервере.", color=0x42aaff)
#                         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                         await ctx.send(embed=embed, ephemeral=True)
#                     else:
#                         embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы размутили ``{member.name}``, на своем сервере.", color=0x42aaff)
#                         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                         await ctx.send(embed=embed, ephemeral=True)
#                         liste.remove(member.id)
                        
        
#                     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
#                             json.dump(nig, f, indent=4)
#                 except:
#                     embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не мутили ``{member.name}`` на своем сервере.", color=0x42aaff)
#                     embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#                     await ctx.send(embed=embed, ephemeral=True)
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось найти пользователя.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)    

@Bot.slash_command(description="Информация о premium")
async def premiumhelp(ctx):
    embed= disnake.Embed(title="Информация о premium")
    embed.add_field(name="Как купить premium?", value="Для покупки ``premium``, вам необходимо находится на [сервере поддержки](https://discord.gg/ubfxg4bbUU).\n Далее вам требуется перейти на этот [сайт](https://boosty.to/vablvable-dev) и купить подписку. ", inline=False)
    embed.add_field(name="Что такое gift-premium?", value="``gift-premium`` это подарочные премиумы для серверов. У вас их всего ``2``.", inline=False)
    embed.add_field(name="Как выдать premium серверу?", value="Чтобы выдать серверу ``premium``, у вас должен быть приобретен ``premium``. \nВы сможете выдать ``premium`` двум ``серверам``, для этого пропишите ``/subscribe `` ", inline=False)
    embed.set_thumbnail(url=Bot.user.avatar)
    await ctx.send(embed=embed,  ephemeral=True)

@Bot.event
async def on_guild_join(guild):
    if guild.id==1061334565232332810:
        beb= await Bot.fetch_guild(1061334565232332810)
        await beb.leave()


# @Bot.event
# async def on_guild_join(guild):
#     limit=0
    
#     for channel in guild.text_channels:
#             limit=limit+1
#             try:
#                 embed= disnake.Embed(title="Информация о  VablVable Bot!", description="Приветствую всех участников этого сервера! Я бот способный общаться за\n счет чего развиваться,\nвы спокойно сможете научить меня ~~``материться``~~ или быть **культурным** (``человеком``)\nКроме функции общения я умею еще очень **``много``**! Полный список моих \nспособностей вы увидите ниже!")
#                 embed.add_field(name="/setchannel",value="</setchannel:1058509408579108987>\nДанная ``команда`` позволит вам установить ``канал`` для\n``общения`` с ботом.\n В ``указан.`` канале бот будет читать и отправлять сообщения.", inline=True)
#                 embed.add_field(name="/reset", value="</reset:1058509408579108990>\nДанная ``команда`` **``обнулит``** словарный запас бота на вашем сервере.\nИспользуйте ее, в **крайнем** случае!",inline=True)
#                 embed.add_field(name="/datatime", value="</datatime:1058509408683950158>\nданная ``команда`` выдаст указан. время.\n ``P.S.``: Если оставить пустым - выдаст точную дату момента написания команды.", inline=True)
#                 embed.add_field(name="/code", value="</code:1058509408683950151>\nДанная ``команда`` закодирует ``указан.`` сообщениe.\n``P.S.``: Есть во вкладе ``'Приложения'``.", inline=True)
#                 embed.add_field(name="/uncode", value="</uncode:1058509408683950152>\n Данная ``команда`` раскодирует ``указан.`` сообщение.\n``P.S.``: Есть во вкладе ``'Приложения'``. ", inline=True)
#                 embed.add_field(name="/report", value="</report:1058494331914309812>\nДанная ``команда`` позволит вам связаться с разработчиком.\n``P.S.``: Использовать по назначению!", inline=True)
#                 embed.add_field(name="/auto-gen-message", value="</auto-gen-message:1058509408579108985>\nДанная ``команда`` установит шанс отправки случ. сообщения.\n``P.S.``: Работает только в ``указ.`` канале.", inline=True)
#                 embed.add_field(name="/deleteping", value="</deleteping:1058509408579108989>\nДанная ``команда`` удалит ваш пинг из БД данного сервера.", inline=True)
#                 embed.add_field(name="/deleteword", value="</deleteword:1058509408579108988>\nДанная ``команда`` удалит ``опр.`` слово из БД данного сервера.", inline=True)
#                 embed.add_field(name="/avatar", value="</avatar:1058509408683950153>\nДанная ``команда`` позволит вам получит аватар ``указ.`` пользователя.\n``P.S.``: Есть во вкладе ``'Приложения'``.", inline=True)
#                 embed.add_field(name="/usersay", value="</usersay:1058509408683950156>\nДанная ``команда`` позволит вам написать от лица ``указ.`` пользователя.\n``P.S.``: Присутствует отправка ``embed'a``.", inline=True)
#                 embed.add_field(name="/say", value="</say:1058509408683950155>\nДанная ``команда`` позволит вам написать от лица бота.\n``P.S``: Присутствует отправка ``embed'a``.", inline=True)
#                 embed.add_field(name="/timeloop", value="</timeloop:1058509408683950154>\nДанная ``команда`` позволит вам создать таймер, \nпо истечению которого будет отправлено сообщение.\n``P.S.``: Если оставить ``msg`` пустым - будет отправлено ``случ.`` сообщение.", inline=True)
#                 embed.add_field(name="/ben", value="</ben:1058509408579108991>\nДанная ``команда`` позволит вам задать вопрос ``Бену``.", inline=True)
#                 embed.add_field(name="/embed", value="</embed:1058509408683950157>\nДанная ``команда`` позволит вам создать ``каст.`` ``embed``.\n``P.S.``: Пункт ``embedjson`` при ``True`` выдаст вам **``json``** ``создан.`` ``embed'a``.", inline=True)
#                 embed.add_field(name="/cats", value="</cats:1058509408579108992>\nДанная ``команда`` позволит вам получить картинку ``рандомного`` ``котика``.", inline=True)
#                 embed.add_field(name="/dogs", value="</dogs:1058509408579108993>\nДанная ``команда`` позволит вам получить картинку ``рандомной`` ``собачки``.", inline=True)
#                 embed.add_field(name="/gallows", value="</gallows:1058509408579108984>\nЗапустит игру ``Виселица``.", inline=True)
#                 embed.add_field(name="/demotivator", value="</demotivator:1058509408579108984>\n Команда создаст демотиватор.", inline=True)
#                 embed.add_field(name="/help", value="</help:1058509408579108984>\nВыдаст ``вам`` это ``сообщение``.", inline=True)
#                 embed.add_field(name="/tts", value="</tts:1058509408579108984>\n Озвучит указанный вами текст.", inline=True)
#                 embed.add_field(name="WhereTrigger", value="</help:1058509408579108984>\n Найдет триггер в сообщении. \n``P.S.``: Во вкладке ``'приложения'``.", inline=True)
#                 embed.add_field(name="/trigger", value="</trigger:1058509408579108984>\n Создаст/Дополнит/Удалит ``триггер``.", inline=True)
#                 await channel.send(embed=embed)
#                 break
#             except:
#                     print("проебались")


@Bot.slash_command(description="Команда для создания демотиватора")
async def demotivator(ctx: disnake.ApplicationCommandInteraction,member:disnake.Member=commands.Param(None,description="Участник, чью аватарку использую для демотиватора."), image:disnake.Attachment=commands.Param(None,description="Вставьте изображение."), mode=commands.Param(choices=["Рандом", "Указанный текст"], description="Режим работы демотиватора"), demotivator1:str=commands.Param(None,description="Текст для заглавия демотиватора. Треб.: Нужный режим.", max_length=50), demotivator2:str=commands.Param(None,description="Текст для описания демотиватора. Треб.: Нужный режим.", max_length=50)):
    
    await ctx.response.defer()
    try:
        if member !=None and image==None:
            image=member.avatar
        if member==None and image !=None:
            image=image
        else:
            pass

        if mode=="Рандом":
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "r") as f:
                nig=json.load(f)
                allword=nig[str("allwords")]
                dem1=nig[str(random.randint(1, int(allword)))]
                dem2=nig[str(random.randint(1, int(allword)))]
        else:
            if demotivator1==None or demotivator2 ==None:
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не заполнили эти пункты ``[demotivator1, demotivator2]``", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed, ephemeral=True)
            else:
                dem1=demotivator1
                dem2=demotivator2
            
        dem = Demotivator(dem1, dem2) # 2 строчки
        dem.create(image, use_url=True,watermark="VablVable Bot", result_filename=f"{ctx.author.id}.png",delete_file=True)
        await ctx.send(file=disnake.File(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\{}.png".format(ctx.author.id)))
        os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\{}.png".format(ctx.author.id))
        try:
            os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\demotivator_picture.png")
        except:
                pass
    except Exception as e:
        print(e)
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось сгенерировать демотиватор.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)

@Bot.slash_command(description="Установить режим общения, для бота")
@commands.has_guild_permissions(administrator=True)
async def mode(ctx:disnake.ApplicationCommandInteraction, modes=commands.Param(description="Режимы", choices=["КАПС", "Смайлики", "СтРаНнЫй", "Нормальный"])):
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
        nig=json.load(f)
    if modes=="КАПС":
        nig[str("mode")] = "caps"
    if modes =="Смайлики":
        nig[str("mode")] = "emoji"
    if modes=="Нормальный":
        nig[str("mode")] = "normal"
    if modes=="СтРаНнЫй":
        nig[str("mode")] = "trslit"


        
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "w") as f:
        json.dump(nig, f, indent=4)
    embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы успешно установили режим ``{modes}`` .", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)

@Bot.slash_command(description="Управление триггерами")
@commands.has_guild_permissions(administrator=True)
async def trigger(ctx, name=commands.Param(None,description="Укажите триггер."), thetext=commands.Param(None,description="Укажите текст для ответа."),  type:str=commands.Param(description="Выберите режим.", choices=["Создать","Дополнить","Удалить"])):
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:
        try:
            prefix = json.load(f)
            alword = prefix[str("prime")]
        except:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
            pass
    if alword==True:
        ana=name.isdigit()
            
        if ana ==True:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы использовали только цифры в триггере.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            messag = await ctx.send(embed=embed,ephemeral=True)
        else:
            

            if type=="Создать" and thetext!=None:
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "r") as f:
                    nig=json.load(f)
                    nig[str(name.lower())] = thetext
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "w") as f:
                    json.dump(nig, f, indent=4)
                embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Был создан триггер ``{name}``, с содержанием ``{thetext}`` .", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed, ephemeral=True)

            elif type!="Удалить" and thetext==None:
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не заполнили пункт ``thetext``!.", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                messag = await ctx.send(embed=embed,ephemeral=True)
            elif type=="Дополнить" and thetext!=None:
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "r") as f:
                    try:
                        nig=json.load(f)
                        l=nig[str(name.lower())]
                        lis=[l]
                        lis.append(thetext)
                        lis=list(dict.fromkeys(lis))
                        nig[str(name.lower())]=lis
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "w") as f:
                            json.dump(nig, f, indent=4)
                        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Триггер ``{name}`` был дополнен. Теперь его содержание ``{lis}`` .", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.send(embed=embed, ephemeral=True)
                        
                    except:
                        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Триггера ``{name}`` нету в БД бота!.", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        messag = await ctx.send(embed=embed,ephemeral=True)
            elif type=="Удалить":
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "r") as f:
                    try:
                        nig=json.load(f)
                        nig.pop(str(name.lower()))
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "w") as f:
                            json.dump(nig, f, indent=4)
                        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Триггер ``{name}`` был удален.", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.send(embed=embed, ephemeral=True)
                            
                    except:
                        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Триггера ``{name}`` нету в БД бота!.", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        messag = await ctx.send(embed=embed,ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        pass
            

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "Пожалуйста укажите **аргументы**.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.reply(embed=embed)
        await messag.add_reaction("❌")
    if isinstance(error, commands.MissingPermissions):
        embed = disnake.Embed(title = "**Ошибка! ❌**",description = "**Вы** не имеете права на эту команду.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.reply(embed=embed)
        await messag.add_reaction("❌")
    if isinstance(error, commands.CommandOnCooldown):
        embed = disnake.Embed(color=0x42aaff)
        embed.title = "**Ошибка! ❌**"
        embed.description = f"Команда находится на задержке, повторите через **{error.retry_after :.0f}** секунд"
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.reply(embed=embed)
        await messag.add_reaction("❌")
    if isinstance(error, commands.BotMissingPermissions):
        embed = disnake.Embed(color=0x42aaff)
        embed.title = "**Ошибка! ❌**"
        embed.description = f"У **``VablVable Bot``** недостаточно прав."
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.reply(embed=embed)
        await messag.add_reaction("❌")

# @Bot.slash_command(description="Получить информацию о всех командах")
# async def help(ctx):
#         embed= disnake.Embed(title="Информация о командах VablVable Bot!")
#         embed.add_field(name="/setchannel",value="</setchannel:1058509408579108987>\nДанная ``команда`` позволит вам установить ``канал`` для\n``общения`` с ботом.\n В ``указан.`` канале бот будет читать и отправлять сообщения.", inline=True)
#         embed.add_field(name="/reset", value="</reset:1058509408579108990>\nДанная ``команда`` **``обнулит``** словарный запас бота на вашем сервере.\nИспользуйте ее, в **крайнем** случае!",inline=True)
#         embed.add_field(name="/datatime", value="</datatime:1058509408683950158>\nданная ``команда`` выдаст указан. время.\n ``P.S.``: Если оставить пустым - выдаст точную дату момента написания команды.", inline=True)
#         embed.add_field(name="/code", value="</code:1058509408683950151>\nДанная ``команда`` закодирует ``указан.`` сообщениe.\n``P.S.``: Есть во вкладе ``'Приложения'``.", inline=True)
#         embed.add_field(name="/uncode", value="</uncode:1058509408683950152>\n Данная ``команда`` раскодирует ``указан.`` сообщение.\n``P.S.``: Есть во вкладе ``'Приложения'``. ", inline=True)
#         embed.add_field(name="/report", value="</report:1058494331914309812>\nДанная ``команда`` позволит вам связаться с разработчиком.\n``P.S.``: Использовать по назначению!", inline=True)
#         embed.add_field(name="/auto-gen-message", value="</auto-gen-message:1058509408579108985>\nДанная ``команда`` установит шанс отправки случ. сообщения.\n``P.S.``: Работает только в ``указ.`` канале.", inline=True)
#         embed.add_field(name="/deleteping", value="</deleteping:1058509408579108989>\nДанная ``команда`` удалит ваш пинг из БД данного сервера.", inline=True)
#         embed.add_field(name="/deleteword", value="</deleteword:1058509408579108988>\nДанная ``команда`` удалит ``опр.`` слово из БД данного сервера.", inline=True)
#         embed.add_field(name="/avatar", value="</avatar:1058509408683950153>\nДанная ``команда`` позволит вам получит аватар ``указ.`` пользователя.\n``P.S.``: Есть во вкладе ``'Приложения'``.", inline=True)
#         embed.add_field(name="/usersay", value="</usersay:1058509408683950156>\nДанная ``команда`` позволит вам написать от лица ``указ.`` пользователя.\n``P.S.``: Присутствует отправка ``embed'a``.", inline=True)
#         embed.add_field(name="/say", value="</say:1058509408683950155>\nДанная ``команда`` позволит вам написать от лица бота.\n``P.S``: Присутствует отправка ``embed'a``.", inline=True)
#         embed.add_field(name="/timeloop", value="</timeloop:1058509408683950154>\nДанная ``команда`` позволит вам создать таймер, \nпо истечению которого будет отправлено сообщение.\n``P.S.``: Если оставить ``msg`` пустым - будет отправлено ``случ.`` сообщение.", inline=True)
#         embed.add_field(name="/ben", value="</ben:1058509408579108991>\nДанная ``команда`` позволит вам задать вопрос ``Бену``.", inline=True)
#         embed.add_field(name="/embed", value="</embed:1058509408683950157>\nДанная ``команда`` позволит вам создать ``каст.`` ``embed``.\n``P.S.``: Пункт ``embedjson`` при ``True`` выдаст вам **``json``** ``создан.`` ``embed'a``.", inline=True)
#         embed.add_field(name="/cats", value="</cats:1058509408579108992>\nДанная ``команда`` позволит вам получить картинку ``рандомного`` ``котика``.", inline=True)
#         embed.add_field(name="/dogs", value="</dogs:1058509408579108993>\nДанная ``команда`` позволит вам получить картинку ``рандомной`` ``собачки``.", inline=True)
#         embed.add_field(name="/gallows", value="</gallows:1058509408579108984>\nЗапустит игру ``Виселица``.", inline=True)
#         embed.add_field(name="/demotivator", value="</demotivator:1058509408579108984>\n Команда создаст демотиватор.", inline=True)
#         embed.add_field(name="/help", value="</help:1058509408579108984>\nВыдаст ``вам`` это ``сообщение``.", inline=True)
#         embed.add_field(name="/tts", value="</tts:1058509408579108984>\n Озвучит указанный вами текст.", inline=True)
#         embed.add_field(name="WhereTrigger", value="</help:1058509408579108984>\n Найдет триггер в сообщении. \n``P.S.``: Во вкладке ``'приложения'``.", inline=True)
#         embed.add_field(name="/trigger", value="</trigger:1058509408579108984>\n Создаст/Дополнит/Удалит ``триггер``.", inline=True)
        

#         await ctx.send(embed=embed, ephemeral=True)
#@Bot.slash_command(test_guilds=[1047132110391095407])
#async def happynewyear(ctx, msg):
#        await ctx.send("Начали!")
#        limit=0
#        for guild in Bot.guilds:
#                for channel in guild.text_channels:
#                        limit=limit+1
#                        try:
#                                embed = disnake.Embed(title = "С новым годом!", description = f"Дорогие ``участники`` этого **сервера**! **Я** признателен __``вам``__, что вы **добавили** ``VablVable Bot`` на этот **сервер**. Хочу __**поздравить**__ вас с Новым, **2023** Годом! ``2022`` год был **не удачным**, но не будем долго о ~~``плохом``~~!\nЕсли у вас случилось что-то **хорошее**, пусть оно так и **``остается``**! Забудем все **плохое**.", color=0x42aaff)
#                                embed.set_footer(text=f"С любовью и признанием от {ctx.author} .", icon_url=ctx.author.avatar)
#                                lol= await Bot.fetch_user(1045034649379950622)
#
#                                embed.set_image(url="https://cdn-images-1.medium.com/max/1600/1*bwdDFgLHb7IZiU0qdN7MJQ.gif")
#                                await channel.send(embed=embed)
#                                print(f"Гуд, {channel.name}, {channel.id}, {guild.name}")
#                                break
#                        except:
#                                if limit>30:
#                                        break
#                                else:
#                                        print(f"проебались, {channel.name}, {channel.id}, {guild.name}")



@Bot.slash_command(name="auto-gen-message", description="Установить шанс отправки рандомного сообщения")
@commands.has_guild_permissions(administrator=True)
async def au(ctx, speed:int=commands.Param(None,description="Укажите шанс, при котором отправится сообщение.")):
    if speed==None:

        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
            prefix = json.load(f)
            prefix[str("autogen")] = None
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** отключили автогенерацию сообщений", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        if speed>100:
            speed=100
            embed = disnake.Embed(title = "**Внимание! ⚠️**", description = f"Т.к. Вы установили число более ``100``, бот автоматически исправил это на ``100``.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)

    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
            prefix = json.load(f)
            prefix[str("autogen")] = int(speed)
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
            json.dump(prefix, f, indent=4)
    embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** изменили скорость автогенерации сообщений на``{speed}``", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)
@Bot.event
async def on_member_update(before, after):
    try:
        async for entry in before.guild.audit_logs(limit=1, action=disnake.AuditLogAction.member_role_update):
            role = disnake.utils.get(before.guild.roles, id=1068238296326623362)
    except: 
        print("fuck nigga")
        pass
    if before.roles != after.roles:
        if role in after.roles:
            if role in before.roles:
                print("fuck nigga")

                pass
            else:
                sas = {
                        "status":True,
                        "primes":2
                }
                async for entry in before.guild.audit_logs(limit=1, action=disnake.AuditLogAction.member_role_update):
                    open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(entry.target.id), 'x') 

                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(entry.target.id), 'w', encoding="utf-8") as f:
                        json.dump(sas, f)
    
        if role not in after.roles:
                if role in before.roles:
                    os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(entry.target.id))
                                                    


@Bot.event
async def on_ready():
    
    status.start()
    clearvip.start()
    
    print("LOOOOOOOOOOOOOOOOL")




@tasks.loop(seconds=15)
async def status():


    await Bot.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"Документации, чтобы стать умным"))
    await asyncio.sleep(15)
    await Bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(name=f"Зайдите на сервер поддержки!!!",type=disnake.ActivityType.competing))
    await asyncio.sleep(15)
    await Bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.playing, name=f"бравл старс"))
    await asyncio.sleep(15)

    await Bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(name="Проблемы? /report!", type=disnake.ActivityType.watching))
    await asyncio.sleep(20)






   

        






@Bot.slash_command(description="Указать, канал для чтения и отправки сообщений")

@commands.has_guild_permissions(administrator=True)
async def setchannel(ctx, allchannel:bool=commands.Param(False,description="Будет ли бот читать и отправлять сообщения во всех каналах?")):
    if allchannel==True:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
                prefix = json.load(f)
                prefix[str("channel")] = allchannel
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Бот читает и отвечает в каждом канале.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'r') as f:
                prefix = json.load(f)
                prefix[str("channel")] = int(ctx.channel.id)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** изменили канал на <#{ctx.channel.id}>.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)

@Bot.slash_command(description="Удалить определенное слово из БД бота")
@commands.has_guild_permissions(administrator=True)
async def deleteword(ctx, theword=commands.Param(description="Текст/Слово для удаления.")):

    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), 'r') as f:
            prefix = json.load(f)
    total = None
    for key in prefix:            
        text=prefix[key]
        text=str(text)
        if theword in text:

            print("я тупой полудурок")

            print(text)
            s=text.replace(theword, "")
            prefix[key]=s
            total=+1
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), 'w') as f:
                    json.dump(prefix, f, indent=4)
    if total!=None:

        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"``{theword}`` Успешно удален из бд бота.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    elif total==None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"``{theword}`` нету в БД бота.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.send(embed=embed,ephemeral=True)



@Bot.slash_command(description="Удалить свой пинг из бд бота")

async def deleteping(ctx):
    theword=f"<@{ctx.author.id}>"

    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), 'r') as f:
            prefix = json.load(f)
    total = None
    for key in prefix:            
        text=prefix[key]
        text=str(text)
        if theword in text:

            print("я тупой полудурок")

            print(text)
            s=text.replace(theword, "")
            prefix[key]=s
            total=key
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), 'w') as f:
                    json.dump(prefix, f, indent=4)
    if total!=None:

        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Ваше упоминание было удалено из БД. .", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    elif total==None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вашего пинга нет в БД", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        messag = await ctx.send(embed=embed,ephemeral=True)

@Bot.slash_command(description="Озвучить текст в формат .mp3")
async def tts(ctx:disnake.ApplicationCommandInteraction, text:str=commands.Param(None,max_length=500, description="Что вы хотите воспроизвести "), slow:bool= commands.Param(False, description="Будет ли текст воспроизводиться медленно?"), lang=commands.Param(choices=["ru", "en"], description="Выберите язык для озвучки"), gen:bool=commands.Param(False, description="Слова сами сгенерируются?")):
    if gen is True:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "r") as f:
            nig=json.load(f)
            allword=nig[str("allwords")]
            text=nig[str(random.randint(1, int(allword)))]
    if gen is False and text ==None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** оставилипустым пункт ``text``.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else: 
        text=text

    await ctx.response.defer()
    obj = gTTS(text=text, lang=lang, slow=slow) 
    print("mandsa")

    adsdsa=obj.save(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\{}.mp3".format(ctx.author.id)) 



    await ctx.send(file=disnake.File(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\{}.mp3".format(ctx.author.id)))
    os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\{}.mp3".format(ctx.author.id))





@Bot.slash_command(description="Обнулить словарный запас бота")
@commands.has_guild_permissions(administrator=True)
async def reset(ctx):
    embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Словарный запас бота был удален.", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)
    sas = {
            "allwords": 0
    }

    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id), "w", encoding="utf-8") as file:
            json.dump(sas, file)
        
        


  



@Bot.slash_command(description="Задать вопрос бену")

async def ben(ctx, question:str=commands.Param(description="Что вы хотите спросить?")):
    frog = ["``Yes``", "``No``", "``Ho Ho Ho``", "*``Oтрыжка``*"]
    r=random.choice(frog)
    embed = disnake.Embed(title = f"**{r}**", description = f"", color=0x42aaff)

    await ctx.send(embed=embed, ephemeral=True)




   
        
            
@Bot.slash_command(description="Коты")
async def cats(ctx): 
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/cat') # Make a request
        catjson = await request.json()

    embed = disnake.Embed (color=0x42aaff)
    embed.set_image(url=catjson['link'])

    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)


@Bot.slash_command(description="Собаки")
async def dogs(ctx): 
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog') # Make a request
        catjson = await request.json()

    embed = disnake.Embed (color=0x42aaff)
    embed.set_image(url=catjson['link'])

    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)


@Bot.slash_command(description="Закодировать текст")
async def code(ctx, *,code:str=commands.Param(description="Текст для кодировки.")):
    def multiple_replace(target_str, replace_values):
            # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
        # меняем все target_str на подставляемое
                target_str = target_str.replace(i, j)
        return target_str

                            # создаем словарь со значениями и строку, которую будет изменять
    replace_values = {"А": "323.=", "Б": "356.=" , "В": "395.=", "Г": "923.=" , "Д": "921.=" , "Е": "012.=" , "Ё": "502.=" , "Ж": "566.=" , "З": "590.=" , "И": "624.=" , "Й": "603.=" , "К": "202.=" , "Л": "620.=" , "М": "6231.=" , "Н": "099.=" , "О": "239.=" , "П": "124.=" , "Р": "129.=" , "С": "7422.=" , "Т": "822.=" , "У": "9652.=" , "Ф": "009.=" , "Х": "654.=" , "Ц": "742.=" , "Ч": "0025.=", "Ш": "0233.=", "Щ": "0234.=" , "Ъ": "0235.=" , "Ы": "0236.=" , "Ь": "0237.=" , "Э": "0238.=", "Ю": "02359.=", "Я": "0249.=","а": "323==", "б": "356==" , "в": "395==", "г": "923==" , "д": "921==" , "е": "012==" , "ё": "502==" , "ж": "566==" , "з": "590==" , "и": "624==" , "й": "603==" , "к": "202==" , "л": "620==" , "м": "6231==" , "н": "099==" , "о": "239==" , "п": "124==" , "р": "129==" , "с": "7482==" , "т": "822==" , "у": "9652==" , "ф": "009==" , "х": "654==" , "ц": "742==" , "ч": "0025==", "ш": "0233==", "щ": "0234==" , "ъ": "0235==" , "ы": "0236==" , "ь": "0237==" , "э": "0238==", "ю": "02359==", "я": "0249==","A": "323.", "B": "356." , "C": "395.", "D": "923." , "E": "921." , "F": "012." , "G": "502." , "H": "566." , "I": "590." , "J": "624." , "K": "603." , "L": "202." , "M": "620." , "N": "6231." , "O": "099." , "P": "239." , "Q": "124." , "R": "129." , "S": "782." , "T": "822." , "U": "9652." , "V": "009." , "W": "654." , "X": "742." , "Y": "0025.", "Z": "023.", " ": "0.", "-": "00000.", "_": "90000.", "a": "323,", "b": "356," , "c": "395,", "d": "923," , "e": "921," , "f": "012," , "g": "502," , "h": "566," , "i": "590," , "j": "624," , "k": "603," , "l": "202," , "m": "620," , "n": "6231," , "o": "099," , "p": "239," , "q": "124," , "r": "129," , "s": "7422," , "t": "822," , "u": "9652," , "v": "009," , "w": "654," , "x": "742," , "y": "0025,", "z": "023,", }
    code = multiple_replace(code, replace_values)
    embed = disnake.Embed(title = "**Успешно!✅**", description = f"**``Сообщение``** было закодированно.\n Результат: **``{code}``**", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)


@Bot.slash_command(description="Раскодировать текст")
async def uncode(ctx, *, uncode: str=commands.Param(description="Текст для раскодировки.")):
    def multiple_replace(target_str, replace_values):
                        # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
                # меняем все target_str на подставляемое
                target_str = target_str.replace(i, j)
        return target_str
    replace_values = {"323.=": "А", "356.=": "Б" , "395.=": "В", "923.=": "Г" , "921.=": "Д" , "012.=": "Е" , "502.=": "Ё" , "566.=": "Ж" , "590.=": "З" , "624.=": "И" , "603.=": "Й" , "202.=": "К" , "620.=": "Л" , "6231.=": "М" , "099.=": "Н" , "239.=": "О" , "124.=": "П" , "129.=": "Р" , "7422.=": "С" , "822.=": "Т" , "9652.=": "У" , "009.=": "Ф" , "654.=": "Х" , "742.=": "Ц" , "0025.=": "Ч", "0233.=": "Ш", "0234.=": "Щ","0235.=": "Ъ","0236.=": "Ы","0237.=": "Ь","0238.=": "Э","02359.=": "Ю","0249.=": "Я", "323==": "а", "356==": "б" , "395==": "в", "923==": "г" , "921==": "д" , "012==": "е" , "502==": "ё" , "566==": "ж" , "590==": "з" , "624==": "и" , "603==": "й" , "202==": "к" , "620==": "л" , "6231==": "м" , "099==": "н" , "239==": "о" , "124==": "п" , "129==": "р" , "7482==": "с" , "822==": "т" , "9652==": "у" , "009==": "Ф" , "654==": "х" , "742==": "ц" , "0025==": "ч", "0233==": "ш", "0234==": "щ","0235==": "ъ","0236==": "ы","0237==": "ь","0238==": "э","02359==": "ю","0249==": "я", "323.": "A", "356.": "B" , "395.": "C", "923.": "D" , "921.": "E" , "012.": "F" , "502.": "G" , "566.": "H" , "590.": "I" , "624.": "J" , "603.": "K" , "202.": "L" , "620.": "M" , "6231.": "N" , "099.": "O" , "239.": "P" , "124.": "Q" , "129.": "R" , "782.": "S" , "822.": "T" , "9652.": "U" , "009.": "V" , "654.": "W" , "742.": "X" , "0025.": "Y", "023.": "Z", "0.": " ","00000.": "-", "90000.": "_","323,": "a", "356,": "b" , "395,": "c", "923,": "d" , "921,": "e" , "012,": "f" , "502,": "g" , "566,": "h" , "590,": "i" , "624,": "j" , "603,": "k" , "202,": "l" , "620,": "m" , "6231,": "n" , "099,": "o" , "239,": "p" , "124,": "q" , "129,": "r" , "7422,": "s" , "822,": "t" , "9652,": "u" , "009,": "v" , "654,": "w" , "742,": "x" , "0025,": "y", "023,": "z", }

    uncode = multiple_replace(uncode, replace_values)
    embed = disnake.Embed(title = "**Успешно!✅**", description = f"**``Сообщение``** было раскодированно.\n Результат: **``{uncode}``**", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)


@Bot.slash_command(description="Получить аватар пользователя")
async def avatar(ctx, member: disnake.Member =commands.Param(None,description="Чьу аватарку вы хотите получить?")):
    if member == None:
        member = ctx.author
        embed = disnake.Embed(title = f"**Аватар пользователя {member.name}!**", description = f"Аватар пользователя {member.mention}, [**Открыть**]({member.avatar})", color=0x42aaff)
        embed.set_image(url=member.avatar)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        
    else:
        
        embed = disnake.Embed(title = f"**Аватар пользователя {member.name}!**", description = f"Аватар пользователя {member.mention}, [**Открыть**]({member.avatar})", color=0x42aaff)
        embed.set_image(url=member.avatar)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)

@Bot.slash_command(description="Запустить таймер")
async def timeloop(ctx, time: str =commands.Param(description="Через сколько сработает таймер? Формат (1s/1m/1h/1d)"), *,msg: str=commands.Param(description="Отправить ли свое сообщение по истечению таймера?")):
    if msg == None:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(ctx.guild.id),"r") as f:
            prefix = json.load(f)
            alword = prefix[str("allwords")]
            ps = prefix[str(random.randint(1, alword))]
    else:
        ps = msg

    if len(ps) > 150:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** привысили лимит допустимых символов.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)


    if time is None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** не указали время.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    
    else:
        try:
            seconds = int(time[:-1])
            duration = time[-1]
            durations = time[-1]
            second = seconds
            if duration == "s" or duration==None:
                    durations="Секунд"
                    pass
            if duration == "m":
                    seconds *= 60
                    durations="Минут"
            if duration == "h":
                    durations="Часов"
                    seconds *= 3600
            if duration == "d":
                    durations="Дней"
                    seconds *= 86400
        except:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** не поставили декоратор ``s``/``m``/``h``/``d``.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
            pass
        timse = datetime.now() + timedelta(seconds=seconds)

        time=(disnake.utils.format_dt(timse, "R"))
        embed = disnake.Embed(title = "**Успешно!✅**", description = f"``Отсчет`` начался,  {time} ``отсчет`` будет завершен.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        print(f"{second} {seconds} {duration}")
        await asyncio.sleep(seconds)

        embed = disnake.Embed(title = "**Успешно!✅**", description = f"По истечению ``{second} {durations}``, я хочу вам сказать ``{ps}``", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
        


@Bot.user_command(name="avatar")
async def avatar(ctx, member: disnake.User):
    embed = disnake.Embed(title = f"**Аватар пользователя {member.name}!**", description = f"Аватар пользователя {member.mention}, [**Открыть**]({member.avatar})", color=0x42aaff)
    embed.set_image(url=member.avatar)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)
# @Bot.message_command(name="WhereTrigger")
# async def code(ctx, code: disnake.Message):

        
#     print(code.content)
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:
#         asr=json.load(f)
#     total=[]
#     for a in asr:
#         print(a)
        

#         print("ПРАШОЛО")
#         print(f"{a}=={code.content}")
#         if str(a) in str(code.content.lower()):
#             total.append(a)
#             print("ИН")
#         if str(a) ==str(code.content.lower()):
#             print("РАВН")
#             total.append(a)

    

#     if total!=[]:
        
#         embed = disnake.Embed(title = f"Найден триггер!✅", description = f"Название триггера в данном сообщении - ``{total}``", color=0x42aaff)

#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
#     else:
#         embed = disnake.Embed(title = "**Ошибка! ❌**", description = "В этом сообщении нету триггера.", color=0x42aaff)
#         embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed, ephemeral=True)
#     print(total)
            
@Bot.message_command(name="Code")
async def code(ctx, code: disnake.Message):
    def multiple_replace(target_str, replace_values):
            # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
        # меняем все target_str на подставляемое
                target_str = target_str.replace(i, j)
        return target_str

                            # создаем словарь со значениями и строку, которую будет изменять
    replace_values = {"А": "323.=", "Б": "356.=" , "В": "395.=", "Г": "923.=" , "Д": "921.=" , "Е": "012.=" , "Ё": "502.=" , "Ж": "566.=" , "З": "590.=" , "И": "624.=" , "Й": "603.=" , "К": "202.=" , "Л": "620.=" , "М": "6231.=" , "Н": "099.=" , "О": "239.=" , "П": "124.=" , "Р": "129.=" , "С": "7422.=" , "Т": "822.=" , "У": "9652.=" , "Ф": "009.=" , "Х": "654.=" , "Ц": "742.=" , "Ч": "0025.=", "Ш": "0233.=", "Щ": "0234.=" , "Ъ": "0235.=" , "Ы": "0236.=" , "Ь": "0237.=" , "Э": "0238.=", "Ю": "02359.=", "Я": "0249.=","а": "323==", "б": "356==" , "в": "395==", "г": "923==" , "д": "921==" , "е": "012==" , "ё": "502==" , "ж": "566==" , "з": "590==" , "и": "624==" , "й": "603==" , "к": "202==" , "л": "620==" , "м": "6231==" , "н": "099==" , "о": "239==" , "п": "124==" , "р": "129==" , "с": "7482==" , "т": "822==" , "у": "9652==" , "ф": "009==" , "х": "654==" , "ц": "742==" , "ч": "0025==", "ш": "0233==", "щ": "0234==" , "ъ": "0235==" , "ы": "0236==" , "ь": "0237==" , "э": "0238==", "ю": "02359==", "я": "0249==","A": "323.", "B": "356." , "C": "395.", "D": "923." , "E": "921." , "F": "012." , "G": "502." , "H": "566." , "I": "590." , "J": "624." , "K": "603." , "L": "202." , "M": "620." , "N": "6231." , "O": "099." , "P": "239." , "Q": "124." , "R": "129." , "S": "782." , "T": "822." , "U": "9652." , "V": "009." , "W": "654." , "X": "742." , "Y": "0025.", "Z": "023.", " ": "0.", "-": "00000.", "_": "90000.", "a": "323,", "b": "356," , "c": "395,", "d": "923," , "e": "921," , "f": "012," , "g": "502," , "h": "566," , "i": "590," , "j": "624," , "k": "603," , "l": "202," , "m": "620," , "n": "6231," , "o": "099," , "p": "239," , "q": "124," , "r": "129," , "s": "7422," , "t": "822," , "u": "9652," , "v": "009," , "w": "654," , "x": "742," , "y": "0025,", "z": "023,", }
    code = multiple_replace(code.content, replace_values)
    embed = disnake.Embed(title = "**Успешно!✅**", description = f"**``Сообщение``** было закодированно.\n Результат: **``{code}``**", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)

@Bot.message_command(name="Uncode")
async def uncode(ctx, uncode: disnake.Message):
    def multiple_replace(target_str, replace_values):
                            # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
                # меняем все target_str на подставляемое
                target_str = target_str.replace(i, j)
        return target_str
    replace_values = {"323.=": "А", "356.=": "Б" , "395.=": "В", "923.=": "Г" , "921.=": "Д" , "012.=": "Е" , "502.=": "Ё" , "566.=": "Ж" , "590.=": "З" , "624.=": "И" , "603.=": "Й" , "202.=": "К" , "620.=": "Л" , "6231.=": "М" , "099.=": "Н" , "239.=": "О" , "124.=": "П" , "129.=": "Р" , "7422.=": "С" , "822.=": "Т" , "9652.=": "У" , "009.=": "Ф" , "654.=": "Х" , "742.=": "Ц" , "0025.=": "Ч", "0233.=": "Ш", "0234.=": "Щ","0235.=": "Ъ","0236.=": "Ы","0237.=": "Ь","0238.=": "Э","02359.=": "Ю","0249.=": "Я", "323==": "а", "356==": "б" , "395==": "в", "923==": "г" , "921==": "д" , "012==": "е" , "502==": "ё" , "566==": "ж" , "590==": "з" , "624==": "и" , "603==": "й" , "202==": "к" , "620==": "л" , "6231==": "м" , "099==": "н" , "239==": "о" , "124==": "п" , "129==": "р" , "7482==": "с" , "822==": "т" , "9652==": "у" , "009==": "Ф" , "654==": "х" , "742==": "ц" , "0025==": "ч", "0233==": "ш", "0234==": "щ","0235==": "ъ","0236==": "ы","0237==": "ь","0238==": "э","02359==": "ю","0249==": "я", "323.": "A", "356.": "B" , "395.": "C", "923.": "D" , "921.": "E" , "012.": "F" , "502.": "G" , "566.": "H" , "590.": "I" , "624.": "J" , "603.": "K" , "202.": "L" , "620.": "M" , "6231.": "N" , "099.": "O" , "239.": "P" , "124.": "Q" , "129.": "R" , "782.": "S" , "822.": "T" , "9652.": "U" , "009.": "V" , "654.": "W" , "742.": "X" , "0025.": "Y", "023.": "Z", "0.": " ","00000.": "-", "90000.": "_","323,": "a", "356,": "b" , "395,": "c", "923,": "d" , "921,": "e" , "012,": "f" , "502,": "g" , "566,": "h" , "590,": "i" , "624,": "j" , "603,": "k" , "202,": "l" , "620,": "m" , "6231,": "n" , "099,": "o" , "239,": "p" , "124,": "q" , "129,": "r" , "7422,": "s" , "822,": "t" , "9652,": "u" , "009,": "v" , "654,": "w" , "742,": "x" , "0025,": "y", "023,": "z", }

    uncode = multiple_replace(uncode.content, replace_values)
    embed = disnake.Embed(title = "**Успешно!✅**", description = f"**``Сообщение``** было раскодированно.\n Результат: **``{uncode}``**", color=0x42aaff)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed, ephemeral=True)





@Bot.slash_command(description="Сказать что-то от имени бота")
async def say(ctx, msg: str=commands.Param(None,description="Обычное сообщение, что вы хотите сказать?"), embedjson=commands.Param(None,description="Код от эмбед сообщения. ")):
    if embedjson==None and msg==None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** оставили пустыми все пункты", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    if embedjson==None:
        await ctx.send(msg)
    else:
        embedjson=ast.literal_eval(embedjson)
        await ctx.send(msg,embed=disnake.Embed.from_dict(embedjson))
                
@Bot.slash_command(description="Выдать серверу premium статус.")
async def subscribe(ctx: disnake.ApplicationCommandInteraction):
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(ctx.author.id), "r") as f:
            prefix = json.load(f)
            userprime=prefix[str("status")]
            sprime=prefix[str("primes")]
                    
    except:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У вас нету ``premium``.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)

        await ctx.send(embed=embed,
        
        components=[
                disnake.ui.Button(label="Информация о premium", style=disnake.ButtonStyle.grey,emoji="💲", custom_id="Buy")
        ],  ephemeral=True)
        pass
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
            prefix = json.load(f)
            thisprem=prefix[str("prime")]
    except:
        thisprem=False
                
                        

    if userprime == True and sprime!=0:
        if thisprem==False:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(ctx.author.id), "r") as f:
                prefix = json.load(f)
                sprime=prefix[str("primes")]
                sprime-=1
                prefix[str("primes")]= sprime
                    
            
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\prime\{}.json".format(ctx.author.id), 'w') as f:
                json.dump(prefix, f, indent=4)

            bebra=datetime.now() + timedelta(days=30)
            tt=bebra.strftime("%Y-%m-%d")
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), "r") as f:
                prefix = json.load(f)
                prefix[str("prime")]=True
                prefix[str("date")]=f"{tt}"
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)
                

            d=disnake.utils.format_dt(datetime.now() + timedelta(days=30), "D")
            r=disnake.utils.format_dt(datetime.now() + timedelta(days=30), "R")
            embed = disnake.Embed(title = "**Успешно!✅**", description = f"``Вы`` успешно выдали ``{ctx.guild.name}`` premium!", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
            owner = await Bot.fetch_user(ctx.guild.owner_id)
            embed = disnake.Embed(title = "**Вам выдали премиум!✅**", description = f"{owner.mention}, Поздравляем!\n Вашему серверу  выдали ``premium``. ", color=0x42aaff)
            embed.add_field(name="Выдал:", value=f"{ctx.author.mention}\n(``{ctx.author.id}``) ",inline=True)
            embed.add_field(name="Окончание:", value=f"{d}\n{r}", inline=True)
            embed.set_footer(text=f"{ctx.guild.name} .", icon_url=ctx.guild.icon)
            embed.set_thumbnail(url=Bot.user.avatar)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
            await owner.send(embed=embed)
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, уже имеет premium.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У вас нету ``gift-premium``.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed,                components=[
                disnake.ui.Button(label="Информация о premium", style=disnake.ButtonStyle.grey,emoji="💲", custom_id="Buy")
        ], ephemeral=True)
                


@tasks.loop(hours=1)
async def clearvip():

    for a in Bot.guilds:
        try:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(a.id), "r") as f:
                prefix = json.load(f)
                stat=prefix[str("prime")]
                data=prefix[str("date")]
                
            if stat is True:
                if datetime.strptime(data,  "%Y-%m-%d") < datetime.today().strftime("%Y-%m-%d"):
                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(a.id), "r") as f:
                        prefix = json.load(f)
                        prefix[str("prime")]=False
                        prefix.pop("date")
                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(a.id), 'w') as f:
                        json.dump(prefix, f, indent=4)
        except:
            pass


        


@Bot.slash_command(description="Написать что-то от лица пользователя")
async def usersay(ctx, member:disnake.Member=commands.Param(description="От чьего лица вы хотите написать?"), message:str=commands.Param(None,description="Что вы хотите написать"), embedjson=commands.Param(None,description="Код от эмбед сообщения. ")):

    if embedjson==None and message==None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** оставили пустыми все пункты", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    if embedjson==None:


        webhok=await ctx.channel.create_webhook(name="USERSAY")



        await webhok.send(content=message, username=member.name, avatar_url=member.avatar)
        embed = disnake.Embed(title = "**Успешно!✅**", description = f"``Сообщение`` успешно отправлено!.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        await webhok.delete()
    else:
        embedjson=ast.literal_eval(embedjson)

        webhok=await ctx.channel.create_webhook(name="USERSAY")



        await webhok.send(content=message,embed=disnake.Embed.from_dict(embedjson), username=member.name, avatar_url=member.avatar)
        embed = disnake.Embed(title = "**Успешно!✅**", description = f"``Сообщение`` успешно отправлено!.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        await webhok.delete()


                

@Bot.message_command(name="Reverse")
async def reverse(ctx, message: disnake.Message):
    await ctx.send(message.content[::-1],ephemeral=True)

@Bot.message_command(name="Embed")
async def embed(ctx, message: disnake.Message):
    if message.embeds:
        embed = disnake.Embed(title = "Json от embed'a", description = f"```{message.embeds[0].to_dict()}```", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = "Данное сообщение не имеет embed'a!", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)







@Bot.slash_command(description="Отправить embed сообщение")
async def embed(ctx,embedjson:bool=commands.Param( description="Хотите получить json ембед'a?"), title:str=commands.Param("", description="Самый верхний текст embed'a."),description:str=commands.Param("", description="Описание embed'a."),image:disnake.Attachment=commands.Param("", description="Центральная картинка embed'a."), thumbnail:disnake.Attachment=commands.Param("", description="Картинка в правом верхнем углу embed'a."), footer:str=commands.Param("", description="Текст для футера embed'a."), footerimg:disnake.Attachment=commands.Param("", description="Картинка для футераembed'а."),author:str=commands.Param("", description="Текст для верхнего `футера` embed'a."), authorimg:disnake.Attachment=commands.Param("", description="Картинка для верхнего `футера` embed'a."), color:str=commands.Param(description="Цвет embed'a",choices=["Красный","Оранжевый","Желтый","Зеленый","Голубой","Синий","Фиолетовый", "Серый", "Черный","Розовый","Белый"])):
    if color=="Красный":
        recolor=0xff0000
    elif color=="Оранжевый":
        recolor=0xffa500
    elif color=="Желтый":
        recolor=0xffff00
    elif color=="Зеленый":
        recolor=0x008000
    elif color=="Голубой":
        recolor=0x42aaff
    elif color=="Синий":
        recolor=0x0000ff     
    elif color=="Фиолетовый":
        recolor=0x8b00ff
    elif color=="Серый":
        recolor=0x808080
    elif color=="Черный":
        recolor=0x000000     
    elif color=="Белый":
        recolor=0xFFFFFF
    elif color=="Розовый":
        recolor=0xffc0cb
    
        

    
    
    embed=disnake.Embed(title=title, description=description, color=recolor)
    embed.set_thumbnail(url=thumbnail)
    embed.set_image(url=image)
    embed.set_author(icon_url=authorimg, name=author)
    embed.set_footer(icon_url=footerimg,text=footer)
    await ctx.send(embed=embed)
    if embedjson==True:
        embeds=disnake.Embed(description=f"```{embed.to_dict()}```", title="Json от ембеда", color=0x42aaff)
        await ctx.send(embed=embeds, ephemeral=True)
    else:
        pass
    

@Bot.slash_command(description="Получить дату в формате <t:>")
async def datatime(ctx, year:int=commands.Param(2023,description="Укажите год"), month:int=commands.Param(1,description="Укажите месяц"), day:int=commands.Param(1,description="Укажите день"), hour:int=commands.Param(00,description="Укажите час"),minute:int=commands.Param(00,description="Укажите минуту")):
        try:
            if year==2022 and month ==1 and day==1 and hour==00 and minute==00:

                    d1=datetime.now()

                    
            else:
                    d1 = td.datetime(year, month, day, hour, minute)
                    

            d=disnake.utils.format_dt(d1, "d")
            D=disnake.utils.format_dt(d1, "D")
            t=disnake.utils.format_dt(d1, "t")
            T=disnake.utils.format_dt(d1, "T")
            f=disnake.utils.format_dt(d1, "f")
            F=disnake.utils.format_dt(d1, "F")
            R=disnake.utils.format_dt(d1, "R")
            embed = disnake.Embed(title=f"Datatime ``{d1}``", description=f"**``{d}``** = {d}\n\n**``{D}``** = {D}\n\n**``{t}``** = {t}\n\n**``{T}``** = {T}\n\n**``{f}``** = {f}\n\n**``{F}``** = {F}\n\n**``{R}``** = {R}",color=0x42aaff)
            await ctx.send(embed=embed, ephemeral=True)
        except:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = "**``Вы``** указали неверные параметры!", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)






  







        












class MyModal(disnake.ui.Modal):
    def __init__(ctx):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Название проблемы",
                placeholder="Бот выключен",
                custom_id="Название:",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Описание проблемы",
                placeholder="Бот выключен, что делат, зачем и почему?",
                custom_id="Описание:",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(
            title="Отправить",
            custom_id="create_discriminator",
            components=components,
        )

    # The callback received when the user input is completed.
    async def callback(ctx, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Содержание")
        embed.add_field(
        name="Отправил:",
        value=f"{inter.author.name}{inter.author.discriminator}``({inter.author.id})``",
        inline=False,)
        fuck=disnake.utils.format_dt(datetime.now(), "R")
        niga=disnake.utils.format_dt(datetime.now(), "f")
        embed.add_field(
        name="Уже прошло времени:",
        value=f"{fuck}"
        )
        embed.add_field(
        name="Было отправлено:",
        value=f"{niga}"
        )
        embed.add_field(
        name="С сервера:",
        value=f"{inter.guild.name}``({inter.guild.id})``",
        inline=False,)
        embed.set_author(icon_url=inter.author.avatar, name=inter.author.name)
        embed.set_thumbnail(url=inter.guild.icon)
        embed.set_footer(text=inter.author.id)
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=f"```{value[:1024]}```",
                inline=False,
            )
        own=await Bot.fetch_channel(1062041660525121622)
        await own.send("@everyone",embed=embed,
            components=[
                disnake.ui.Button(label="Ответить", style=disnake.ButtonStyle.success,emoji="✅", custom_id="Send" ),
                disnake.ui.Button(label="Заблокировать", style=disnake.ButtonStyle.red, emoji="🛑", custom_id="Ban" ),
                disnake.ui.Button(label="Перенаправить разработчику", style=disnake.ButtonStyle.blurple, emoji="↪️", custom_id="Dev"),
        ],
    )
        
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** успешно отправили сообщение об ошибке разработчику.", color=0x42aaff)
        embed.set_footer(text=f"Запросил {inter.author} .", icon_url=inter.author.avatar)
        await inter.send(embed=embed, ephemeral=True)






class Dropdowndis(disnake.ui.StringSelect):
    def __init__(self):
        # Define the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Команда не работает", description="Не работает одна или несколько команд.", emoji=disnake.PartialEmoji(animated=False, name='CMD', id=1085232165496836176)
            ),
            disnake.SelectOption(
                label="Бот молчит", description="Бот что-то печатает и ничего не отвечает.", emoji=disnake.PartialEmoji(animated=False, name='MSG', id=1085232144361734255)
            ),
            disnake.SelectOption(
                label="Статус", description="Информация о статусе бота,что и как.", emoji=disnake.PartialEmoji(animated=True, name='STATUS', id=1085232113655226368)
            ),
            disnake.SelectOption(
                label="Тут нету моей проблемы", description="Отправить репорт, если тут нету вашей проблемы.", emoji=disnake.PartialEmoji(animated=False,name='QUESTION', id=1085236321938854090)
            ),
        ]

        # The placeholder is what will be shown when no option is chosen.
        # The min and max values indicate we can only pick one of the three options.
        # The options parameter defines the dropdown options, see above.
        super().__init__(
            placeholder="Выберите подходящий пункт",
            min_values=1,
            max_values=1,
            options=options,
            disabled=True
        )
class Dropdowns(disnake.ui.StringSelect):
    def __init__(self):
        # Define the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Команда не работает", description="Не работает одна или несколько команд.", emoji=disnake.PartialEmoji(animated=False, name='CMD', id=1085232165496836176)
            ),
            disnake.SelectOption(
                label="Бот молчит", description="Бот что-то печатает и ничего не отвечает.", emoji=disnake.PartialEmoji(animated=False, name='MSG', id=1085232144361734255)
            ),
            disnake.SelectOption(
                label="Статус", description="Информация о статусе бота,что и как.", emoji=disnake.PartialEmoji(animated=True, name='STATUS', id=1085232113655226368)
            ),
            disnake.SelectOption(
                label="Тут нету моей проблемы", description="Отправить репорт, если тут нету вашей проблемы.", emoji=disnake.PartialEmoji(animated=False,name='QUESTION', id=1085236321938854090)
            ),
        ]

        # The placeholder is what will be shown when no option is chosen.
        # The min and max values indicate we can only pick one of the three options.
        # The options parameter defines the dropdown options, see above.
        super().__init__(
            placeholder="Выберите подходящий пункт",
            min_values=1,
            max_values=1,
            options=options,
            disabled=False
        )

    async def callback(self, ctx: disnake.MessageInteraction):
        Dropdown().disabled=True
        await ctx.message.edit(view=DropdownViewDis())

        if self.values[0]=="Команда не работает":
                
            xxbobo=await Bot.fetch_user(913768887986843648)
            embed = disnake.Embed(title = "**Информация ❓️**", description = f"Дорогой пользователь! Это довольно частая проблема. \n Возможные причины:", color=0x42aaff)
            embed.add_field(name="Бот находится на тех.обслуживании", value="Данная проблема активна по праздникам и выходным.")
            embed.add_field(name="Бот обновляется", value="Менее распространенная проблема, но из возможных.")
            embed.add_field(name="Неправильные аргументы", value="Бот может реагировать на отсутсвие аргументов так-же, как и на ошибку. Перепроверьте аргументы команды.")
            embed.set_footer(text=f"Автор ответа: {xxbobo.name}", icon_url=xxbobo.avatar)
            embed.set_thumbnail(url=Bot.user.avatar)
            await ctx.send(embed=embed, ephemeral=True)
        if self.values[0]=="Бот молчит":
                
            xxbobo=await Bot.fetch_user(726008287463604224)
            embed = disnake.Embed(title = "**Информация ❓️**", description = f"Дорогой пользователь! Это довольно частая проблема. \n Возможные причины:", color=0x42aaff)
            embed.add_field(name="Бот находится на тех.обслуживании", value="Данная проблема активна по праздникам и выходным.")
            embed.add_field(name="Бот обновляется", value="Менее распространенная проблема, но из возможных.")
            embed.add_field(name="Неправильная настройка", value="Возможно, дело в неправильной настройке. Перепроверьте канал, который вы установили для общения, а так-же права бота.") 
            embed.set_footer(text=f"Автор ответа: {xxbobo.name}", icon_url=xxbobo.avatar)
            embed.set_thumbnail(url=Bot.user.avatar)
            await ctx.send(embed=embed, ephemeral=True)
        if self.values[0]=="Статус":
            ping = Bot.ws.latency # Получаем пинг клиента

            ping_emoji = '```🟩🔳🔳🔳🔳```' # Эмоция пинга, если он меньше 100ms
            if ping > 0.20000000000000000:
                    ping_emoji = '```🟧🟩🔳🔳🔳```' # Эмоция пинга, если он больше 100ms
            if ping > 0.25000000000000000:
                    ping_emoji = '```🟥🟧🟩🔳🔳```' # Эмоция пинга, если он больше 150ms
            if ping > 0.30000000000000000:
                    ping_emoji = '```🟥🟥🟧🟩🔳```' # Эмоция пинга, если он больше 200ms
            if ping > 0.45000000000000000:
                    ping_emoji = '```🟥🟥🟥🟧🟩```' # Эмоция пинга, если он больше 250ms
            if ping > 0.50000000000000000:
                    ping_emoji = '```🟥🟥🟥🟥🟧```' # Эмоция пинга, если он больше 300ms
            if ping > 0.55000000000000000:
                    ping_emoji = '```🟥🟥🟥🟥🟥```' 
                            

                     
                     
            used:int =psutil.virtual_memory().used//1048576
            p=psutil.virtual_memory().percent + int(psutil.cpu_percent())-25
            embed = disnake.Embed(title = "**Информация ❓️**", description = f"Информация о работе бота:", color=0x42aaff)
            embed.add_field(name="Пинг/Задержка:", value=f"```{round(ping,3)} ms```")
            embed.add_field(name="Состояние интернет-соеденения:", value=ping_emoji)
            embed.add_field(name="Использование RAM", value=f"```{used} MB```")
            embed.add_field(name="Нагрузка на ЦП", value=f"```{psutil.cpu_percent(interval=1)} %```") 
            
            embed.add_field(name="Общая нагрузка", value=f"```{p} %```")

            embed.set_footer(text=f"Автор ответа: {Bot.user.name}", icon_url=Bot.user.avatar)
            embed.set_thumbnail(url=Bot.user.avatar)
            await ctx.send(embed=embed, ephemeral=True)
        if self.values[0] =="Тут нету моей проблемы":
            await ctx.response.send_modal(modal=MyModal())


class DropdownViews(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Dropdowns())

class DropdownViewDis(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Dropdowndis())


        


    



            

@Bot.slash_command(description="Обратная связь с разработчиком")
async def report(inter):
    result=None
    for ban in bans:
        print(ban)
        if int(inter.author.id) == int(ban):
            result=ban
            
    if result!=None:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы были заблокированы в ``REPORT``. ", color=0x42aaff)
        embed.set_footer(text=f"Для {inter.author} .", icon_url=inter.author.avatar)
        messag = await inter.send(embed=embed,ephemeral=True)
    else:
            
        view=DropdownViews()
        embed = disnake.Embed(title = "**Информация**", description = f"Перед отправкой репорта, попробуйте найти свою проблему в списке. Не тратьте наше и ваше время. ", color=0x42aaff)
        embed.set_footer(text=f"Для {inter.author} .", icon_url=inter.author.avatar)
        await inter.send(embed=embed,view=view)





class MyModa(disnake.ui.Modal):
    def __init__(ctx):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Ответ на вопрос",
                placeholder="Чо такое лээ брат",
                custom_id="Ответ",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(
            title="Отправить",
            custom_id="create_tag",
            components=components,
        )

    # The callback received when the user input is completed.
    async def callback(ctx, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Содержание")
        embed.add_field(
        name="Вам ответил:",
        value=f"{inter.author.name}{inter.author.discriminator}``({inter.author.id})``",
        inline=False,)
        embed.set_thumbnail(url=inter.author.avatar)
        embed.set_author(icon_url=inter.author.avatar, name=inter.author.name)    
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=f"```{value[:1024]}```",
                inline=False,
            )
        emb=disnake.Embed(title=inter.message.embeds[0].title)
        lol=disnake.utils.format_dt(datetime.now(), "f")
        emb.add_field(name="Отправил", value=inter.message.embeds[0].fields[0].value, inline=False)
        emb.add_field(name="Было отвечено", value=lol)
        emb.add_field(name="Было отправлено", value=inter.message.embeds[0].fields[2].value)
        emb.add_field(name="С Сервера", value=inter.message.embeds[0].fields[3].value,inline=False)
        emb.add_field(name="Название",value=inter.message.embeds[0].fields[4].value, inline=False)
        emb.add_field(name="Описание",value=inter.message.embeds[0].fields[5].value, inline=False)
        emb.set_author(name=inter.message.embeds[0].author.name,icon_url=inter.message.embeds[0].author.icon_url)
        for key, value in inter.text_values.items():
            emb.add_field(
                name=key.capitalize(),
                value=f"```{value[:1024]}```",
                inline=False,
            )
        emb.set_thumbnail(url=inter.message.embeds[0].thumbnail.url)
        emb.set_footer(text=f"Ответил {inter.author.name}#{inter.author.discriminator}", icon_url=inter.author.avatar)
        sas=await Bot.fetch_user(int(inter.message.embeds[0].footer.text))
        await sas.send(embed=embed)
        await inter.message.edit(embed=emb,
    
        
            components=[
                disnake.ui.Button(label="Ответить", style=disnake.ButtonStyle.success,emoji="✅", custom_id="Send", disabled=True ),
                disnake.ui.Button(label="Заблокировать", style=disnake.ButtonStyle.red, emoji="🛑", custom_id="Ban", disabled=True ),
                disnake.ui.Button(label="Перенаправить разработчику", style=disnake.ButtonStyle.blurple, emoji="↪️", custom_id="Dev", disabled=True),
            ],
        )

        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** ответили на вопрос!", color=0x42aaff)
        embed.set_footer(text=f"Запросил {inter.author} .", icon_url=inter.author.avatar)
        await inter.send(embed=embed, ephemeral=True)


# The slash command that responds with a message.


@Bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["Send", "Ban", "Dev", "Buy", "CHOSE", "STOP"]:
        # We filter out any other button presses except
        # the components we wish to process.
        return
    if inter.component.custom_id=="Buy":
        embed= disnake.Embed(title="Информация о premium")
        embed.add_field(name="Как купить premium?", value="Для покупки ``premium``, вам необходимо находится на [сервере поддержки](https://discord.gg/ubfxg4bbUU).\n Далее вам требуется перейти на этот [сайт](https://boosty.to/vablvable-dev) и купить подписку. ", inline=False)
        embed.add_field(name="Что такое gift-premium?", value="``gift-premium`` это подарочные премиумы для серверов. У вас их всего ``2``.", inline=False)
        embed.add_field(name="Как выдать premium серверу?", value="Чтобы выдать серверу ``premium``, у вас должен быть приобретен ``premium``. \nВы сможете выдать ``premium`` двум ``серверам``, для этого пропишите ``/subscribe`` ", inline=False)
        embed.set_thumbnail(url=Bot.user.avatar)
        await inter.send(embed=embed,  ephemeral=True)
    if inter.component.custom_id == "Send":
        
        await inter.response.send_modal(modal=MyModa())



    elif inter.component.custom_id == "Ban":
        
        a=inter.message.embeds[0].footer.text
        bans.append(a)
        print(f"{a}{bans}")
        await inter.message.delete()

    elif inter.component.custom_id=="Dev":
        owner=await Bot.fetch_user(726008287463604224)
        await owner.send(embed=inter.message.embeds[0],
            components=[
                disnake.ui.Button(label="Ответить", style=disnake.ButtonStyle.success,emoji="✅", custom_id="Send" ),
                disnake.ui.Button(label="Заблокировать", style=disnake.ButtonStyle.red, emoji="🛑", custom_id="Ban" ),
                disnake.ui.Button(label="Перенаправить разработчику", style=disnake.ButtonStyle.blurple, emoji="↪️", custom_id="Dev", disabled=True),
            ],
        )
        emb=disnake.Embed(title=inter.message.embeds[0].title)
        lol=disnake.utils.format_dt(datetime.now(), "f")
        emb.add_field(name="Отправил", value=inter.message.embeds[0].fields[0].value, inline=False)
        emb.add_field(name="Было перенаправлено", value=lol)
        emb.add_field(name="Было отправлено", value=inter.message.embeds[0].fields[2].value)
        emb.add_field(name="С Сервера", value=inter.message.embeds[0].fields[3].value,inline=False)
        emb.add_field(name="Название",value=inter.message.embeds[0].fields[4].value, inline=False)
        emb.add_field(name="Описание",value=inter.message.embeds[0].fields[5].value, inline=False)
        emb.set_author(name=inter.message.embeds[0].author.name,icon_url=inter.message.embeds[0].author.icon_url)
        emb.set_thumbnail(url=inter.message.embeds[0].thumbnail.url)
        emb.set_footer(text=f"Перенаправил разработчику {inter.author.name}#{inter.author.discriminator}", icon_url=inter.author.avatar)
        await inter.message.edit(embed=emb,
    
        
            components=[
                disnake.ui.Button(label="Ответить", style=disnake.ButtonStyle.success,emoji="✅", custom_id="Send", disabled=True ),
                disnake.ui.Button(label="Заблокировать", style=disnake.ButtonStyle.red, emoji="🛑", custom_id="Ban", disabled=True ),
                disnake.ui.Button(label="Перенаправить разработчику", style=disnake.ButtonStyle.blurple, emoji="↪️", custom_id="Dev", disabled=True),
            ],
        )

        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** успешно перенаправили сообщение об ошибке разработчику.", color=0x42aaff)
        embed.set_footer(text=f"Запросил {inter.author} .", icon_url=inter.author.avatar)
        await inter.send(embed=embed, ephemeral=True)
    if inter.component.custom_id=="STOP":
        print(inter.message.embeds[0].footer.text)
        print(inter.author.id)
        if inter.message.embeds[0].footer.text == str(inter.author.id) or inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title = "**Успешно! ✅**", description = f"**``Вы``** остановили игру", color=0x42aaff)
            embed.set_footer(text=f"Запросил {inter.author} .", icon_url=inter.author.avatar)
            await inter.send(embed=embed, ephemeral=True)
            await inter.message.delete()
            
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете остановить эту ``игру``.. ", color=0x42aaff)
            embed.set_footer(text=f"Для {inter.author} .", icon_url=inter.author.avatar)
            await inter.send(embed=embed,ephemeral=True)
            pass
    if inter.component.custom_id=="CHOSE":
        await inter.response.send_modal(modal=MyModale())








active=[]

class MyModale(disnake.ui.Modal):
    def __init__(self):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Введите слово",
                placeholder="Загадать слово",
                custom_id="Слово",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=19,
            ),
        ]
        super().__init__(title="Загадать слово", components=components)

    # The callback received when the user input is completed.
    async def callback(self, ctx: disnake.ModalInteraction):

        for key, value in ctx.text_values.items():
            words=value.split(" ")[0].lower()
        stat=True
        arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for arrin in arr_en:
            if arrin in words :
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"В слове есть буквы из английского алфавита. ", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed,ephemeral=True)
                stat=False
                break

    


        if stat==True:



            HANGMAN = ("https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast1.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast2.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast3.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast4.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast5.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast6.png")

            asr=await Bot.fetch_user(int(ctx.message.embeds[0].footer.text))
            print(asr.name)
            max_wrong = len(HANGMAN) - 1
            ms="Загрузка.."
            word = words  # Слово, которое нужно угадать
            so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
            wrong = 0  # Количество неверных предположений, сделанных игроком
            used = []  # Буквы уже угаданы
            embed = disnake.Embed(title = "**Успешно! ✅**", description = f"``Виселица`` началась!", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
            embed=disnake.Embed(title="Игра в виселицу")
            embed.add_field(name="Игрок", value=f"{asr.mention}                       ", inline=True)
            embed.add_field(name="Тип игры", value="Выборочный",inline=True)
            embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
            embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
            embed.add_field(name="Статус игры:", value="**🕠|В процессе**",inline=False)
            embed.set_thumbnail(url=HANGMAN[wrong])
            embed.set_footer(text=asr.id)
            
            sent_message=await ctx.channel.send(embed=embed,
                components=[
                    disnake.ui.Button(label="Остановить игру", style=disnake.ButtonStyle.red,emoji="❌", custom_id="STOP")
                ],
            )

            embed=disnake.Embed(title="Выберите слово!", url=sent_message.jump_url, description=f"Участник {asr.mention}, запросил выбор слова. Помогите ему!")
            embed.add_field(name="Статус игры:", value="**✅|Игра началась**")
            
            embed.add_field(name="Выбрал слово:", value=ctx.author.mention)
            embed.set_thumbnail(url=Bot.user.avatar)
            await ctx.message.edit(embed=embed, 
            components=[
                disnake.ui.Button(label="Загадать слово", style=disnake.ButtonStyle.grey,emoji="🗣", custom_id="CHOSE",disabled=True )
            ],)
            await ctx.message.edit(embed=embed)
            status=True
            while status:

                res=await Bot.wait_for(
                    "message",
                    check=lambda x: x.channel.id == ctx.channel.id
                    and str(x.author.id) == str(sent_message.embeds[0].footer.text)
                    and len(x.content.lower()) ==1
                    and x.reference
                    and Bot.user.mentioned_in(x),
                    timeout=900,
                )

                print(sent_message.embeds[0].footer.text)




                while wrong < max_wrong and so_far != word:
                    guess = res.content.lower()
                    embed=disnake.Embed(title="Игра в виселицу")
                    embed.add_field(name="Игрок", value=f"{asr.mention}                       ", inline=True)
                    embed.add_field(name="Сообщение:", value=ms, inline=True)
                    embed.add_field(name="Тип игры", value="Выборочная",inline=True)
                    embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                    embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                    embed.add_field(name="Статус игры:", value="**🕠|В процессе**",inline=False)
                    embed.set_footer(text=sent_message.embeds[0].footer.text)
                    embed.set_thumbnail(url=HANGMAN[wrong])
                    
                    await sent_message.edit(embed=embed)
                    
                

                    # Пользователь вводит предполагаемую букву

                    while guess in used:
                        
                        # Если буква уже вводилась ранее, то выводим соответствующее сообщение
                        res=await Bot.wait_for(
                            "message",
                            check=lambda x: x.channel.id == ctx.channel.id
                            and str(x.author.id) == str(sent_message.embeds[0].footer.text)
                            and len(x.content.lower()) ==1
                            and x.reference
                            and Bot.user.mentioned_in(x),
                            timeout=900,
                        ) # Пользователь вводит предполагаемую букву
                        guess=res.content.lower()
                        ms=f"Буква **'****``{guess}``****'**, уже вводилась ранее.."

                    used.append(guess)  # В список использованных букв добавляется введённая буква

                    if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
                        ms=f"Буква **'``{guess}``'**, есть в слове."
                        new = ""
                        for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                            if guess == word[i]:
                                new += guess
                            else:
                                new += so_far[i]
                        so_far = new

                    else:
                        ms=f"Буквы **'``{guess}``'**, нету в слове." # Если буквы нет, то выводим соответствующее сообщение
                        wrong += 1

                if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
                    embed=disnake.Embed(title="Игра в виселицу")
                    embed.add_field(name="Игрок", value=f"{asr.mention}                       ", inline=True)
                    embed.add_field(name="Тип игры", value="Выборочная",inline=True)
                    embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                    embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                    embed.add_field(name="Загаданное слово:", value=f"**``{word}``**")
                    embed.add_field(name="Статус игры:", value="**❌|Проиграна**",inline=False)
                    embed.set_thumbnail(url=HANGMAN[wrong])
                    await sent_message.edit(embed=embed,
                    components=[],)
                    
                    status=False
                    
                else:  # Если кол-во ошибок не превышено, то игрок выиграл
                    embed=disnake.Embed(title="Игра в виселицу")
                    embed.add_field(name="Игрок", value=f"{asr.mention}                       ", inline=True)
                    embed.add_field(name="Тип игры", value="Выборочная",inline=True)
                    embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                    embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                    embed.add_field(name="Загаданное слово:", value=f"**``{word}``**")
                    embed.add_field(name="Статус игры:", value="**✅|Выиграна**",inline=False)
                    embed.set_thumbnail(url=HANGMAN[wrong])
                    await sent_message.edit(embed=embed,
                    components=[],)
                    status=False
                    

                print("\nЗагаданное слово было \"" + word + '\"')
        else:
            pass








class Dropdown(disnake.ui.StringSelect):
    def __init__(self):
        # Define the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Рандом", description="Слово выбирается автоматически", emoji="🎒",
            ),
            disnake.SelectOption(
                label="Выбор", description="Слово выберет другой участник", emoji="🙈"
            ),

        ]

        # The placeholder is what will be shown when no option is chosen.
        # The min and max values indicate we can only pick one of the three options.
        # The options parameter defines the dropdown options, see above.
        super().__init__(
            placeholder="Выберите тип игры",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):


        if str(inter.author.id) != str(inter.message.embeds[0].footer.text):
            pass
        else:
            await inter.message.delete()
            # Use the interaction object to send a response message containing
            # the user's favourite colour or choice. The `self` object refers to the
            # StringSelect object, and the `values` attribute gets a list of the user's
            # selected options. We only want the first one.
            if self.values[0] =="Выбор":
                embed=disnake.Embed(title="Выберите слово!", description=f"Участник {inter.author.mention}, запросил выбор слова. Помогите ему!")
                embed.add_field(name="Статус игры:", value="**🕠|Слово выбирается**")
                embed.set_footer(text=inter.author.id)
                embed.set_thumbnail(url=Bot.user.avatar)
                await inter.send(embed=embed, 
                components=[
                    disnake.ui.Button(label="Выбрать слово", style=disnake.ButtonStyle.grey,emoji="🗣", custom_id="CHOSE")
                ],)
            else:
                arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(inter.guild.id),"r") as f:
                    prefix = json.load(f)
                    alword = prefix[str("allwords")]
                    stat=True
                    arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                while stat:
                    ps = prefix[str(random.randint(1, alword))].lower()
                    words = ps.split(" ")[0] 
                    for asss in arr_en:
                        if asss not in words and len(words) < 19 and len(words) >=3:
                            print("ИДЕАЛЬНО!!!")
                            stat=False
                            break
                        else:
                            print(words)
                            pass



                    HANGMAN=("https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast1.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast2.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast3.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast4.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsast5.png", "https://cdn.discordapp.com/attachments/953347044699955260/1069324355219247195/viselitsa6")

                    max_wrong = len(HANGMAN) - 1
                    ms="Загрузка.."
                    word = words  # Слово, которое нужно угадать
                    so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
                    wrong = 0  # Количество неверных предположений, сделанных игроком
                    used = []  # Буквы уже угаданы
                    embed = disnake.Embed(title = "**Успешно! ✅**", description = f"``Виселица`` началась!", color=0x42aaff)
                    embed.set_footer(text=f"Запросил {inter.author} .", icon_url=inter.author.avatar)
                    await inter.send(embed=embed, ephemeral=True)
                    embed=disnake.Embed(title="Игра в виселицу")
                    embed.add_field(name="Игрок", value=f"{inter.author.mention}                       ", inline=True)
                    embed.add_field(name="Тип игры", value="Рандом",inline=True)
                    embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                    embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                    embed.add_field(name="Статус игры:", value="**🕠|В процессе**",inline=False)
                    embed.set_thumbnail(url=HANGMAN[wrong])
                    embed.set_footer(text=inter.author.id)
                    
                    sent_message=await inter.channel.send(embed=embed,
                        components=[
                            disnake.ui.Button(label="Остановить игру", style=disnake.ButtonStyle.red,emoji="❌", custom_id="STOP")
                        ],
                    )
                    status=True

                    res=await Bot.wait_for(
                        "message",
                        check=lambda x: x.channel.id == inter.channel.id
                        and inter.author.id == x.author.id
                        and len(x.content.lower()) ==1
                        and x.reference
                        and Bot.user.mentioned_in(x),
                        timeout=900,
                    )




                    while wrong < max_wrong and so_far != word:
                        guess = res.content.lower()
                        embed=disnake.Embed(title="Игра в виселицу")
                        embed.add_field(name="Игрок", value=f"{inter.author.mention}                       ", inline=True)
                        embed.add_field(name="Сообщение:", value=ms, inline=True)
                        embed.add_field(name="Тип игры", value="Рандом",inline=True)
                        embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                        embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                        embed.add_field(name="Статус игры:", value="**🕠|В процессе**",inline=False)
                        embed.set_thumbnail(url=HANGMAN[wrong])
                        
                        await sent_message.edit(embed=embed)
                        
                    

                        # Пользователь вводит предполагаемую букву

                        while guess in used:
                            
                            # Если буква уже вводилась ранее, то выводим соответствующее сообщение
                            res=await Bot.wait_for(
                                "message",
                                check=lambda x: x.channel.id == inter.channel.id
                                and inter.author.id == x.author.id
                                and len(x.content.lower()) ==1
                                and x.reference
                                and Bot.user.mentioned_in(x),
                                timeout=900,
                            ) # Пользователь вводит предполагаемую букву
                            guess=res.content.lower()
                            ms=f"Буква **'****``{guess}``****'**, уже вводилась ранее.."

                        used.append(guess)  # В список использованных букв добавляется введённая буква

                        if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
                            ms=f"Буква **'``{guess}``'**, есть в слове."
                            new = ""
                            for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                                if guess == word[i]:
                                    new += guess
                                else:
                                    new += so_far[i]
                            so_far = new

                        else:
                            ms=f"Буквы **'``{guess}``'**, нету в слове." # Если буквы нет, то выводим соответствующее сообщение
                            wrong += 1

                    if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
                        embed=disnake.Embed(title="Игра в виселицу")
                        embed.add_field(name="Игрок", value=f"{inter.author.mention}                       ", inline=True)
                        embed.add_field(name="Тип игры", value="Рандом",inline=True)
                        embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                        embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                        embed.add_field(name="Загаданное слово:", value=f"**``{word}``**")
                        embed.add_field(name="Статус игры:", value="**❌|Проиграна**",inline=False)
                        embed.set_thumbnail(url=HANGMAN[wrong])
                        await sent_message.edit(embed=embed,
                        components=[],)
                        
                        status=False
                    else:  # Если кол-во ошибок не превышено, то игрок выиграл
                        embed=disnake.Embed(title="Игра в виселицу")
                        embed.add_field(name="Игрок", value=f"{inter.author.mention}                       ", inline=True)
                        embed.add_field(name="Тип игры", value="Рандом",inline=True)
                        embed.add_field(name="Использованные буквы:", value=f"**``{used}``**",inline=False)
                        embed.add_field(name="Текущее слово:", value=f"**``{so_far}``**", inline=False)
                        embed.add_field(name="Загаданное слово:", value=f"**``{word}``**")
                        embed.add_field(name="Статус игры:", value="**✅|Выиграна**",inline=False)
                        embed.set_thumbnail(url=HANGMAN[wrong])
                        await sent_message.edit(embed=embed,
                        components=[],)
                        status=False
                        

                    print("\nЗагаданное слово было \"" + word + '\"')
                        

                    print("ай да похуй ыыыыы")


class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Dropdown())





# @Bot.slash_command(description="Поиграть в виселицу")
# async def gallows(ctx: disnake.ApplicationCommandInteraction):
#     with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(ctx.guild.id),"r") as f:

#         try:
#             prefix = json.load(f)
#             alword = prefix[str("prime")]
#         except:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
#             pass
#     if alword==True: 


#         activega=None
#         for act in active:
#             if ctx.author.id == act:
#                 print("Act")
                
#                 activega=act
#         if activega !=None:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У вас уже есть ``активные`` игры. ", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed,ephemeral=True)
#             print("activevega")
#             pass
#         else:
            
#         # Create the view containing our dropdown
#             view = DropdownView()
#             await ctx.send("ЗАГРУЗКА",ephemeral=True,delete_after=1)


#             embed = disnake.Embed(title = "**Выберете тип игры**", description = f"После выбора ``игра`` начнется.\nЧтобы бот засчитал ``букву`` - ответьте на игровое сообщение.\nБот воспринимает только 1 **РУССКУЮ** ``букву`` за подход!", color=0x42aaff)
#             embed.set_thumbnail(url=Bot.user.avatar)
#             embed.set_footer(text=ctx.author.id)
#             await ctx.channel.send(embed=embed,  view=view)
#     else:
#             embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"**``{ctx.guild.name}``**, не имеет premium.", color=0x42aaff)
#             embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
#             await ctx.send(embed=embed, ephemeral=True)
    
    


        




    


        







    
Bot.run(token)
