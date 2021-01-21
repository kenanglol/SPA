from home.models import ServiceSatisfaction
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class SatisfactionController:
    def satisfaction_add(self, offid, pro_score=None, cus_score=None):
        guid = Generator.generate(Services.ServiceSatisfaction)
        ServiceSatisfaction(guid, offid, pro_score, cus_score).save()

    def satisfaction_get(self, sat_id):
        return ServiceSatisfaction.objects.filter(service_satisfaction_id=sat_id)

    def satisfaction_get(self, offid):
        return ServiceSatisfaction.objects.filter(off_id=offid)
