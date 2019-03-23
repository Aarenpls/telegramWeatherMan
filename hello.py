import urllib.request, json
import datetime

now = datetime.datetime.now()

currentDateTimeURL = "https://api.data.gov.sg/v1/environment/air-temperature?date_time=" + now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + now.strftime("%H") + "%3A" + now.strftime("%M") + "%3A" + now.strftime("%S")

with urllib.request.urlopen(currentDateTimeURL) as url:
    data = json.loads(url.read().decode())
    # print(data["metadata"])
    
stations = data["metadata"]["stations"]
def findIndex(index):
    for x in stations:
                                  #REPLACE WITH USER INPUT
        if stations[index]["name"] == "East Coast Parkway":
            return index
        else:
            index = index + 1
            continue

indexForData = findIndex(0)
tempToPrint = data["items"][0]["readings"][indexForData]["value"]
print("The temperature now at East Coast Parkway is " + str(tempToPrint))
