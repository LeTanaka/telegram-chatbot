#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Habilita os logs para gerenciar o bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define os comandos. Com os argumentos Update, CallbackContext
def start(update: Update, context: CallbackContext) -> None:
    """Envia menssagem ao comando /start."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Eaee {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Mensagem que responde ao comando /help."""
    update.message.reply_text('Que help oque, pesquise no google!')

def unesp(update: Update, context: CallbackContext) ->None:
    campus = context.args[0]
    if campus == "bauru":
        img = "unesp-bauru.jpeg"
        update.message.reply_text('O campus mais brabo de todos!')
    else:
        return update.message.reply_text("Nao conheco nenhum outro campus :D")
        
    path = "tmp/unesp-bauru.jpeg"
    update.message.reply_photo(photo=open(path, "rb"))


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Inicia o bot"""
    # Cria Updater e passa o token do bot
    arq = open("token.txt")
    TOKEN = arq.read()
    arq.close()
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Comandos do Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("unesp", unesp))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()