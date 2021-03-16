# Credit To Azael#1111 For Help (https://github.com/azaelgg)
# Found By Jinxy#1800 & Azael#1111
import requests
import os

from colorama import Fore, init

init(convert=True)
clear = lambda: os.system('cls')

token = os.getenv('TOKEN')

headers = {'Authorization': token, 'Content-Type': 'application/json'}
res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
res = res.json()

user_id = res['id']
user = res['username']

def starter():
    clear()
    cc = f'''
         ▄████▄   ▄▄▄        ██████ ▓█████     ▄████▄   ██▓     ▒█████    ██████ ▓█████ ▓█████▄ 
        ▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓█   ▀    ▒██▀ ▀█  ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ ▒██▀ ██▌
        ▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒███      ▒▓█    ▄ ▒██░    ▒██░  ██▒░ ▓██▄   ▒███   ░██   █▌
        ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒▒▓█  ▄    ▒▓▓▄ ▄██▒▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ ░▓█▄   ▌
        ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒░▒████▒   ▒ ▓███▀ ░░██████▒░ ████▓▒░▒██████▒▒░▒████▒░▒████▓ 
        ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▒▓  ▒ 
          ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░     ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░ ▒  ▒ 
        ░          ░   ▒   ░  ░  ░     ░      ░          ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░    ░ ░  ░ 
        ░ ░            ░  ░      ░     ░  ░   ░ ░          ░  ░    ░ ░        ░     ░  ░   ░    
        ░                                     ░                                          ░                   
    '''.replace('▒', f'{Fore.BLUE}▒{Fore.RESET}').replace('░', f'{Fore.BLUE}░{Fore.RESET}').replace('▒', f'{Fore.BLUE}▒{Fore.RESET}')
    return cc

def disable():
    print(starter())
    print(f'[{Fore.GREEN}!{Fore.RESET}] {Fore.LIGHTBLACK_EX}Successfully Logged In: {user} ({user_id})!{Fore.RESET}')
    input(f"[{Fore.BLUE}!{Fore.RESET}] {Fore.LIGHTBLACK_EX}Press Enter To Start!{Fore.RESET}")
    for username in open('users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token, 'Content-Type': 'application/json'}, json={'username': usr[0], 'discriminator': usr[1]})
            print(f"[{Fore.GREEN}{r.status_code}{Fore.RESET}] {Fore.LIGHTBLACK_EX}{usr[0]}#{usr[1]} Added!{Fore.RESET}")
        except:
            print(f"[{Fore.RED}!{Fore.RESET}]{Fore.LIGHTBLACK_EX} Something Went Wrong!{Fore.RESET}")

disable()
