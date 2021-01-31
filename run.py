import instabot

bot = instabot.InstaBot('PATH_TO_CHROMEDRIVER.EXE', 'YOUR_USERNAME', 'YOUR_PASSWORD')
bot.open()
bot.login()
bot.search("YOUR_HASTAG_WITHOUT_HASH")
bot.like(YOUR_VALUE)