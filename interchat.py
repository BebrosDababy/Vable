import disnake
from disnake.ext import commands, tasks
import json
import asyncio
import os
from os import walk,remove
import base64

Bot=commands.Bot(command_prefix="+", intents=disnake.Intents.all())
Bot.remove_command('help')

            
@Bot.slash_command(description="Установить приватный межсерверный канал")
@commands.has_guild_permissions(administrator=True)
@commands.bot_has_permissions(view_channel=True, manage_webhooks=True)

async def privchannel(ctx, token:str=commands.Param(description="Токен приватного межсерверного чата")):
    penis=False
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "r") as f:
            asd=json.load(f)
            adre=asd[str("servers")]
        for bebra in adre:
            if bebra==ctx.guild.id:
                penis=True
    except:
        penis=False

    if penis ==True:
        
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "r") as f:
            asd=json.load(f)
            try:
                nefr=asd[str(ctx.channel.id)]
                asd.pop(str(nefr))
            except:
                pass

            asd[str(token)] = ctx.channel.id
            asd[str(ctx.channel.id)] = token
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "w") as f:
            json.dump(asd, f, indent=4)
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Канал для ``{token}`` установлен!", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не находитесь в данном чате", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        

                    

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

    if isinstance(error, commands.BotMissingPermissions):     

        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"У бота не хватает прав для выполнения этой команды", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)




@Bot.event
async def on_message(msg:disnake.Message):

    if msg.author.bot==False:


        try:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(msg.guild.id), "r") as f:
                nig=json.load(f)
                penis=nig[str(msg.channel.id)]
                chaid=nig[str(penis)]

                
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(penis), "r") as f:
                nig=json.load(f)
                urls=nig[str("urls")]
                invites=nig[str("invites")]
                srv=nig[str("servers")]


        except:
            chaid=None
        ban=False
        if msg.author.bot==False:
            if msg.channel.id == chaid:
                for bebra in srv:
                    bebra=await Bot.fetch_guild(int(bebra))

                    work=True
                    try:
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                            nig=json.load(f)
                            
                    except:
                        work=False
                    if work==True:
                        if "https" not in msg.content or urls==True:
                            if "discord.gg/" not in msg.content or invites==True:
                                try:
                                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                        nig=json.load(f)
                                        chaid=nig[str(penis)]
                                except:
                                    chaid=None
                
                                if chaid==None:
                                    pass
                                else:
                        
                                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                        nig=json.load(f)
                                    try:
                                        bans=nig[str("muted")]
                                        for mem in bans:
                                            if msg.author.id ==mem:
                                                ban=True
                                    except:
                                        ban=False

                                    if ban==False:
                                        if msg.guild.id != bebra.id:
                                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                                nig=json.load(f)
                                                try:
                                                    chaid=nig[str("privatechannel")]
                                                except:
                                                    pass
                                            try:
                                                channel=await Bot.fetch_channel(int(chaid))
                                                mywh=None
                                                for wh in nig:
                                                    if wh=="privatewebhook":
                                                        mywh=nig[str("privatewebhook")]
                                                if mywh!=None:
                                                    webhook= await Bot.fetch_webhook(int(mywh))

                                                else:
                                                    webhook=await channel.create_webhook(name="Vable Private Chat")
                                                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                                            nig=json.load(f)
                                                            nig[str("privatewebhook")]=webhook.id
                                                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "w") as f:
                                                            json.dump(nig, f, indent=4)
                                                newcontent=msg.content.replace("@everyone", "")
                                                newcontent=newcontent.replace("@here", "")
                                                print(bebra)
                                                await webhook.send(content=newcontent, username=f"{msg.author.id}", avatar_url=msg.author.avatar)
                                                print(bebra)
                                            except:
                                                pass
    bababoy=False
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", "r") as f:
        nig=json.load(f)
        banesd=nig[str("Ban")]
    for susyy in banesd:
        if susyy==msg.author.id:
            bababoy=True
         
    if bababoy==False:
        try:
            if msg.author.bot==False:
            
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(msg.guild.id), "r") as f:
                    nig=json.load(f)
                    chaid=nig[str("servchannel")]
        except:
            chaid=None
        ban=False
        if msg.author.bot==False:
            if msg.channel.id == chaid:
                for bebra in Bot.guilds:

                    work=True
                    try:
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                            nig=json.load(f)
                    except:
                        work=False
                    if work==True and "https" not in msg.content and "invite" not in msg.content and "discord.gg" not in msg.content:
                        try:
                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                nig=json.load(f)
                                chaid=nig[str("servchannel")]
                        except:
                            chaid=None
        
                        if chaid==None:
                            pass
                    
                        else:
                
                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                nig=json.load(f)
                            try:
                                bans=nig[str("muted")]
                                for mem in bans:
                                    if msg.author.id ==mem:
                                        ban=True
                            except:
                                ban=False

                            if ban==False:
                                if msg.guild.id != bebra.id:
                                    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                        nig=json.load(f)
                                        try:
                                            chaid=nig[str("servchannel")]
                                        except:
                                            chaid=None
                                            
                                    try:
                                        channel=await Bot.fetch_channel(int(chaid))
                                        
                                        mywh=None
                                        for wh in nig:
                                            if wh=="webhook":
                                                mywh=nig[str("webhook")]
                                        if mywh!=None:
                                            
                                            webhook= await Bot.fetch_webhook(int(mywh))

                                        else:
                                            webhook=await channel.create_webhook(name="Vable Chat")
                                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "r") as f:
                                                    nig=json.load(f)
                                                    nig[str("webhook")]=webhook.id
                                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(bebra.id), "w") as f:
                                                    json.dump(nig, f, indent=4)
                                        newcontent=msg.content.replace("@everyone", "")
                                        newcontent=newcontent.replace("@here", "")
                                        await webhook.send(content=newcontent, username=f"{msg.author.id}", avatar_url=msg.author.avatar)
                                    except:
                                        pass
@Bot.slash_command(name="leave-chat", description="Выйти из  приватного чата")
@commands.has_guild_permissions(administrator=True)
async def rlpg(ctx,  token:str=commands.Param(description="Токен чата, от которого вы хотите отключить сервер")):

    id=ctx.guild.id


        

    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "r") as f:
            ads=json.load(f)
            servers=ads[str("servers")]
            adm=ads[str("adminserv")]
            none=False

    except:
        none=True

    if none==True:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Чата с токеном ``{token}`` нету.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        if adm==ctx.guild.id:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете покинуть чат, т.к. \nэтот сервер является основным ", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
        else:

            try:
                servers.remove(int(id))
                next=True
            except:
                next=False
            if next==False:
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вашего сервера нету в ``{token}``", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed, ephemeral=True)
            else:
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "w") as f:
                    json.dump(ads, f, indent=4)

                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(id), "r") as f:
                    sex=json.load(f)
                    chaid=sex[str(token)]
                    sex.pop(str(chaid))
                    sex.pop(str(token))
                    led:list=sex[str("chats")]
                    sex[str("chats")]=led.remove(token)
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(id), "w") as f:
                    json.dump(sex, f, indent=4)
                embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы отключились от этого приватного межсерверного чата!", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)

                embed.set_thumbnail(url=Bot.user.avatar)
                await ctx.send(embed=embed, ephemeral=True)
@tasks.loop(hours=10)
async def clears():
    for (dirpath, dirnames, filenames) in walk(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats"):
        files=filenames
    for file in files:
        file:str
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}".format(file), "r") as f:
            adsa=json.load(f)
            try:
                adm=adsa[str("adminserv")]
            except:
                pass
        if adsa[str("servers")]==[adm]:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(adm), "r") as f:
                a=json.load(f)
                try:
                    chan=a[str(file.replace(".json", ""))]
                    a.pop(chan)
                    a.pop(file.replace(".json", ""))
                except:
                    pass
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(adm), "w") as f:
                json.dump(a,f,indent=4)
            os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}".format(file))


    
@Bot.slash_command(name="remove-private-guild", description="Отключить сервер от вашего приватного чата")
async def rpg(ctx, id:str=commands.Param(description="Айди сервера, который вы хотите отключить"), token:str=commands.Param(description="Токен чата, от которого вы хотите отключить сервер")):
    if id==str(ctx.guild.id):
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете отключить свой-же сервер.`", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:

        zuk=True
        try:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token),"r") as f:
                zopa=json.load(f)
                perms=zopa[str("admin")]
        except:
            perms=None

            
        if int(perms) == ctx.author.id: 
            try:
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "r") as f:
                    ads=json.load(f)
                    servers=ads[str("servers")]
                    adm=ads[str("adminserv")]
                    none=False

            except:
                none=True
            if none==True:
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Чата с токеном ``{token}`` нету.", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed, ephemeral=True)
            else:
                if adm==ctx.guild.id:
                    embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете отключить этот сервер, т.к. \nон является основным ", color=0x42aaff)
                    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                    await ctx.send(embed=embed, ephemeral=True)
                else:
                    if int(perms) == ctx.author.id:
                        try:
                            servers.remove(int(id))
                            next=True
                        except:
                            next=False
                        if next==False:
                            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Такого сервера нету в ``{token}``", color=0x42aaff)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                            await ctx.send(embed=embed, ephemeral=True)
                        else:
                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "w") as f:
                                json.dump(ads, f, indent=4)
                            embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы отключили данный сервер от приватного межсерверного чата!", color=0x42aaff)
                            embed.set_thumbnail(url=Bot.user.avatar)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)

                            await ctx.send(embed=embed, ephemeral=True)
                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(id), "r") as f:
                                sex=json.load(f)
                                chaid=sex[str(token)]
                                sex.pop(str(chaid))
                                sex.pop(str(token))
                                led:list=sex[str("chats")]
                                sex[str("chats")]=led.remove(token)
                            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(id), "w") as f:
                                json.dump(sex, f, indent=4)
@Bot.slash_command(description="Список чатов, в которых есть ваш сервер")
async def fromchats(ctx):
    
    embed=disnake.Embed(title="Успешно! ✅", description="Вы получили список приватных серверов в чате.", color=0x42aaff)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_footer(text=f"Запросил {ctx.author}", icon_url=ctx.author.avatar)
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "r") as f:
        nig=json.load(f)
        mutes=nig[str("chats")]
    
    for mute in mutes:
        try:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(mute), "r") as f:
                nig=json.load(f)
                idios=nig[str("admin")]
            niger=await Bot.fetch_user(int(idios))
            embed.add_field(name=f"{mute}", value=f"Создатель: ``{niger.name}``",inline=False)    
        except:
            pass
    await ctx.send(embed=embed, ephemeral=True)

@Bot.slash_command(description="Просмотреть список серверов в приватном чате")
async def privateguilds(ctx,token:str=commands.Param(description="Токен приватного чата")):
    try:
        embed=disnake.Embed(title="Успешно! ✅", description="Вы получили список приватных серверов в чате.", color=0x42aaff)
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_footer(text=f"Запросил {ctx.author}", icon_url=ctx.author.avatar)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "r") as f:
            nig=json.load(f)
            mutes=nig[str("servers")]
        
        for mute in mutes:
            
            memb=await Bot.fetch_guild(int(mute))
            niger=await Bot.fetch_user(int(memb.owner_id))
            embed.add_field(name=f"{memb.name}", value=f"Создатель: ``{niger.name}``\nАйди: ``{memb.id}``",inline=False)    
        await ctx.send(embed=embed, ephemeral=True)
    except:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Такого приватного межсерверного чата нету!", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
        
@Bot.event
async def on_guild_remove(guild):

        os.remove(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(guild.id))

            

@Bot.slash_command(name="connect-to", description="Подключиться к приватному межсерверному чату")
@commands.cooldown(1, 120, commands.BucketType.user)

@commands.has_guild_permissions(administrator=True)
async def apg(ctx, token:str=commands.Param(description="Токен чата, к которому хотите подключиться")):
    skip=False
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token), "r") as f:
            aboba=json.load(f)

            admin=aboba[str("admin")]
            next=True
        
    except:
        next=False


    if next==False:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Такого приватного межсерверного чата нету!", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    
    else:
        for susa in aboba[str("servers")]:
            if susa==ctx.guild.id:
                skip=True
        if skip==False:
            print("нефалс")
            try:
                embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Запрос на присоеденение отправлен!", color=0x42aaff)
                embed.set_footer(text=f"Убедитесь,что бот может написать создателю чата.")
                await ctx.send(embed=embed, ephemeral=True)
                print("каксука")
                embed=disnake.Embed(title="Внимание! ⚠️", description="В ваш межсерверный чат хочет подключиться новый сервер!\n Разрешить подключение?", color=0x42aaff)
                embed.set_thumbnail(url=ctx.guild.icon)
                embed.set_footer(text=ctx.guild.id)
                embed.add_field(name="Название:", value=f"{ctx.guild.name}")
                embed.add_field(name="Токен чата:", value=f"{token}")
                embed.add_field(name="Владелец:", value=f"{ctx.guild.owner.name}")
                embed.set_author(name="Разрешить подключение?")
                pidr=await Bot.fetch_user(int(admin))
                await pidr.send(embed=embed,
                                                components=[
                                disnake.ui.Button(label="Да", style=disnake.ButtonStyle.green, custom_id="yea"),
                                disnake.ui.Button(label="Нет", style=disnake.ButtonStyle.red, custom_id="no")
                                
                        ],)

            except:
                embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Бот не может отправить сообщение {pidr.mention}``({pidr.name}#{pidr.tag})``", color=0x42aaff)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                await ctx.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы уже находитесь в этом чате!", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
        
@apg.error
async def apgsserr(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):

        time=error.retry_after
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Эй! Подожди. Попробуй еще раз через {time:.2f} ``Cек.``", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed, ephemeral=True)

@Bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id=="yea":
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(inter.message.embeds[0].fields[1].value), "r") as f:
            pe=json.load(f)
            servs=pe[str("servers")]
        servs.append(int(inter.message.embeds[0].footer.text))
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(inter.message.embeds[0].fields[1].value), "w") as f:
            json.dump(pe, f, indent=4)
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(inter.message.embeds[0].footer.text),"r") as f:
            prefix=json.load(f)
            try:
                asd=prefix[str("chats")]
                asd.append(inter.message.embeds[0].fields[1].value)
            except:
                prefix[str("chats")]=[inter.message.embeds[0].fields[1].value]

                
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(inter.message.embeds[0].footer.text),"w") as f:
            json.dump(prefix, f, indent=4)
        await inter.message.edit(embed=inter.message.embeds[0],                                         components=[
                        disnake.ui.Button(label="Да", style=disnake.ButtonStyle.green, custom_id="yea", disabled=True),
                        disnake.ui.Button(label="Нет", style=disnake.ButtonStyle.red, custom_id="no", disabled=True)
                        
                ],)
        
        await inter.send("Успешно!")
    
    if inter.component.custom_id=="no":
        await inter.message.delete()

@Bot.slash_command(name="config", description="Настройка тех. функций чата.")
async def conf(ctx,param=commands.Param(choices=["invites", "urls"]), mode:bool=commands.Param(description="Статус функции."), token:str=commands.Param(description="Токен приватного чата")):
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token),"r") as f:
            beb=json.load(f)
            admin=beb[str("admin")]
            ban=False
            print("анскил")
    except:
        ban=True
        print("ухади")
    if ban == True:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Такого чата нету!", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        if admin == ctx.author.id:

            beb[str(param)]= mode
            print("1")
            embed = disnake.Embed(title = "**Успешно! ✅**", description =f"Значение параметра ``{param}`` теперь ``{mode}`` ", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)      
            print("2")
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(token),"w") as f:
                json.dump(beb, f, indent=4)
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не владелец этого чата!", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)

    
@Bot.slash_command(name="create-chat", description="Создать приватный межсерверный чат", pass_context=True)
@commands.cooldown(2, 86400, commands.BucketType.user)

@commands.has_guild_permissions(administrator=True)
async def apgs(ctx):
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\counter.json","r") as f:
        nigae=json.load(f)
        count=nigae[str("count")]
        counte=count+1
        nigae[str("count")] = counte

    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\counter.json","w") as f:
        json.dump(nigae, f, indent=4)




    niga=f"{ctx.guild.id}"
    tken=f"{niga[4 : -4]}{counte}"
    tken=base64.b64encode(bytes(tken, "utf-8"))
    print(tken)
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id),"r") as f:
            prefix=json.load(f)
            try:
                asd=prefix[str("chats")]
                asd.append(f"{tken}")
            except:
                prefix[str("chats")]=[f"{tken}"]

                
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id),"w") as f:
        json.dump(prefix, f, indent=4)

    

    sas= {
        "admin": ctx.author.id,
        "adminserv": ctx.guild.id,
        "servers":[ctx.guild.id],
        "urls": False,
        "invites": False
    }
    open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(tken), 'x')
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats\{}.json".format(tken), "w", encoding="utf-8") as file:
        json.dump(sas, file)
    embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы создали приватный межсерверный чат. Его токен ``{tken}``!", color=0x42aaff)
    embed.set_thumbnail(url=Bot.user.avatar)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)

    await ctx.send(embed=embed, ephemeral=True)
@apgs.error
async def apgserr(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):

        time=error.retry_after/60/60
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы привысили лимит создания приватных чатов. Попробуйте снова через {time:.2f} ``Час(ов).``", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed, ephemeral=True)
@Bot.slash_command(description="Замутить пользователя в своем межсерверном чате")
@commands.has_guild_permissions(administrator=True)

async def mute(ctx, id:str=commands.Param(description="Айди пользователя")):
    use=None
    member=None
    if str(ctx.author.id)!=id or id==str(Bot.user.id):
        try:
            member= await Bot.fetch_user(int(id))
        except:

            pass
        
        if member!=None:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "r") as f:
                    nig=json.load(f)
                    try:
                        
                        liste=nig[str("muted")]
                        for us in liste:
                            if us==member.id:
                                use=us
                        if use!=None:
                            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы уже замутили ``{member.name}`` на своем сервере.", color=0x42aaff)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                            await ctx.send(embed=embed, ephemeral=True)
                        else:
                            embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы замутили ``{member.name}``, на своем сервере.", color=0x42aaff)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                            await ctx.send(embed=embed, ephemeral=True)
                            liste.append(member.id)
            
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "w") as f:
                                json.dump(nig, f, indent=4)
                    except:
                        nig[str("muted")] = [member.id]
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "w") as f:
                            json.dump(nig, f, indent=4)
                        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы замутили ``{member.name}``, на своем сервере.", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось найти пользователя.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете замутить себя или бота!", color=0x42aaff)
        embed.set_footer(text=f"Каков в этом смысл..", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
                     
            
@Bot.slash_command(description="Список заткнутых участников в вашем межсерверном чате")
@commands.has_guild_permissions(administrator=True)

async def muted(ctx):
    embed=disnake.Embed(title="Успешно! ✅", description="Вы получили список заткнутых участников.", color=0x42aaff)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_footer(text=f"Запросил {ctx.author}", icon_url=ctx.author.avatar)
    try:
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "r") as f:
            nig=json.load(f)
            mutes=nig[str("muted")]
    
        for mute in mutes:
            memb=await Bot.fetch_user(int(mute))
            embed.add_field(name=f"{memb.name}#{memb.discriminator}", value=f"``{memb.id}``",inline=False)    
    except:
        embed.add_field(name="Пусто", value="Вы не затыкали никого в вашем межсерверном чате")
    await ctx.send(embed=embed, ephemeral=True)
    
            
@Bot.event
async def on_ready():
    
        status.start()
        clears.start()
        print("!!!NEW LOGGED!!!")
        a=0
        print("Bot name: " +Bot.user.name)
        print(f"Bot id: {Bot.user.id}")
        print(f"Bot tag: {Bot.user.discriminator}")

        print(f"Bot servers: {len(Bot.guilds)}")
        print(f"Bot token: MTAyMTc4MzEyMzk2MjM4MDI4OA.GkqTnQ.ym_KMlpifRBn76GnSTMF0STVc5okZES__fsb1s")
        print("Succeful login")
        
        print("All chats:")
        for (dirpath, dirnames, filenames) in walk(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\chats"):
            for file in filenames:
                a=a+1
                print(f"{a}: {file}")

        
  


@tasks.loop(seconds=15)
async def status():


        await Bot.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"Документации, чтобы стать лучше"))
        await asyncio.sleep(15)
        await Bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(name=f"Зайдите на сервер поддержки!!!",type=disnake.ActivityType.competing))
        await asyncio.sleep(15)
        await Bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.playing, name=f"Клеш роял"))
        await asyncio.sleep(15)




            
@Bot.slash_command(description="Установить межсерверный канал")
@commands.has_guild_permissions(administrator=True)
@commands.bot_has_permissions(view_channel=True, manage_webhooks=True)

async def servchannel(ctx):
    with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), 'r') as f:
        prefix = json.load(f)
        try:
            a=prefix[str("ban")]
        except:
            a=False
    if a==False:
        try:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), 'r') as f:
                    prefix = json.load(f)
                    prefix[str("servchannel")] = ctx.channel.id 
                    niger=prefix[str("webhook")]
                    aberb=await Bot.fetch_webhook(int(niger))
                    a=aberb.edit(name="Vable Chat", channel=ctx.channel)
                    await aberb.delete()

                    prefix[str("webhook")]=a.id
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), 'w') as f:
                    json.dump(prefix, f, indent=4)
        except:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), 'r') as f:
                prefix = json.load(f)
                prefix[str("servchannel")] = ctx.channel.id 
                a=await ctx.channel.create_webhook(name="Vable chat")
                prefix[str("webhook")]= a.id
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), 'w') as f:
                    json.dump(prefix, f, indent=4)

                    
        embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы установили межсерверный канал - <#{ctx.channel.id}>", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Ваш сервер был заблокирован в межсерверном чате.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
            
@Bot.slash_command(description="Размутить пользователя в своем межсерверном чате")
@commands.has_guild_permissions(administrator=True)

async def unmute(ctx, id:str=commands.Param(description="Айди пользователя.")):
    
    if id!=str(ctx.author.id):
        try:
            member=await Bot.fetch_user(int(id))
        except:
            member=None
        if member!=None:
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "r") as f:
                    nig=json.load(f)
                    try:
                        
                        liste=nig[str("muted")]
                        for use in liste:
                            if use==member.id:
                                a=use
                        if use==None:
                            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не мутили ``{member.name}`` на своем сервере.", color=0x42aaff)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                            await ctx.send(embed=embed, ephemeral=True)
                        else:
                            liste.remove(member.id)

                            embed = disnake.Embed(title = "**Успешно! ✅**", description = f"Вы размутили ``{member.name}``, на своем сервере.", color=0x42aaff)
                            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                            await ctx.send(embed=embed, ephemeral=True)
                            
            
                        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(ctx.guild.id), "w") as f:
                                json.dump(nig, f, indent=4)
                    except:
                        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не мутили ``{member.name}`` на своем сервере.", color=0x42aaff)
                        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Не удалось найти пользователя.", color=0x42aaff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await ctx.send(embed=embed, ephemeral=True)    
    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Вы не можете размутить себя.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)
@Bot.slash_command(test_guilds=[1047132110391095407], description="Глобальный межсерверный мут [ДЛЯ МОДЕРАТОРОВ VABLE]")
async def gmute(ctx: disnake.ApplicationCommandInteraction ,id):
    abcd=False
    a=True
    gu= await Bot.fetch_guild(1047132110391095407)
    
    for b in [1047243772263665784,1047243783030448158,1047244301572243556,1047243615971311619]:
        ro=  disnake.utils.get(gu.roles, id=b)
        if ro in ctx.author.roles:
            abcd=True

    if abcd==True:
        try:
            member=await Bot.fetch_user(int(id))
        except:
            member=None
        if member!=None:
        
            with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", 'r') as f:
                prefix = json.load(f)
                sex=prefix[str("Ban")]
            for ab in sex:
                if ab==member.id:
                    a=False
            if a==True:
                sex.append(member.id)
                with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\banned.json", 'w') as f:
                    json.dump(prefix, f, indent=4)
                await ctx.send("Клоун в муте", ephemeral=True)
            else:
                pass            


    else:
        embed = disnake.Embed(title = "**Ошибка! ❌**", description = f"Эта команда доступна только для сотрудников VablVable.", color=0x42aaff)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, ephemeral=True)    

@Bot.event
async def on_guild_join(guild):
        ses={
                "servchannel":None
        }
        open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(guild.id), 'x')
        with open(r"C:\Users\ak29r\OneDrive\Рабочий стол\Vab-py\interchat\{}.json".format(guild.id), "w", encoding="utf-8") as file:
                json.dump(ses, file)

    
      
Bot.run("")
