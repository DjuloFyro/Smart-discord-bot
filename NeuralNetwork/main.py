import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        

        #if message.content.startswith('!hello'):
        if "pen" in message.content:
            await message.channel.send("A pen ? A penalty ?\nDonde esta ?\nyo soy Pristiano Penaldo, el mejor jugador del mundo")
                #await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()
client.run("OTY0OTgwMzAwODU1NzkxNjU3.Ylsh8A.RI24aZ8KvBCe-N1uAa8w9djIh5w")