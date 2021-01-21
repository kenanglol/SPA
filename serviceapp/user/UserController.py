from home.models import User
from serviceapp.IDGenerator import IDGenerator as Generator
from serviceapp.Enums import Services


class UserController:
    def user_add(self, name, surname, mail, score=0):
        guid = Generator.generate(Services.User)
        User(guid, name, surname, mail, score).save()
