#Imports
import telebot
import wikipedia
import pyowm
import pyshorteners#new
from forex_python.converter import CurrencyRates #new
import random
from tmdbv3api import Movie, TMDb
from time import sleep
from telebot import types
from telebot.types import Message
from telebot import apihelper, types
from urllib.request import urlopen as url_open
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
from google_trans import Translator#new
from decimal import Decimal #new
from dialogflow_lite.dialogflow import Dialogflow#new
import lyricsgenius

#Token
token = "742874199:AAEd7j8rRFh3Ymmg_g1ccsgMMARQzj-cfcE"
bot = telebot.TeleBot(token=token)
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'
#client = Client('ylFpj3mg5MhcKlQGkSnqcnyU1NCQm88KicZVFLHV')
url = 'https://api.nasa.gov/planetary/apod?' # I don't get how url queries work, someone help
API_KEY = 'api_key=ylFpj3mg5MhcKlQGkSnqcnyU1NCQm88KicZVFLHV' #own API key, please register for your own at NASA Open APIs
client_access_token = '7f9559e9436744a9bef9a562551c16ff'
dialogflow = Dialogflow(client_access_token=client_access_token)
genius = lyricsgenius.Genius("cw_sMUY8L7tqlykWOqiWwasqcPq_9SofNKX8CxKyOMIarw4TABsU2x6WxSeKol_j")
translator = Translator()
c = CurrencyRates()
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
jokes = ["https://raw.githubusercontent.com/cnderton/windows/master/Screenshot_20200116-213702_Instagram%20(2).jpg" , "https://ruinmyweek.com/wp-content/uploads/2019/05/21-damn-funny-memes-everyone-should-see-this-morning-16.jpg" , "https://preview.redd.it/53o0u089qr941.jpg?width=640&height=756&crop=smart&auto=webp&s=009ce8eb5c1eda639b1869067f1959ccae826d76" , "https://preview.redd.it/wh63r3wiqka41.jpg?width=640&crop=smart&auto=webp&s=dff976e7bbd522004cddcafb7b9583346cd74f58" , "https://preview.redd.it/p7lynnvlt4b41.jpg?width=640&crop=smart&auto=webp&s=8e19418b580d54ad0ce728464a16bcfa6e70e2ad" , "https://i.redd.it/45ib7na1i5b41.jpg" , "https://preview.redd.it/84f3z7w0k4b41.jpg?width=640&crop=smart&auto=webp&s=e01c4a77f9b3d17aa729d7fc1e94b6f01020818a" , "https://preview.redd.it/yt1si5kmwza41.jpg?width=640&crop=smart&auto=webp&s=9d8ea1762efdb854381542cb932d8f51eb8dadf9" , "https://preview.redd.it/6p1g6wtry8941.jpg?width=640&crop=smart&auto=webp&s=72e44928e2274527a18b71ee540dbb75f3c52ac3" , "https://preview.redd.it/4906dkbaoya41.jpg?width=640&crop=smart&auto=webp&s=0708b95fafb8acc225078f09a11626f3cdc9d8f6" , "https://preview.redd.it/80avvadxgga41.jpg?width=640&crop=smart&auto=webp&s=6dda4d0d8383f7ccaa2d16b5c7cb834f3ec49ca3" , "https://preview.redd.it/29rtu3f6ow941.jpg?width=640&crop=smart&auto=webp&s=20caa5b383cb0fcaa912c5b29e32038f6bcbd874" , "https://preview.redd.it/zmz1nsxv5l941.jpg?width=640&crop=smart&auto=webp&s=bf698faeebc41cf910a4a9298f811c471555bb7d" , "https://i.redd.it/78luedbauta41.png" , "https://i.redd.it/3ghlucwbwu241.jpg" , "https://preview.redd.it/o3vkuwmnp8241.jpg?width=640&crop=smart&auto=webp&s=b5dc842ce27833bffe798c56460fd5433683b538" , "https://i.redd.it/gjp7s00du8w31.png" , "https://preview.redd.it/yvicqmymgdr31.jpg?width=640&crop=smart&auto=webp&s=52a9041f88059775c804d3e77d1129ce64944a10" , 
"https://i.redd.it/j4645sg45gk41.jpg" , "https://i.redd.it/xw54jno4f9k41.jpg" , "https://i.redd.it/glqtaopw2gk41.jpg" , "https://i.redd.it/46h42h7esfk41.jpg" , "https://i.redd.it/lclm4yjhyfk41.jpg" , "https://i.redd.it/0iprrtim2ak41.jpg" , "https://i.redd.it/v0rix24jpfk41.jpg" , "https://i.redd.it/uz3d56z1gfk41.png" , "https://i.redd.it/oek28q7wlek41.jpg" , "https://i.redd.it/8jjgsbb1dek41.jpg" , "https://i.redd.it/0m9m7gbalfk41.jpg" , "https://i.redd.it/n9d5h3b9zek41.jpg" , "https://i.redd.it/9fjnd32uyak41.jpg" , "https://i.redd.it/4pqqx042eck41.jpg" , "https://i.redd.it/y7mpsliiybk41.jpg" , "https://i.redd.it/9eqndz6ykfk41.jpg" , "https://i.redd.it/gkjx9uo4sbk41.jpg" , "https://i.redd.it/utv3415trfk41.png" , 
"https://i.redd.it/3pzu0srceek41.jpg" , "https://i.redd.it/y3ru3pz06bk41.jpg" , "https://i.redd.it/2ob4rwe2wbk41.jpg" , "https://i.redd.it/5skmfmbmoek41.jpg" , "https://i.redd.it/pv5k00j5oek41.jpg" , "https://i.redd.it/2q08os415fk41.jpg" , "https://i.redd.it/4g7iw88rtbk41.jpg" , "https://i.redd.it/wswr2wsbkek41.jpg" , "https://i.redd.it/0klm4g73xek41.jpg" , "https://i.redd.it/0v4c5z5gxdk41.png" , "https://preview.redd.it/yrtq8lxkzek41.jpg?width=640&crop=smart&auto=webp&s=0c7aabc8bbbf360b8caf9ac91b4f9e35efecd8ed" , "https://i.redd.it/7qgolmwarfk41.jpg" , "https://raw.githubusercontent.com/cnderton/windows/master/funny.jpg" ,
"https://i.redd.it/gqg2ixi1pgl41.jpg" , "https://i.redd.it/tsrro2usgfl41.jpg" , "https://i.redd.it/e5awis7jiel41.jpg" , "https://i.redd.it/h8xuw5zzggl41.jpg" , "https://i.redd.it/b9mmnvlagel41.jpg" , "https://i.redd.it/72crm871qgl41.jpg" , "https://i.redd.it/2z6a627smfl41.jpg" , "https://i.redd.it/v5ikvwwhdfl41.jpg" , "https://i.redd.it/ymvxfjzy8gl41.jpg" , "https://i.redd.it/zcf1663t7fl41.jpg" , "https://i.redd.it/nxim4m9bqgl41.jpg" , "https://i.redd.it/3y5u4pd8jgl41.jpg" , "https://i.redd.it/xkig6fcl2gl41.jpg" , "https://i.redd.it/hzuh80s0lgl41.jpg" , "https://i.redd.it/3olihjzwjfl41.jpg" , "https://i.redd.it/m8fk6kx37gl41.jpg" , 
"https://i.redd.it/8b6knqmvnse41.jpg" , "https://i.redd.it/jy7kiim5lci41.png" ,"https://i.redd.it/0qb5v90v2vi31.png" , "https://i.redd.it/qez06favaul41.jpg" , "https://i.redd.it/2dnu20467vl41.png" , "https://i.redd.it/scn7mb03yva41.jpg" , "https://i.redd.it/etqqo4sq4z331.png" , "https://i.redd.it/xmubtp2zkzl31.png" , "https://i.redd.it/4m9ufq53w7521.jpg" , "https://i.redd.it/bihsr3miawl41.jpg" , "https://i.redd.it/cc2fcv23bsl41.jpg" , "https://i.redd.it/umgz4voc5wl41.png" , "https://i.redd.it/yunjnvieuul41.jpg" , "https://i.redd.it/bhgowkdaztl41.jpg" , "https://i.redd.it/uy3ft3rbcvl41.jpg" , "https://i.redd.it/63qxkxpr4ul41.jpg" , "https://i.redd.it/99c76kb2wul41.jpg" , "https://i.redd.it/yut8qi5n1ul41.jpg" ]



@bot.message_handler(commands=['start'])
def handle_start_help(message):
    name = message.from_user.first_name
    #vdeo = open('https://github.com/cnderton/windows/blob/master/Rush%20Story_0366.mp4', 'rb')
    #bot.send_video(message.chat.id , 'https://github.com/cnderton/windows/blob/master/Rush%20Story_0366.mp4')
    bot.send_message(message.chat.id, "Welcome " + name + ".  I'm your Telegram asistant. You can call me Avrean😊.To find out my features just click /commands button." )
    bot.send_message('-1001318088745' , name + ' @' + message.from_user.username +' just started using bot.' )
    
@bot.message_handler(commands=['commands'])
def handle_start(message):
    bot.send_photo(message.chat.id , "https://github.com/cnderton/windows/blob/master/AVrean.jpg?raw=true")
    bot.send_message(message.chat.id , "🅐🅥🅡🅔🅐🅝  🅕🅔🅐🅣🅤🅡🅔🅢\n●/about - More about us\n--------------------------------------------------------\n●/weather - Find out current temperature in your region\n--------------------------------------------------------\n●/review - Share your ideas and experience\n--------------------------------------------------------\n●/wikipedia - Get needed information from Wikipedia without leaving Telegram\n--------------------------------------------------------\n●/contact - Contact with the developer\n--------------------------------------------------------\n●/talk - Have a talk with Avrean\n--------------------------------------------------------\n●/jokes - Funny jokes:)\n--------------------------------------------------------\n●/movie - Get suggested & popular movies and overviews\n--------------------------------------------------------\n●/translate - Translate words & sentences from English to other languages.\n--------------------------------------------------------\n●/currency - Get free live currency rates & count currrencies using the accurate data\n--------------------------------------------------------\n●/lyrics - Search lyrics of songs\n--------------------------------------------------------\n●/link - Make long links shorter")

@bot.message_handler(commands=['currency'])
def start_of_currency(message):
    main_cy     = types.InlineKeyboardMarkup()
    live_currency = types.InlineKeyboardButton(text="Currency Rates"  , callback_data="live_currency")
    count_currency = types.InlineKeyboardButton(text="Count Currencies" , callback_data="count_currency")
    main_cy.add(live_currency , count_currency)
    bot.send_message(message.chat.id , "Make a choice" , reply_markup=main_cy)
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'currency' feature")



@bot.message_handler(commands = ['jokes'])
def jokess(message):
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'jokes' feature" )
    #bot.send_photo(message.chat.id , random.choice(jokes) ,reply_markup=emotion )
    emotion     = types.InlineKeyboardMarkup(row_width=2)
    emo1         = types.InlineKeyboardButton(text="👍"   , callback_data="emo1" )
    emo2          =types.InlineKeyboardButton(text="👎"   , callback_data="emo2")
    emotion.add(emo1 , emo2)
    bot.send_photo(message.chat.id , random.choice(jokes) ,reply_markup=emotion )
    
     
@bot.message_handler(commands=['about'])
def handle(message):
    bot.send_message(message.chat.id , " Meet the multifucntional bot 'Avrean' that can be used on telegram as your assistant. Bot gets smarter with every update. It lets you do some basic operations without leaving telegram app. Click /commands to see features. ")
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'about' feature")   
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
            bot.send_message(message.chat.id, "Temperature in " + str(city) +"\n\n" + str(temperature) + "°C  " + str(desc) + '🌡\nSpeed of wind: ' + str(wind) + ' km/h 💨' + '\nHumidity: ' + str(hum) + '% 💧')
            bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'weather' feature. TEXT:" + message.text)   
      except Exception as e:
            bot.reply_to(message, 'oooops. We could not find the city :(\nTry again using  /weather  command')


@bot.message_handler(commands=['links'])
def mdg(message):
    a = bot.send_message(message.chat.id , "Just paste the original link")
    bot.register_next_step_handler(a , link)

@bot.message_handler(commands=['wikipedia'])
def wikiipedia(message):
    v = message.text
    bot.send_message(message.chat.id, "type your request. To get result you MUST add 'wiki' after typing your request.")
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'wikipedia' feature")
    sleep(15)
   
@bot.message_handler(func = lambda message: message.text and 'wiki' in message.text)    
def echo_all(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        g = message.text[:-4]
        bot.send_message(message.chat.id, wikipedia.summary(g) )
        a = wikipedia.page(message.text) 
        bot.send_message(message.chat.id ,a.url )
        bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'wikipedia' feature. TEXT: " + message.text)
        sleep(1)
        bot.send_message(message.chat.id,'/commands')      
    except Exception:
        bot.reply_to(message , "Oops,we couldn't find any results :(")



@bot.message_handler(commands=['contact'])
def errorr_soo(message):
    link     = types.InlineKeyboardMarkup()
    link2         = types.InlineKeyboardButton(text="Contact with Developer"   , callback_data="link" , url = "https://t.me/demoonov")
    link.add(link2)
    bot.send_message(message.chat.id , "Contact with developer by clicking a link below." , reply_markup=link)

@bot.message_handler(commands=['lyrics'])
def handle_start_help(message):
    singer = bot.send_message(message.chat.id , "Type the artist's name")
    bot.register_next_step_handler(singer , sbs) 
    #HERE LOGS

@bot.message_handler(commands=['talk'])
def talk_me(message):
    talkkk   = types.InlineKeyboardMarkup()
    talkk           =types.InlineKeyboardButton(text="Talk" , callback_data="talkk")
    talkkk.add(talkk)
    bot.reply_to(message , "Sure,let's talk:). Click 'talk' to start." , reply_markup=talkkk) 


@bot.message_handler(commands=["movie"])
def movie_1(message):
    keyboard     = types.InlineKeyboardMarkup(row_width=2)
    suggested         = types.InlineKeyboardButton(text="Suggested movies"   , callback_data="suggested")
    popularr  = types.InlineKeyboardButton(text="Popular movies"      , callback_data="popularr")
    keyboard.add(suggested , popularr)
    bot.send_message(message.chat.id, "Choose an action", reply_markup=keyboard)
   

@bot.message_handler(commands=['translate'])
def lang_functions(message):
    lang     = types.InlineKeyboardMarkup(row_width=2)
    russian         = types.InlineKeyboardButton(text="🇷🇺 Russian 🇷🇺"   , callback_data="russian")      
    turkish         = types.InlineKeyboardButton(text="🇹🇷 Turkish 🇹🇷"   , callback_data="turkish")
    czech           = types.InlineKeyboardButton(text="🇨🇿 Czech 🇨🇿"     , callback_data="czech")
    spanish         = types.InlineKeyboardButton(text="🇪🇸 Spanish 🇪🇸"   , callback_data="spanish")   
    azeri           = types.InlineKeyboardButton(text="🇦🇿 Azerbaijani 🇦🇿" , callback_data="azeri")  
    english       = types.InlineKeyboardButton(text="🇬🇧 English 🇬🇧"        , callback_data='english')
    #url             = types.InlineKeyboardButton(text="Url"             , callback_data='url' , url = "google.com")
    #lang.add(url)
    lang.add(english , russian , turkish , czech , spanish , azeri )
    #lang.add(azeri)
    bot.send_message(message.chat.id , "Choose a language to translate" , reply_markup = lang)
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'translate' feature")

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):    
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

 
  
    if call.message:
        if call.data == "live_currency":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Your Choice: Currency Rates",
                reply_markup=None)
                currency     = types.InlineKeyboardMarkup()
                usd_rub        = types.InlineKeyboardButton(text="USD -> RUB"   , callback_data="usd_rub" )
                rub_usd        =types.InlineKeyboardButton(text="RUB -> USD"   , callback_data="rub_usd")
                tr_usd         =types.InlineKeyboardButton(text="TRY -> USD"   , callback_data="tr_usd")
                usd_tr         = types.InlineKeyboardButton(text="USD -> TRY"  , callback_data="usd_tr")
                tr_rub      =types.InlineKeyboardButton(text="TRY -> RUB"   , callback_data="tr_rub")
                rub_tr      =types.InlineKeyboardButton(text ="RUB -> TRY"  , callback_data="rub_tr")
                euro_rub        =types.InlineKeyboardButton(text="EUR -> RUB"   , callback_data="euro_rub")
                euro_usd        =types.InlineKeyboardButton(text="EUR -> USD"   , callback_data="euro_usd")
                euro_tr        =types.InlineKeyboardButton(text="EUR -> TRY"   , callback_data="euro_tr")
                usd_euro        =types.InlineKeyboardButton(text="USD -> EUR"   , callback_data="usd_euro")

                currency.add(usd_rub , rub_usd , tr_usd , usd_tr , rub_tr , tr_rub , rub_tr , euro_tr , euro_usd , euro_rub , usd_euro)
                bot.send_message(call.message.chat.id, "Choose one", reply_markup=currency)

    if call.message:
        if call.data == "count_currency":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Your Choice: Count currency",
                reply_markup=None)
                currencyy     = types.InlineKeyboardMarkup()
                usd_rubb        = types.InlineKeyboardButton(text="USD -> RUB"   , callback_data="usd_rubb" )
                rub_usdd        =types.InlineKeyboardButton(text="RUB -> USD"   , callback_data="rub_usdd")
                tr_usdd         =types.InlineKeyboardButton(text="TRY -> USD"   , callback_data="tr_usdd")
                usd_trr         = types.InlineKeyboardButton(text="USD -> TRY"  , callback_data="usd_trr")
                tr_rubb     =types.InlineKeyboardButton(text="TRY -> RUB"   , callback_data="tr_rubb")
                rubb_try      =types.InlineKeyboardButton(text ="RUB -> TRY"  , callback_data="rubb_try")
                euro_rub        =types.InlineKeyboardButton(text="EUR -> RUB"   , callback_data="euro_rubb")
                euro_usdd       =types.InlineKeyboardButton(text="EUR -> USD"   , callback_data="euro_usdd")
                euro_trr        =types.InlineKeyboardButton(text="EUR -> TRY"   , callback_data="euro_trr")
                usd_euuro        =types.InlineKeyboardButton(text="USD -> EUR"   , callback_data="usd_euuro")
                #talkk           =types.InlineKeyboardButton(text="Talk" , callback_data="talkk")

                currencyy.add(usd_rubb , rub_usdd , tr_usdd , usd_trr , tr_rubb , rubb_try , euro_trr , euro_usdd , euro_rub,usd_euuro )
                bot.send_message(call.message.chat.id, "Choose one", reply_markup=currencyy)
    # I N L I N E ends here                       
   

           
    #  R A T E starts here
    if call.message:
        if call.data == "usd_euro":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nUSD -> EUR\n\nCost of 1$ is " + str( c.get_rate('USD', 'EUR') ) + "€" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "USD -> EUR\n\nCost of 1$ is " + str( c.get_rate('USD', 'EUR') ) + "€" , reply_markup=markup)
            

    if call.message:
        if call.data == "usd_rub":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nUSD -> RUB\n\nCost of 1$ is " + str( c.get_rate('USD', 'RUB') ) + "₽" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "USD -> RUB\n\nCost of 1$ is " + str( c.get_rate('USD', 'RUB') ) + "₽" , reply_markup=markup)

    if call.message:
        if call.data == "rub_usd":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nRUB -> USD\n\nCost of 1₽ is " + str(c.get_rate('RUB', 'USD') )+ "$" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "RUB -> USD\n\nCost of 1₽ is " + str(c.get_rate('RUB', 'USD') )+ "$" , reply_markup=markup)

    if call.message:
        if call.data == "tr_usd":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nTRY -> USD\n\nCost of 1₺ is " + str(c.get_rate('TRY', 'USD') )+ "$" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "TRY -> USD\n\nCost of 1₺ is " + str(c.get_rate('TRY', 'USD') )+ "$" , reply_markup=markup)       
                                                 
    if call.message:
        if call.data == "usd_tr":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nUSD -> TRY\n\nCost of 1$ is " + str(c.get_rate('USD', 'TRY') )+"₺" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "USD -> TRY\n\nCost of 1$ is " + str(c.get_rate('USD', 'TRY') )+"₺" , reply_markup=markup)  

    if call.message:
        if call.data == "rub_tr":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nRUB -> TRY\n\nCost of 1₽ is " + str(c.get_rate('RUB', 'TRY') )+"₺" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "RUB -> TRY\n\nCost of 1₽ is " + str(c.get_rate('RUB', 'TRY') )+"₺" , reply_markup=markup)  

    if call.message:
        if call.data == "tr_rub":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nTRY -> RUB\n\nCost of 1₺ is " + str(c.get_rate('TRY', 'RUB') )+"₽" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "TRY -> RUB\n\nCost of 1₺ is " + str(c.get_rate('TRY', 'RUB') )+"₽" , reply_markup=markup)  

    if call.message:
        if call.data == "euro_tr":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nEUR -> TRY\n\nCost of 1€ is " + str(c.get_rate('EUR', 'TRY') )+"₺" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "EUR -> TRY\n\nCost of 1€ is " + str(c.get_rate('EUR', 'TRY') )+"₺" , reply_markup=markup)
   
    if call.message:
        if call.data == "euro_usd":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nEUR -> USD\n\nCost of 1€ is " + str(c.get_rate('EUR', 'USD') )+"$" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "EUR -> USD\n\nCost of 1€ is " + str(c.get_rate('EUR', 'USD') )+"$" , reply_markup=markup)    

    if call.message:
        if call.data == "euro_rub":
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query= "\n\nEUR -> RUB\n\nCost of 1€ is " + str(c.get_rate('EUR', 'RUB') )+"₽" )
            markup.add(switch_button)    
            bot.send_message(call.message.chat.id, "EUR -> RUB\n\nCost of 1€ is " + str(c.get_rate('EUR', 'RUB') )+"₽" , reply_markup=markup)             

       
   
    # R A T E ends here
    if call.message:
        if call.data == "usd_euuro":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, dollar_euro)


    if call.message:
        if call.data == "rub_usdd":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, usd_rrub)
            
    if call.message:
        if call.data == "tr_usdd":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, tr_dollar)
  

  
  
    if call.message:
        if call.data == "usd_rubb":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, usd_rubl)  

   
    
   
    if call.message:
        if call.data == "usd_trr":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, usd_turkey) 

   
   
    if call.message:
        if call.data == "tr_rubb":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, tr_ruble)


   
   
    if call.message:
        if call.data == "rubb_try":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message , ruble_tr)


   
    if call.message:
        if call.data == "euro_rubb":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, eur_rubb)


    if call.message:
        if call.data == "euro_usdd":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, euro_dollar)


    if call.message:
        if call.data == "euro_trr":
            bot.send_message(call.message.chat.id , "Type ONLY amount")
            bot.register_next_step_handler(call.message, euro_turk)

    if call.message:
        if call.data == 'english' :
            bot.send_message(call.message.chat.id , "Just enter text. To translate to english language you don't need to specify your language. Just enter text in your language.")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇬🇧 English 🇬🇧",
                reply_markup=None)
            bot.register_next_step_handler(call.message, in_english)    

            
    if call.message:
        if call.data == 'russian' :
            bot.send_message(call.message.chat.id , "Just enter text")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇷🇺 Russian 🇷🇺",
                reply_markup=None)
            bot.register_next_step_handler(call.message, in_russian)    

    if call.message:
        if call.data == 'turkish':
            bot.send_message(call.message.chat.id , "Just enter text")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇹🇷 Turkish 🇹🇷",
                reply_markup=None) 
            bot.register_next_step_handler(call.message, in_turkish)      
    if call.message:
        if call.data == 'czech':
            bot.send_message(call.message.chat.id , "Just enter text" )    
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇨🇿 Czech 🇨🇿",
                reply_markup=None)
            bot.register_next_step_handler(call.message , in_czech)  
    if call.message:
        if call.data == "spanish":
            bot.send_message(call.message.chat.id ,"Just enter text" )        
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇪🇸 Spanish 🇪🇸",
                reply_markup=None)
            bot.register_next_step_handler(call.message , in_spanish)          
    if call.message:
        if call.data == "azeri":
            bot.send_message(call.message.chat.id , "Just enter text")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇦🇿 Azerbaijani 🇦🇿",
                reply_markup=None) 
            bot.register_next_step_handler(call.message , in_azeri)    
    
    if call.message:
        if call.data == "talkk":
            bot.send_message(call.message.chat.id , "Hi:)")
            bot.register_next_step_handler(call.message, talk_to_me)

def in_azeri(message):
    a = translator.translate(message.text , src='en', dest='az').text 
    bot.reply_to(message , a)
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Eng - Azeri]: " + message.text)

def in_spanish(message):
    a = translator.translate(message.text , src='en', dest='es').text 
    bot.reply_to(message , a)
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Eng - Spanish]: " + message.text)

def in_czech(message):  
    a = translator.translate(message.text , src='en', dest='cs').text      
    bot.reply_to(message , a )
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Eng - Czech]: " + message.text)

def in_russian(message):
    a = translator.translate(message.text ,  src='en', dest='ru').text 
    bot.reply_to(message ,  a )
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Eng - Russian]: " + message.text)     

def in_turkish (message):
    a = translator.translate(message.text , src='en', dest='tr').text 
    bot.reply_to(message , a ) 
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Eng - Turkish]: " + message.text)   

def in_english(message):
    a = translator.translate(message.text , dest='en').text 
    bot.reply_to(message , a ) 
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used translate [Undefined - English]: " + message.text)     

def usd_rrub(message):   
    bot.send_chat_action(message.chat.id, 'typing')
    j = message.text
    g = c.convert('RUB' , 'USD' , Decimal(j))
    f = flaera = str(g)
    bot.send_message(message.chat.id , "𝗥𝗨𝗕 -> 𝗨𝗦𝗗\n\nCost of " + j + "₽ is " + f[:-7] +"$"  ) 

def tr_dollar(message):
    bot.send_chat_action(message.chat.id, 'typing')
    p = message.text
    d = c.convert('TRY' , 'USD' , Decimal(p))
    v = str(d)
                   #pyperclip.copy(v)
    bot.send_message(message.chat.id , "𝗧𝗥𝗬 -> 𝗨𝗦𝗗\n\nCost of " + message.text + "₺ is " + v[:-7]  + "$"  )      

def usd_rubl(message):
    bot.send_chat_action(message.chat.id, 'typing')
    t = message.text
    t = c.convert('USD' , 'RUB' , Decimal(t))
    s = str(t)
                #pyperclip.copy(s)
    bot.send_message(message.chat.id ,  "𝗨𝗦𝗗  -> 𝗥𝗨𝗕\n\nCost of " + message.text + "$ is " + s[:-7] + "₽")

def usd_turkey(message):
    bot.send_chat_action(message.chat.id, 'typing')
    r = message.text
    n = c.convert('USD' , 'TRY' , Decimal(r))
    h = str(n)
    bot.send_message(message.chat.id ,  "𝗨𝗦𝗗  -> 𝗧𝗥𝗬\n\nCost of " + message.text + "$ is " + h[:-7] + "₺")  

def tr_ruble(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    g = message.text
    a = c.convert('TRY' , 'RUB' , Decimal(g))
    k = str(a)
    bot.send_message(message.chat.id ,  "𝗧𝗥𝗬 -> 𝗥𝗨𝗕\n\nCost of " + message.text + "₺ is " + k[:-7] + "₽") 

def ruble_tr(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    y = message.text
    e = c.convert('RUB' , 'TRY' , Decimal(y))
    x = str(e)
    bot.send_message(message.chat.id ,  "𝗥𝗨𝗕 -> 𝗧𝗥𝗬\n\nCost of " + message.text + "₽ is " + x[:-7] + "₺") 

def eur_rubb(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    q = message.text
    b = c.convert('EUR' , 'RUB' , Decimal(q))
    z = str(b)
    bot.send_message(message.chat.id ,  "𝗘𝗨𝗥 -> 𝗥𝗨𝗕\n\nCost of " + message.text + "€ is " + z + "₽")

def euro_dollar(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    q = message.text
    b = c.convert('EUR' , 'USD' , Decimal(q))
    z = str(b)
    bot.send_message(message.chat.id ,  "𝗘𝗨𝗥 -> 𝗨𝗦𝗗\n\nCost of " + message.text + "€ is " + z + "₺")    

def euro_turk(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    q = message.text
    b = c.convert('EUR' , 'TRY' , Decimal(q))
    z = str(b)
    bot.send_message(message.chat.id ,  "𝗘𝗨𝗥 -> 𝗧𝗥𝗬\n\nCost of " + message.text + "€ is " + z + "₺")              

def dollar_euro(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    q = message.text
    b = c.convert('USD' , 'EUR' , Decimal(q))
    z = str(b)
    a = bot.send_message(message.chat.id ,  "𝗨𝗦𝗗 -> 𝗘𝗨𝗥\n\nCost of " + message.text + "$ is " + z[:-7] + "€" )

    
    

def sbs(message):  
    global a  
    a = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    v = bot.send_message(message.chat.id , "Now type the song's name")
    bot.register_next_step_handler(v , song)
    

def song(message):
    try:
        b = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        song = genius.search_song(b, a)
        bot.send_message(message.chat.id , song.lyrics)
        bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'lyrics' feature TEXT: " + a + ' ' + message.text)

    except AttributeError:
        bot.send_message(message.chat.id , "No results for your request.Make sure that you typed everything correctly. Click /lyrics to try again")   


def link(message):
    try:
       markup = types.InlineKeyboardMarkup() 
       s = pyshorteners.Shortener(api_key='ef941aaa8d3343585156eb1b19362bc916727cc2')
       a = s.bitly.short(message.text)  
       switch_button = types.InlineKeyboardButton(text="Share" ,  switch_inline_query =  '\n\n Made with Avrean - ' + s.bitly.short(message.text) )
       markup.add(switch_button)
       bot.send_message(message.chat.id, "Here is the short version of the original link: - " + s.bitly.short(message.text) , reply_markup=markup) 

    except Exception:
        bot.send_message(message.chat.id , "Wrong link! Make sure that your link includes 'https://' or you don't have any other mistakes in your link.")        

@bot.message_handler(func = lambda message: 'hey' or 'Hey' or 'HEY' in message.text)
def talk_to_me (message):       
    bot.send_chat_action(message.chat.id, 'typing')
             #response = dialogflow.text_request(message.text) 
    bot.send_message(message.chat.id , dialogflow.text_request(message.text) )
    bot.send_message('-1001318088745' , message.chat.first_name + ' @' + message.from_user.username + " used 'talk'. TEXT: " + message.text)


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
