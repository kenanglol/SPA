from home.models import User, Provider, Customer
from serviceapp.IDGenerator import IDGenerator as Generator
from serviceapp.Enums import Services
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404


class UserController:
    @staticmethod
    def user_add(password, name, surname, mail, loc):
        guid = Generator.generate(Services.User)
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        hashpass = cipher_suite.encrypt(password.encode('utf-8'))
        User(guid, hashpass, key, name, surname, mail, 3, loc).save()
        return guid

    @staticmethod
    def login(email, password):
        loguser = get_object_or_404(User, mail=email)
        cipher_suite = Fernet(loguser.key)
        if password == cipher_suite.decrypt(loguser.hashpass).decode('utf-8'):
            return True
        else:
            return False


class ProviderController:
    provider = None

    def __init__(self, provid):
        try:
            self.provider = Provider.objects.filter(provider_id=provid).get()
        except Exception as e:
            print(e + "\nID ile obje bulunamadı.")

    @staticmethod
    def provider_add(password, name, surname, mail, loc, exp, spec):
        guid = UserController.user_add(password, name, surname, mail, loc)
        Provider(guid, exp, spec).save()

    def provider_update(self, mail, loc, exp):
        provider_user = User.objects.filter(user_id=self.provider.provider_id)
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
    def customer_add(password, name, surname, mail, loc):
        guid = UserController.user_add(password, name, surname, mail, loc)
        Customer(guid).save()

    def customer_update(self, mail, loc):
        customer_user = User.objects.filter(user_id=self.customer.customer_id)
        customer_user.mail = mail
        customer_user.location = loc
        customer_user.save()
