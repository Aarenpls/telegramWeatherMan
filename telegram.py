import telebot
from datetime import datetime, timedelta
import urllib.request, json

bot_token = '808951815:AAEHHP271TDAib_Bo2IdPexCoXLqM8SnTj4' # NOT THE ACTUAL TOKEN FOR OUR BOT
bot = telebot.TeleBot(token = bot_token)

def getTemp(location):
    utc_now = datetime.utcnow()
    sg_now = utc_now + timedelta(hours=8)
    currentDateTime = sg_now.strftime("%Y") + "-" + sg_now.strftime("%m") + "-" + sg_now.strftime("%d") + "T" + sg_now.strftime("%H") + "%3A" + sg_now.strftime("%M") + "%3A" + sg_now.strftime("%S")
    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/air-temperature?date_time=" + currentDateTime

    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    return data

def findIndex(location, stations):
    index = 0
    for x in stations:
        if stations[index]["name"] == location:
            return index
        else:
            index = index + 1
            continue

def printTemp(data, location, stations):
    indexForData = findIndex(location, stations)
    try:
        tempToPrint = data["items"][0]["readings"][indexForData]["value"]
        toPrint = ("Current temperature: " + str(tempToPrint) + chr(176) + "C")
        return toPrint
    except:
        return "Current temperature: Not available"

def getUV():
    utc_now = datetime.utcnow()
    sg_now = utc_now + timedelta(hours=8)
    currentDateTime = sg_now.strftime("%Y") + "-" + sg_now.strftime("%m") + "-" + sg_now.strftime("%d") + "T" + sg_now.strftime("%H") + "%3A" + sg_now.strftime("%M") + "%3A" + sg_now.strftime("%S")
    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/uv-index?date_time=" + currentDateTime

    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    valueOfUV = data["items"][0]["index"][0]["value"]
    toPrint = "Current UV Index: " + str(valueOfUV)
    if valueOfUV < 3:
        toPrint += " (Low)"
    elif valueOfUV < 6:
        toPrint += " (Moderate)"
    elif valueOfUV < 8:
        toPrint += " (High)"
    elif valueOfUV < 11:
        toPrint += " (Very high)"
    else:
        toPrint += " (EXTREME)"
    return toPrint

def getForecast(area):
    utc_now = datetime.utcnow()
    sg_now = utc_now + timedelta(hours=8)
    currentDateTime = sg_now.strftime("%Y") + "-" + sg_now.strftime("%m") + "-" + sg_now.strftime("%d") + "T" + sg_now.strftime("%H") + "%3A" + sg_now.strftime("%M") + "%3A" + sg_now.strftime("%S")
    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date_time=" + currentDateTime
    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    toPrint = "Area forecast (6hrs): " + str(data["items"][0]["periods"][0]["regions"][area])
    return toPrint

def getPSI(area):
    utc_now = datetime.utcnow()
    sg_now = utc_now + timedelta(hours=8)
    currentDateTime = sg_now.strftime("%Y") + "-" + sg_now.strftime("%m") + "-" + sg_now.strftime("%d") + "T" + sg_now.strftime("%H") + "%3A" + sg_now.strftime("%M") + "%3A" + sg_now.strftime("%S")
    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/psi?date_time=" + currentDateTime
    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())
    valueOfPSI = data["items"][0]["readings"]["psi_twenty_four_hourly"][area]
    toPrint = "Current PSI reading: " + str(valueOfPSI)
    if valueOfPSI < 51:
        toPrint += " (Good)"
    elif valueOfPSI < 101:
        toPrint += " (Moderate)"
    elif valueOfPSI < 201:
        toPrint += " (Unhealthy)"
    elif valueOfPSI < 301:
        toPrint += " (Very unhealthy)"
    else:
        toPrint += " (This is bad...)"
    return toPrint

def getNearestStation(userLatitude, userLongitude):
    utc_now = datetime.utcnow()
    sg_now = utc_now + timedelta(hours=8)
    currentDateTime = sg_now.strftime("%Y") + "-" + sg_now.strftime("%m") + "-" + sg_now.strftime("%d") + "T" + sg_now.strftime("%H") + "%3A" + sg_now.strftime("%M") + "%3A" + sg_now.strftime("%S")
    currentDateTimeURL = "https://api.data.gov.sg/v1/environment/air-temperature?date_time=" + currentDateTime

    with urllib.request.urlopen(currentDateTimeURL) as url:
        data = json.loads(url.read().decode())

    stations = data["metadata"]["stations"]

    nearestStation = "dummy"
    nearestDistance = 1000
    index = 0
    for x in stations:
        stationLatitude = stations[index]["location"]["latitude"]
        stationLongitude = stations[index]["location"]["longitude"]
        latToCompare = abs(stationLatitude - userLatitude)
        longToCompare = abs(stationLongitude - userLongitude)
        distance = latToCompare + longToCompare
        if distance < nearestDistance:
            nearestDistance = distance
            nearestStation = stations[index]["name"]
        index = index + 1

    return nearestStation

def getNearestArea(location):
    if location == "Ang Mo Kio Avenue 5":
        return "central"
    elif location == "Banyan Road":
        return "west"
    elif location == "Clementi Road":
        return "west"
    elif location == "East Coast Parkway":
        return "east"
    elif location == "Kim Chuan Road":
        return "east"
    elif location == "Marina Gardens Drive":
        return "south"
    elif location == "Nanyang Avenue":
        return "west"
    elif location == "Old Choa Chu Kang Road":
        return "west"
    elif location == "Pulau Ubin":
        return "east"
    elif location == "Scotts Road":
        return "central"
    elif location == "Sentosa":
        return "south"
    elif location == "Tuas South Avenue 3":
        return "west"
    elif location == "Upper Changi Road North":
        return "east"
    elif location == "West Coast Highway":
        return "west"
    elif location == "Woodlands Avenue 9":
        return "north"
    elif location == "Woodlands Road":
        return "north"
    else:
        return "central"

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    msg = "This is a bot that tells the current weather." + "\n" + "Type /<AREA> to get that location's current weather." + " \U0001F60A \U0001F61D"
    bot.reply_to(message, msg)

@bot.message_handler(commands = ['angmokio'])
def send_welcome(message):
    location = "Ang Mo Kio Avenue 5"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['banyan'])
def send_welcome(message):
    location = "Banyan Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['clementi'])
def send_welcome(message):
    location = "Clementi Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['eastcoast'])
def send_welcome(message):
    location = "East Coast Parkway"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['kimchuan'])
def send_welcome(message):
    location = "Kim Chuan Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['marinagardens'])
def send_welcome(message):
    location = "Marina Gardens Drive"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['nanyang'])
def send_welcome(message):
    location = "Nanyang Avenue"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['choachukang'])
def send_welcome(message):
    location = "Old Choa Chu Kang Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['pulauubin'])
def send_welcome(message):
    location = "Pulau Ubin"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['scotts'])
def send_welcome(message):
    location = "Scotts Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['sentosa'])
def send_welcome(message):
    location = "Sentosa"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['tuas'])
def send_welcome(message):
    location = "Tuas South Avenue 3"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['changi'])
def send_welcome(message):
    location = "Upper Changi Road North"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['westcoast'])
def send_welcome(message):
    location = "West Coast Highway"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['woodlandsave9'])
def send_welcome(message):
    location = "Woodlands Avenue 9"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(commands = ['woodlandsroad'])
def send_welcome(message):
    location = "Woodlands Road"
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    userLatitude = message.location.latitude
    userLongitude = message.location.longitude
    print(userLatitude, userLongitude)
    location = getNearestStation(userLatitude, userLongitude)
    data = getTemp(location)
    stations = data["metadata"]["stations"]
    area = getNearestArea(location)
    toPrint = location + "\n" + printTemp(data, location, stations) + "\n" + getUV() + "\n" + getPSI(area) + "\n" + getForecast(area)
    bot.reply_to(message, toPrint)

while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
