import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Streaming(name="설윤의 직캠", url='https://www.youtube.com/watch?v=LTyc7mwLNys'))
  #await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  

 @client.event
async def on_message(message):
"""
message.author : 메시지를 보낸 사람
message.guild : 메시지를 보낸 서버
message.channel : 메시지를 보낸 채널
"""

if message.author.bot: # 봇이 보낸 메시지이면 반응하지 않게 합니다
return

if message.content == "설윤아 안녕":
await message.channel.send(message.author.nick + "님 안녕하세요. 저는 NMIXX 설윤입니다!")

if message.content == "설윤아 자기소개 해봐":
await message.channel.send(message.author.nick + "님! 나무위키를 쳐 보세요 ^__^")

  print("윤채원:",client.user.name,"954369596956217395:",client.user.id,"01:",discord.__version__)


client.run(os.environ['token'])