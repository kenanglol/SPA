from home.models import ServiceOffer, OfferSessions
from serviceapp.Enums import Services, ServiceStatus
from serviceapp.IDGenerator import IDGenerator as Generator


class OfferController:
    def offer_add(self, cusid, advertid, customerconditions, satis_id):
        guid = Generator.generate(Services.ServiceOffer)
        ServiceOffer(guid, cusid, advertid, customerconditions, satis_id, ServiceStatus.Offered).save()

    def offer_get(self, offid):
        return ServiceOffer.objects.filter(service_offer_id=offid)

    def session_add(self, offid, sessionid):
        OfferSessions(offid, sessionid)
