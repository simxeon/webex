from flask import Flask, request, json
from secrets import BOT_TOKEN, SMARTSHEET_TOKEN

import mySmartSheet

#import json
import requests


bot_email = "SpiffyMcSpiff@webex.bot"
bot_name = "spiffymcspiff"

# Webex variables
url = "https://api.ciscospark.com/v1/messages"
headers = {
    'Authorization': "Bearer " + BOT_TOKEN,
    'Content-Type': "application/json",
    'cache-control': "no-cache"
}


# Smart Sheet variables
sheet_id = "2089577960761220"

payload = ""
ss_headers = {
    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
    'cache-control': "no-cache",
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

   #    sendmsg(roomID)
        
        command = gettext(text).lower()
        command = (command.replace(bot_name, '')).strip()
        print (command)
        
        if command == "spiff" or command == "news" or command == "promo" or command == "services":
            sendmsg(roomID, "Current {}'s are:".format(command))
            current_spiff = get_ss_object_data(ss_search(command))
            sendmsg(roomID, current_spiff)
        else:
            return "false"

        return 'JSON posted'
    else:
        return "true"
#------------------------------------------#


def sendmsg(space, message):
    print("\nEntering sendmsg\n")
    print("{\r\n")
 
    if type(message) == list:
        mark_msg = ("#### {}".format(str(message[0][0])))
        x = 1
        while True:
            try:
                mark_msg +=("\n* {}".format(str(message[0][x])))
            except IndexError:
                break
            x += 1
#        mark_msg = ("#### {}".format(str(message[0][0])))
        payload = {"roomId": space,
                   "markdown": mark_msg}

    else:
        payload = {"roomId": space,
                   "text": message}


#    ** working code, using new format below using json **
#    payload = "{\r\n  \"roomId\" : \"" + space +"\",\r\n  \"text\" : \"Monday\"\r\n}"
#    response = requests.request("POST",url, data=payload, headers=headers)
#    print (payload)


#    headers = {
#    	    'Authorization': "Bearer " + bearer,
#    	    'Content-Type': "application/json",
#    	    'cache-control': "no-cache"
#    	    }
#   response = requests.request("POST",url, data=payload, headers=headers)
    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)
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


##################################################
#              SMARTSHEET SECTION                #
##################################################

def ss_search(text):
    url = "https://api.smartsheet.com/2.0/search/sheets/" + sheet_id
    querystring = {"query": text}
    text = text.lower()

    response = requests.request(
        "GET", url, data=payload, headers=ss_headers, params=querystring)
    response = json.loads(response.text)  # type is dict

    object_id = []
    x = 0
    while x < response["totalCount"]:
        #        print (response["results"][x]["text"])
        if response["results"][x]["text"] == text:
            object_id.append(response["results"][x]["objectId"])
            x += 1
        else:
            x += 1
#    print (object_id)
    return object_id  # type is list
    # returns the rows IDs of the keyword -- pass list to another method to process the data within


def get_ss_object_data(list_obj):
    # passes in list of rowID values based on search criteria (news, spiff, promos etc)
    combined_return = []

    for rowID in list_obj:
        url = "https://api.smartsheet.com/2.0/sheets/" + \
            sheet_id + "/rows/" + str(rowID)

        response = requests.request(
            "GET", url, data=payload, headers=ss_headers)
        response = json.loads(response.text)  # type is dict

        combined = []
        for line_item in response["cells"]:
            if "value" in line_item:  # searches if the word value exists in list
                combined.append(line_item["value"])
#        print (combined[3:]) #list
        combined_return.append(combined[3:])
    return combined_return  # list


if __name__ == "__main__":
    app.run(debug=True, port=4996)
