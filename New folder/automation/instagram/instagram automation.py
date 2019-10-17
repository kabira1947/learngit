from instabot import Bot
bot=Bot()

bot.login(username="",password="")
tags=['funny','likun','prabhu']
for i in tags:
    bot.like_hastag(i,amount=20)
bot.upload_photo("pic.jpg",caption="hello this is a bot #bot #hello" )
bot.follow_followers("i know python",nfollows=10)
