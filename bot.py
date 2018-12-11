from flask import Flask, request
from secrets import BOT_TOKEN

import json
import requests


bot_email = "SpiffyMcSpiff@webex.bot"
bot_name = "SpiffyMcSpiff"
bearer = BOT_TOKEN
bat_signal = "https://upload.wikimedia.org/wikipedia/en/c/c6/Bat-signal_1989_film.jpg"

url = "https://api.ciscospark.com/v1/messages"
headers = {
    'Authorization': "Bearer " + bearer,
    'Content-Type': "application/json",
    'cache-control': "no-cache"
}

app = Flask(__name__)


@app.route('/', methods=['POST'])
#------------------------------------------#
def index():
    print("-----------------------------------\n")
 #   print (request.is_json)

    content = request.get_json()
 #  print (content)
    print()
    roomID = content["data"]["roomId"]
    identity = content["data"]["personEmail"]
    text = content["data"]["id"]

    if identity != bot_email:
        # printing HTTP POST information key value pairs
        for key, value in content.items():
            print(key, ":", value)
        print("\n\n\n")
       
        sendmsg(roomID)
        print(gettext(text))

        return 'JSON posted'
    else:
        return "true"
#------------------------------------------#


def sendmsg(space):
    print("\nEntering sendmsg\n")
    print("{\r\n")


 
#    ** working code, using new format below using json **
#    payload = "{\r\n  \"roomId\" : \"" + space +"\",\r\n  \"text\" : \"Monday\"\r\n}"
#    response = requests.request("POST",url, data=payload, headers=headers)
#    print (payload)


    payload = {"roomId": space,
           "text": "Xu Mai"}


#    headers = {
#    	    'Authorization': "Bearer " + bearer,
#    	    'Content-Type': "application/json",
#    	    'cache-control': "no-cache"
#    	    }
#   response = requests.request("POST",url, data=payload, headers=headers)
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return response


def gettext(text):
    print("\n\n\n *** Entering gettext *** \n\n\n")
#    response = requests.request("GET",)
    urltext = url + "/" + text
    payload = ""

#    headers = {
#        'Authorization': "Bearer " + bearer,
#        'cache-control': "no-cache",
#    }

    response = requests.request("GET", urltext, data=payload, headers=headers)
    response = json.loads(response.text)
    return response["text"]






if __name__ == "__main__":
    app.run(debug=True, port=4996)
