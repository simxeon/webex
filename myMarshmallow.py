from marshmallow import Schema, fields, pprint, post_load

class Architecture(object):
    def __init__(self, date, arch, category, bullet, bLink, subBullet1, sb1Link, subBullet2, sb2Link, subBullet3, sb3Link, subBullet4, sb4Link, subBullet5, sb5Link, rowID):
        self.date       = date
        self.arch       = arch
        self.category   = category
        self.bullet     = bullet
        self.bLink      = bLink
        self.subBullet1 = subBullet1
        self.sb1Link    = sb1Link
        self.subBullet2 = subBullet2
        self.sb2Link    = sb2Link
        self.subBullet3 = subBullet3
        self.sb3Link    = sb3Link
        self.subBullet4 = subBullet4
        self.sb4Link    = sb4Link
        self.subBullet5 = subBullet5
        self.sb5Link    = sb5Link
        self.rowID      = rowID
    
    def __repr__(self):
        return "rowID: {} , date: {}  , bullet: {}".format(str(self.rowID), self.date, self.bullet)


class ArchitectureSchema(Schema):
    date        = fields.String()
    arch        = fields.String()
    category    = fields.String()
    bullet      = fields.String()
    bLink       = fields.String()
    subBullet1  = fields.String()
    sb1Link     = fields.String()
    subBullet2  = fields.String()
    sb2Link     = fields.String()
    subBullet3  = fields.String()
    sb3Link     = fields.String()
    subBullet4  = fields.String()
    sb4Link     = fields.String()
    subBullet5  = fields.String()
    sb5Link     = fields.String()
    rowID       = fields.Integer()

    @post_load
    def createArchitecture(self, data):
        return Architecture(**data) 



class Event(object):
    def __init__(self, date, arch, region, city, address, content, summary, reg, email, rowID):
        self.date       = date
        self.arch       = arch
        self.region     = region
        self.city       = city
        self.address    = address
        self.content    = content
        self.summary    = summary
        self.reg        = reg
        self.email      = email
        self.rowID      = rowID
    
    def __repr__(self):
        return "rowID: {} , date: {}  , summary: {}".format(str(self.rowID), self.date, self.summary)

        #reset all vars to empty for each row loop


class EventSchema(Schema):
    date       = fields.String()
    arch       = fields.String()
    region     = fields.String()
    city       = fields.String()
    address    = fields.String()
    content    = fields.String()
    summary    = fields.String()
    reg        = fields.String()
    email      = fields.String()
    rowID      = fields.Integer()

    @post_load
    def createEvent(self, data):
        return Event(**data) 

class areaEvents(object):
    def __init__(self,amcID,eventName,area,eventDate,status,quarter,city,state,arch,vertical,eventType,lead,segment, localContact, eventLead,comment,regReport,regReportPass,url ):
        
        self.amcID      = amcID
        self.eventName  = eventName
        self.area       = area
        self.eventDate  = eventDate     
        self.status     = status
        self.quarter    = quarter
        self.city       = city    
        self.state      = state
        self.arch       = arch    
        self.vertical   = vertical
        self.eventType  = eventType
        self.lead       = lead
        self.segment    = segment
        self.localContact = localContact
        self.eventLead  = eventLead
        self.comment    = comment
        self.regReport  = regReport
        self.regReportPass = regReportPass
        self.url        = url  

class areaEventSchema(Schema):
    amcID           = fields.String()
    eventName       = fields.String()
    area            = fields.String()
    eventDate       = fields.String()
    status          = fields.String()
    quarter         = fields.String()
    city            = fields.String()
    state           = fields.String()
    arch            = fields.String()
    vertical        = fields.String()
    eventType       = fields.String()
    comment         = fields.String()
    lead            = fields.String()
    segment         = fields.String()
    localContact    = fields.String()
    eventLead       = fields.String()
    regReport       = fields.String()
    regReportPass   = fields.String()
    url             = fields.String()
    

#ss_dict = {'date':date,'internal':internal,'category':category,etc}
#schema = ArchitectureSchema()
#archResult = schema.load(ss_dict)