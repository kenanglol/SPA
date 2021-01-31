from home.models import Service


class ServiceController:
    @staticmethod
    def service_add(name, summary, category):
        Service(name, summary, category).save()

    @staticmethod
    def service_get_by_category(category):
        return Service.objects.filter(category=category)
