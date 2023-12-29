import json
import time
from flask import jsonify
import websocket
from websocket._core import create_connection


class APICaller(object):

    def __init__(self, url):
        file = open("resources/api.json")
        data = json.load(file)
        self.token = data["token"]
        self.version = data["version"]
        self.url = url

    def get_guild(self, guildid,token):
        print(guildid)
        ws = create_connection(self.url)
        curly_open = "{"
        curly_close = "}"
        request = f'{curly_open}"req_id": 0,"platform": "android","guild_id": {guildid},"version": "{self.version}","token": "{self.token}","lang": "en","task": "logged/guild/getguild"{curly_close}'
        print(request)
        ws.send(request)
        time.sleep(2)
        returned = ws.recv()
        ws.close()
        return returned
