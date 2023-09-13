from bumble.bumble import BumbleBot

with BumbleBot() as bot:
    bot.land_first_page()
    bot.dismissCookies()
    bot.clickSignIn()
    bot.loginWithFB()

    while True:
        bot.like()