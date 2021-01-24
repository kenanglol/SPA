from enum import Enum


class Category(Enum):
    Cleaning = "Cleaning"
    Modification = "Modification"
    Shipping = "Shipping"
    Wrecking = "Wrecking"
    PrivateTuition = "Private Tuition"
    Health = "Health"
    Wedding = "Wedding"


class OfferStatus(Enum):
    OFFERED = 1
    ACCEPTED = 2
    REJECTED = 3
    DONE = 4
    CANCELLED = 5


class Services(Enum):
    Message = 1
    ServiceOffer = 2
    User = 3
    Service = 4
    Advert = 5
    Session = 6
