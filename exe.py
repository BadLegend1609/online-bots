while True:
    try:
        from discord_bot import DiscordBot
        from time import sleep
        from credentials import discord_username, discord_password
        import sys

        loop_list = []
        db = DiscordBot(discord_username, discord_password)
        db.remake_channels()
        db.driver.close()
        sleep(2)
        sys.modules[__name__].__dict__.clear()
    except Exception:
        pass