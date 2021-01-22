from home.models import Message, User
from django.utils import timezone
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class MessageController:
    def message_add(self, context, sender):
        guid = Generator.generate(Services.Message)
        Message(guid, context, timezone.now,
                sender.id).save()

    def message_add(self, context, id):
        guid = Generator.generate(Services.Message)
        Message(guid, context, id).save()

    def message_getsome(self):
        allmessage = Message.objects.all()
        return allmessage

    def message_getall(self, num):
        allmessage = Message.objects.order_by('sendtime')[:num].get()
        return allmessage
