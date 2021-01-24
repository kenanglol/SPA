from home.models import Advert, User
from serviceapp.Enums import Services
from serviceapp.IDGenerator import IDGenerator as Generator


class AdvertController:
    advertisement = None
    max_price = Advert.objects.order_by("price").get().price

    def __init__(self, advid):
        try:
            self.servicadvertisement = Advert.objects.filter(advert_id=advid).get()
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def advert_add(name, price, summary, provider_id):
        guid = Generator.generate(Services.Advert)
        Advert(guid, name, price, summary, provider_id).save()

    def advert_update(self, title, price, summary):
        self.advertisement.name = title
        self.advertisement.price = price
        self.advertisement.summary = summary
        self.advertisement.save()

    def advert_delete(self):
        Advert.objects.filter(advert_id=self.advertisement.advert_id).delete()

    @staticmethod
    def get_adverts(custid, minprice=20, maxprice=(max_price + 1)):
        loc = User.objects.filter(user_id=custid).get().location
        return Advert.objects.filter(prov_id__provider_id__location=loc, price__gt=minprice, price__lt=maxprice)
