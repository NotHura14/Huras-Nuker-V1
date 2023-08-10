from websocket import WebSocket
from base64 import b64encode
import random
import string
import json
import websocket
import time
import requests

class Discord:
    def __init__(self, token):
        self.headers={
            'authorization': 'Bot {}'.format(
                token
            )
        }
        self.client=requests.Session()
        self.client.headers = self.headers
    def get_channels(self, guild_id):
        channels = [channel['id'] for channel in json.loads(self.client.get(
            f"https://discord.com/api/v9/guilds/{guild_id}/channels"
            ).text)]
        return channels
    def get_roles(self, guild_id):
            roles = [role['id'] for role in json.loads(self.client.get(
                f"https://discord.com/api/v9/guilds/{guild_id}/roles").text)]
            return roles
    def create_channel(self, name, guild_id):
        try:
            self.client.post(
                f"https://discord.com/api/v9/guilds/{guild_id}/channels", json={
                    "name": name, 
                    "permission_overwrites": [], 
                    "type": 0
                    })
        except:
            pass
    def delete_channels(self, channel_id):
        try:
            self.client.delete(
                f"https://discord.com/api/v9/channels/{channel_id}")
        except:
            pass
    def change_guild_name(self, new_name, guild_id):
        try:
            self.client.patch(f"https://discord.com/api/v9/guilds/{guild_id}", json={
                "name": new_name
            })
        except:
            pass
    def create_roles(self, guild_id, name):
        try:
            self.client.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", json={
                "name": name
            })
        except:
            pass
    def delete_role(self, guild_id, role_id):
        try:
            self.client.delete(
                f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}")
        except:
            pass
    def send_message(self, message, channel_id):
        try:
            self.client.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages", data={
                    "content": message
                })
        except:
            pass