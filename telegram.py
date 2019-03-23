import telebot
import time
import urllib.request, json
import datetime

bot_token = '808951815:AAEHHP271TDAib_Bo2IdPexCoXLqM8SnTj4'
bot = telebot.TeleBot(token = bot_token)

def getTemp(location):
    now = datetime.datetime.now()

    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/air-temperature?date_time=" + now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + now.strftime("%H") + "%3A" + now.strftime("%M") + "%3A" + now.strftime("%S")

    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    return data
    # print(data["metadata"])

def findIndex(index, location, stations):
    for x in stations:
        if stations[index]["name"] == location:
            return index
        else:
            index = index + 1
            continue

def printTemp(data, location, stations):
    indexForData = findIndex(0, location, stations)
    tempToPrint = data["items"][0]["readings"][indexForData]["value"]
    toPrint = ("The temperature at " + location + " is " + str(tempToPrint))
    return toPrint

def getUV():
    now = datetime.datetime.now()

    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/uv-index?date_time=" + now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + now.strftime("%H") + "%3A" + now.strftime("%M") + "%3A" + now.strftime("%S")

    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    toPrint = "UV Index is now " + str(data["items"][0]["index"][0]["value"])
    return toPrint

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome!")

@bot.message_handler(commands = ['angmokio'])
def send_welcome(message):
    location = "Ang Mo Kio Avenue 5"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['banyan'])
def send_welcome(message):
    location = "Banyan Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['clementi'])
def send_welcome(message):
    location = "Clementi Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['eastcoast'])
def send_welcome(message):
    location = "East Coast Parkway"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['kimchuan'])
def send_welcome(message):
    location = "Kim Chuan Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['marinagardens'])
def send_welcome(message):
    location = "Marina Gardens Drive"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['nanyang'])
def send_welcome(message):
    location = "Nanyang Avenue"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['choachukang'])
def send_welcome(message):
    location = "Old Choa Chu Kang Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['pulauubin'])
def send_welcome(message):
    location = "Pulau Ubin"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['scotts'])
def send_welcome(message):
    location = "Scotts Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['sentosa'])
def send_welcome(message):
    location = "Sentosa"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['tuas'])
def send_welcome(message):
    location = "Tuas South Avenue 3"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['changi'])
def send_welcome(message):
    location = "Upper Changi Road North"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['westcoast'])
def send_welcome(message):
    location = "West Coast Highway"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['woodlandsave9'])
def send_welcome(message):
    location = "Woodlands Avenue 9"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['woodlandsroad'])
def send_welcome(message):
    location = "Woodlands Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    toPrint = printTemp(data, location, stations) + "\n" + getUV()
    bot.reply_to(message, toPrint)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
