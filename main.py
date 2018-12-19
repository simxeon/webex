from flask import Flask, request, json
from secrets import BOT_TOKEN, SMARTSHEET_TOKEN
from datetime import datetime 
import time
from myMarshmallow import Architecture, ArchitectureSchema, Event, EventSchema

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
#        print (command)
        if command in ("spiff","news","promo","services","partner","capital"):
            
            sendmsg(roomID, "Current {}'s items are:".format(command))
            current_spiff = get_message_format(command)
            sendmsg(roomID, current_spiff)
        if command in ("en","dc","collab","sec","security", "data center", "datacenter"):
            if command == "security":
                command = "sec"
            if command in ("data center","datacenter"):
                command = "dc"
            arch = get_arch_info(command)
            sendmsg(roomID,arch)    
            
        else:
            return "false"

        return 'JSON posted'
    else:
        return "true"
#------------------------------------------#


def sendmsg(space, message):
    payload = {"roomId": space,"markdown": message}
    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)
    
    return response


def gettext(text):
    urltext = url + "/" + text
    payload = ""

    response = requests.request("GET", urltext, data=payload, headers=headers)
    response = json.loads(response.text)
    print ("Message to bot : {}\n\n".format(response["text"]))
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
        if response["results"][x]["text"] == text:
            object_id.append(response["results"][x]["objectId"])
            x += 1
        else:
            x += 1
    return object_id  # type is list
    # returns the rows IDs of the keyword -- pass list to another method to process the data within


def get_ss_object_data(list_obj):
 #   start_time = datetime.now()
 #   start = int(time.time())
 #   print ("Start script at: {0}".format(start_time))

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

        combined_return.append(combined[3:])
#    end_time = datetime.now()
#    end = int(time.time())
#    print("Ended script at {0}".format(end_time))
    return combined_return  # list


def get_ss_parsed(archSelect):
    url = "https://api.smartsheet.com/2.0/sheets/{}".format(sheet_id)
    response = requests.request("GET", url, data=payload, headers=ss_headers)
    response = json.loads(response.text)

    EN_list = []
    SEC_list = []
    DC_list = []
    COLLAB_list = []
    APP_list = []

    for x in response['rows']:
        # print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
        # reset all vars to empty for each row loop
        date = ""
        arch = ""
        # internal    = ""
        category = ""
        bullet = ""
        bLink = ""
        subBullet1 = ""
        sb1Link = ""
        subBullet2 = ""
        sb2Link = ""
        subBullet3 = ""
        sb3Link = ""
        subBullet4 = ""
        sb4Link = ""
        subBullet5 = ""
        sb5Link = ""
        rowID = x['id']

        for i in x['cells']:
            if 'value' in i:
                # print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
                if i['columnId'] == 6004582892496772:
                    date = i['value']
                # if i['columnId'] == 8256382706182020:
                #    internal = i['value']
                if i['columnId'] == 938033311704964:
                    category = i['value']
                if i['columnId'] == 5441632939075460:
                    bullet = i['value']
                if i['columnId'] == 3189833125390212:
                    bLink = i['value']
                if i['columnId'] == 425317295777668:
                    subBullet1 = i['value']
                if i['columnId'] == 8588091620386692:
                    sb1Link = i['value']
                if i['columnId'] == 4084491993016196:
                    subBullet2 = i['value']
                if i['columnId'] == 6336291806701444:
                    sb2Link = i['value']
                if i['columnId'] == 1832692179330948:
                    subBullet3 = i['value']
                if i['columnId'] == 7462191713544068:
                    sb3Link = i['value']
                if i['columnId'] == 2958592086173572:
                    subBullet4 = i['value']
                if i['columnId'] == 5210391899858820:
                    sb4Link = i['value']
                if i['columnId'] == 706792272488324:
                    subBullet5 = i['value']
                if i['columnId'] == 8025141666965380:
                    sb5Link = i['value']
                if i['columnId'] == 3752783078811524:  # arch
                    arch = i['value']

        archObject = Architecture(date,arch,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link, rowID)
        schema = ArchitectureSchema()
        archDict, errors = schema.dump(archObject)

        if arch == 'EN':
            EN_list.append(archDict)    
        elif arch == 'SEC':
            SEC_list.append(archDict)  
        elif arch == 'DC':
            DC_list.append(archDict)  
        elif arch == 'COLLAB':
            COLLAB_list.append(archDict)  
        elif arch == 'APP':
            APP_list.append(archDict)


    if archSelect == 'EN':
        return EN_list
    elif archSelect == 'SEC':
        return SEC_list
    elif archSelect == 'DC':
        return DC_list
    elif archSelect == 'COLLAB':
        return COLLAB_list
    elif archSelect == 'APP':
        return APP_list
    elif archSelect == 'ALL':
        return EN_list, SEC_list, DC_list, COLLAB_list, APP_list



def markdown_msg(tech_list):
    message_format = ""
    message_format += ("* **{}**".format(tech_list["bullet"]))
    if bool(tech_list["bLink"]):
        message_format += ("- [LINK]({})  ".format(tech_list["bLink"]))
    else:
        message_format +=(" \n")   
    x = 1
    var = True
    while x <5 and var:
        if bool(tech_list["subBullet{}".format(x)]):
            if x == 1:
                message_format += ("\n    * {}".format(tech_list["subBullet{}".format(x)]))
            else:
                message_format += ("\n    * {}  \n".format(tech_list["subBullet{}".format(x)]))            
        if tech_list["sb{}Link".format(x)] != "":
            if x == 1:
                message_format += (" - [LINK]({})  \n".format(tech_list["sb{}Link".format(x)]))
            else:
                message_format += (" - [LINK]({})".format(tech_list["sb{}Link".format(x)]))    
        x +=1
    message_format += ("\n")
    return message_format



def get_message_format(text):
    message_format = ""
    
    for list_all in get_ss_parsed("ALL"):
        for tech_list in list_all:
            if tech_list["category"] == text:
                message_format += markdown_msg(tech_list)
    return message_format

def get_arch_info(arch):
    news = "## *_- News - _*\n"
    events = "## *_- Events - _*\n"
    demo = "## *_- Demos - _*\n"
    services = "## *_- Services - _*\n"
    ea = "## *_- EA - _(internal)*\n"
    capital = "## *_- Capital - _(internal)*\n"
    promo = "## *_-Promotions - _(internal)*\n"
    proposal = "## *_- Proposals - _(internal)*\n"
    spiff = "## *_- SPIFFS - _(internal)*\n"
    combined = ""
    
    var = arch.upper()
    parsed = get_ss_parsed("{}".format(var))
    
    
    for list_all in parsed:
        if list_all["category"] == "news":
            news += markdown_msg(list_all)
        if list_all["category"] == "events":
            events += markdown_msg(list_all)
        if list_all["category"] == "demo":
            demo += markdown_msg(list_all)
        if list_all["category"] == "services":
            services += markdown_msg(list_all)
        if list_all["category"] == "ea":
            ea += markdown_msg(list_all)
        if list_all["category"] == "capital":
            capital += markdown_msg(list_all)
        if list_all["category"] == "promo":
            promo += markdown_msg(list_all)
        if list_all["category"] == "proposal":
            proposal += markdown_msg(list_all)
        if list_all["category"] == "spiff":
            spiff += markdown_msg(list_all)
    combined = ("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(news,events,demo,services,ea,capital,promo,proposal,spiff))
    return combined


#sendmsg("Y2lzY29zcGFyazovL3VzL1JPT00vZDMxNjMxMzEtZDA5Mi0zYTdmLWE2OWQtN2RjZWIwMGQ5MThh", get_arch_info("EN"))



if __name__ == "__main__":
    app.run(debug=True, port=4996)
