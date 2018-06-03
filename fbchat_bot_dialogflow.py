from fbchat import Client, log
from fbchat.models import *
import apiai, codecs, json


class ChatBotClient(Client):
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = 'aa877a38eb264e9c867284d151dfdssd'  # replace with your DialogFlow Client access token
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de'
        self.request.session_id = '<SESSION ID, UNIQUE FOR EACH USER>'

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("Message {} from {} in {}.".format(message_object, thread_id, thread_type.name))
        self.apiaiCon()
        msgText = message_object.text
        self.request.query = msgText
        response = self.request.getresponse()
        obj = json.load(response)
        reply = obj['result']['fulfillment']['speech']
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)


client = ChatBotClient('<Your facebook email>', '<your facebook password>')
client.listen()
