from datetime import datetime
import time

#convert system date time
present = datetime.now()
present = str(present)
present = present.split()
present = present[0].split("-")

#present = present.split("-")
eventDate = ["2018", "12", "10"]
present = "{}/{}/{}".format(present[1],present[2],present[0])
eventDate = "{}/{}/{}".format(eventDate[1],eventDate[2],eventDate[0])

print (present)
print (eventDate)


a = datetime.strptime(present, "%m/%d/%Y")
b = datetime.strptime(eventDate, "%m/%d/%Y")
print (b <a )
