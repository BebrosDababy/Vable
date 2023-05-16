import os
import asyncio



import random
import urllib
import regex as re
import youtube_dl

import discord
from discord.ext import commands, tasks



import json


import aiohttp

Current = "+"
intents = discord.Intents.default()

token = ""
intents.message_content=True
Bot = commands.Bot(command_prefix="+",intents=intents)
Bot.remove_command('help')



@Bot.event
async def on_guild_join(guild):
          
        sas = {
                "allwords": 0
                
        }
        ses={

                "channel":None,
                "prime": False,
                "servchannel":None,
                

                "autogen":0
        }
        open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guild.id), 'x')
        open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), 'x')
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guild.id), "w", encoding="utf-8") as file:
                json.dump(sas, file)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), "w", encoding="utf-8") as file:
                json.dump(ses, file)

        


                            

                
                






        







@Bot.event
async def on_guild_remove(guild):

        os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guild.id))
        os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id))


@Bot.event
async def on_ready():
        await Bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="Токен бота был утерян. В скором времени вы получите компенсацию"))
        print("LOOOOOOOOOOOOOOOOL")
        



        


@Bot.event
async def on_message(message: discord.Message):
        
        
        
        await Bot.process_commands(message)
        
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                prefix = json.load(f)
      

                msgrand= prefix[str("autogen")]


                
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
        
                
                prefix = json.load(f)
                alword = prefix[str("allwords")]
         
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                prefix = json.load(f)
                d = prefix[str("channel")]
        if msgrand!=None:
                autgen=random.randint(1,100)
   
                if autgen<msgrand:
          
                        if d==True:
                                if Bot.user==message.author or message.author.bot:

                                        pass
                                else:
                                        if d == True:
                                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                        prefix = json.load(f)
                                                        alword=prefix[str("allwords")]


                                                async with message.channel.typing():
                                                        await asyncio.sleep(random.uniform(0.0, 2.9))
                                                        


                                                        
                                                cho = ["", "!", "?", ".", "...", ":face_with_monocle:", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                    

                                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                        prefix = json.load(f)
                                                        alword=prefix[str("allwords")]
                                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                                                        prefixs = json.load(f)
        

                                                try:
                                                        mode=prefixs[str("mode")]
                                                except:
                                                        mode="normal"
                                                        
                                                async with message.channel.typing():
                                                        await asyncio.sleep(random.uniform(0.0, 2.9))
                                                        


                                                        
                                                cho = ["", "!", "?", ".", "...", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                                ms1 = prefix[str(random.randint(1, alword))]
                                                print(mode)
                                                if mode =="emoji":
                                                        emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                        for a in emojies:
                                                                emoj=random.choice(emojies)
                                                                ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                                if mode=="normal":
                                                        ms1=ms1
                                                if mode=="caps":
                                                        
                                                        ms1=ms1.upper()
                                                if mode=="trslit":
                                                        ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                        
                                                while ms1=="" or ms1==" ":
                                                        print("maxword1 err")
                                                        ms1 = prefix[str(random.randint(1, alword))]
                                                        if mode =="emoji":
                                                                emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                                for a in emojies:
                                                                        emoj=random.choice(emojies)
                                                                        ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                                        if mode=="normal":
                                                                ms1=ms1
                                                        if mode=="caps":
                                                                
                                                                ms1=ms1.upper()
                                                        if mode=="trslit":
                                                                ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                        
                                                        await message.channel.send(ms1+random.choice(cho), reference=message)
                                                if "?" in ms1 or "!" in ms1 or "..." in ms1 or "." in ms1 or ":face_with_monocle:":
                                                        await message.channel.send(ms1, reference=message)
                                                else:
                                                        await message.channel.send(ms1+random.choice(cho), reference=message)

                                              
                        elif d==message.channel.id:
                      
                                if Bot.user==message.author or message.author.bot:
                         

                                        pass
                                else:
          
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]
                                                
                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))
                                                


                                                
                                        cho = ["", "!", "?", ".", "...", ":face_with_monocle:", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                                                prefixs = json.load(f)
      

                                        try:
                                                mode=prefixs[str("mode")]
                                        except:
                                                mode="normal"
                                                
                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))
                                                


                                                
                                        cho = ["", "!", "?", ".", "...", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                        ms1 = prefix[str(random.randint(1, alword))]
                                        print(mode)
                                        if mode =="emoji":
                                                emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                for a in emojies:
                                                        emoj=random.choice(emojies)
                                                        ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                        if mode=="normal":
                                                ms1=ms1
                                        if mode=="caps":
                                                
                                                ms1=ms1.upper()
                                        if mode=="trslit":
                                                ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                        while ms1=="" or ms1==" ":
                                                print("maxword1 err")
                                                ms1 = prefix[str(random.randint(1, alword))]
                                                if mode =="emoji":
                                                        emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                        for a in emojies:
                                                                emoj=random.choice(emojies)
                                                                ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                                if mode=="normal":
                                                        ms1=ms1
                                                if mode=="caps":
                                                        
                                                        ms1=ms1.upper()
                                                if mode=="trslit":
                                                        ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                                await message.channel.send(ms1+random.choice(cho), reference=message)
                                        if "?" in ms1 or "!" in ms1 or "..." in ms1 or "." in ms1 or ":face_with_monocle:":
                                                await message.channel.send(ms1, reference=message)
                                        else:
                                                await message.channel.send(ms1+random.choice(cho), reference=message)


                

                                                        
        if Bot.user.mentioned_in(message):
                if message.author is Bot.user:
                        pass
                if d == None:
                        embed = discord.Embed(title = "**Ошибка! ❌**", description = f"{message.guild.owner.mention} Канал для чтения сообщений не установлен! Исправьте ситуацию используя </setchannel:1052301287540137994>!", color=0x464451)

                        await message.channel.send(embed=embed)

                elif d==True:
                        if Bot is message.author:
                                print("бот ин месадже автор")

                                pass
                        else:
                                if d == True:
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]
   
                                                
                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))

                                                
                                        cho = ["", "!", "?", ".", "...", ":face_with_monocle:", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                

                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                                                prefixs = json.load(f)
      

                                        try:
                                                mode=prefixs[str("mode")]
                                        except:
                                                mode="normal"
                                                
                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))
                                                


                                                
                                        cho = ["", "!", "?", ".", "...", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                        ms1 = prefix[str(random.randint(1, alword))]
                                        print(mode)
                                        if mode =="emoji":
                                                emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                for a in emojies:
                                                        emoj=random.choice(emojies)
                                                        ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                        if mode=="normal":
                                                ms1=ms1
                                        if mode=="caps":
                                                
                                                ms1=ms1.upper()
                                        if mode=="trslit":
                                                ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                        while ms1=="" or ms1==" ":
                                                print("maxword1 err")
                                                ms1 = prefix[str(random.randint(1, alword))]
                                                if mode =="emoji":
                                                        emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                        for a in emojies:
                                                                emoj=random.choice(emojies)
                                                                ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                                if mode=="normal":
                                                        ms1=ms1
                                                if mode=="caps":
                                                        
                                                        ms1=ms1.upper()
                                                if mode=="trslit":
                                                        ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                                await message.channel.send(ms1+random.choice(cho), reference=message)
                                        if "?" in ms1 or "!" in ms1 or "..." in ms1 or "." in ms1 or ":face_with_monocle:":
                                                await message.channel.send(ms1, reference=message)
                                        else:
                                                await message.channel.send(ms1+random.choice(cho), reference=message)

                        
                else:
                        
                        if Bot is message.author:
                                

                                pass
                        if "@everyone" in message.content:
                                
                                print("ass")
                                return
                        if "@here" in message.content:
                                
                                print("ass")
                                return
                        if message.author.bot:
                                pass

                        else:
                                if message.channel.id == d:
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]

                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))


                                                
                                        cho = ["", "!", "?", ".", "...", ":face_with_monocle:", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                                prefix = json.load(f)
                                                alword=prefix[str("allwords")]
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                                                prefixs = json.load(f)
      

                                        try:
                                                mode=prefixs[str("mode")]
                                        except:
                                                mode="normal"
                                                
                                        async with message.channel.typing():
                                                await asyncio.sleep(random.uniform(0.0, 2.9))
                                                


                                                
                                        cho = ["", "!", "?", ".", "...", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                                        ms1 = prefix[str(random.randint(1, alword))]
                                        print(mode)
                                        if mode =="emoji":
                                                emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                for a in emojies:
                                                        emoj=random.choice(emojies)
                                                        ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                        if mode=="normal":
                                                ms1=ms1
                                        if mode=="caps":
                                                
                                                ms1=ms1.upper()
                                        if mode=="trslit":
                                                ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                        while ms1=="" or ms1==" ":
                                                print("maxword1 err")
                                                ms1 = prefix[str(random.randint(1, alword))]
                                                if mode =="emoji":
                                                        emojies=["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]
                                                        for a in emojies:
                                                                emoj=random.choice(emojies)
                                                                ms1=ms1.replace(" ", f"ㅤ{emoj}ㅤ", 1)
                                                if mode=="normal":
                                                        ms1=ms1
                                                if mode=="caps":
                                                        
                                                        ms1=ms1.upper()
                                                if mode=="trslit":
                                                        ms1= ''.join(x.lower() if i%2 else x.upper() for i, x in enumerate(ms1))
                                                
                                                await message.channel.send(ms1+random.choice(cho), reference=message)
                                        if "?" in ms1 or "!" in ms1 or "..." in ms1 or "." in ms1 or ":face_with_monocle:":
                                                await message.channel.send(ms1, reference=message)
                                        else:
                                                await message.channel.send(ms1+random.choice(cho), reference=message)
                        
        else:
                print("Err")
                pass

        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(message.guild.id), 'r') as f:
                prefix = json.load(f)
                d = prefix[str("channel")]
        if message.content.startswith('/'):
                print("ss")
                pass
        else:
                if message.channel.id == d or d ==True:
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                prefix = json.load(f)



                        
                        msg=message.content.replace("<@1045034649379950622>", "")
                

        
                        if message.author==Bot:
                                print("as")
                                pass 
                        
                        if "@everyone" in message.content:
                                
                                print("ass")
                                return
                        
                        if "/code" in message.content or "/ben" in message.content or "/avatar" in message.content or "/uncode" in message.content or "/cats" in message.content or "/dogs" in message.content or "/setchannel" in message.content or "/timeloop" in message.content or "/reset" in message.content or "/serverinfo" in message.content:
                                pass
                        if "@here" in message.content:
                                print("help")
                                return
                        if message.content in prefix:
                                
                                print("bila takoe")
                                pass
                        if len(msg) > 160 or msg=="":
                                return
                        if message.content.startswith("https://") and "invite" in message.content:
                                print(message.content)
                                return

                
                        result = None
                        for key in prefix:
                                if prefix[key] == message.content:
                                        result = key
                        if result is not None:
                                print("")
                                pass
                        else:
                                msg=message.content.replace("@everyone", "")
                                msg=message.content.replace("@here", "")

                                
                        

                        

                                alword=alword+1
                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), 'r') as f:
                                        prefix = json.load(f)
                                        prefix[str("allwords")] = alword
                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), "w") as f:
                                        json.dump(prefix, f, indent=4)
                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), "r") as f:
                                        prefix = json.load(f)
                                prefix[str(alword)] = f"{msg}"
                                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), "w") as f:
                                        json.dump(prefix, f, indent=4)
                        
                else:
                        print("мат") 
        if message.author.id==1045034649379950622:
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\totalmsg.json", "r") as f:
                        prefix = json.load(f)
                        asus = prefix[str("totalmsg")]
                        prefix[str("totalmsg")] = asus+1
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\totalmsg.json", "w") as f:
                        json.dump(prefix, f, indent=4)
        if Bot.user.mentioned_in(message) is False:
                if d==True or d==message.channel.id:
                        if message.author.bot:
                                pass
                        if message.author.bot:
                                
                                pass
                        if message.author is Bot.user:
                                pass
                        
                        else:
                                if message.author.bot is False:
                                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(message.guild.id), "r") as f:
                                                try:
                                                        nig=json.load(f)
                                                        aprim=nig["prime"]
                                                        if aprim==True:
                                                                for a in nig:
                                                                        if str(a).isdigit():
                                                                                
                                                                                pass
                                                                        else:
                                                                                if message.content.lower() == a :
                                                                                        print(a.isdigit())
                                                                                        if type(nig[a]) is str:
                                                                                                await message.channel.send(nig[a],reference=message)
                                                                                                break
                                                                                        elif type(nig[a]) is list:
                                                                                                await message.channel.send(random.choice(nig[a]),reference=message)
                                                                                                break
                                                                                elif a in message.content.lower() and len(a) >= 3 and len(message.content.lower()) > 6:
                                                                                        if type(nig[a]) is str:
                                                                                                await message.channel.send(nig[a] ,reference=message)
                                                                                                break
                                                                                        elif type(nig[a]) is list:
                                                                                                await message.channel.send(random.choice(nig[a]), reference=message)
                                                                                                break

                                                except:
                                                        pass


     



@Bot.command()
@commands.is_owner()
async def premium_add(ctx, guildid: int):
        guild = Bot.get_guild(guildid)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), 'r') as f:
                prefix = json.load(f)
                prefix[str(f"premium")] = True
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)

        invite = await guild.text_channels[0].create_invite(max_age=100, max_uses=9, temporary=False)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guildid), "r") as f:
                prefix = json.load(f)
                prefix[str("more")] = 0
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guildid), "w") as f:
                json.dump(prefix, f, indent=4)
  


   
        embed = discord.Embed(title = "**Успешно!✅**", description = f"**``Премиум``** был выдан [{guild.name}](https://discord.gg/{invite.code})! ", color=0x464451)
        await ctx.send(embed=embed)





@Bot.command()
@commands.is_owner()
async def premium_rem(ctx, guildid):
        guild = await Bot.fetch_guild(int(guildid))
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), 'r') as f:
                prefix = json.load(f)
                prefix[str(f"premium")] = False
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}.json".format(guild.id), 'w') as f:
                json.dump(prefix, f, indent=4)
                
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guildid), "r") as f:
                prefix = json.load(f)
                prefix[str("more")] = 0
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\guild\{}W.json".format(guildid), "w") as f:
                json.dump(prefix, f, indent=4)

        chan = guild.system_channel
        embed = discord.Embed(title = "**Успешно!✅**", description = f"**``Премиум``** был снят с этого сервера!:cry: Все органичения вновь активны!:cry: ", color=0x464451)

        await messag.add_reaction("✅")
        messag= await chan.send(embed=embed)
        await messag.pin()
        embed = discord.Embed(title = "**Успешно!✅**", description = f"**``Премиум``** был cнят с {guild.name}! ", color=0x464451)
        await ctx.send(embed=embed)
        await ctx.send(embed=embed)




        



        






                
                


                










    
Bot.run(token)
