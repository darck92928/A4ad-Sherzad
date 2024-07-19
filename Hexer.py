import requests
import telebot



bot = telebot.TeleBot('6552995612:AAGpPJPmKHJBKeSbzNJPxjxM3-8HDXa_rec')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'سلاو بەخیر هاتی بۆ بۆت مارکیت بۆ زانیاری دەربارەی بۆت ئەمە داگرە /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"""
دەربارەی بۆت بۆ هەر یارمەتیکی لیرەدا هەیە

-----------------------------------------
/coin
-------------
بۆ کین وەرگرتن کۆین داگرە
-----------------------------------------
/sendlink
-------------
بۆ یارمەتی دانیکت سیند لینک داگرە بۆ کەسیک یان لە چەنال یان هەر شتیکی تر بیت تۆ وەک پشت گریک یارمەتی منت داوە ❤️
-----------------------------------------
/profile
-------------
بۆ سەیرکردینی زانیاری ئەکاونتی تیلیگرامت لەلایەن ئەم بۆتە بزانە بە داگرتنی پرۆفایلی
------------------------------------------

""")

@bot.message_handler(commands=['coin'])
def coin(message):
    id = message.chat.id
    coin = 1
    coin = str(coin)
    bot.send_message(message.chat.id, f"""
    کۆینی ئەمرۆت وەرگرت
    
💰 coin : {coin}

------------------------------
   تکایە کە کۆینی ئەمرۆت وەرگرت هتا بەیانی بوەستا چونکەم توانی کۆینەکە بوستینم بەس رۆژانە بۆتان زیادی دەکەم 
دەبیت بوەستی هتا 
⏱️ hour : 24
    """)
@bot.message_handler(commands=['profile'])
def profile(message):
    id = message.chat.id
    name = message.chat.first_name
    user = message.chat.username
    coin = 1
    bot.send_message(message.chat.id, f"""

پرۆفایلی خۆت 
----------------------------------


📇 name : {name}
----------------
👤 username : @{user}
----------------
🆔 id : {id}
----------------
💰 coin : {coin}
----------------

💻 create bot by @B52_Plan_B
    
    """)

@bot.message_handler(commands=['sendlink'])
def send(message):
    id = message.chat.id
    coin = 1
    bot.send_message(message.chat.id, f"""
    کۆینی ئەمرۆت وەرگرت
بانگیشت کردنی خەلکی تر وەک پشت گیریک بۆ من 

------------------------------------------

link bot : https://t.me/Kasnem_Bot?start={id}
    
    """)


bot.polling()