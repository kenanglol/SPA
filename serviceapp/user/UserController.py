from home.models import User, Provider, Customer
from serviceapp.IDGenerator import IDGenerator as Generator
from serviceapp.Enums import Services


class ProviderController:
    provider = None

    def __init__(self, provid):
        try:
            self.provider = Provider.objects.filter(provider_id=provid).get()
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def provider_add(name, surname, mail, loc, exp, spec):
        guid = Generator.generate(Services.User)
        User(guid, name, surname, mail, 3, loc).save()
        Provider(guid, exp, spec).save()

    def provider_update(self, mail, loc, exp):
        provider_user = User.pbjects.filter(user_id=self.provider.provider_id)
        provider_user.mail = mail
        provider_user.location = loc
        provider_user.save()
        self.provider.experience = exp
        self.provider.save()


class CustomerController:
    customer = None

    def __init__(self, custid):
        try:
            self.customer = Customer.objects.filter(customer_id=custid).get()
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def customer_add(name, surname, mail, loc):
        guid = Generator.generate(Services.User)
        User(guid, name, surname, mail, 3, loc).save()
        Customer(guid).save()

    def customer_update(self, mail, loc):
        customer_user = User.pbjects.filter(user_id=self.customer.customer_id)
        customer_user.mail = mail
        customer_user.location = loc
        customer_user.save()
