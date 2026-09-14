from address import Address
from mailing import Mailing

to_address = Address(123456, "Москва", "пр-т. Ленина", "30", "кв. 20")
from_address = Address(654321, "Санкт-Петербург", "пр. Невский", "40", "кв.35")

mailing = Mailing(to_address, from_address, 500, "TRK789465897")

print(f"Отправление {mailing.track} из {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.building} - {mailing.to_address.flat} в {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.flat}. Стоимость {mailing.cost} рублей.")