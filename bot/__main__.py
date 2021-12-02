import logging
from bot import app
from utils import temp
from pyrogram.raw.all import layer
from pyrogram import idle, __version__

# Run Bot
if __name__ == "__main__":
    app.start()
    me = app.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    app.send_message(617426792, f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")
    logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")
    idle()
