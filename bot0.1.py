import telebot
import pyaztro
import datetime

bot = telebot.TeleBot("692288960:AAHJrOsfapNmCczDPS12lSn2ty36bn2kEbE")
x = datetime.datetime.now()
print(x)  

@bot.message_handler(commands=['start' , 'help'])
def send_welcome(message):
    
    bot.reply_to(message, "enter a zodiac sign on 'ua' or 'en' also it can be a emoji sign: ")

@bot.message_handler(content_types=['text','text'])
def send_message(message):
    sign = message.text
    if message.text == 'Leo'or message.text =='♌️'or message.text =='лев'or message.text =='Лев':
        sign = 'leo'
    elif message.text == 'Pisces'or message.text =='♓️'or message.text =='Риба'or message.text =='риба':
        sign = 'pisces'
    elif message.text == 'Aquarius'or message.text =='♒️'or message.text =='Водолій'or message.text =='водолій':
        sign = 'aquarius'
    elif message.text == 'Capricorn'or message.text =='♑️'or message.text =='Козеріг'or message.text =='козеріг':
        sign = 'capricorn'
    elif message.text == 'Sagittarius'or message.text =='♐️'or message.text =='Стрілець'or message.text =='стрілець':
        sign = 'sagittarius'
    elif message.text == 'Scorpio'or message.text =='♏️'or message.text =='Скорпіон'or message.text =='скорпіон':
        sign = 'scorpio'
    elif message.text == 'Libra'or message.text =='♎️'or message.text =='Терези'or message.text =='терези':
        sign = 'libra'
    elif message.text == 'Virgo'or message.text =='♍️'or message.text =='Діва'or message.text =='діва':
        sign = 'virgo'
    elif message.text == 'Cancer'or message.text =='♋️'or message.text =='рак'or message.text =='Рак':
        sign = 'cancer'
    elif message.text == 'Gemini'or message.text =='♊️'or message.text =='Близнюки'or message.text =='близнюки':
        sign = 'gemini'
    elif message.text == 'Taurus'or message.text =='♉️'or message.text =='телець'or message.text =='Телець':
        sign = 'taurus'
    elif message.text == 'Aries'or message.text =='♈️'or message.text =='овен'or message.text =='Овен':
        sign = 'aries'
    else:
        sign = 'aries'
    
    horoscope = pyaztro.Aztro(sign,day = 'today')
    horoscope1 = pyaztro.Aztro(sign,day = 'tomorrow')
                
    h = (sign + "\n" + "horoscope on today:  " +str(horoscope.description) + "\n\n" + "horoscope on tomorrow:  " + str(horoscope1.description) +
    "\n\n" + 'you compatibility: ' + str(horoscope.compatibility) + "\n\n" + 'your mood: ' + str(horoscope.mood) + "\n\n" +
    'your color: ' + str(horoscope.color) + "\n\n" + 'your lucky number: ' + str(horoscope.lucky_number)+ "\n\n" )
    bot.send_message(message.chat.id, h)

bot.polling( none_stop = True )
