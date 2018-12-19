from secrets import SMARTSHEET_TOKEN, BOT_TOKEN
from myMarshmallow import Architecture, ArchitectureSchema, Event, EventSchema, areaEvents, areaEventSchema
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
eventSheet = "2175182816208772"

payload = ""
headers = {
    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
    'cache-control': "no-cache",
}

url = "https://api.ciscospark.com/v1/messages"


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

def sendmsg(message):
    headers = {
    'Authorization': "Bearer " + BOT_TOKEN,
    'Content-Type': "application/json",
    'cache-control': "no-cache"
}
    payload = {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjBlMDFmOTAtZjRiYy0xMWU4LWE0ZTMtNTlkNDY3MzRlY2Y1","markdown": message}
    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)
    
    return response

#Y2lzY29zcGFyazovL3VzL1JPT00vZDMxNjMxMzEtZDA5Mi0zYTdmLWE2OWQtN2RjZWIwMGQ5MThh 1:1 room
#Y2lzY29zcGFyazovL3VzL1JPT00vNjBlMDFmOTAtZjRiYy0xMWU4LWE0ZTMtNTlkNDY3MzRlY2Y1


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










##################################################
#                  Area Events                   #
##################################################



def get_ss_area(stateSel):
    url = "https://api.smartsheet.com/2.0/sheets/489009441990532"
    response = requests.request("GET", url, data=payload, headers=headers)
    response = json.loads(response.text)
    
    stateSel.upper()
    
    AK_list = []
    AL_list = []
    AR_list = []
    AZ_list = []
    CA_list = []
    CO_list = []
    CT_list = []
    DC_list = []
    DE_list = []
    FL_list = []
    GA_list = []
    GU_list = []
    HI_list = []
    IA_list = []
    ID_list = []
    IL_list = []
    IN_list = []
    KS_list = []
    KY_list = []
    LA_list = []
    MA_list = []
    MD_list = []
    ME_list = []
    MH_list = []
    MI_list = []
    MN_list = []
    MO_list = []
    MS_list = []
    MT_list = []
    NC_list = []
    ND_list = []
    NE_list = []
    NH_list = []
    NJ_list = []
    NM_list = []
    NV_list = []
    NY_list = []
    OH_list = []
    OK_list = []
    OR_list = []
    PA_list = []
    PR_list = []
    PW_list = []
    RI_list = []
    SC_list = []
    SD_list = []
    TN_list = []
    TX_list = []
    UT_list = []
    VA_list = []
    VI_list = []
    VT_list = []
    WA_list = []
    WI_list = []
    WV_list = []
    WY_list = []
    virt_list =[]

    for x in response['rows']:
        # print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
        # reset all vars to empty for each row loop
        amcID = ""
        eventName = ""
        area = ""
        eventDate = ""
        status = ""
        quarter = "" 
        city = ""
        state = ""
        arch = ""
        vertical = ""
        eventType = ""
        lead = ""
        segment = ""
        localContact = ""
        eventLead = ""
        comment = ""
        regReport = ""
        regReportPass = ""
        url = ""
        for i in x['cells']:
            if 'value' in i:
                # print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
                if i['columnId'] == 4914842529228676:
                    amcID = i['value']
                # if i['columnId'] == 8256382706182020:
                #    internal = i['value']
                if i['columnId'] == 4193604173358980:
                    eventName = i['value']
                if i['columnId'] == 8697203800729476:
                    area = i['value']
                if i['columnId'] == 2481664568911748:
                    eventDate = i['value']
                if i['columnId'] == 2964285748995972:
                    status = i['value']
                if i['columnId'] == 4409256964319108:
                    quarter = i['value']
                if i['columnId'] == 7289828917176196:
                    try:
                        city = i['value']
                    except KeyError:
                        city = " "
                if i['columnId'] == 6985264196282244:
                    try:
                        state = i['value']
                    except KeyError:
                        state = ""
                if i['columnId'] == 2786229289805700:
                    arch = i['value']
                if i['columnId'] == 992286747191172:
                    vertical = i['value']
                if i['columnId'] == 5859364289439620:
                    eventType = i['value']
                if i['columnId'] == 5296414336018308:
                    lead = i['value']
                if i['columnId'] == 6589440010282884:
                    segment = i['value']
                if i['columnId'] == 3607564475754372:
                    try:
                        localContact = i['value']
                    except KeyError:
                        localContact = ""
                if i['columnId'] == 184410042591108:  # arch
                    try:
                        eventLead = i['value']
                    except KeyError:
                        eventLead = ""
                if i['columnId'] == 3547617704601476:  # arch
                    try:
                        comment = i['value']
                    except KeyError:
                        comment = ""
                if i['columnId'] == 4275694881531780:  # arch
                    try:
                        regReport = i['value']
                    except KeyError:
                        regReport = ""
                if i['columnId'] == 8779294508902276:  # arch
                    try:
                        regReportPass = i['value']
                    except KeyError:
                        regReportPass = ""
                if i['columnId'] == 1473495319242628:  # arch
                    try:
                        url = i['value']
                    except KeyError:
                        url = ""
         
    
        areaObject = areaEvents(amcID,eventName,area,eventDate,status,quarter,city,state,arch,vertical,eventType,lead,segment,localContact,eventLead,comment,regReport, regReportPass, url)
        schema = areaEventSchema()
        areaDict, errors = schema.dump(areaObject)
        
        if state == "AK":
            AK_list.append(areaDict)
        elif state == "AL":
            AL_list.append(areaDict)
        elif state == "AR":
            AR_list.append(areaDict)
        elif state == "AZ":
            AZ_list.append(areaDict)
        elif state == "CA":
            CA_list.append(areaDict)
        elif state == "CO":
            CO_list.append(areaDict)
        elif state == "CT":
            CT_list.append(areaDict)
        elif state == "DC":
            DC_list.append(areaDict)
        elif state == "DE":
            DE_list.append(areaDict)
        elif state == "FL":
            FL_list.append(areaDict)
        elif state == "GA":
            GA_list.append(areaDict)
        elif state == "GU":
            GU_list.append(areaDict)
        elif state == "HI":
            HI_list.append(areaDict)
        elif state == "IA":
            IA_list.append(areaDict)
        elif state == "ID":
            ID_list.append(areaDict)
        elif state == "IL":
            IL_list.append(areaDict)
        elif state == "IN":
            IN_list.append(areaDict)
        elif state == "KS":
            KS_list.append(areaDict)
        elif state == "KY":
            KY_list.append(areaDict)
        elif state == "LA":
            LA_list.append(areaDict)
        elif state == "MA":
            MA_list.append(areaDict)
        elif state == "MD":
            MD_list.append(areaDict)
        elif state == "ME":
            ME_list.append(areaDict)
        elif state == "MH":
            MH_list.append(areaDict)
        elif state == "MI":
            MI_list.append(areaDict)
        elif state == "MN":
            MN_list.append(areaDict)
        elif state == "MO":
            MO_list.append(areaDict)
        elif state == "MS":
            MS_list.append(areaDict)
        elif state == "MT":
            MT_list.append(areaDict)
        elif state == "NC":
            NC_list.append(areaDict)
        elif state == "ND":
            ND_list.append(areaDict)
        elif state == "NE":
            NE_list.append(areaDict)
        elif state == "NH":
            NH_list.append(areaDict)
        elif state == "NJ":
            NJ_list.append(areaDict)
        elif state == "NM":
            NM_list.append(areaDict)
        elif state == "NV":
            NV_list.append(areaDict)
        elif state == "NY":
            NY_list.append(areaDict)
        elif state == "OH":
            OH_list.append(areaDict)
        elif state == "OK":
            OK_list.append(areaDict)
        elif state == "OR":
            OR_list.append(areaDict)
        elif state == "PA":
            PA_list.append(areaDict)
        elif state == "PR":
            PR_list.append(areaDict)
        elif state == "PW":
            PW_list.append(areaDict)
        elif state == "RI":
            RI_list.append(areaDict)
        elif state == "SC":
            SC_list.append(areaDict)
        elif state == "SD":
            SD_list.append(areaDict)
        elif state == "TN":
            TN_list.append(areaDict)
        elif state == "TX":
            TX_list.append(areaDict)
        elif state == "UT":
            UT_list.append(areaDict)
        elif state == "VA":
            VA_list.append(areaDict)
        elif state == "VI":
            VI_list.append(areaDict)
        elif state == "VT":
            VT_list.append(areaDict)
        elif state == "WA":
            WA_list.append(areaDict)
        elif state == "WI":
            WI_list.append(areaDict)
        elif state == "WV":
            WV_list.append(areaDict)
        elif state == "WY":
                WY_list.append(areaDict)
        elif eventType == "Virtual":
            virt_list.append(areaDict)
            
            


    if stateSel == "AK":
        return AK_list
    elif stateSel == "AL":
        return AL_list
    elif stateSel == "AR":
        return AR_list
    elif stateSel == "AZ":
        return AZ_list
    elif stateSel == "CA":
        return CA_list
    elif stateSel == "CO":
        return CO_list
    elif stateSel == "CT":
        return CT_list
    elif stateSel == "DC":
        return DC_list
    elif stateSel == "DE":
        return DE_list
    elif stateSel == "FL":
        return FL_list
    elif stateSel == "GA":
        return GA_list
    elif stateSel == "GU":
        return GU_list
    elif stateSel == "HI":
        return HI_list
    elif stateSel == "IA":
        return IA_list
    elif stateSel == "ID":
        return ID_list
    elif stateSel == "IL":
        return IL_list
    elif stateSel == "IN":
        return IN_list
    elif stateSel == "KS":
        return KS_list
    elif stateSel == "KY":
        return KY_list
    elif stateSel == "LA":
        return LA_list
    elif stateSel == "MA":
        return MA_list
    elif stateSel == "MD":
        return MD_list
    elif stateSel == "ME":
        return ME_list
    elif stateSel == "MH":
        return MH_list
    elif stateSel == "MI":
        return MI_list
    elif stateSel == "MN":
        return MN_list
    elif stateSel == "MO":
        return MO_list
    elif stateSel == "MS":
        return MS_list
    elif stateSel == "MT":
        return MT_list
    elif stateSel == "NC":
        return NC_list
    elif stateSel == "ND":
        return ND_list
    elif stateSel == "NE":
        return NE_list
    elif stateSel == "NH":
        return NH_list
    elif stateSel == "NJ":
        return NJ_list
    elif stateSel == "NM":
        return NM_list
    elif stateSel == "NV":
        return NV_list
    elif stateSel == "NY":
        return NY_list
    elif stateSel == "OH":
        return OH_list
    elif stateSel == "OK":
        return OK_list
    elif stateSel == "OR":
        return OR_list
    elif stateSel == "PA":
        return PA_list
    elif stateSel == "PR":
        return PR_list
    elif stateSel == "PW":
        return PW_list
    elif stateSel == "RI":
        return RI_list
    elif stateSel == "SC":
        return SC_list
    elif stateSel == "SD":
        return SD_list
    elif stateSel == "TN":
        return TN_list
    elif stateSel == "TX":
        return TX_list
    elif stateSel == "UT":
        return UT_list
    elif stateSel == "VA":
        return VA_list
    elif stateSel == "VI":
        return VI_list
    elif stateSel == "VT":
        return VT_list
    elif stateSel == "WA":
        return WA_list
    elif stateSel == "WI":
        return WI_list
    elif stateSel == "WV":
        return WV_list
    elif stateSel == "WY":
        return WY_list
    elif stateSel == "ALL":
        return AK_list,AL_list,AR_list,AZ_list,CA_list,CO_list,CT_list,DC_list,DE_list,FL_list,GA_list,GU_list,HI_list,IA_list,ID_list,IL_list,IN_list,KS_list,KY_list,LA_list,MA_list,MD_list,ME_list,MH_list,MI_list,MN_list,MO_list,MS_list,MT_list,NC_list,ND_list,NE_list,NH_list,NJ_list,NM_list,NV_list,NY_list,OH_list,OK_list,OR_list,PA_list,PR_list,PW_list,RI_list,SC_list,SD_list,TN_list,TX_list,UT_list,VA_list,VI_list,VT_list,WA_list,WI_list,WV_list,WY_list


"""
# Should make get_ss_area(state) a global variable and pass it into methods. #
"""

#########################
parsed = get_ss_area("TX") #change tx to command inputted
# if user inputs city -- google serch correct spelling?
# if user inputs city -- 
#########################

def get_state_info_slim(state):
    msg = ("## Events in {}\n".format(state))

    
#    print ("\n # of events in {} are {}".format(state, len(parsed)))
    temp_city = []
    city_list = [] #purged list of cities
    stateEvents = ""

    #Grabs city name from all events in the desired state
    for get_city in parsed:
        temp_city.append(get_city["city"].lower())
    #Purges duplicate cities
    for c in temp_city:
        if c not in city_list:
            city_list.append(c)
    
#    city_list.append("virtual")
#    print(parsed)

    for city_name in city_list: #Houston
        if city_name == "virtual":
            stateEvents += "\n\n*** \n## {}\n***".format(city_name.title())
        else:
            stateEvents += "\n\n*** \n## {}, {}\n***".format(city_name.title(),state)

        for events in parsed:
            if events["city"].lower() == city_name:
                stateEvents += markdown_event(events)
            elif events["eventType"].lower() == "virtual": #elif
                stateEvents += markdown_event(events)

    
    return stateEvents

def get_city_event(city):
    return True


def markdown_event(event):
    message_format = ""
#    print("--------------")
#    print("Printing event info: \n {}".format(event))
    eDate = event["eventDate"].split("-")
    eDate = "{}/{}/{}".format(eDate[1],eDate[2],eDate[0])
    
    present = datetime.now()
    present = str(present)
    present = present.split()
    present = present[0].split("-")
    present = "{}/{}/{}".format(present[1],present[2],present[0])

    a = datetime.strptime(present, "%m/%d/%Y")
    b = datetime.strptime(eDate, "%m/%d/%Y")

    if b < a:
        return message_format #checks to see if events are in past, True = do not process
    if event["status"] == "Cancelled":
        return message_format
       
        
    if bool(event["url"]):
        if "https://" not in event["url"]:
            if "http://" in event["url"]:
                url = event["url"].replace("http://","https://")
                event["url"] = url
            else:
                url = "https://{}".format(event["url"])
                event["url"] = url

        message_format += ("\n\n**{} - [Reg Link]({})**".format(event["eventName"], event["url"]))
    else:
        message_format += ("\n\n**{}**".format(event["eventName"]))

    message_format += ("\n * **Date** : {}  ".format(eDate))
    message_format += ("\n * **Tech** : {}  ".format(event["arch"]))
    message_format += ("\n * **Type** : {}      [Live/Virtual/Hybrid]  ".format(event["eventType"]))
    message_format += ("\n * **Status** : {}  ".format(event["status"]))
    try:
        if event["eventLead"] == " ":
            return message_format
        else:
            message_format += ("\n * **Contact** : {}  ".format(event["eventLead"]))
        
    except KeyError:
        message_format += ("\n * **Contact** : N/A")

    return message_format


events = get_state_info_slim("TX")
sendmsg(events)






"""
Slim output
<State> Events
## Austin
* arch 
    * eventName - eventDate
    * url (registration link)
    * event type
    * status

Sample output

Houston
* Data Center
    * Application Agility and Cloud Workload Protection -- 1/15/2019 --> possible could turn event name into hyperlink
    * Registation -- hyperlink <url>
    * Live (Live/Virtual/Hybrid)
    * <status> (Confirmed/Cancelled)
* Security
    * Firepower Test Drive - 1/1/1
    * Registration -- hyperlink <url>
    * Hybrid -- Live + Virtual
    * <status>

Austin

"""



def get_state_info_detailed(state):
    return True