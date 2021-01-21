from django.db import models
from django.utils import timezone


class Service(models.Model):
    service_id = models.CharField(primary_key=True,
                                  max_length=20,
                                  db_column='SERVICEID')
    service_name = models.CharField(max_length=20,
                                    db_column='SERVICENAME',
                                    null=False)
    summary = models.CharField(max_length=500, db_column='SERVSUMMARY')
    category = models.CharField(max_length=20,
                                null=False,
                                db_column='CATEGORY',
                                default="Undefined")

    class Meta:
        db_table = "SERVICE"


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20, db_column='GUID')
    name = models.CharField(max_length=30, db_column='NAME', null=False)
    surname = models.CharField(max_length=30, null=False)
    mail = models.EmailField(db_column='MAIL', null=False)
    score = models.FloatField(db_column='USER_SCORE', default=0)

    class Meta:
        db_table = "USER"


class Customer(models.Model):
    customer_id = models.OneToOneField(User,
                                       primary_key=True,
                                       max_length=20,
                                       db_column='CUSID',
                                       on_delete=models.CASCADE)

    class Meta:
        db_table = "CUSTOMER"


class Provider(models.Model):
    provider_id = models.OneToOneField(User,
                                       primary_key=True,
                                       max_length=20,
                                       db_column='PROID',
                                       on_delete=models.CASCADE)
    location = models.CharField(max_length=100,
                                db_column='LOCATION',
                                null=False)
    experience = models.IntegerField(db_column='EXP')

    speciality = models.ForeignKey(Service,
                                   db_column='SPECIALITYID',
                                   null=False,
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = "PROVIDER"


class Advert(models.Model):
    advert_id = models.CharField(primary_key=True,
                                 max_length=20,
                                 db_column='ADVERTID')
    advert_name = models.CharField(max_length=100,
                                   db_column='ADVERTNAME',
                                   null=False)
    price = models.IntegerField(db_column='PRICE', null=False)
    summary = models.CharField(max_length=500, db_column='ADVSUMMARY')
    prov_id = models.ForeignKey(Provider,
                                max_length=20,
                                db_column='PROVID',
                                on_delete=models.CASCADE)

    class Meta:
        db_table = "ADVERT"


class ServiceOffer(models.Model):
    service_offer_id = models.CharField(primary_key=True,
                                        max_length=20,
                                        db_column='SERVICEOFFID')
    purchaser = models.ForeignKey(Customer,
                                  db_column='PURCHASERID',
                                  null=False,
                                  on_delete=models.CASCADE)
    adver_id = models.ForeignKey(Advert,
                                 db_column='ADVERID',
                                 null=False,
                                 on_delete=models.CASCADE)
    customer_conditions = models.CharField(max_length=100,
                                           db_column='CUSTOMERCOND',
                                           null=False)
    satisfaction_id = models.CharField(max_length=20,
                                       db_column='SATISFACTIONID',
                                       null=False)
    status = models.CharField(max_length=10,
                              null=False,
                              db_column='STATUS',
                              default="Undetermined")

    class Meta:
        db_table = "SERVICEOFFER"


class Schedule(models.Model):
    session_id = models.CharField(primary_key=True,
                                  max_length=20,
                                  db_column='SESSIONID')
    expert_id = models.ForeignKey(Provider,
                                  max_length=20,
                                  on_delete=models.CASCADE,
                                  db_column='EXPERTID')
    session_date = models.DateField(null=False, db_column='SESSIONDATE')
    hour = models.IntegerField(db_column='SESSIONHOUR', null=False)
    customer_id = models.ForeignKey(Customer,
                                    max_length=20,
                                    db_column='CUSTID',
                                    null=True,
                                    on_delete=models.CASCADE)

    class Meta:
        db_table = "SCHEDULE"


class OfferSessions(models.Model):
    offer_id = models.ForeignKey(ServiceOffer,
                                 db_column='SOFFERID',
                                 null=False,
                                 on_delete=models.CASCADE)
    session_id = models.ForeignKey(Schedule,
                                   db_column='OFFERID',
                                   null=False,
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = "OFFERSESSION"


class ServiceSatisfaction(models.Model):
    service_satisfaction_id = models.CharField(primary_key=True,
                                               max_length=20,
                                               db_column='SERVICESATID')
    off_id = models.ForeignKey(ServiceOffer,
                               max_length=20,
                               db_column='OFFID',
                               null=False,
                               on_delete=models.CASCADE)
    customer_performance = models.IntegerField(db_column='CUSTOMERSCORE',
                                               null=False)
    provider_performance = models.IntegerField(db_column='PROVIDERSCORE',
                                               null=False)

    class Meta:
        db_table = "SERVICESATISFACTION"


class SatisfactionFails(models.Model):
    satisfaction_id = models.CharField(primary_key=True,
                                       max_length=20,
                                       db_column='SATISFACID')

    failure = models.CharField(max_length=20, db_column='FAILURE', null=False)


class Message(models.Model):
    message_id = models.CharField(primary_key=True,
                                  max_length=20,
                                  db_column='MESID')
    context = models.CharField(max_length=1000,
                               db_column='CONTEXT',
                               null=False)
    sendtime = models.DateTimeField(db_column='SENDTIME', default=timezone.now)
    sender = models.ForeignKey(User,
                               db_column='SENDERID',
                               null=False,
                               on_delete=models.CASCADE)

    class Meta:
        db_table = "MESSAGE"


class Chat(models.Model):
    mess_id = models.ForeignKey(Message,
                                max_length=20,
                                db_column='MESSID',
                                null=False,
                                on_delete=models.CASCADE)
    offer_id = models.ForeignKey(ServiceOffer,
                                 max_length=20,
                                 db_column='OFID',
                                 null=False,
                                 on_delete=models.CASCADE)
