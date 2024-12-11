from private import *
import pywhatkit
from tryto import trytostring

class message():

    def __init__(self, message):
        self.GroupId = WhatsApp_GroupId_tw
        self.message = message

    
    def sendwhatmsg_to_group_instantly(self):
        pywhatkit.sendwhatmsg_to_group_instantly(trytostring(self.GroupId), trytostring(self.message))