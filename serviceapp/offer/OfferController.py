from home.models import ServiceOffer, OfferSessions, Schedule
from serviceapp.Enums import Services, ServiceStatus
from serviceapp.IDGenerator import IDGenerator as Generator


class OfferController:
    serviceoffer = None

    def __init__(self, offid):
        try:
            self.serviceoffer = ServiceOffer.objects.filter(service_offer_id=offid).get()
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def offer_add(cusid, advertid, customerconditions, satis_id):
        guid = Generator.generate(Services.ServiceOffer)
        ServiceOffer(guid, cusid, advertid, customerconditions, satis_id, ServiceStatus.Offered).save()

    def offer_get(self):
        return self.serviceoffer

    def session_add(self, sessionid, customerid):
        availablesession = OfferSessions(self.serviceoffer.service_offer_id, sessionid)
        Schedule.objects.fiter(session_id=sessionid).customer_id = customerid
        availablesession.save()

    def providerscore_add(self, proscore):
        self.serviceoffer.provider_performance = proscore
        self.serviceoffer.save()

    def customerscore_add(self, custscore):
        self.serviceoffer.customer_performance = custscore
        self.serviceoffer.save()

    def offer_status_change(self, servstatus):
        self.serviceoffer.status = servstatus
        self.serviceoffer.save()
