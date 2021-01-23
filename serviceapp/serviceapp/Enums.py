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
    User = 3
    Service = 4
    Advert = 5
    Session = 6
