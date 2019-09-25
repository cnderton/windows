#Imports

import telebot
import wikipedia
import pyowm
import pyjokes
import random
from time import sleep
from emailverifier import Client
from emailverifier import exceptions
from urllib.request import urlopen as url_open
import json
#Token
token = '939354885:AAHPdTAK8PdTlx0ICYC6HZ6Hvca_TgPYz_Q'
bot = telebot.TeleBot(token=token)
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'
client = Client('at_Gzzvwmp3zBAnbVjRYpO7P2MdXpE3b')
url = 'https://api.nasa.gov/planetary/apod?' # I don't get how url queries work, someone help
API_KEY = 'api_key=dWpZtxYFFudFeJi4KnQmoDXZz6y8rf7pPus6yoqu' #own API key, please register for your own at NASA Open APIs

def find_at(msg):
      for text in msg:
          if '@' in text:
              return text

#a = wikipedia.page(message.text) 

#AI
greetings = ["Hello😃", "Hey there 😃"]
how_are_you = ["I'm feeling positively tip top thanks.😎", "Feeling like a lean,mean,asisting ,machine!✌", "pretty good ツ",  "I'm doing very well,thank you." , "Not bad ツ"]
wcyd = ["---Here are some stuff I can do -- \n /about - 𝕄𝕠𝕣𝕖 𝕒𝕓𝕠𝕦𝕥 𝕦𝕤.\n--------------------------------------------------------\n/weather - 𝕃𝕖𝕥𝕤 𝕪𝕠𝕦 𝕜𝕟𝕠𝕨 𝕥𝕙𝕖 𝕔𝕦𝕣𝕣𝕖𝕟𝕥 𝕥𝕖𝕞𝕡𝕖𝕣𝕒𝕥𝕦𝕣𝕖 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕔𝕚𝕥𝕪.\n--------------------------------------------------------\n/review - 𝕊𝕙𝕒𝕣𝕖 𝕪𝕠𝕦𝕣 𝕟𝕖𝕨 𝕚𝕕𝕖𝕒𝕤 𝕒𝕟𝕕 𝕣𝕖𝕧𝕚𝕖𝕨𝕤 𝕨𝕚𝕥𝕙 𝕞𝕖.\n--------------------------------------------------------\n /insta - 𝕊𝕙𝕒𝕣𝕖 𝕪𝕠𝕦𝕣 𝕟𝕖𝕨 𝕚𝕕𝕖𝕒𝕤 𝕒𝕟𝕕 𝕣𝕖𝕧𝕚𝕖𝕨𝕤 𝕨𝕚𝕥𝕙 𝕞𝕖.\n--------------------------------------------------------\n /wikipedia - 𝔾𝕖𝕥 𝕟𝕖𝕖𝕕𝕖𝕕 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟 𝕗𝕣𝕠𝕞 𝕎𝕚𝕜𝕚𝕡𝕖𝕕𝕚𝕒 𝕨𝕚𝕥𝕙𝕠𝕦𝕥 𝕝𝕖𝕒𝕧𝕚𝕟𝕘 𝕥𝕖𝕝𝕖𝕘𝕣𝕒𝕞.\n--------------------------------------------------------\n/contact - ℂ𝕠𝕟𝕥𝕒𝕔𝕥 𝕨𝕚𝕥𝕙 𝕦𝕤.\n--------------------------------------------------------\n/talk - 𝕋𝕒𝕝𝕜 𝕨𝕚𝕥𝕙 𝔸𝕧𝕣𝕖𝕒𝕟\n--------------------------------------------------------\n /astro - 𝔾𝕖𝕥 𝕤𝕠𝕞𝕖 𝕚𝕟𝕥𝕖𝕣𝕖𝕤𝕥𝕚𝕟𝕘 𝕚𝕟𝕗𝕠 𝕒𝕓𝕠𝕦𝕥 𝕒𝕤𝕥𝕣𝕠𝕟𝕠𝕞𝕪.\n--------------------------------------------------------\n/jokes - 𝕊𝕠𝕞𝕖 𝕗𝕦𝕟𝕟𝕪 𝕛𝕠𝕜𝕖𝕤:)\n--------------------------------------------------------\n"]
pleasure = ["My pleasure!" , "That's what I'm here for😃" , "Always a pleasure 😃" , "You're welcome 😃" , "That makes me so happy! You're most welcome ☺" , "You're certainly welcome indeed.😊"]
beauty = ["Oh wow. You can't tell but I'm totally blushing right now.😘" , 'Thanks! I try just be my regular helpful self 😎' , " Stop it,you'll make me blush😘" , 'Oh wow. If I could blush I definitely would 😜']
love = ['I got another one... ;)']
astronomy = ['If you want to get some exciting astrnomical facts just click this >>> /astro <<<']
lv2 = ['He is my love ♥' , 'He is my founder.']
emoji = ["😂",'🤣','😅','😆']
dont_get_it = ["I don't understand you 😔" , "I'm afraid I don't understand." , "Sorry,I don't understand." , "I don't understand."]
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.reply_to(message, "-- Hello dear user -- \n I'm currently working on this bot. It already can do some basic things. \n If you want to know what this bot can do and commands to turn it on. JUST USE /commands command.")


@bot.message_handler(commands=['commands'])
def handle_start(message):
    bot.reply_to(
        message, "🅐🅥🅡🅔🅐🅝  🅕🅔🅐🅤🅣🅤🅡🅔🅢\n/about - 𝕄𝕠𝕣𝕖 𝕒𝕓𝕠𝕦𝕥 𝕦𝕤.\n--------------------------------------------------------\n/weather - 𝕃𝕖𝕥𝕤 𝕪𝕠𝕦 𝕜𝕟𝕠𝕨 𝕥𝕙𝕖 𝕔𝕦𝕣𝕣𝕖𝕟𝕥 𝕥𝕖𝕞𝕡𝕖𝕣𝕒𝕥𝕦𝕣𝕖 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕔𝕚𝕥𝕪.\n--------------------------------------------------------\n/review - 𝕊𝕙𝕒𝕣𝕖 𝕪𝕠𝕦𝕣 𝕟𝕖𝕨 𝕚𝕕𝕖𝕒𝕤 𝕒𝕟𝕕 𝕣𝕖𝕧𝕚𝕖𝕨𝕤 𝕨𝕚𝕥𝕙 𝕞𝕖.\n--------------------------------------------------------\n /insta - 𝕊𝕙𝕒𝕣𝕖 𝕪𝕠𝕦𝕣 𝕟𝕖𝕨 𝕚𝕕𝕖𝕒𝕤 𝕒𝕟𝕕 𝕣𝕖𝕧𝕚𝕖𝕨𝕤 𝕨𝕚𝕥𝕙 𝕞𝕖.\n--------------------------------------------------------\n /wikipedia - 𝔾𝕖𝕥 𝕟𝕖𝕖𝕕𝕖𝕕 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟 𝕗𝕣𝕠𝕞 𝕎𝕚𝕜𝕚𝕡𝕖𝕕𝕚𝕒 𝕨𝕚𝕥𝕙𝕠𝕦𝕥 𝕝𝕖𝕒𝕧𝕚𝕟𝕘 𝕥𝕖𝕝𝕖𝕘𝕣𝕒𝕞.\n--------------------------------------------------------\n/contact - ℂ𝕠𝕟𝕥𝕒𝕔𝕥 𝕨𝕚𝕥𝕙 𝕦𝕤.\n--------------------------------------------------------\n/talk - 𝕋𝕒𝕝𝕜 𝕨𝕚𝕥𝕙 𝔸𝕧𝕣𝕖𝕒𝕟\n--------------------------------------------------------\n /astro - 𝔾𝕖𝕥 𝕤𝕠𝕞𝕖 𝕚𝕟𝕥𝕖𝕣𝕖𝕤𝕥𝕚𝕟𝕘 𝕚𝕟𝕗𝕠 𝕒𝕓𝕠𝕦𝕥 𝕒𝕤𝕥𝕣𝕠𝕟𝕠𝕞𝕪.\n--------------------------------------------------------\n /jokes - 𝕊𝕠𝕞𝕖 𝕗𝕦𝕟𝕟𝕪 𝕛𝕠𝕜𝕖𝕤:)\n--------------------------------------------------------\n")

@bot.message_handler(commands = ['jokes'])
def jokes(message):
    bot.reply_to(message , pyjokes.get_joke() + random.choice(emoji) )

@bot.message_handler(commands = ['astro'])
def first(message): 
        bot.reply_to(message , 'Processing...')
        sleep(5)
        decoded_string = url_open(url + API_KEY).read().decode('utf-8') #url_open().read() returns a string with b prepended, which needs to be decoded first with decode('utf-8') before it can be transformed into json format
        decoded_json = json.loads(decoded_string)
        for key in decoded_json: #iterate through the json dictionary
            value = decoded_json[key]
            bot.reply_to(message , '{}: {}'.format(key, value))


@bot.message_handler(commands=['about'])
def handle(message):
    bot.reply_to(message, " 'Avrean' is a new business project from Winderton which allows you to get instant answers to your questions.\nRight now, I'm constantly improving this bot. \n   /commands ")
       
@bot.message_handler(commands=['review'])
def error_soo(message):
    bot.reply_to(message, " If you have a new idea for this project, you can share it with me here.\nAlso you can share your experience about this project with me.\nI would love to know about your experience.\n Write your feedback here: @Wingine\n   /commands ")


@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "Type city name first.")
    bot.register_next_step_handler(city, weath)


def weath(message):
      try:
            owm = pyowm.OWM("f2e8fbf7c64ac203354e80290ae0fc51")
            city = message.text
            weather = owm.weather_at_place(city)
            w = weather.get_weather()
            desc = w.get_detailed_status()
            hum = w.get_humidity()
            wind = w.get_wind()["speed"]
            temperature = w.get_temperature("celsius")["temp"]
            bot.send_message(message.chat.id, "Current temperature in " + str(city) +  " is: " + str(temperature) + "°C  " + str(desc) + '\n Speed of wind: ' + str(wind) + ' km/h ' + '\n Humidity: ' + str(hum) + '%' + '/commands' )
      except Exception as e:
            bot.reply_to(message, 'oooops. We could not find the city :(\nTry again using  /weather  command')

@bot.message_handler(commands=['insta'])
def cool_messsage(message):
      bot.reply_to(message , " Type the username.And don't forget to add '@' before u type username. " )
      
@bot.message_handler(func = lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
      texts = message.text.split()
      at_text = find_at(texts)
      bot.reply_to(message, 'Here you go - ' 'https://instagram.com/{}'.format(at_text[1:] ,) )


@bot.message_handler(commands=['wikipedia'])
def wikiipedia(message):
    v = message.text
    bot.send_message(message.chat.id, "type your request. To get result you MUST add '.' before you type your request.")
    #bot.register_next_step_handler(v, a)
    sleep(15)
   
@bot.message_handler(func = lambda message: message.text and '.' in message.text)    
def echo_all(message):
    try:
        bot.reply_to(message , 'Processing...')
        bot.reply_to(message, wikipedia.summary(message.text) )
        a = wikipedia.page(message.text) 
        bot.reply_to(message ,a.url )
        sleep(1)
        bot.reply_to(message,'/commands')      
    except Exception:
        bot.reply_to(message , "Oops,we couldn't find any results :(")

@bot.message_handler(commands=['contact'])
def errorr_soo(message):
      bot.reply_to(message, "My phone number: +994 55 414 31 95\nMy e-mail: boredguy982@gmail.com\nMy telegram: @Wingine\n   /commands  ")

@bot.message_handler(commands=['talk'])
def talk_me(message):
    bot.reply_to(message , 'Talk to me 😁')   
@bot.message_handler(content_types = ['text'])
def talkk (message):    
    if message.text == "Hello" or message.text == "hi" or message.text == "hey" or message.text == 'hey there' or message.text == 'hello there' or message.text == 'hello':
        bot.send_message(message.chat.id, random.choice(greetings) + ' ' + message.chat.first_name)
    elif message.text == "how are you?"  or message.text == "how u doin'? " or message.text == 'How you doing?' or message.text == '?' or message.text == 'How are you doing?' or message.text == 'how are you doing?' or message.text == 'How are you?' or message.text == 'how are you' or message.text =='How are you':
        bot.send_message(message.chat.id, random.choice(how_are_you))
    elif message.text == 'What can you do?' or message.text == 'what can you do?' or message.text == 'What are your functions?' or message.text == 'what can u do' or message.text == 'what can you do':   
        bot.send_message(message.chat.id , random.choice(wcyd) )
    elif message.text == 'tell me the weather' or message.text == "What's the weather like today?" or message.text == "What's the weather like?"  or message.text == "what's the weather like ?" or message.text == 'whats the weather like?' or message.text == 'weather' or message.text == 'Tell me the weather' or message.text == 'weather' :
        bot.send_message(message.chat.id , " If you want to know the weather use the '/weather' command 🌥 ")    
    elif message.text == 'thank you' or message.text == 'Thanks' or message.text == 'Thank you':
        bot.send_message(message.chat.id , random.choice(pleasure))
    elif message.text == 'you are beautiful' or message.text == 'You are beautiful' or  message.text == "you are cute" or message.text == 'You are cute' or message.text == 'You are extremely lovely' or message.text == 'You are lovely' or message.text == 'Oh beauty':
        bot.send_message == (message.chat.id , random.choice(beauty))
    elif message.text == 'I love you'or message.text == 'love you' or message.text == 'i love you':
        bot.send_message(message.chat.id ,random.choice(love) )
    elif message.text == 'Where do you live?' or message.text == 'Where are you living?' or message.text == "Where are you from?" or message.text == "Where are you from" or message.text == "where are you from" or message.text == "where are you from?":
        bot.send_message(message.chat.id , "I live in cloud,but I like to think that home is where the questions are😊")     
    elif message.text == 'Facts about astronomy' or message.text == 'Interesting facts' or message.text == 'Astronomy facts' or message.text == 'Astronomy' or message.text == 'Information about astronomy' or message.text == 'Astronomicial facts' or message.text == "Give me some interesting astronomicial facts":
        bot.send_message(message.chat.id , random.choice(astronomy))
    elif message.text == 'Do you have a boyfriend?' or message.text == 'Do you have a girlfriend?' or message.text == 'Are you alone?' or message.text == 'Do you have boyfriend?' or message.text == 'Do you have girlfriend?':
        bot.send_message(message.chat.id , "The only thing Im really feeling a strong connection to the wi-fi!")    
    elif message.text == "Great" or message.text == 'Cool':
        bot.send_message(message.chat.id , 'Thanks')    
    elif message.text == "Who is ilham?" or message.text == "Who is Ilham?":
        bot.send_message(message.chat.id , 'He is founder of Avrean.')    
    elif message.text == "Who are you?" or message.text == "who are you?" or message.text == "Who are you" or message.text == "who are you" or message.text == "What's your name?" or message.text == "What's your name" or message.text == "what's your name?" or message.text == "what's your name":
        bot.send_message(message.chat.id , "I'm Avrean 😊")
    elif message.text == "Tell me a joke" or message.text == 'Tell me joke' or message.text == 'Funny jokes' or message.text == 'funny jokes' or message.text == "tell me a joke" or message.text == "Tell me some funny jokes" or message.text == "Jokes" or message.text == 'jokes' or message.text == "Make some funny jokes" or message.text == "Funny joke" or message.text == "Make a funny joke" or message.text == "Make a joke" or message.text == "joke" or message.text == "Joke":
        bot.send_message(message.chat.id , pyjokes.get_joke() + random.choice(emoji))
    elif message.text == "Who created you?" or message.text == "Who is your creator?" or message.text == "Who created you" or message.text == "Who is your creator" or message.text == "who created you" or message.text == "Who's your creator?" or message.text == "Who's created you?" or message.text == "Who's your creator?" or message.text == "Who's your creator" or message.text == "Who's your founder?" or message.text == "who's your founder?" or message.text == "who's your founder" or message.text == "Who is your founder?" or message.text == "Who is your founder":
        bot.send_message(message.chat.id , "My creator is Ilham. He's the god of this temple🔱")  
    else:
        bot.send_message(message.chat.id , random.choice(dont_get_it) )   
         

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    bot.send_sticker(message.chat.id, STICKER_ID)



def console_listener(messages):
    for message in messages:
        try:
            # Print the good stuff on the console
            print('[Sender ID: ' + str(message.chat.id) + '] Text: ' + message.text)
        except:
            # Ignore errors at printing the messages
            pass

bot.set_update_listener(console_listener)

bot.polling(timeout=15)
