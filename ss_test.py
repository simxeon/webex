from secrets import SMARTSHEET_TOKEN
from myMarshmallow import Architecture, ArchitectureSchema, Event, EventSchema
import mySmartSheet
import json
import requests
import pprint
from datetime import datetime
import time


ss_client = mySmartSheet.ss_get_client(SMARTSHEET_TOKEN)
ss_sheet = mySmartSheet.ss_get_all_sheets(ss_client)
# url = "https://api.smartsheet.com/2.0/"
sheet_id = "2089577960761220"

payload = ""
headers = {
    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
    'cache-control': "no-cache",
}


"""
# payload = ""
# headers = {
#    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
#    'cache-control': "no-cache",
#    }

# category column ID
column_id = "938033311704964"

print("\n\n----------------------------------")

url = "https://api.smartsheet.com/2.0/sheets/2089577960761220/rows/4586270930298756"

payload = ""
headers = {
    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)
response = json.loads(response.text)


sheet_response = requests.request(
    "GET", "https://api.smartsheet.com/2.0/sheets/2089577960761220/", data=payload, headers=headers)
print (type(sheet_response))
sheet_response = json.loads(sheet_response.text)
pprint.pprint(sheet_response)
print ("\n\n")
# response["cells"] = dict
# response["cells"][2] = list
# response["cells"][2]["value"] = dict
# list @ 2 =  category colum
# print (response["cells"][2]["value"])

for key, value in response.items():
    if(key == "cells"):
        val = 0
        while val < len(response["cells"]):
            print("List ID: {} : {}".format(val,response["cells"][val]))
            val += 1
    else:
        print(key, ":", value)



# print(response)
"""


def ss_search(text):
    url = "https://api.smartsheet.com/2.0/search/sheets/" + sheet_id
    querystring = {"query": text}
    text = text.lower()

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=querystring)
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
    start_time = datetime.now()
    start = int(time.time())
    print("Start script at: {0}".format(start_time))

    # passes in list of rowID values based on search criteria (news, spiff, promos etc)
    combined_return = []

    for rowID in list_obj:
        url = "https://api.smartsheet.com/2.0/sheets/" + \
            sheet_id + "/rows/" + str(rowID)
#        start_time = datetime.now()
#        start = int(time.time())
#        print ("Start script at: {0}".format(start_time))

        response = requests.request(
            "GET", url, data=payload, headers=headers)
        response = json.loads(response.text)  # type is dict


#        end_time = datetime.now()
#        end = int(time.time())
#        print("Ended script at {0}".format(end_time))
        print("\n")
        print(response["cells"])
        print("\n")
#        print (type(response["cells"]))
#        print ("\n")

        combined = []
        for line_item in response["cells"]:
            #            print (line_item)
            if "value" in line_item:  # searches if the word value exists in list
                combined.append(line_item["value"])

        combined_return.append(combined[3:])
    end_time = datetime.now()
    end = int(time.time())
    print("Ended script at {0}".format(end_time))

    print("\n")
    return combined_return  # list


def get_ss_parsed(archSelect):
    url = "https://api.smartsheet.com/2.0/sheets/2089577960761220"
    response = requests.request("GET", url, data=payload, headers=headers)
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


#print (len(get_ss_parsed("DC")))



def markdown_msg(tech_list):
    message_format = ""
    message_format += ("**{}**".format(tech_list["bullet"]))
    if bool(tech_list["bLink"]):
        message_format += ("- [LINK]({})  ".format(tech_list["bLink"]))
    else:
        message_format +=(" \n")   
    x = 1
    var = True
    while x <5 and var:
        if bool(tech_list["subBullet{}".format(x)]):
#           print (tech_list["subBullet{}".format(x)])
            message_format += ("* {}  \n".format(tech_list["subBullet{}".format(x)]))           
        if tech_list["sb{}Link".format(x)] != "":
#           print (tech_list["sb{}Link".format(x)])
            message_format += (" - [LINK]({})".format(tech_list["sb{}Link".format(x)])) 
        #else:
        #    message_format += ("asdf")
        #    var = False        
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
#                print ("\n" + tech_list["bullet"])
#                message_format += ("\n#### {}".format(tech_list["bullet"]))
#                if bool(tech_list["bLink"]):
#                    message_format += ("\n* [LINK]({})".format(tech_list["bLink"]))
#                    
#                x = 1
#                while x <5:
#                    if bool(tech_list["subBullet{}".format(x)]):
##                       print (tech_list["subBullet{}".format(x)])
#                        message_format += ("\n* {}".format(tech_list["subBullet{}".format(x)]))
#                            
#                    if tech_list["sb{}Link".format(x)] != "":
##                       print (tech_list["sb{}Link".format(x)])
#                        message_format += ("\n* [LINK]({})".format(tech_list["sb{}Link".format(x)]))
#                            
#                    x +=1
#    print (message_format)





def get_arch_info(arch):
    news = "## News  \n"
    events = "## Events\n"
    demo = "## Demostrations \n"
    services = "## Services\n"
    ea = "## EA\n"
    capital = "## Capital\n"
    promo = "## Promotions\n"
    proposal = "## Proposals\n"
    spiff = "## SPIFFS\n"
    combined = ""
    
    parsed = get_ss_parsed(arch)
   
    for list_all in parsed:
        if list_all["category"] == "news":
            news += markdown_msg(list_all)
            print (news)
        if list_all["category"] == "events":
            events += markdown_msg(list_all)
        if list_all["category"] == "demo":
            demo += markdown_msg(list_all)
        if list_all["category"] == "servives":
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


variable = get_arch_info("EN")
print (variable)

print("\n\n----------------------------------")
