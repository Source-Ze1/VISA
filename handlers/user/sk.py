
# from aiogram import *

# import random_address

# import requests
# from main import dp
# from main import PREFIX

# from handlers.user.newf import cc_gen
# import re
# @dp.message_handler(commands=['sk'], commands_prefix=PREFIX)
# async def sh1(message: types.Message):
#   await message.delete()
#   await message.answer_chat_action("typing")

#   user = message.text[len('/sk '):]

#   fg = user[0:10]
#   kg = user[-6:]

#   password = ""

#   try:
#     url1 = 'https://api.stripe.com/v1/balance'

#     re = requests.get(url1, auth=(user, password))
#     res = re.text
#     jee = re.json()
#     blnc = jee["pending"]
#     for blc in blnc:
#       amt = blc["amount"]
#       curr = blc["currency"]
#     if "true" in res:

#       await message.answer(f""" 
# ✅ <b> LIVE KEY </b>: <code>{user}</code>

# 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: Succeeded ✅ 
# 𝗕𝗮𝗹𝗮𝗻𝗰𝗲: {amt}
# 𝗖𝘂𝗿𝗿𝗲𝗻𝗰𝘆: {curr}
# <b>Checked by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
# <b>Bot by </b> -» <a href="tg://user?id=6509622797"><b>HOLY CARDERS</b></a>
#           """)

#     else:

#       await message.answer(f"""
#   Status: DEAD KEY🚫 
#   Sk key:{user}
#   Reason: dead key
#           """)

#   except:
#     await message.answer(f"""
#   Status: DEAD KEY🚫 
#   Sk key: {user}
#   Reason: dead key
#           """)




# @dp.message_handler(commands=['gen'], commands_prefix=PREFIX)
# async def igfgnfokc(message: types.Message):

#   m = await message.answer("generating......")

#   cards = ''
#   text = message.text[len('/gen '):]
#   cc = text


#   input = re.findall(r"[0-9]+", text)

#   if len(input) == 1:
#     cc = input[0]
#     mes = 'x'
#     ano = 'x'
#     cvv = 'x'


#   if len(input) == 2:
#     cc = input[0]
#     mes = input[1]
#     ano = 'x'
#     cvv = 'x'
#   if len(input) == 3:
#     cc = input[0]
#     mes = input[1]
#     ano = input[2]
#     cvv = 'x'
#   if len(input) == 4:
#     cc = input[0]
#     mes = input[1]
#     ano = input[2]
#     cvv = input[3]
#   else:

#     ccs = cc_gen(cc, mes, ano, cvv)
#     cards = '\n'.join(ccs)

#   BIN = str(cc[:6])


#   mess = f"""
# <b>Card Generated </b>
# Bin⇢ <b>{BIN}</b> ✅

# {cards}
# <b>generated by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
# Bot by -» <a href="tg://user?id=6509622797">HOLY CARDERS</a>
# """

#   await m.edit_text(mess)




# @dp.message_handler(commands=['fake'], commands_prefix=PREFIX)
# async def igfgnfokc(message: types.Message):
#   import requests
#   import random,string

#   URL = "https://random-data-api.com/api/users/random_user"

#   response = requests.get(url = URL)

#   data = response.json()

#   N = 8
#   ph = ''.join(random.choices(string.digits, k=N))
#   phone = "98" + ph
#   name1 = data["first_name"]
#   name2 = data["last_name"]
#   email = data["email"]
#   dob = data["date_of_birth"]
#   zip = data["address"]["zip_code"]
#   add1 = data["address"]["street_address"]
#   city = data["address"]["city"]
#   state = data["address"]["state"]
#   co = data["address"]["country"]

#   inf = f"""
# data generated :)
# <b>
# Name  = <code> {name1} {name2} </code>
# Email = <code>{email}</code>
# phone = <code>{phone}</code>
# street = <code>{add1}  </code> 
# city = <code>{city}</code>
# state = <code>{state}</code>
# country = <code>{co}</code>
# zip code = <code>{zip}</code>
# DOB = <code>{dob}</code>

# <b>generated by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
# </b>
#   """


#   return await message.reply(inf)


from aiogram import *
import requests,random,sys,string
from loader import dp
from main import PREFIX
import os
import argparse
from aiogram.types import Message
import requests, string, random, argparse, sys






@dp.message_handler(commands=['sk'], commands_prefix=PREFIX)
async def sh1(message: types.Message):
  await message.delete()
  await message.answer_chat_action("typing")
  user = message.text[len('/sk '):]
  data = 'card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2022&card[cvc]=354'
  first = requests.post('https://api.stripe.com/v1/tokens', data = data, auth = (user, ' '))
  status = first.status_code
  if status == 200:
      r_text = 'VALID API KEY ✅'
  else:
      if 'error' in first.json():
          if 'code' in first.json()['error']:
              r_res = first.json()['error']['code'].replace('_',' ').strip()
          else:
              r_res = 'INVALID API KEY'
      else:
          r_res = 'INVALID API KEY'
          
      r_text = '❌'+ r_res
  await message.answer(f""" 
{r_text} - <code>{user}</code>

<b>Checked by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by </b> -» <a href="tg://user?id=6509622797"><b>srfxdz</b></a>
          """)

    



def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate(proxies):
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick+"@"+"gmail"+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload,proxies=proxies)
    print(r.json())

    if r.status_code==200:
        if r.json()['status']==1:
          text = f"""
Auto Spotify Created! ✅
[+] isPremium-»  False
[+] Email-» <b>{email}</b>
[+] Password-»<code>{passw}</code>"""
          
          return (text)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))








@dp.message_handler(commands=['spotify'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
  proxies = {
  "http": "http://gate.proxiware.com:2000",
  "https": "http://gate.proxiware.com:2000"
}


  return await message.reply(generate(proxies))


# --------------------------------------------------------promote---------------------------------------------------------------------------------
