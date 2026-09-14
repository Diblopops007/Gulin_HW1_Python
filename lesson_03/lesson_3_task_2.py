from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79201112233"),
    Smartphone("Samsung", "Galaxy S24", "+79032223344"),
    Smartphone("Xiaomi", "14T Pro", "+79113334455"),
    Smartphone("Siemens", "C35", "+79123456789"),
    Smartphone("Nokia", "3310", "+79009876543")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.phone_number}")