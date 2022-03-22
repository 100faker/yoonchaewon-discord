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
    await message.channel.send("https://namu.wiki/w/%EC%84%A4%EC%9C%A4 킹무위키를 참고해주세요 ^^")

  if message.content == "설윤 직캠":
    await message.channel.send("https://www.youtube.com/watch?v=Da4vIWM3H0Y")

  if message.content == "설윤아 사랑해":
    await message.channel.send("저두요 :heart:")

  if message.content == "설윤아 사랑한다":
    await message.channel.send("저도 사랑합니다 :heart:")

  if message.content == "설윤아 사귀자":
    await message.channel.send("고민이 좀 필요할 것 같아요~")

  if message.content == "설윤아 결혼하자":
    await message.channel.send("그건 검토를 좀 해봐야겠어요~ :raised_hand:")

  if message.content == "설윤아아":
    await message.channel.send("저는 아이스 아메리카노 좋아해요~")

  if message.content == "설윤 이행시":
    await message.channel.send("〈설〉 설윤은 〈윤〉 예쁘다")

  if message.content == "설윤아 너 좋아해":
    await message.channel.send("으악 :mask:")

  if message.content == "설윤아 광효가 너 좋아한데":
    await message.channel.send("아 씨X")

  if message.content == "설윤아 무슨 생각해":
    await message.channel.send("김광X씨가 제 생각한다는데 그게 너무 킹받아요")

  if message.content == "설윤아 뭐해":
    await message.channel.send(message.author.nick + "생각이요!")

  if message.content == "설윤아 나랑 게임할래":
    await message.channel.send("싫어요")

  if message.content == "설윤아 너는 나 어때":
    await message.channel.send("저는 당신을 단 한 번도 생각해본 적 없어요 :thinking:")

  if message.content == "설윤아 뭐하니":
    await message.channel.send("우리 팬 분들 생각하고 있어요~")

  if message.content == "승트 어때":
    await message.channel.send("제가 더 예뻐요 :smile:")

  if message.content == "야이":
    await message.channel.send("어쩔")

  if message.content == "설윤이 누구야":
    await message.channel.send("나다")

  if message.content == "설윤아 나랑 커피 한 잔 할래?":
    await message.channel.send("김광효 씨가 만든 커피는 마시기 싫어요")

  if message.content == "설윤아":
    await message.channel.send("네?")

  if message.content == "설윤이 신고":
    await message.channel.send("너무 예쁜 죄로 신고하겠다면.. 어쩔 수 없네요")

  if message.content == "설윤이 혼인신고":
    await message.channel.send("시X")

  if message.content == "설윤아 웃음이 나와?":
    await message.channel.send("네! :smiley: :smiley: :smiley: :smiley:")

  if message.content == "설윤아 몇살이야":
    await message.channel.send("저는 2004년 1월 26일생이고, 만 18세입니다 ^^")

  if message.content == "설윤아 광효 어때":
    await message.channel.send("진짜 진짜 진짜 싫어요!!! :pinching_hand: :pinching_hand: :pinching_hand:")

  if message.content == "자살":
    await message.channel.send("자살은 노노노! 제 직캠 보시고 힐링하세요 https://www.youtube.com/watch?v=0JEdfpvKm_4")

  print("윤채원:",client.user.name,"954369596956217395:",client.user.id,"01:",discord.__version__)

client.run(os.environ['token'])