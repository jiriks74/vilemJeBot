import discord
from decouple import config



client = discord.Client()


@client.event
async def on_ready():
  activity = discord.Game(name="!help",)
  print('ONLINE')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  name = message.author.name
  mess = message.content

  if message.content.startswith('!code'):

    await message.channel.send('''
```if random.person.here == True:
    Get.Out.Of(here, right_now_pls)
else:
    print("What's up, HACKERS?")
``` ''')
    print("Replied to", message.author.name, "to message",message.content)

  if message.content.startswith('!tutorial'):

    await message.channel.send("```print('hello world')```")
    print("Replied to", message.author.name, "to message",message.content)

  if message.content.startswith('!help'):

    await message.channel.send("```!code, !tutorial, !help, !wtf, !who, !zabuč, xd or ?...```")
    print("Replied to", message.author.name, "to message",message.content)

  if message.content.startswith('!wtf'):

    await message.channel.send('''```
if confused():
  go.away
```
''')
    print("Replied to", message.author.name, "to message",message.content)

  if message.content.startswith('!who'):

    await message.channel.send("Who? Vilém vole")
    print("Replied to", message.author.name, "to message",message.content)

  if message.content.startswith('!zabuč'):

    await message.channel.send("BOOOOOOOO")
    print("Replied to", message.author.name, "to message",message.content)

  if mess.endswith('xd') or message.content.startswith('xd'):

    await message.channel.send(":joy:")
    print("Replied to", message.author.name, "to message",message.content)
  
  if mess.endswith('?') or message.content.startswith('?'):
    await message.channel.send(":open_mouth:")
    print("Replied to", message.author.name, "to message",message.content)

  if name == "JustSuzi":
    await message.add_reaction()
    print("Replied to", message.author.name, "to message",message.content)

client.run(config('TOKEN'))
