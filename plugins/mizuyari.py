# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import default_reply
from threading import Thread
import time

class MizuyariThread(Thread):
    def __init__(self,message):
        self._message = message
        Thread.__init__(self)

    def run(self):
        time.sleep(10)
        self._message.send("水やり終了")


@respond_to('mizuyari')
def mizuyari(message):
    message.send("水やり開始")
    mizuyariThread = MizuyariThread(message)
    mizuyariThread.start()
