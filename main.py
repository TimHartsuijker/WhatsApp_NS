import sendwhatsappmsg
import reisinformatieAPI
from tryto import trytostring

lang = "nl"
uicCode = "8400216"
maxJourneys = "2"
   
reis_informatie = reisinformatieAPI.reisinformatie(lang, uicCode, maxJourneys)

ri = reis_informatie.get_reis_informatie()

msg = ""

for sublist in ri:
    for element in sublist:
        msg += "\n" + trytostring(element)
    msg += "\n"

print(msg)

# new_message = sendwhatsappmsg.message(msg)
# new_message.sendwhatmsg_to_group_instantly()