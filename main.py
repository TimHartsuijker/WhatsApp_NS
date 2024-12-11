import json
import sendwhatsappmsg
import reisinformatieAPI

lang = "nl"
uicCode = "8400216"
maxJourneys = "1"
   
reis_informatie = reisinformatieAPI.reisinformatie(lang, uicCode, maxJourneys)

reis_informatie.get_reis_informatie()

new_message = sendwhatsappmsg.message(reis_informatie.get_reis_informatie())
new_message.sendwhatmsg_to_group_instantly()