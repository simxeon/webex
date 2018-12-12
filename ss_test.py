from secrets import SMARTSHEET_TOKEN
import mySmartSheet
import json
import requests
import pprint


ss_client = mySmartSheet.ss_get_client(SMARTSHEET_TOKEN)
ss_sheet = mySmartSheet.ss_get_all_sheets(ss_client)
#url = "https://api.smartsheet.com/2.0/"
sheet_id = "2089577960761220"

payload = ""
headers = {
       'Authorization': "Bearer "+ SMARTSHEET_TOKEN,
       'cache-control': "no-cache",
       }


"""
#payload = ""
#headers = {
#    'Authorization': "Bearer " + SMARTSHEET_TOKEN,
#    'cache-control': "no-cache",
#    }

#category column ID
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


sheet_response = requests.request("GET", "https://api.smartsheet.com/2.0/sheets/2089577960761220/", data=payload, headers=headers)
print (type(sheet_response))
sheet_response = json.loads(sheet_response.text)
pprint.pprint(sheet_response)
print ("\n\n")
#response["cells"] = dict
#response["cells"][2] = list
#response["cells"][2]["value"] = dict
#list @ 2 =  category colum
#print (response["cells"][2]["value"])

for key, value in response.items():
    if(key == "cells"):
        val = 0
        while val < len(response["cells"]):
            print("List ID: {} : {}".format(val,response["cells"][val]))
            val += 1
    else:
        print(key, ":", value)



#print(response)
"""


def ss_search(text):
    url = "https://api.smartsheet.com/2.0/search/sheets/"+ sheet_id
    querystring = {"query": text}
    text = text.lower()

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    response = json.loads(response.text) #type is dict
    
    object_id = []
    x = 0
    while x < response["totalCount"]:
#        print (response["results"][x]["text"])
        if response["results"][x]["text"] == text:
            object_id.append(response["results"][x]["objectId"])
            x +=1
        else:
            x+=1
#    print (object_id)
    return object_id #type is list
    #returns the rows IDs of the keyword -- pass list to another method to process the data within

ss_search("spiff")

def get_ss_object_data(list_obj):
#passes in list of rowID values based on search criteria (news, spiff, promos etc)
    combined_return = []

    for rowID in list_obj:
        url = "https://api.smartsheet.com/2.0/sheets/" + sheet_id + "/rows/" + str(rowID)

        response = requests.request("GET", url, data=payload, headers=headers)
        response = json.loads(response.text) #type is dict

#       print (type(response["cells"])) #type is list
#       print (response["cells"][3]) #type is dict
#       print (response["cells"][3]["value"]) #type is string
#       print (bool(response["cells"][3]["value"]))
#        print (response["cells"])
#        print (response["cells"][3])
#        print ("Length " + str(len(response["cells"][3])))


        combined = []
        for line_item in response["cells"]:
            if "value" in line_item:
                combined.append(line_item["value"])
#        print (combined[3:]) #list
        combined_return.append(combined[3:])
    return combined_return #list





object_data = get_ss_object_data(ss_search("promo"))


for item in object_data:
    print ("\n")
    x = 0
    while x < len(item):
        print (item[x])
        x +=1
    
    








print ("\n\n----------------------------------")
