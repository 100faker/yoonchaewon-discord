import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Streaming(name="설윤이 직캠", url='https://www.youtube.com/watch?v=LTyc7mwLNys'))
  #await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content == "설윤아 안녕":
    await message.channel.send(message.author.nick + "님 저는 당신이 안 반가워요! :pinching_hand: :pinching_hand: :pinching_hand:")

  if message.content == "설윤아 자기소개 해봐":
    await message.channel.send("싫어요 :pinching_hand: :pinching_hand: :pinching_hand:")

  if message.content == "설윤 직캠":
    await message.channel.send("https://www.youtube.com/watch?v=Da4vIWM3H0Y")

  if message.content == "설윤아 사랑해":
    await message.channel.send("저두요 :heart:")

  if message.content == "설윤아 사랑한다":
    await message.channel.send("저도 사랑합니다 :heart:")

  print("윤채원:",client.user.name,"954369596956217395:",client.user.id,"01:",discord.__version__)

client.run(os.environ['token'])