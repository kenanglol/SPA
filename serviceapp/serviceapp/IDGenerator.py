import datetime
from serviceapp.Enums import *
from home.models import *


class IDGenerator:
    @staticmethod
    def generate(servis):
        idcode = ''
        lastid = ""
        try:
            if servis == Services.Message:
                idcode = 'MSG'
                last_object = Message.objects.all().order_by(
                    'message_id').last()
                lastid = last_object.message_id
            elif servis == Services.Advert:
                idcode = 'ADV'
                last_object = Advert.objects.all().order_by('advert_id').last()
                lastid = last_object.advert_id
            elif servis == Services.ServiceOffer:
                idcode = 'OFF'
                last_object = ServiceOffer.objects.all().order_by(
                    'service_offer_id').last()
                lastid = last_object.service_offer_id
            elif servis == Services.User:
                idcode = 'USR'
                last_object = User.objects.all().order_by('user_id').last()
                lastid = last_object.user_id
            elif servis == Services.Session:
                idcode = 'SES'
                last_object = Schedule.objects.all().order_by(
                    'session_id').last()
                lastid = last_object.session_id
            elif servis == Services.Service:
                idcode = 'SVR'
                last_object = Service.objects.all().order_by(
                    'service_id').last()
                lastid = last_object.service_id
            return IDGenerator.generatenumber(idcode, lastid)
        except Exception as e:
            print(e)
            return IDGenerator.generatefirst(idcode)

    @staticmethod
    def generatenumber(idcode, lastid):
        obj_int = int(lastid[9:13])
        new_message_int = obj_int + 1
        new_id = idcode + str(str(datetime.date.today().year)) + str(
            datetime.date.today().month).zfill(2) + str(new_message_int).zfill(
            4)
        return new_id

    @staticmethod
    def generatefirst(idcode):
        return idcode + str(datetime.date.today().year) + str(
            datetime.date.today().month).zfill(2) + '0000'
