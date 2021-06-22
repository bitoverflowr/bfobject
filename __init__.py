import json
import random

class Object:
  def __init__(self,var=None):
      self.var = var  
  

  def create(self,source,destination,command,resptype, requestdata, respcommand = None):
    self.source = source
    self.destination = destination
    self.command = command
    self.resptype = resptype
    self.requestdata = requestdata
    self.responsedata = None
    self.responsecommand = None
    self.DuplicationErrorRandomNumber =  random.randint(0,999999999999999)
    self.responsecommand = respcommand
    
    
  def format(self):
    communicate = { "source" : self.source,
                    "destination" : self.destination ,
                    "command" : self.command ,
                    "type" : self.resptype,
                    "data" : self.requestdata ,
                    "duplicateerror" : self.DuplicationErrorRandomNumber
                    }
    if self.responsecommand != None:
       communicate["responsecommand"] = self.responsecommand
    
    return json.dumps(communicate)
    
  def loads(self,string):
     jsondata = json.loads(string)
     self.source = jsondata['source']
     self.destination = jsondata['destination']
     self.command = jsondata['command']
     self.resptype = jsondata['type']
     self.requestdata = jsondata['data']
     self.responsedata = None
     self.DuplicationErrorRandomNumber = jsondata['duplicateerror']
     
     try:
        self.responsecommand = jsondata['responsecommand']
     except:
        self.responsecommand = None
     



  def Response(self,data, command = "response"):
    self.var.log("Adding response for " + self.command)
    self.responsedata = data 
    self.responsecommand = command


  def IN_DATA(self):
    return json.dumps(self.requestdata)


  
     
     
     
