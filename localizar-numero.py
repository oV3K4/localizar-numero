import phonenumbers 
from phonenumbers import geocoder, carrier

#Digite o número com código do país e DD
phoneNumer = phonenumbers.parse("DIGITE O CÓDIGO AQUI")

Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

Region = geocoder.description_for_number(phoneNumer, 'pt-br')

print('A operadora é: ' + Carrier)
print('O estado é: ' + Region)