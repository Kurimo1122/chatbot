# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
#channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_secret = "59b4a1251985159c2402b4e4368181a7"
#channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_access_token = "auc88xgS/u82PgBMADBvkcv6GZQ77Ud471fhfV0L3Tos3IU6Ta2izgrDGsuMClCFtoC1WRsWoY9jnxFZJdc4c0kxjK1U/63nIlEN0+3mg3PuNXMLCLwkwGmDBivgg3wBbSApaHDWTHduWd9UE98D4gdB04t89/1O/w1cDnyilFU="
#channel_secret = os.environ['LINE_CHANNEL_SECRET']
#channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        """
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        """
        #app.logger.info("details.message: " + event.details[].message.text)
        print("hello world")
        sys.stdout.flush()

        print(event)
        sys.stdout.flush()

        print(event.reply_token)
        sys.stdout.flush()

        if isinstance(event, MessageEvent):    
            line_bot_api.reply_message(
                
                event.reply_token,
                #event.replyToken,
                #event[1],
                TextSendMessage(text=event.message.text)
                #TextSendMessage(text=event.details[].message.text)
                #TextSendMessage(text="aiueo")
            )

    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    #app.run(debug=options.debug, port=options.port)
    app.run(debug=True)