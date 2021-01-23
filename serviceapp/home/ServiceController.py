from home.models import Service
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class ServiceController:
    @staticmethod
    def service_add(name, summary, category):
        guid = Generator.generate(Services.Service)
        Service(guid, name, summary, category).save()

    @staticmethod
    def service_get_by_category(self, category):
        Service.objects.filter(category=category)
