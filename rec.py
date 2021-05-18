import discord, time
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, cooldown, MissingPermissions, check, has_role
import random
import datetime
import asyncio
import convert
import requests
from io import BytesIO
from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command
from datetime import datetime
from discord.utils import get
from discord_webhook import DiscordEmbed
import json
import os
from termcolor import colored
import aiofiles
import math
import sr_api
import contextlib
import io
import os
import logging

# Third party libraries
import textwrap
from traceback import format_exception

import discord
from pathlib import Path
import motor.motor_asyncio

# Local code




client = sr_api.Client("")

os.chdir("C:\\Users\\Reaper\\Desktop\\Aniko")




intents = discord.Intents.all()
client = commands.Bot(command_prefix = "d?", intents=intents, help_command=None, allowed_mentions = discord.AllowedMentions(
        everyone=False, 
        users=True, 
        roles=False, 
        replied_user=True
    ))
client.warnings = {}
client.sniped_messages = {}





def convert(time):
    pos = ["s","m","h","d"]  

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]

    

@client.event
async def on_ready():
	print("Bot is online")

async def ch_pr():
    await client.wait_until_ready()

    statuses = [f"d?help", "Invite me when?"]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)

client.loop.create_task(ch_pr())

	



@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
	if filename.endswith('py'):
		client.load_extension(f'cogs.{filename[:-3]}')








client.event
async def on_member_join(member):
    channel = member.server.get_channel("")
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}'
    await ctx.send_message(channel, fmt.format(member, member.server))

client.event
async def on_member_remove(member):
    channel = member.server.get_channel("")
    fmt = '{0.mention} has left/been kicked from the server.'
    await ctx.send_message(channel, fmt.format(member, member.server))





	



@client.group(invoke_without_command=True)
async def help(ctx):
    guild = ctx.guild
    Guild = ctx.guild
    em = discord.Embed(title = "**Here's a list of all my commands₊˚⊹₊‧**", description="・You can type d?help [command name] to get info about a specific command!", colour=discord.Color.from_rgb(255,253,208))


    em.add_field(name = "**— ୨୧︰Dank︰**", value = "<:w_dot:843232541531832320> heist\n<:w_dot:843232541531832320> heistimer\n<:w_dot:843232541531832320> taxcalc\n<:w_dot:843232541531832320> heistban\n<:w_dot:843232541531832320> stopheistban")
    em.add_field(name = "**— ୨୧︰Moderation︰**", value = "<:w_dot:843232541531832320> ban\n<:w_dot:843232541531832320> blacklist\n<:w_dot:843232541531832320> unban\n<:w_dot:843232541531832320> kick\n<:w_dot:843232541531832320> mute\n<:w_dot:843232541531832320> purge\n<:w_dot:843232541531832320> role\n<:w_dot:843232541531832320> warn\n<:w_dot:843232541531832320> warns\n<:w_dot:843232541531832320> drop")
    em.add_field(name = "**— ୨୧︰Others︰**", value = "<:w_dot:843232541531832320> invite\n<:w_dot:843232541531832320> help\n<:w_dot:843232541531832320> avatar\n<:w_dot:843232541531832320> whois\n<:w_dot:843232541531832320> serverinfo\n<:w_dot:843232541531832320> ping\n<:w_dot:843232541531832320> invite\n<:w_dot:843232541531832320> roleinfo\n<:w_dot:843232541531832320> gstart")

    await ctx.send(embed = em)






@client.group(invoke_without_command=True)
async def invite(ctx):
    em = discord.Embed(title = "Invite Link", description = "click below to invite me",color = ctx.author.color)

    em.add_field(name = "Invite me - ", value = "[Link](https://discord.com/api/oauth2/authorize?client_id=828366739988807721&permissions=4228902135&scope=bot)")

    await ctx.send(embed = em)





@client.command(name="eval", aliases=["exec"])
@commands.is_owner()
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
    )

    await pager.start(ctx)














@client.command()
async def mock(ctx, *, message):
    embed = discord.Embed(
    colour=discord.Color.from_rgb(255,253,208)
    )
    embed.set_thumbnail(url="https://www.pinclipart.com/picdir/big/497-4973607_mocking-spongebob-download-free-clipart-with-a-transparent.png")
    embed.add_field(name = "mocked message", value =''.join(random.choice((str.upper, str.lower))(c) for c in message))
    await ctx.send(embed=embed) 

@commands.command()
@commands.guild_only()
async def blush(self, ctx):
    embed = discord.Embed(
    colour=discord.Color.from_rgb(244, 182, 89)
    )

    embed.add_field(name="Emotes", value=f'{ctx.message.author.mention} is blushing', inline=False)
    embed.set_image(url=random.choice(blushgifdata))
    await ctx.send(embed=embed)

@commands.command()
@commands.guild_only()
async def dance(self, ctx):
    embed = discord.Embed(
    colour=discord.Color.from_rgb(244, 182, 89)()
    )

    embed.add_field(name="Emotes", value=f'{ctx.message.author.mention} is dancing', inline=False)
    embed.set_image(url=random.choice(dancegifdata))
    await ctx.send(embed=embed)

                         

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member,*, reason= "No reason provided"):
	await member.send("You have been kicked from the server, Because:"+reason)
	await member.kick(reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member : discord.Member,*, reason= "No reason provided"):
	await member.send(f"{member.name}, You have been banned from {ctx.guild.name}. Reason {reason}")
	await member.ban(reason=reason)




@client.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
  user = await client.fetch_user(id)
  await ctx.guild.unban(user)
  await ctx.send(f"{user} successfully unbanned") 
  embed = discord.Embed(title="Unban", timestamp=ctx.message.created_at, description=f"ID: {id}\nUser: {user}\n Responsible Moderator: {ctx.author}",colour=discord.Color.from_rgb(94, 255, 49))
  mod_log = ctx.guild.get_channel(823045546972938241)
  await mod_log.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, time, *, reason="Reason not given"):
    sleeptime = convert(time)
    embed = discord.Embed(title="Mute", timestamp=ctx.message.created_at, description=f"**Offender**: {member}\n**Duration**: {time}\n**Reason**: {reason}\n **Responsible Moderator:** {ctx.author}",colour=discord.Color.from_rgb(244, 137, 66))
    embed.set_footer(text=f"ID: {member.id}")
    mod_log = ctx.guild.get_channel(823045546972938241)
    await mod_log.send(embed=embed)

    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name="Muted")

    if not muteRole:
        muteRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=False)

    await member.add_roles(muteRole, reason=reason)

    if time[-1] == "m":
      await ctx.send(f"Successfully Muted {member} for {time[:-1]} minutes")

    if time[-1] == "s":
      await ctx.send(f"Successfully Muted {member} for {time[:-1]} seconds")

    if time[-1] == "h":
      await ctx.send(f"Successfully Muted {member} for {time[:-1]} hours")

    if time[-1] == "d":
      await ctx.send(f"Successfully Muted {member} for {time[:-1]} days")

    try:
        if time[-1] == "m":
          await member.send(f"You have been muted for {time[:-1]} minutes. Reason: {reason}. Moderator {ctx.message.author}")

        if time[-1] == "s":
          await member.send(f"You have been muted for {time[:-1]} seconds. Reason: {reason}. Moderator {ctx.message.author}")

        if time[-1] == "h":
          await member.send(f"You have been muted for {time[:-1]} hours. Reason: {reason}. Moderator {ctx.message.author}")

        if time[-1] == "d":
          await member.send(f"You have been muted for {time[:-1]} days. Reason: {reason}. Moderator {ctx.message.author}")

    except:
    	await ctx.send("<:muted:828800100750852136>")

    await asyncio.sleep(sleeptime)
    await member.remove_roles(muteRole, reason="Automatic unmute")
    try:
        await member.send(f"**You are now unmuted**")
        embed = discord.Embed(title="Unmute", timestamp=ctx.message.created_at, description=f"**Offender**: {member}\n**Reason**: Automatic unmute from mute made {time} ago by {ctx.author} (ID: {ctx.author.id})\n **Responsible Moderator:** {ctx.author}",colour=discord.Color.from_rgb(66, 244, 167))
        embed.set_footer(text=f"ID: {member.id}")
        await mod_log.send(embed=embed)

    except:
        embed = discord.Embed(title="Unmute", timestamp=ctx.message.created_at, description=f"**Offender**: {member}\n**Reason* *: Automatic unmute from mute made {time} ago by {ctx.author} (ID: {ctx.author.id})\n **Responsible Moderator:** {ctx.author}",colour=discord.Color.from_rgb(66, 244, 167))
        embed.set_footer(text=f"ID: {member.id}")
        await mod_log.send(embed=embed)



@client.command(aliases=['delete'])
@commands.has_permissions(manage_messages = True)
async def purge(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f"Purged {amount} Messages")



@client.command(aliases=['whois'])
async def info(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = "\n".join([role.mention for role in member.roles])
    embed = discord.Embed(colour=discord.Color.from_rgb(255,253,208), timestamp=ctx.message.created_at,
                          title=f"Users Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="Members ID:", value=member.id)
   
    embed.add_field(name="Account Created On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    x = len(roles)
    if x < 750:
        embed.add_field(name="Roles", value=roles)
    else:
        embed.add_field(name="Roles", value="To many to list")

    

    await ctx.send(embed=embed)    



@client.command(name = "hpurge")
async def helppurge(ctx):

    em = discord.Embed(Title = "PURGE", description = "Deletes the amount of messages you input", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "?purge <amount>")

    await ctx.send(embed = em)



client.command(aliases=['si'])
async def serverinfo(ctx):
	h = 0
	for channel in ctx.guild.text_channels:
		h += 1

	v = 0
	for channel in ctx.guild.voice_channels:
		v += 1

	bot = 0
	for member in ctx.guild.members:
		if member.bot:
			bot += 1

	roles = 0
	for role in ctx.guild.roles:
		roles += 1


	guild = ctx.guild
	Guild = ctx.guild
	em = discord.Embed(title = "__Server Info__", color=discord.Color(0xEFE720))
	em.set_author(name=f"{ctx.guild.name}", icon_url = "")
	em.set_thumbnail(url=f"{guild.icon_url}")
	em.add_field(name="Server Owner", value = f":crown: {guild.owner}")
	em.add_field(name="Features", value= f":white_check_mark:  Invite Splash\n:white_check_mark:  News Channels\n:white_check_mark:  Animated Icon")
	em.add_field(name="Boosts", value = f"<a:booster:829061426546343956> Level {guild.premium_tier}\n<a:booster:829061426546343956> {guild.premium_subscription_count} Boosts")
	em.add_field(name="Channels", value=f"<:TextChannel:829051535081603092> {h} Text\n<:VoiceChannel:829051558603391046> {v} Voice")
	em.add_field(name="Prefix", value=f"<a:diamond:829063082621009961> `?`")
	em.add_field(name="Members", value=f"<a:amongusrainbow:829062086410633277> Total: {len(ctx.guild.members)}\nğŸ§ Humans: {len([member for member in guild.members if not member.bot])}\n<:bot:829062312744190004> Bots: {bot}", inline = True)
	em.add_field(name="Roles", value=f"<a:discordblob:829083826511806465> {roles} Roles", inline = True)
	em.add_field(name="Role Information", value=f":crown: Owner Role: <@&800426526889607229>\n:tools: Modeator Roles: <@&810800169712746508> <@&782044759954161674> <@&782041445418532886>\n:person_standing: Member Role: <@&782044513383219220>", inline = False)
	em.add_field(name="Info", value=f":computer: Server Region: {guild.region}\n<a:verify:829094509895876639> Verification Level: {Guild.verification_level}\n<:discordlogo:829094698797760602> Icon: [Icon Link]({Guild.icon_url})", inline = True)
	em.add_field(name="Dank Memer", value=f"<a:premiumcrown:829102168183275531> Premium: Yes\n:frog: Auto Meme: Enabled\n:frog: Auto Meme Channel: <#818602841375244339>\n:moneybag: Rob Disabled: True\n<a:diamond:829063082621009961> Prefix: pls", inline = True)
	em.set_footer(text="ID: 782041178489094154, Created â€¢ 11/27/2020")

	await ctx.send(embed = em)


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    if ctx.guild.id in client.sniped_messages:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

        embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")

        await ctx.channel.send(embed=embed)
    else:
        await ctx.send("There's nothing to snipe!")


@client.command(aliases=['av'])
async def avatar(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(
        colour=discord.Color.from_rgb(244, 182, 89)
    )
    embed.add_field(name=f"{member}", value=f"[[Download]]({member.avatar_url})")
    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)



@client.command()
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.send(mesg)


@client.group(invoke_without_command=True)
@commands.has_permissions(manage_roles=True)
async def role(ctx, member : discord.Member, *, role : discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(f"Removed **{role}** from **{member}**.")
    else:
        await member.add_roles(role)
        await ctx.send(f"Added **{role}** to **{member}**.")





@role.command()
async def info(ctx, *, role : discord.Role):
    x = role.created_at

    creation = x.strftime("%A, %B %d At %I:%M %p, %Y")
    em = discord.Embed(title = f"{role}", description = f"{role.mention}\nMembers: {len(role.members)} | Position: {role.position:}\nColor: {role.color}\nHoisted: {role.hoist}\nMentionable: {role.mentionable}\nCreated At: {creation}", color=role.color)
    em.set_footer(text=f"ID: {role.id}")
    await ctx.send(embed=em)



@client.command()
@commands.has_permissions(manage_messages = True)
async def drop(ctx, time, *, prize):
    await ctx.message.delete()
    sleeptime = convert(time)
    em = discord.Embed(title=f"<a:poghype:818892261769216061> INCOMING DROP FOR {prize}", description= f"BE ON THE LOOKOUT FOR A DROP IN THIS CHANNEL IN {time}", colour=discord.Color.from_rgb(244, 182, 3))
    eme = discord.Embed(title="INCOMING DROP", description= "COMING IN 4", color=discord.Color.from_rgb(50, 24, 100))
    emb = discord.Embed(title="INCOMING DROP", description= "COMING IN 3", color=discord.Color.from_rgb(20, 24, 240))
    embe = discord.Embed(title="INCOMING DROP", description= "COMING IN 2", color=discord.Color.from_rgb(240, 1, 240))
    embed = discord.Embed(title="INCOMING DROP", description= "COMING IN 1", color=discord.Color.from_rgb(1, 255, 1))
    e = discord.Embed(title=f"<a:giveaway_yellow:819392280490278942> {prize} HAS BEEN DROPPED", description= f"**FIRST TO REACT TO <a:giveaway_yellow:819392280490278942> GETS {prize}!!**", color=discord.Color.from_rgb(1, 255, 1))
    role = ctx.guild.get_role(805147568723329035)
    msgr = await ctx.send(role.mention)
    msge = await ctx.send(embed=em)
    await asyncio.sleep(sleeptime)
    msg = await ctx.send(embed=eme)
    await asyncio.sleep(1)
    await msg.edit(embed=emb)
    await asyncio.sleep(1)
    await msg.edit(embed=embe)
    await asyncio.sleep(1)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)
    await msg.edit(embed=e)
    await msg.add_reaction("<a:giveaway_yellow:819392280490278942>")

    def check(reaction, user):
        return user != ctx.guild.me and str(reaction.emoji) == '<a:giveaway_yellow:819392280490278942>'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('You were unable to react in time')
    else:
        ytyt = discord.Embed(title=f"{prize}", timestamp=ctx.message.created_at, description=f"Winner: {user.mention}\n\nHosted By: {ctx.author.mention}")
        ytyt.set_author(name="This Drop has Ended")
        await msg.edit(embed=ytyt)
        await ctx.send(f"***CONGRATS***\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winner:** {user.mention}!\n<a:cool:819391289418055760> Please DM {ctx.author.mention} for your prize")
        embed = discord.Embed(title="Its Your Lucky Day!", description = f"You have won {prize} from a Drop in {ctx.guild.name}!\n Please contact {ctx.author.mention} to receive {prize}!", color=discord.Color.from_rgb(255,192,203))
        await user.send(embed=embed)
    await msge.delete()


@client.command()
async def hack(ctx, member : discord.Member=None):
    if member is None:
        member = ctx.author

    email = [f"{member.name}eatsButt@hotmail.com,", f"{member.name}isgay@gmail.com", f"{member.name}isCoolXD@icloud.com", f"{member.name}likesfortnite@gmail.com", f"{member.name}hasabigbooty@hotmail.com"]
    dm = [f"yeah she goes to another school", "Parallel Dankers is the Best Server", "man I love my mommy", "should I shave my neckbeard", "I took a test today I have corona now Ima Spread it", "What to do if i have raped a moose", "Im eating rn", "What is crabs", "Yea just checked my penis is 12 inches", "Mine is 1 Inch", "When is the Heist", "ShrekFan101 is Daddy", "What to do if my dog can't walk"]
    word = ["meme", "Kek", "penis", "Lmao", "e", "reeeee", "Gay", "Hot", "Weiner", "WeGay", "LifeAlert", "Help", "Shrek", "69", "Chungus"]
    emote = ["<a:kek:807392377429819392>", "<:zoomer:814336954039795724>", "<a:rickroll:809556864287244339>", "<a:wink:808614394476494858>", "<:linus:809642233288589313>"]
    password = ["123456789", "Password", f"{member.name} is hot", "I eat feet", f"{member.name} is a virgin123", f"{member.name} likes anime", f"bigweiner123", "big penis oh yeah", "Weinerboy123"]
    msg = await ctx.send(f"Hacking {member.name} Now")
    ip = ["127.0.0.1:2129","696.9.6:9696", "127.0.0.1:6969", "127.1.1.1:4209"]
    await asyncio.sleep(3)
    await msg.edit(content="[▖] Finding discord login... (2fa bypassed)")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▘] Found:\n**Email:** `{random.choice(email)}`\n**Password:** `{random.choice(password)}`")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▝] Fetching dms with closest friends (if there are any friends at all)")
    await asyncio.sleep(1)
    await msg.edit(content=f'[▗] **Last DM:** "{random.choice(dm)}"')
    await asyncio.sleep(2)
    await msg.edit(content=f'[▖] Finding most common word...')
    await asyncio.sleep(1)
    await msg.edit(content=f'[▘] const mostCommon = "{random.choice(word)}"')
    await asyncio.sleep(1)
    await msg.edit(content=f'[▝] Injecting trojan virus into discriminator #{member.discriminator}')
    await asyncio.sleep(1)
    await msg.edit(content=f'[▗] Virus injected, emotes stolen {random.choice(emote)}')
    await asyncio.sleep(1)
    await msg.edit(content=f"[▖] Setting up Epic Store account..")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▘] Hacking Epic Store account.... <a:chugmyjug:829809122945400832>")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▝] Finding IP address")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▗] **IP address:** {random.choice(ip)}")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▖] Selling Data to the Government...")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▘] Reporting account to discord for breaking TOS...")
    await asyncio.sleep(1)
    await msg.edit(content=f"[▝] Hacking medical records")
    await asyncio.sleep(1)
    await msg.edit(content=f"Finished hacking {member.name}")
    await ctx.send("The *totally* real and dangerous hack is complete")




@client.command()
async def amongus(ctx):
    embed1 = discord.Embed(title = "Who's the imposter?", description = "Find out who the imposter is before the reactor breaks!", colour= discord.Colour.red())
    embed1.add_field(name = 'Red' , value= '<:amongus_red:828659744200851559>')
    embed1.add_field(name = 'Blue' , value= '<:amongus_blue:828659518090117130>')
    embed1.add_field(name = 'Lime' , value= '<:amongus_lime:828659802254868560>')
    embed1.add_field(name = 'Green' , value= '<:amongus_green:828659842758869072>')
    embed1.add_field(name = 'Yellow', value = '<:amongus_yellow:829573909027487744>')
    embed1.add_field(name = 'Cyan', value = '<:amongus_cyan:829574506993025035>')
    msg = await ctx.send(embed=embed1)

    emojis = {
        'red': '<:amongus_red:828659744200851559>',
        'blue': '<:amongus_blue:828659518090117130>',
        'lime': '<:amongus_lime:828659802254868560>',
        'green': '<:amongus_green:828659842758869072>',
        'yellow': '<:amongus_yellow:829573909027487744>',
        'cyan': '<:amongus_cyan:829574506993025035>'
    }

    imposter = random.choice(list(emojis.items()))
    imposter = imposter[0]

    print(emojis[imposter])

    for emoji in emojis.values():
        await msg.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in emojis.values()

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)

    except asyncio.TimeoutError:
        description= "Reactor Meltdown.{0} was the imposter...".format(imposter)
        embed = discord.Embed(title = "Defeat", description= description, colour = discord.Colour.green())
        await ctx.send(embed=embed)
    else:
        if str(reaction.emoji) == emojis[imposter]:
            description = "**{0}** was the imposter...".format(imposter)
            embed = discord.Embed(title = "Victory", description= description, colour = discord.Colour.green())
            
            await ctx.send(embed=embed)

        else:
            for key, value in emojis.items(): 
                if value == str(reaction.emoji):
                    description = "**{0}** was not the imposter...".format(key)
                    embed = discord.Embed(title = "Defeat", description= description, colour =  discord.Colour.green())
                    await ctx.send(embed=embed)
                    break







mainshop = [{"name":"Nothing","price":1000},
            {"name":"Nothing","price":2000}]


@client.command(aliases = ['bal'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed = discord.Embed(
        title = f'{ctx.author.name} Balance',
        color = discord.Color.blue()
    )
    embed.add_field(name = "***Wallet:***", value = f":coin:{wallet_amt}:coin:", inline = True)
    embed.add_field(name = "***Bank:***", value = f":coin:{bank_amt}:coin:", inline = True)
    await ctx.send(embed= embed)


@client.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    embed = discord.Embed(
        title = "Withdraw",
        description = f'{ctx.author.mention} You withdrew {amount} coins',
        color = discord.Color.blue()
    )
    await ctx.send(embed = embed)    


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def give(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'wallet')
    await update_bank(member,amount,'wallet')
    embed = discord.Embed(
        title = f"Shared {amount}",
        description = f'{ctx.author.mention} You gave {member} {amount} coins',
        color = discord.Color.blue()
    )
    await ctx.send(embed = embed)

@give.error
async def give_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Your not Bill Gates",
            description = "Woahhh there buddy, your not as rich as Bill Gates. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)    


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    embed = discord.Embed(
        title = f"{ctx.author.name} Robbed {member.name}",
        description = f'You Robbed {member} For {earning} :coin:',
        color = discord.Color.blue()
    )
    await ctx.send(embed = embed)

@rob.error
async def rob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Woah there",
            description = "Woahhh there buddy. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)

        final.append(a)
    
    embed = discord.Embed(
        title = f"{ctx.author}'s slot machine",
        description = f"**>** {final[0]} {final[1]} {final[2]} **<**",
        inline = True
    )
    msg = await ctx.send(embed = embed)
    eme = discord.Embed(title = f"{ctx.author.name}'s Mega Winning Slot Machine", description = f"**>** {final[0]} {final[1]} {final[2]} **<**\n\nYou won **⏣ {4*amount}**\nYou now have **⏣ {bal}**", color = discord.Color.green())
    em = discord.Embed(title = f"{ctx.author.name}'s Losing Slot Machine", description = f"**>** {final[0]} {final[1]} {final[2]} **<**\n\nYou lost **⏣ {-1*amount}**\nYou now have **⏣ {bal}**", color = discord.Color.red())
    emb = discord.Embed(title = f"{ctx.author.name}'s Winning Slot Machine", description = f"**>** {final[0]} {final[1]} {final[2]} **<**\n\nYou won **⏣ {2*amount}**\nYou now have **⏣ {bal}**", color = discord.Color.green())
    await asyncio.sleep(2)

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await msg.edit(embed=emb)
    elif final[0] == final[1] == final[2]:
        await update_bank(ctx.author,4*amount)
        await msg.edit(embed=eme)
    else:
        await update_bank(ctx.author,-1*amount)
        await msg.edit(embed=em)

@slots.error
async def slots_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Chill there buddy",
            description = "Dont try to break me. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)        
        

@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def shop(ctx):
    em = discord.Embed(
        title = "Shop",
        description = f"Your Shop Items In mainshop = {"Beans\nAK"}",
        color = discord.Color.blue(),
        inline = True
    )
    await ctx.send(embed = em)



@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Item Isn't There!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    embed = discord.Embed(
        title = f"You Bought {amount} {item}'s",
        color = discord.Color.blue()
    )
    await ctx.send(embed = embed)

@buy.error
async def buy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Your not Bill Gates",
            description = "Woahhh there buddy, your not as rich as Bill Gates. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)





@client.command(aliases = ['inv'])
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        inv = users[str(user.id)]["inv"]
    except:
        inv = []


    em = discord.Embed(title = "Inventory", color = discord.Color.blue())
    for item in inv:
        name = item["item"]
        amount = item["amount"]
        
        em.add_field(name = name, value = amount, inline = True)    

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["inv"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["inv"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Item Isn't There!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your inventory.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your inventory.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

@sell.error
async def sell_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Woah there buddy",
            description = "Woahhh there buddy, dont try to break me. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)   




@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    embed = discord.Embed(
        title = "Deposited!",
        description = f'{ctx.author.mention} You deposited {amount} coins',
        color = discord.Color.blue()
    )
    await ctx.send(embed = embed)





@client.command(aliases = ["lb"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def leaderboard(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = f'{member.name}#{member.discriminator}'
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@leaderboard.error
async def leaderboard_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Woah calm down",
            description = "Woahhh there buddy, call down dont try to break me. Wait **{:.2f} seconds**".format(error.retry_after),
            color = discord.Color(0x3F51B5)
        )
        await ctx.send(embed = embed)



async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 50
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal


@withdraw.error
async def withdraw_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title = "Cooldown",
            description = 'This Command Is On A Cooldown, Please Try Again In {:.2f}s'.format(error.retry_after),
            color = discord.Color.blue()
        )
        await ctx.send(embed = embed)
    else:
        raise error                    

#<a:Timer:830264560103194675>

@client.command()
@commands.has_permissions(manage_messages=True)
async def heist(ctx, amount=None, req : discord.Role=None):
    await ctx.message.delete()
    if amount is None:
        await ctx.send("You need to add an amount")
        return
    guild = ctx.guild
    heistlog = guild.get_channel(820042650911899708)

    if req is None:
    	req = ctx.guild.default_role
    if amount.endswith('e1'):
        z = float(amount)
        x = int(z)
        y = x*10
    if amount.endswith('e2'):
        z = float(amount)
        x = int(z)
        y = x*100
    if amount.endswith('e3'):
        z = float(amount)
        x = int(z)
        y = x*1000
    if amount.endswith('e4'):
        z = float(amount)
        x = int(z)
        y = x*10000
    if amount.endswith('e5'):
        z = float(amount)
        x = int(z)
        y = x*100000
    if amount.endswith('e6'):
        z = float(amount)
        x = int(z)
        y = x*1000000
    if amount.endswith('e7'):
        z = float(amount)
        x = int(z)
        y = x*10000000
    if amount.endswith('e8'):
        z = float(amount)
        x = int(z)
        y = x*100000000

    y = int(x)
    commas = "{:,}".format(y)
    if y > 10000000:
        heistime = 240
        em = discord.Embed(title=f"<a:pepeheist:818731868245458954> Heist Event", timestamp=ctx.message.created_at, description=f"**__Tips and Tricks:__**\n\n> 💰 Withdraw **`\u23e3 2000 coins`**\n> <:wow:808610056408662016> Turn off passive\n> <:lifesaver:831712690316640327> Get a life saver **`pls buy saver`**\n> <a:pepe_heist:808612393058959401> Type **`JOIN HEIST`** when this channel unlocks!\n> <:mochatime:831712955887910932> The Channel unlocks for **4 Minutes**", color=discord.Color(0xffff00))
        em.add_field(name=f"Member Count:", value=f"\n**```ini\n🧍 [{len(ctx.guild.members)}]```**", inline=True)
        em.add_field(name=f"Heist Amount:", value=f"\n**```ini\n💸 [{commas}]```**", inline=True)
        em.add_field(name=f"Heist Status:", value=f"\n**```ini\n📈 [Awaiting!]```**", inline=True)
        em.add_field(name=f"**﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏**", value=f"**```fix\n📊 The channel unlocks when the heist starts.```**", inline=False)
        emb = discord.Embed(title=f"<a:pepeheist:818731868245458954> Heist Event", timestamp=ctx.message.created_at, description=f"**__Tips and Tricks:__**\n\n> 💰 Withdraw **`\u23e3 2000 coins`**\n> <:wow:808610056408662016> Turn off passive\n> <:lifesaver:831712690316640327> Get a life saver **`pls buy saver`**\n> <a:pepe_heist:808612393058959401> Type **`JOIN HEIST`** when this channel unlocks!\n> <:mochatime:831712955887910932> The Channel unlocks for **4 Minutes**", color=discord.Color(0xffff00))
        emb.add_field(name=f"Member Count:", value=f"\n**```ini\n🧍 [{len(ctx.guild.members)}]```**", inline=True)
        emb.add_field(name=f"Heist Amount:", value=f"\n**```ini\n💸 [{commas}]```**", inline=True)
        emb.add_field(name=f"Heist Status:", value=f"\n**```ini\n📈 [Completed!]```**", inline=True)
        emb.add_field(name=f"**﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏**", value=f"**```fix\n📊 The channel unlocks when the heist starts.```**", inline=False)
        channel = ctx.channel
        msge = await channel.send(embed=em)
    if y < 10000000:
        heistime = 90
        em = discord.Embed(title=f"<a:pepeheist:818731868245458954> Heist Event", timestamp=ctx.message.created_at, description=f"**__Tips and Tricks:__**\n\n> 💰 Withdraw **`\u23e3 2000 coins`**\n> <:wow:808610056408662016> Turn off passive\n> <:lifesaver:831712690316640327> Get a life saver **`pls buy saver`**\n> <a:pepe_heist:808612393058959401> Type **`JOIN HEIST`** when this channel unlocks!\n> <:mochatime:831712955887910932> The Channel unlocks for **1 Minute** and **30 Seconds**", color=discord.Color(0xffff00))
        em.add_field(name=f"Member Count:", value=f"\n**```ini\n🧍 [{len(ctx.guild.members)}]```**", inline=True)
        em.add_field(name=f"Heist Amount:", value=f"\n**```ini\n💸 [{commas}]```**", inline=True)
        em.add_field(name=f"Heist Status:", value=f"\n**```ini\n📈 [Awaiting!]```**", inline=True)
        em.add_field(name=f"**﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏**", value=f"**```fix\n📊 The channel unlocks when the heist starts.```**", inline=False)
        emb = discord.Embed(title=f"<a:pepeheist:818731868245458954> Heist Event", timestamp=ctx.message.created_at, description=f"**__Tips and Tricks:__**\n\n> 💰 Withdraw **`\u23e3 2000 coins`**\n> <:wow:808610056408662016> Turn off passive\n> <:lifesaver:831712690316640327> Get a life saver **`pls buy saver`**\n> <a:pepe_heist:808612393058959401> Type **`JOIN HEIST`** when this channel unlocks!\n> <:mochatime:831712955887910932> The Channel unlocks for **1 Minute** and **30 Seconds**", color=discord.Color(0xffff00))
        emb.add_field(name=f"Member Count:", value=f"\n**```ini\n🧍 [{len(ctx.guild.members)}]```**", inline=True)
        emb.add_field(name=f"Heist Amount:", value=f"\n**```ini\n💸 [{commas}]```**", inline=True)
        emb.add_field(name=f"Heist Status:", value=f"\n**```ini\n📈 [Completed!]```**", inline=True)
        emb.add_field(name=f"**﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏**", value=f"**```fix\n📊 The channel unlocks when the heist starts.```**", inline=False)
        channel = ctx.channel
        msge = await channel.send(embed=em)
    await ctx.send('<a:Timer:830115308739887104> Listening for a heist in this channel... Type "CANCEL" to Cancel')
    def check(m):
        return m.content.endswith('soon!') and m.channel == channel
    try: 
        msg = await client.wait_for('message', check=check, timeout=60)
        await ctx.channel.set_permissions(req, send_messages = True)
        await ctx.send(f"Channel Unlocked for {req}")
        await msge.edit(embed=emb)
        await asyncio.sleep(heistime)
        await ctx.channel.set_permissions(req, send_messages = False)
        await ctx.send(f"Channel Locked for {req}")
        embed = discord.Embed(title=f"<a:pepeheist:818731868245458954> {guild.name} Heists", timestamp=ctx.message.created_at, description=f"<a:pepemoneyrain:819391189009956875> **Amount:** [__`⏣ {commas}`__](https://youtube.com)\n<a:wave:831434903207280640> **Host: {ctx.author.mention}**\n🔒 **Requirement: {req.mention}**", color=discord.Color.red())
        await heistlog.send(embed=embed)
    except asyncio.TimeoutError:
        await ctx.send("No heist Found")

@client.command()
@commands.has_permissions(manage_messages=True)
async def heistimer(ctx,amount):
	ex = discord.Embed(title=f"{amount} Heist Timer", description=f"**29** minutes, **59** seconds\nHosted by {ctx.author}")
	em = discord.Embed(title=f"{amount} Heist Timer", description=f"**29** minutes, **29** seconds\nHosted by {ctx.author}")
	emb = discord.Embed(title=f"{amount} Heist Timer", description=f"**28** minutes, **59** seconds\nHosted by {ctx.author}")
	embe = discord.Embed(title=f"{amount} Heist Timer", description=f"**28** minutes, **29** seconds\nHosted by {ctx.author}")
	embed = discord.Embed(title=f"{amount} Heist Timer", description=f"**27** minutes, **59** seconds\nHosted by {ctx.author}")
	a = discord.Embed(title=f"{amount} Heist Timer", description=f"**27** minutes, **29** seconds\nHosted by {ctx.author}")
	b = discord.Embed(title=f"{amount} Heist Timer", description=f"**26** minutes, **59** seconds\nHosted by {ctx.author}")
	c = discord.Embed(title=f"{amount} Heist Timer", description=f"**26** minutes, **29** seconds\nHosted by {ctx.author}")
	d = discord.Embed(title=f"{amount} Heist Timer", description=f"**25** minutes, **59** seconds\nHosted by {ctx.author}")
	e = discord.Embed(title=f"{amount} Heist Timer", description=f"**25** minutes, **29** seconds\nHosted by {ctx.author}")
	f = discord.Embed(title=f"{amount} Heist Timer", description=f"**24** minutes, **59** seconds\nHosted by {ctx.author}")
	g = discord.Embed(title=f"{amount} Heist Timer", description=f"**24** minutes, **29** seconds\nHosted by {ctx.author}")
	h = discord.Embed(title=f"{amount} Heist Timer", description=f"**23** minutes, **59** seconds\nHosted by {ctx.author}")
	i = discord.Embed(title=f"{amount} Heist Timer", description=f"**23** minutes, **29** seconds\nHosted by {ctx.author}")
	j = discord.Embed(title=f"{amount} Heist Timer", description=f"**22** minutes, **59** seconds\nHosted by {ctx.author}")
	k = discord.Embed(title=f"{amount} Heist Timer", description=f"**22** minutes, **29** seconds\nHosted by {ctx.author}")
	l = discord.Embed(title=f"{amount} Heist Timer", description=f"**21** minutes, **59** seconds\nHosted by {ctx.author}")
	m = discord.Embed(title=f"{amount} Heist Timer", description=f"**21** minutes, **29** seconds\nHosted by {ctx.author}")
	n = discord.Embed(title=f"{amount} Heist Timer", description=f"**20** minutes, **59** seconds\nHosted by {ctx.author}")
	o = discord.Embed(title=f"{amount} Heist Timer", description=f"**20** minutes, **29** seconds\nHosted by {ctx.author}")
	p = discord.Embed(title=f"{amount} Heist Timer", description=f"**19** minutes, **59** seconds\nHosted by {ctx.author}")
	q = discord.Embed(title=f"{amount} Heist Timer", description=f"**19** minutes, **29** seconds\nHosted by {ctx.author}")
	r = discord.Embed(title=f"{amount} Heist Timer", description=f"**18** minutes, **59** seconds\nHosted by {ctx.author}")
	s = discord.Embed(title=f"{amount} Heist Timer", description=f"**18** minutes, **29** seconds\nHosted by {ctx.author}")
	t = discord.Embed(title=f"{amount} Heist Timer", description=f"**17** minutes, **59** seconds\nHosted by {ctx.author}")
	u = discord.Embed(title=f"{amount} Heist Timer", description=f"**17** minutes, **29** seconds\nHosted by {ctx.author}")
	v = discord.Embed(title=f"{amount} Heist Timer", description=f"**16** minutes, **59** seconds\nHosted by {ctx.author}")
	w = discord.Embed(title=f"{amount} Heist Timer", description=f"**16** minutes, **29** seconds\nHosted by {ctx.author}")
	x = discord.Embed(title=f"{amount} Heist Timer", description=f"**15** minutes, **59** seconds\nHosted by {ctx.author}")
	y = discord.Embed(title=f"{amount} Heist Timer", description=f"**15** minutes, **29** seconds\nHosted by {ctx.author}")
	z = discord.Embed(title=f"{amount} Heist Timer", description=f"**14** minutes, **59** seconds\nHosted by {ctx.author}")
	aa = discord.Embed(title=f"{amount} Heist Timer", description=f"**14** minutes, **29** seconds\nHosted by {ctx.author}")
	ab = discord.Embed(title=f"{amount} Heist Timer", description=f"**13** minutes, **59** seconds\nHosted by {ctx.author}")
	ac = discord.Embed(title=f"{amount} Heist Timer", description=f"**13** minutes, **29** seconds\nHosted by {ctx.author}")
	ad = discord.Embed(title=f"{amount} Heist Timer", description=f"**12** minutes, **59** seconds\nHosted by {ctx.author}")
	ae = discord.Embed(title=f"{amount} Heist Timer", description=f"**12** minutes, **29** seconds\nHosted by {ctx.author}")
	af = discord.Embed(title=f"{amount} Heist Timer", description=f"**11** minutes, **59** seconds\nHosted by {ctx.author}")
	ag = discord.Embed(title=f"{amount} Heist Timer", description=f"**11** minutes, **29** seconds\nHosted by {ctx.author}")
	ah = discord.Embed(title=f"{amount} Heist Timer", description=f"**10** minutes, **59** seconds\nHosted by {ctx.author}")
	ai = discord.Embed(title=f"{amount} Heist Timer", description=f"**10** minutes, **29** seconds\nHosted by {ctx.author}")
	aj = discord.Embed(title=f"{amount} Heist Timer", description=f"**9** minutes, **59** seconds\nHosted by {ctx.author}")
	ak = discord.Embed(title=f"{amount} Heist Timer", description=f"**9** minutes, **29** seconds\nHosted by {ctx.author}")
	al = discord.Embed(title=f"{amount} Heist Timer", description=f"**8** minutes, **59** seconds\nHosted by {ctx.author}")
	am = discord.Embed(title=f"{amount} Heist Timer", description=f"**8** minutes, **29** seconds\nHosted by {ctx.author}")
	an = discord.Embed(title=f"{amount} Heist Timer", description=f"**7** minutes, **59** seconds\nHosted by {ctx.author}")
	ao = discord.Embed(title=f"{amount} Heist Timer", description=f"**7** minutes, **29** seconds\nHosted by {ctx.author}")
	ap = discord.Embed(title=f"{amount} Heist Timer", description=f"**6** minutes, **59** seconds\nHosted by {ctx.author}")
	aq = discord.Embed(title=f"{amount} Heist Timer", description=f"**6** minutes, **29** seconds\nHosted by {ctx.author}")
	ar = discord.Embed(title=f"{amount} Heist Timer", description=f"**5** minutes, **59** seconds\nHosted by {ctx.author}")
	ass = discord.Embed(title=f"{amount} Heist Timer", description=f"**5** minutes, **29** seconds\nHosted by {ctx.author}")
	at = discord.Embed(title=f"{amount} Heist Timer", description=f"**4** minutes, **59** seconds\nHosted by {ctx.author}")
	au = discord.Embed(title=f"{amount} Heist Timer", description=f"**4** minutes, **29** seconds\nHosted by {ctx.author}")
	av = discord.Embed(title=f"{amount} Heist Timer", description=f"**3** minutes, **59** seconds\nHosted by {ctx.author}")
	aw = discord.Embed(title=f"{amount} Heist Timer", description=f"**3** minutes, **29** seconds\nHosted by {ctx.author}")
	ax = discord.Embed(title=f"{amount} Heist Timer", description=f"**2** minutes, **59** seconds\nHosted by {ctx.author}")
	ay = discord.Embed(title=f"{amount} Heist Timer", description=f"**2** minutes, **29** seconds\nHosted by {ctx.author}")
	az = discord.Embed(title=f"{amount} Heist Timer", description=f"**1** minutes, **59** seconds\nHosted by {ctx.author}")
	ba = discord.Embed(title=f"{amount} Heist Timer", description=f"**1** minutes, **29** seconds\nHosted by {ctx.author}")
	bb = discord.Embed(title=f"{amount} Heist Timer", description=f"**0** minutes, **59** seconds\nHosted by {ctx.author}")
	bc = discord.Embed(title=f"{amount} Heist Timer", description=f"**0** minutes, **29** seconds\nHosted by {ctx.author}")
	bd = discord.Embed(title=f"{amount} Heist Timer", description=f"**Timer Complete**\nHeist Incoming\nHosted by {ctx.author}")

	msg = await ctx.send(embed=ex)
	await asyncio.sleep(30)
	await msg.edit(embed=em)
	await asyncio.sleep(30)
	await msg.edit(embed=emb)
	await asyncio.sleep(30)
	await msg.edit(embed=embe)
	await asyncio.sleep(30)
	await msg.edit(embed=embed)
	await asyncio.sleep(30)
	await msg.edit(embed=a)
	await asyncio.sleep(30)
	await msg.edit(embed=b)
	await asyncio.sleep(30)
	await msg.edit(embed=c)
	await asyncio.sleep(30)
	await msg.edit(embed=d)
	await asyncio.sleep(30)
	await msg.edit(embed=e)
	await asyncio.sleep(30)
	await msg.edit(embed=f)
	await asyncio.sleep(30)
	await msg.edit(embed=g)
	await asyncio.sleep(30)
	await msg.edit(embed=h)
	await asyncio.sleep(30)
	await msg.edit(embed=i)
	await asyncio.sleep(30)
	await msg.edit(embed=j)
	await asyncio.sleep(30)
	await msg.edit(embed=k)
	await asyncio.sleep(30)
	await msg.edit(embed=l)
	await asyncio.sleep(30)
	await msg.edit(embed=m)
	await asyncio.sleep(30)
	await msg.edit(embed=n)
	await asyncio.sleep(30)
	await msg.edit(embed=o)
	await asyncio.sleep(30)
	await msg.edit(embed=p)
	await asyncio.sleep(30)
	await msg.edit(embed=q)
	await asyncio.sleep(30)
	await msg.edit(embed=r)
	await asyncio.sleep(30)
	await msg.edit(embed=s)
	await asyncio.sleep(30)
	await msg.edit(embed=t)
	await asyncio.sleep(30)
	await msg.edit(embed=u)
	await asyncio.sleep(30)
	await msg.edit(embed=v)
	await asyncio.sleep(30)
	await msg.edit(embed=w)
	await asyncio.sleep(30)
	await msg.edit(embed=x)
	await asyncio.sleep(30)
	await msg.edit(embed=y)
	await asyncio.sleep(30)
	await msg.edit(embed=z)
	await asyncio.sleep(30)
	await msg.edit(embed=aa)
	await asyncio.sleep(30)
	await msg.edit(embed=ab)
	await asyncio.sleep(30)
	await msg.edit(embed=ac)
	await asyncio.sleep(30)
	await msg.edit(embed=ad)
	await asyncio.sleep(30)
	await msg.edit(embed=ae)
	await asyncio.sleep(30)
	await msg.edit(embed=af)
	await asyncio.sleep(30)
	await msg.edit(embed=ag)
	await asyncio.sleep(30)
	await msg.edit(embed=ah)
	await asyncio.sleep(30)
	await msg.edit(embed=ai)
	await asyncio.sleep(30)
	await msg.edit(embed=aj)
	await asyncio.sleep(30)
	await msg.edit(embed=ak)
	await asyncio.sleep(30)
	await msg.edit(embed=al)
	await asyncio.sleep(30)
	await msg.edit(embed=am)
	await asyncio.sleep(30)
	await msg.edit(embed=an)
	await asyncio.sleep(30)
	await msg.edit(embed=ao)
	await asyncio.sleep(30)
	await msg.edit(embed=ap)
	await asyncio.sleep(30)
	await msg.edit(embed=aq)
	await asyncio.sleep(30)
	await msg.edit(embed=ar)
	await asyncio.sleep(30)
	await msg.edit(embed=ass)
	await asyncio.sleep(30)
	await msg.edit(embed=at)
	await asyncio.sleep(30)
	await msg.edit(embed=au)
	await asyncio.sleep(30)
	await msg.edit(embed=av)
	await asyncio.sleep(30)
	await msg.edit(embed=aw)
	await asyncio.sleep(30)
	await msg.edit(embed=ax)
	await asyncio.sleep(30)
	await msg.edit(embed=ay)
	await asyncio.sleep(30)
	await msg.edit(embed=az)
	await asyncio.sleep(30)
	await msg.edit(embed=ba)
	await asyncio.sleep(30)
	await msg.edit(embed=bb)
	await asyncio.sleep(30)
	await msg.edit(embed=bc)
	await asyncio.sleep(30)
	await msg.edit(embed=bd)
	await ctx.send("Timer is Done!")

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.authory
    earnings = random.randrange(100000)


    wallet_amt = users[str(user.id)]["wallet"]

    await ctx.send(f"You know Im pretty poor but Ill give u ⏣ {earnings}")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.command()
@commands.cooldown(1, 8, commands.BucketType.user)
async def bet(ctx,amount=None):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    wallet_amt = users[str(user.id)]["wallet"]

    if amount == None:
        await ctx.send("Please enter the amount")
        return

    x = amount
    y = int(x)
    z = wallet_amt
    h = int(z)

    if y > 500000:
    	await ctx.send("You can't bet more than 500k")
    if h > 10000000:
    	await ctx.send("You are to rich to Gamble")
    else:
        user = ctx.author
        bal = await update_bank(ctx.author)
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
    
        amount = int(amount)

        if amount > bal[0]:
            await ctx.send('You do not have sufficient balance')
            return
        if amount < 0:
            await ctx.send('Amount must be positive!')
            return

        user_amt = random.randrange(13)
        bot_amt = random.randrange(13)
        win_amt = 2.5*amount
        winning_amt = random.randrange(win_amt)

        if bot_amt > user_amt:
            await update_bank(ctx.author,-1*amount)
            balance = wallet_amt - amount
            em = discord.Embed(title=f"{ctx.author.name}'s losing gambling game", description=f"You lost **⏣ {amount}**\n\n**New Balance**: ⏣ {balance}",color = discord.Color(0xE53935))
            em.add_field(name=f"{ctx.author.name}", value=f"\nRolled `{user_amt}`", inline=True)
            em.add_field(name=f"Aniko", value=f"\nRolled `{bot_amt}`", inline=True)
            await ctx.send(embed=em)
        else:
            await update_bank(ctx.author,winning_amt)
            balance = wallet_amt + winning_amt
            emb = discord.Embed(title=f"{ctx.author.name}'s winning gambling game", description=f"You won **⏣ {(winning_amt)}**\n\n**New Balance**: ⏣ {balance}", color = discord.Color(0x4CAF50))
            emb.add_field(name=f"{ctx.author.name}", value=f"\nRolled `{user_amt}`", inline=True)
            emb.add_field(name=f"Aniko", value=f"\nRolled `{bot_amt}`", inline=True)
            await ctx.send(embed=emb)

@client.command(aliases=['tc'])
async def taxcalc(ctx,amount=None):
    if amount is None:
        ctx.send("You need to put a number")
    x = amount
    if amount.endswith('e1'):
        z = float(amount)
        x = int(z)
        y = x*10
    if amount.endswith('e2'):
        z = float(amount)
        x = int(z)
        y = x*100
    if amount.endswith('e3'):
        z = float(amount)
        x = int(z)
        y = x*1000
    if amount.endswith('e4'):
        z = float(amount)
        x = int(z)
        y = x*10000
    if amount.endswith('e5'):
        z = float(amount)
        x = int(z)
        y = x*100000
    if amount.endswith('e6'):
        z = float(amount)
        x = int(z)
        y = x*1000000
    if amount.endswith('e7'):
        z = float(amount)
        x = int(z)
        y = x*10000000
    if amount.endswith('e8'):
        z = float(amount)
        x = int(z)
        y = x*100000000

    y = int(x)
    commas = "{:,}".format(y)
    total = y*1.086956522
    usergets = y*.08
    userget = y-usergets

    embed = discord.Embed(description=f"**User gets: `⏣ {round(userget)}`**\n**Lost to tax: `⏣ {round(usergets)}`**\n\n*To send someone `⏣ {amount}` after tax you need to pay **`⏣ {round(total)}`***")
    embed.set_footer(text="TAX RATE: 8%")
    await ctx.send(embed=embed)            


esnipe_message_content = None
snipe_message_author = None
snipe_message_id = None
snipe_message_channel = None
afteredit_message_content = None 


@client.event
async def on_message_edit(message , message2):  
    global snipe_message_channel
    global esnipe_message_content
    global snipe_message_author
    global snipe_message_id
    global afteredit_message_content

    snipe_message_channel = message.channel
    esnipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_id = message.id
    afteredit_message_content = message2.content   
    await asyncio.sleep(1800)

    if message.id == snipe_message_id:
        snipe_message_author = None
        esnipe_message_content = None
        snipe_message_id = None
        afteredit_message_content = None 

    await client.process_commands(message)


@client.command()
async def esnipe(message, message2=None): 
    if esnipe_message_content == None:
        await message.channel.send("There is nothing to snipe.")

    else:
        if snipe_message_channel != message.channel:
            await message.channel.send("There is nothing to snipe.")
        else:
            embed = discord.Embed(
                description=f"``Before:``  {esnipe_message_content} \n``After:`` {afteredit_message_content}", 
                colour=message.author.colour)
            embed.set_footer(
                text=f"Asked by {message.author.name}",
                icon_url=message.author.avatar_url)
            embed.set_author(name=f"Edited by {snipe_message_author}")
            await message.channel.send(embed=embed)


@client.event
async def on_ready():
    for guild in client.guilds:
        async with aiofiles.open(f"Warns_{guild.name}.txt", mode="a") as temp:
            pass
        
        client.warnings[guild.id] = {}

    for guild in client.guilds:
        async with aiofiles.open(f"Warns_{guild.name}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    
    print(client.user.name + " is ready.")

@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
        
    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"Warns_{ctx.guild.name}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"**Warned** {member.name}")
    await member.send(f"You have been warned in {ctx.guild.name} by {ctx.author} for: {reason}")

@client.command(aliases=['warns'])
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour(0xffff00))
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning #{i}** given by: {admin.name} for: {reason}\n\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")


        


@help.command()
async def kick(ctx):

    em = discord.Embed(Title = "KICK", description = "kicks a member from the guild", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "d?kick <member> [reason]")

    await ctx.send(embed = em)

@help.command()
async def Ban(ctx):

    em = discord.Embed(Title = "BAN", description = "Bans a member from the guild", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "d?ban <member> [reason]")

    await ctx.send(embed = em)

@help.command()
async def whois(ctx):

    em = discord.Embed(Title = "WHOIS", description = "Gives information about the mentioned User", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "d?whois <member>")

    await ctx.send(embed = em)

@help.command()
async def dog_fact(ctx):

    em = discord.Embed(Title = "DOG FACT", description = "Gives random facts about dogs", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "d?dog_fact")

    await ctx.send(embed = em)

@help.command()
async def cat_fact(ctx):

    em = discord.Embed(Title = "CAT FACT", description = "Gives random facts about cats", color = ctx.author.color)
    em.add_field(name = "**Syntax", value = "d?cat_fact")

    await ctx.send(embed = em)  

@help.command()
async def purge(ctx):

    em = discord.Embed(Title = "PURGE", description = "Deletes the amount of messages you input", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "d?purge <amount>")

    await ctx.send(embed = em)   


@help.command()
async def snipe(ctx):

    em = discord.Embed(Title = "SNIPE", description = "Retrieves a deleted message in the channel where the command was invoked ", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "```xml\n< use d?snipe >```")

    await ctx.send(embed = em)

@help.command()
async def mod(ctx):

    em = discord.Embed(Title = "Moderation", description = "Here's a list of commands", colour=discord.Color.from_rgb(244, 182, 89))
    em.add_field(name = "**Ban**", value = "Bans a member fom the guild```xml\n< ?ban <user> [reason] >```")
    em.add_field(name  = "**Unban**", value = "Unbans a member```\n< d?unban [member id] >``` ")
    em.add_field(name  = "**Kick**", value = "Kicks a member from the guild```\n< d?kick [member(id)] >``` ")
    em.add_field(name  = "**Mute**", value = "Mutes the member mentioned```\n< d?mute [member] [time] [reason] >``` ")
    em.add_field(name  = "**Purge**", value = "Deletes the amount of messages given```\n< d?purge [amount] >``` ")
    em.add_field(name  = "**Role**", value = "Gives the mentioned role to the user mentioned or removes it```\n< d?role [member(id)] >``` ")
    em.add_field(name  = "**Warn**", value = "Warns the mentioned user```xml\n< d?warn [member(id)] [reason] >``` ")
    em.add_field(name  = "**Warns**", value = "Shows the mentioned user warns in the guild```\n< d?warns [member(id)] >``` ")
    em.add_field(name  = "**Drop**", value = "Pings giveaway role max time is 30 minutes```\n< d?drop [name(time)] >``` ")

@help.command()
async def info(ctx):

    em = discord.Embed(Title = "Info", description = "Here's a few commands", colour=discord.Color.from_rgb(244, 182, 89))
    em.add_field(name = "**Serverinfo**", value = "Shows the info on the server incluiding channels and roles```xml\n< ?serverinfo >```")
    em.add_field(name  = "**Whois**", value = "Shows all the info on the user mentioned```\n< d?whois [user] >``` ")
    em.add_field(name  = "**Avatar**", value = "Displays the members avatar```\n< d?avatar [user] >``` ")
    em.add_field(name  = "**Ping**", value = "Displays the bots latency```\n< d?Ping >``` ")
    em.add_field(name  = "**Roleinfo**", value = "Displays the info of the mentioned role```\n< d?role info [role(ID)] >``` ")
    em.add_field(name  = "**Invite**", value = "Gets the bot invite link```\n< d?invite >``` ")

@help.command()
async def fun(ctx):



#avatar whois serverinfo ping invite roleinfo
    await ctx.send(embed = em)

@client.command()
async def timer(self, ctx, timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        if time >= 3600:
            message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
        elif time >= 60:
            message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
        elif time < 60:
            message = await ctx.send(f"Timer: {time} seconds")
        while True:
            try:
                await asyncio.sleep(5)
                time -= 5
                if time >= 3600:
                    await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                elif time >= 60:
                    await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
                elif time < 60:
                    await message.edit(content=f"Timer: {time} seconds")
                if time <= 0:
                    await message.edit(content="Ended!")
                    await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
                    break
            except:
                break
    except:
        await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def ping(ctx):

	msg = await ctx.send(f"Latency is ")
	await msg.edit(content=f"Latency is ```{round(client.latency * 1000)}ms```")





client.run("BOT TOKEN HERE")

