from dis import dis
from turtle import update
from Comandos import Commands
from Data.Token import TokenDiscord
#from Data.Doc import DevDoc
import discord


commands = Commands()
tokenDiscord = TokenDiscord()
#devDoc = DevDoc()
badwors = open("DiscordBot/Data/Badwords.txt", 'r').read().lower().split('\n')

class MyClient(discord.Client):
    async def on_ready(self):
        print("I'm ready! I'm connected like {0}!".format(self.user))

    # recebe os eventos
    async def on_message(self, event):
        print('Message from {0.author}: {0.content}'.format(event))
        event.content = event.content.lower()
        if event.author.bot:
            return

        # algoritimo para apagar msg improprias
        for word in event.content.lower().split():
            if word in badwors:
                await event.channel.send(f"Por favor {event.author.name} não ofenda os demais usuários!")
                await event.delete()

        # recebe os comandos
        if event.content.startswith('/'):
            try:
                if event.content == "/rules":
                    await event.channel.send(commands.rules())
                elif event.content == "/help":
                    embed = discord.Embed(title="Comandos", description="Essas são as unicas ordens que eu obedeço, se quiser mais, faça você mesmo", color=0x00ff00)
                    embed.add_field(name="Ok", value="Vou lista os comandos para você",inline=False)
                    for key in commands.commands().keys():
                        if key != "erro":
                            embed.add_field(name=key, value=commands.commands()[key], inline=False)
                    await event.channel.send(embed = embed)
                elif event.content == "/devdoc":
                    embed = discord.Embed(title="Documentação", description="Agora você quer estudar né!!...Então vou lista as documentações das principais linguagens de programação", color=0x206694)

                    embed.add_field(name="Blz então", value="Aqui etá todas as documentações que eu conheço...Se você achar uma melhor || uma que não tenha no meu repositorio, avise meu criador",inline=False)
                    for doc in commands.devDoc().keys():
                        if doc != "erro":
                            embed.add_field(name=doc, value=commands.devDoc()[doc], inline=False)
                    await event.channel.send(embed = embed)
                else:
                    allcommands = {}
                    allcommands.update(commands.commands())
                    allcommands.update(commands.devDoc())
                    embed = discord.Embed()
                    embed.add_field(name=event.content[1::], value=allcommands[event.content])
                    await event.channel.send(embed=embed)
                await event.delete()
            except Exception as e:
                await event.channel.send("Meu criador aina não me programor direito :(")
                print(e)

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            welcome = f"{member.mention} acabou de entrar no {guild.name}"
            await guild.system_channel.send(welcome)


intents = discord.Intents.default()
intents.members = True

client = MyClient()
client.run(TokenDiscord.uploadToken()['token'])