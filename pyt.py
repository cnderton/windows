#Imports
import telebot
import wikipedia
import pyowm
import random
from tmdbv3api import Movie, TMDb
from time import sleep
from telebot import types
from urllib.request import urlopen as url_open
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import translators as ts
from translate import Translator
from currency_converter import CurrencyConverter
#Token
token = '742874199:AAEd7j8rRFh3Ymmg_g1ccsgMMARQzj-cfcE'
bot = telebot.TeleBot(token=token)
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'
#client = Client('ylFpj3mg5MhcKlQGkSnqcnyU1NCQm88KicZVFLHV')
url = 'https://api.nasa.gov/planetary/apod?' # I don't get how url queries work, someone help
API_KEY = 'api_key=ylFpj3mg5MhcKlQGkSnqcnyU1NCQm88KicZVFLHV' #own API key, please register for your own at NASA Open APIs
tmdb = TMDb()
tmdb.api_key = 'ee01893e3d8f4d2026795ad38b8bb5fe'
tmdb.language = 'en'
movie = Movie()
#c = CurrencyConverter()

def find_at(msg):
      for text in msg:
          if '@' in text:
              return text

#a = wikipedia.page(message.text) 

#AI
greetings = ["Hello😃", "Hey there 😃"]
how_are_you = ["I'm feeling positively tip top thanks.😎", "Feeling like a lean,mean,asisting ,machine!✌", "pretty good ツ",  "I'm doing very well,thank you." , "Not bad ツ"]
wcyd = ["---Here are some stuff I can do -- \n ●/about - 𝑴𝒐𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 𝒖𝒔.\n--------------------------------------------------------\n●/weather - 𝑭𝒊𝒏𝒅 𝒐𝒖𝒕 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒕𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒖𝒓𝒆 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒓𝒆𝒈𝒊𝒐𝒏\n--------------------------------------------------------\n●/review - 𝑺𝒉𝒂𝒓𝒆 𝒚𝒐𝒖𝒓 𝒏𝒆𝒘 𝒊𝒅𝒆𝒂𝒔 𝒂𝒏𝒅 𝒓𝒆𝒗𝒊𝒆𝒘𝒔 𝒘𝒊𝒕𝒉 𝒎𝒆.\n--------------------------------------------------------\n●/wikipedia - 𝑮𝒆𝒕 𝒏𝒆𝒆𝒅𝒆𝒅 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒇𝒓𝒐𝒎 𝑾𝒊𝒌𝒊𝒑𝒆𝒅𝒊𝒂 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒍𝒆𝒂𝒗𝒊𝒏𝒈 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎.\n--------------------------------------------------------\n●/contact - 𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒘𝒊𝒕𝒉 𝒎𝒆\n--------------------------------------------------------\n●/talk - 𝑯𝒂𝒗𝒆 𝒂 𝒕𝒂𝒍𝒌 𝒘𝒊𝒕𝒉 𝑨𝒗𝒓𝒆𝒂𝒏.\n--------------------------------------------------------\n●/astro - 𝑰𝒏𝒕𝒆𝒓𝒆𝒔𝒕𝒊𝒏𝒈 𝒇𝒂𝒄𝒕𝒔 𝒂𝒃𝒐𝒖𝒕 𝒂𝒔𝒕𝒓𝒐𝒏𝒐𝒎𝒚.\n--------------------------------------------------------\n●/jokes - 𝑭𝒖𝒏𝒏𝒚 𝒋𝒐𝒌𝒆𝒔\n--------------------------------------------------------\n●/movie - 𝑮𝒆𝒕 𝒔𝒖𝒈𝒈𝒆𝒔𝒕𝒆𝒅 & 𝒑𝒐𝒑𝒖𝒍𝒂𝒓 𝒎𝒐𝒗𝒊𝒆𝒔 𝒏𝒂𝒎𝒆 𝒂𝒏𝒅 𝒐𝒗𝒆𝒓𝒗𝒊𝒆𝒘𝒔.\n--------------------------------------------------------\n●/translate - 𝑻𝒓𝒂𝒏𝒔𝒍𝒂𝒕𝒆 𝒘𝒐𝒓𝒅𝒔 & 𝒔𝒆𝒏𝒕𝒆𝒏𝒄𝒆𝒔 𝒇𝒓𝒐𝒎 𝑬𝒏𝒈𝒍𝒊𝒔𝒉 𝒕𝒐 𝒐𝒕𝒉𝒆𝒓 𝒍𝒂𝒏𝒈𝒖𝒂𝒈𝒆𝒔.\n--------------------------------------------------------\n●/currency - 𝑮𝒆𝒕 𝒇𝒓𝒆𝒆 𝒍𝒊𝒗𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒄𝒚 𝒓𝒂𝒕𝒆𝒔 𝒖𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒂𝒄𝒄𝒖𝒓𝒂𝒕𝒆 𝒅𝒂𝒕𝒂.\n--------------------------------------------------------"]
pleasure = ["My pleasure!" , "That's what I'm here for😃" , "Always a pleasure 😃" , "You're welcome 😃" , "That makes me so happy! You're most welcome ☺" , "You're certainly welcome indeed.😊"]
beauty = ["Oh wow. You can't tell but I'm totally blushing right now.😘" , 'Thanks! I try just be my regular helpful self 😎' , " Stop it,you'll make me blush😘" , 'Oh wow. If I could blush I definitely would 😜']
love = ['I got another one... ;)']
astronomy = ['If you want to get some exciting astrnomical facts just click this >>> /astro <<<']
lv2 = ['He is my love ♥' , 'He is my founder.']
emoji = ["😂",'🤣','😅','😆']
jokes = ["https://raw.githubusercontent.com/cnderton/windows/master/Screenshot_20200116-213702_Instagram%20(2).jpg" , "https://ruinmyweek.com/wp-content/uploads/2019/05/21-damn-funny-memes-everyone-should-see-this-morning-16.jpg" , "https://preview.redd.it/53o0u089qr941.jpg?width=640&height=756&crop=smart&auto=webp&s=009ce8eb5c1eda639b1869067f1959ccae826d76" , "https://preview.redd.it/wh63r3wiqka41.jpg?width=640&crop=smart&auto=webp&s=dff976e7bbd522004cddcafb7b9583346cd74f58" , "https://preview.redd.it/p7lynnvlt4b41.jpg?width=640&crop=smart&auto=webp&s=8e19418b580d54ad0ce728464a16bcfa6e70e2ad" , "https://i.redd.it/45ib7na1i5b41.jpg" , "https://preview.redd.it/84f3z7w0k4b41.jpg?width=640&crop=smart&auto=webp&s=e01c4a77f9b3d17aa729d7fc1e94b6f01020818a" , "https://preview.redd.it/yt1si5kmwza41.jpg?width=640&crop=smart&auto=webp&s=9d8ea1762efdb854381542cb932d8f51eb8dadf9" , "https://preview.redd.it/6p1g6wtry8941.jpg?width=640&crop=smart&auto=webp&s=72e44928e2274527a18b71ee540dbb75f3c52ac3" , "https://preview.redd.it/4906dkbaoya41.jpg?width=640&crop=smart&auto=webp&s=0708b95fafb8acc225078f09a11626f3cdc9d8f6" , "https://preview.redd.it/80avvadxgga41.jpg?width=640&crop=smart&auto=webp&s=6dda4d0d8383f7ccaa2d16b5c7cb834f3ec49ca3" , "https://preview.redd.it/29rtu3f6ow941.jpg?width=640&crop=smart&auto=webp&s=20caa5b383cb0fcaa912c5b29e32038f6bcbd874" , "https://preview.redd.it/zmz1nsxv5l941.jpg?width=640&crop=smart&auto=webp&s=bf698faeebc41cf910a4a9298f811c471555bb7d" , "https://i.redd.it/78luedbauta41.png" , "https://i.redd.it/3ghlucwbwu241.jpg" , "https://preview.redd.it/o3vkuwmnp8241.jpg?width=640&crop=smart&auto=webp&s=b5dc842ce27833bffe798c56460fd5433683b538" , "https://i.redd.it/gjp7s00du8w31.png" , "https://preview.redd.it/yvicqmymgdr31.jpg?width=640&crop=smart&auto=webp&s=52a9041f88059775c804d3e77d1129ce64944a10"]
dont_get_it = ["I don't understand you 😔" , "I'm afraid I don't understand." , "Sorry,I don't understand." , "I don't understand."]
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, "Welcome " + name + ".  I'm your Telegram asistant. You can call me Avrean 😁. To find out my features just click /commands button." )
    bot.send_message('-1001318088745' , message.chat.first_name + ' just started using bot.' )
@bot.message_handler(commands=['commands'])
def handle_start(message):
    bot.send_photo(message.chat.id , "https://github.com/cnderton/windows/blob/master/AVrean.jpg?raw=true")
    bot.send_message(message.chat.id , "🅐🅥🅡🅔🅐🅝  🅕🅔🅐🅣🅤🅡🅔🅢\n●/about - 𝑴𝒐𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 𝒖𝒔.\n--------------------------------------------------------\n●/weather - 𝑭𝒊𝒏𝒅 𝒐𝒖𝒕 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒕𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒖𝒓𝒆 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒓𝒆𝒈𝒊𝒐𝒏\n--------------------------------------------------------\n●/review - 𝑺𝒉𝒂𝒓𝒆 𝒚𝒐𝒖𝒓 𝒏𝒆𝒘 𝒊𝒅𝒆𝒂𝒔 𝒂𝒏𝒅 𝒓𝒆𝒗𝒊𝒆𝒘𝒔 𝒘𝒊𝒕𝒉 𝒎𝒆.\n--------------------------------------------------------\n●/wikipedia - 𝑮𝒆𝒕 𝒏𝒆𝒆𝒅𝒆𝒅 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒇𝒓𝒐𝒎 𝑾𝒊𝒌𝒊𝒑𝒆𝒅𝒊𝒂 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒍𝒆𝒂𝒗𝒊𝒏𝒈 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎.\n--------------------------------------------------------\n●/contact - 𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝒘𝒊𝒕𝒉 𝒎𝒆\n--------------------------------------------------------\n●/talk - 𝑯𝒂𝒗𝒆 𝒂 𝒕𝒂𝒍𝒌 𝒘𝒊𝒕𝒉 𝑨𝒗𝒓𝒆𝒂𝒏.\n--------------------------------------------------------\n●/astro - 𝑰𝒏𝒕𝒆𝒓𝒆𝒔𝒕𝒊𝒏𝒈 𝒇𝒂𝒄𝒕𝒔 𝒂𝒃𝒐𝒖𝒕 𝒂𝒔𝒕𝒓𝒐𝒏𝒐𝒎𝒚.\n--------------------------------------------------------\n●/jokes - 𝑭𝒖𝒏𝒏𝒚 𝒋𝒐𝒌𝒆𝒔\n--------------------------------------------------------\n●/movie - 𝑮𝒆𝒕 𝒔𝒖𝒈𝒈𝒆𝒔𝒕𝒆𝒅 & 𝒑𝒐𝒑𝒖𝒍𝒂𝒓 𝒎𝒐𝒗𝒊𝒆𝒔 𝒏𝒂𝒎𝒆 𝒂𝒏𝒅 𝒐𝒗𝒆𝒓𝒗𝒊𝒆𝒘𝒔.\n--------------------------------------------------------\n●/translate - 𝑻𝒓𝒂𝒏𝒔𝒍𝒂𝒕𝒆 𝒘𝒐𝒓𝒅𝒔 & 𝒔𝒆𝒏𝒕𝒆𝒏𝒄𝒆𝒔 𝒇𝒓𝒐𝒎 𝑬𝒏𝒈𝒍𝒊𝒔𝒉 𝒕𝒐 𝒐𝒕𝒉𝒆𝒓 𝒍𝒂𝒏𝒈𝒖𝒂𝒈𝒆𝒔.\n--------------------------------------------------------\n●/currency - 𝑮𝒆𝒕 𝒇𝒓𝒆𝒆 𝒍𝒊𝒗𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒄𝒚 𝒓𝒂𝒕𝒆𝒔 𝒖𝒔𝒊𝒏𝒈 𝒕𝒉𝒆 𝒂𝒄𝒄𝒖𝒓𝒂𝒕𝒆 𝒅𝒂𝒕𝒂.\n--------------------------------------------------------")

@bot.message_handler(commands = ['jokes'])
def jokess(message):
    #bot.send_photo(message.chat.id , random.choice(jokes) ,reply_markup=emotion )
    emotion     = types.InlineKeyboardMarkup(row_width=2)
    emo1         = types.InlineKeyboardButton(text="👍"   , callback_data="emo1" )
    emo2          =types.InlineKeyboardButton(text="👎"   , callback_data="emo2")
    emotion.add(emo1 , emo2)
    bot.send_photo(message.chat.id , random.choice(jokes) ,reply_markup=emotion )
    bot.send_message('-1001318088745' , message.chat.first_name , " used 'jokes' feature" )
    
@bot.message_handler(commands = ['currency'])
def currencyy(message):
    bot.send_message(message.chat.id , "❌This feature is currently unavaible.❌")
    bot.send_message('-1001318088745' , message.chat.first_name + " used 'currency' feature")
@bot.message_handler(commands=['about'])
def handle(message):
    bot.reply_to(message, " 'Avrean' is a new business project from Winderton which allows you to get instant answers to your questions.\nRight now, I'm constantly improving this bot. \n   /commands ")
    bot.send_message('-1001318088745' , message.chat.first_name + " used 'about' feature")   
@bot.message_handler(commands=['review'])
def error_soo(message):
    linkk    = types.InlineKeyboardMarkup()
    link3         = types.InlineKeyboardButton(text="Write your feedback here"   , callback_data="link" , url = "https://t.me/demoonov")
    linkk.add(link3)
    bot.send_message(message.chat.id , "I would highly rate it if you write your feedback about this bot. You can contact with me by clicking the link below." , reply_markup=linkk)
    bot.send_message('-1001318088745' , message.chat.first_name + " used 'review' feature")
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
            bot.send_message(message.chat.id, "Current temperature in " + str(city) +  " is: " + str(temperature) + "°C  " + str(desc) + '\n Speed of wind: ' + str(wind) + ' km/h ' + '\n Humidity: ' + str(hum) + '%' + '\n(This feature will be updated soon)' )
            bot.send_message('-1001318088745' , message.chat.first_name + " used 'weather' feature")   
      except Exception as e:
            bot.reply_to(message, 'oooops. We could not find the city :(\nTry again using  /weather  command')


@bot.message_handler(commands=['wikipedia'])
def wikiipedia(message):
    v = message.text
    bot.send_message(message.chat.id, "type your request. To get result you MUST add ':' after typing your request.")
    bot.send_message('-1001318088745' , message.chat.first_name + " used 'wikipedia' feature")
    sleep(15)
   
@bot.message_handler(func = lambda message: message.text and ':' in message.text)    
def echo_all(message):
    try:
        bot.send_message(message.chat.id , 'Processing...')
        bot.send_message(message.chat.id, wikipedia.summary(message.text) )
        a = wikipedia.page(message.text) 
        bot.send_message(message.chat.id ,a.url )
        sleep(1)
        bot.send_message(message.chat.id,'/commands')      
    except Exception:
        bot.reply_to(message , "Oops,we couldn't find any results :(")

def Turkish_language(message):
    if "Tr" in message.text:
        bot.reply_to(message , ts.google(message.text , 'auto', 'tr') )  

@bot.message_handler(commands=['contact'])
def errorr_soo(message):
    link     = types.InlineKeyboardMarkup()
    link2         = types.InlineKeyboardButton(text="Contact with Developer"   , callback_data="link" , url = "https://t.me/demoonov")
    link.add(link2)
    bot.send_message(message.chat.id , "Contact with developer by clicking a link below." , reply_markup=link)

@bot.message_handler(commands=['talk'])
def talk_me(message):
    bot.reply_to(message , 'Talk to me 😁') 


@bot.message_handler(commands=["movie"])
def movie_1(message):
    keyboard     = types.InlineKeyboardMarkup(row_width=2)
    suggested         = types.InlineKeyboardButton(text="Suggested movies"   , callback_data="suggested")
    popularr  = types.InlineKeyboardButton(text="Popular movies"      , callback_data="popularr")
    keyboard.add(suggested , popularr)
    bot.send_message(message.chat.id, "Choose an action", reply_markup=keyboard)

@bot.message_handler(commands=['translate'])
def lang_functions(message):
    bot.reply_to(message , "❌This feature is currently unavaible.❌")    
    if call.message:
        if call.data == "emo1":
            bot.answer_callback_query(callback_query_id=call.id, show_alert= False,
                text="Thanks a million:)"  ) 
    if call.message:
        if call.data == "emo2":
            bot.answer_callback_query(callback_query_id=call.id, show_alert= False,
                text="Thanks a million:)"  )        

#def film_part(call):

    if call.message:
        if call.data == "suggested":
            bot.send_message(call.message.chat.id, "Please wait...")
            sleep(3)
            movie = Movie()
            recommendations = movie.recommendations(movie_id=111)
            for recommendation in recommendations:
                bot.send_message(
                    call.message.chat.id, "Film name - " + recommendation.title)
                sleep(1)
                bot.send_message(call.message.chat.id, "Overwiew - " +
                                 recommendation.overview) 

    if call.message:
        if call.data == "popularr":
            bot.send_message(call.message.chat.id , "Please wait...")
            #movie = Movie()

            movie = Movie()
            popular = movie.popular()
            sleep(5)
        
            for p in popular:
                bot.send_message(call.message.chat.id ,"Film name - " +  p.title)
                sleep(1)
                bot.send_message(call.message.chat.id ,"Overview - " + p.overview )
                sleep(1)

            bot.send_message(call.message.chat.id , "That's all for now😊")


            
@bot.message_handler(content_types = ['text'])
def talkk (message): 
    if message.text == message.text:
        bot.send_message('-1001318088745' , message.chat.first_name + ": " + message.text)   
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
bot.polling(none_stop=True)
