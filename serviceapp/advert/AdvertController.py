from home.models import Advert, User, Provider
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class AdvertController:
    advertisement = None
    max_price = 0

    def __init__(self, advid):
        try:
            self.servicadvertisement = Advert.objects.filter(advert_id=advid).get()
            if not Advert.objects.all():
                self.max_price = Advert.objects.order_by("price").first().price
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def advert_add(name, price, summary, provider_id):
        guid = Generator.generate(Services.Advert)
        prov = Provider.objects.filter(provider_id=provider_id).get()
        spec = prov.speciality
        Advert(guid, name, price, summary, provider_id, spec).save()

    def advert_update(self, title, price, summary):
        self.advertisement.name = title
        self.advertisement.price = price
        self.advertisement.summary = summary
        self.advertisement.save()

    def advert_delete(self):
        Advert.objects.filter(advert_id=self.advertisement.advert_id).delete()

    @staticmethod
    def get_adverts(custid, subservice, minprice=20, maxprice=(max_price + 1)):
        loc = User.objects.filter(user_id=custid).get().location
        return Advert.objects.filter(prov_id__provider_id__location=loc, price__gt=minprice, price__lt=maxprice,
                                     advert_service=subservice)

    def get_advert(self):
        return self.advertisement
