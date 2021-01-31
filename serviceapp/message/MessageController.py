from datetime import datetime
from home.models import Message, ServiceOffer, User
from datetime import datetime
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class MessageController:
    mesoffer = None

    def __init__(self, offid):
        try:
            self.mesoffer = ServiceOffer.objects.filter(pk=offid).get()
        except Exception as e:
            print(e.__str__() + "\nID ile obje bulunamadı.")

    def message_add(self, context, user_id):
        guid = Generator.generate(Services.Message)
        new_message = Message(message_id=guid,
                              context=context,
                              mesoffid=self.mesoffer,
                              sender=User.objects.filter(pk=user_id).get(),
                              sendtime=datetime.now())
        new_message.save()

    def message_getall(self):
        allmessage = Message.objects.filter(
            mesoffid=self.mesoffer.service_offer_id).order_by('sendtime')
        return allmessage

    def message_getsome(self, num):
        allmessage = self.message_getall()[:num].tolist()
        return allmessage
