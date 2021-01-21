from enum import Enum


class Category(Enum):
    Cleaning = "Cleaning"
    Modification = "Modification"
    Shipping = "Shipping"
    Wrecking = "Wrecking"
    PrivateTuition = "Private Tuition"
    Health = "Health"
    Wedding = "Wedding"


class ServiceStatus(Enum):
    Offered = 1
    Accepted = 2
    Rejected = 3
    Done = 4
    Cancelled = 5


class Services(Enum):
    Message = 1
    ServiceOffer = 2
    ServiceSatisfaction = 3
    User = 4
    Service = 5
    Advert = 6
    Session = 7
