#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6786324246:AAHFgRcLWUOpgVtsgvIg-JjJNU96d-CsmagU")
    API_ID = int(os.environ.get("API_ID", "16732227"))
    API_HASH = os.environ.get("API_HASH", "8b5594ad7ad37f3a0a7ddbfb3963bb51")
    AUTH_USERS = "1411895712"


