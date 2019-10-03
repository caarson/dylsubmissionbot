# -*- coding: utf-8 -*-
import time
import traceback
import discord.ext
from os import listdir
from lib import utility_func
from discord.ext import commands
from os.path import isfile, join


client = commands.Bot(command_prefix='dylbot ', description="description of bot...")
client.remove_command('help')

class Authenticate:
    def __init__(self):
        self.discord_key = utility_func.load_json('./config/tokens.json')

async def bot_extensions():
    for extension in [f.replace(".py", "") for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            if not "__init__" in extension:
                print("[++] loading extension: {}".format(extension))
                client.load_extension("cogs.%s" % (extension))
                print("loaded extension successfully")
        except Exception as e:
            print("[!!] failed to load extension {}".format(extension))
            traceback.print_exc()


def start_bot():
    try:
        client.run(Authenticate().discord_key['discord-code'])
    except BaseException:
        time.sleep(10)
        client.run(Authenticate().discord_key['discord-code'])

@client.event
async def on_ready():
    print('[+] Deploying bot...')
    backend = client.get_channel(620463856246063124)  # defines backend channel.
    await backend.send('DYLUMINATI has been deployed.')
    print('[~] %s | %s' % (client.user.name, client.user.id))

    # execute functions here VV
    await bot_extensions()
    await find_submit_channel()

########################################################

async def find_submit_channel():
    submit_channel = "submit"
    print(str(submit_channel))
    for channel in guild.get_all_channels()





start_bot()







