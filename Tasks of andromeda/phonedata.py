import phonenumbers
# from Testphone import number
from phonenumbers import geocoder

number = input("Please enter the phone number here:  ")

#Country recognition of location of the number
ch_nmber = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_nmber, "en"))

#Company service provider of the number
from phonenumbers import carrier

service_nmbr = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmbr, "en"))