# coding: utf-8

from slackbot.bot import default_reply
from datetime import datetime

@default_reply()
def default(message):
    message.reply("Hey")
    #print("[papaya bot][{datetime}] {user} saied".format(datetime=str(datetime.now()),user=message.user()))
    date = str(datetime.now())
    name = message.user["name"]
    body = message.body["text"]
    print("[slackbot][{date}][INFO][{name}]: {body}".format(date=date, name=name, body=body))
