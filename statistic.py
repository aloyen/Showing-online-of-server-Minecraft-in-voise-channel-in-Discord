import discord
import time
from mcstatus import MinecraftServer

global a

a = 1

client = discord.Client()

@client.event
async def on_ready():
 time_r = 30 #Задержка между проверками онлайна (в секундах). Меньше 10 лучше не 
 game = discord.Game("game-activity")
 await client.change_presence(status=discord.Status.idle, activity=game) #Вид активности
 print("Бот начал шалить на аккаунте {0.user}".format(client)) #Сообщение о запуске
 a = 0
 while True:
  server1 = MinecraftServer.lookup("ip:port")
  status = server1.status()
  channel = client.get_channel(id channel)
  await discord.VoiceChannel.edit(channel, name = "Людей на сервере: {0}".format(status.players.online))
  a = a+1
  print(f"Обновлено ", a, " раз")
  time.sleep(time_r)

client.run("tocken ds bot")
