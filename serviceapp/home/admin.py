from django.contrib import admin

from .models import ServiceOffer,Customer,Provider,Schedule, Message,Service,SatisfactionFails,OfferSessions,Advert,User
class ServiceAdmin(admin.ModelAdmin):#admin paneline servisleri ayrıntılı görüntüleme filtreleme gibi secenekleri ekler
    list_display=['service_name','category']
    list_filter=['category']
    search_fields=['service_name','category']
    class Meta:
        model=Service

admin.site.register(ServiceOffer)
admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Schedule)
admin.site.register(Message)
admin.site.register(Service,ServiceAdmin)
admin.site.register(SatisfactionFails)
admin.site.register(OfferSessions)
admin.site.register(Advert)
#admin.site.register(User)










