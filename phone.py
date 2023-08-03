import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_valid_phone_number():
    while True:
        phone_number = input("Enter Phone number with country code (+xx xxxxxxxxx): ")
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if phonenumbers.is_valid_number(parsed_number):
                return parsed_number
            else:
                print("Invalid phone number. Please try again.")
        except phonenumbers.NumberParseException:
            print("Invalid phone number format. Please try again.")

# Doğru biçimde telefon numarasını al
phone_number = get_valid_phone_number()

# Numara bilgilerini göster
print('Phone Number belongs to region:', timezone.time_zones_for_number(phone_number))
print('Service Provider:', carrier.name_for_number(phone_number, "en"))
print('Phone number belongs to country:', geocoder.description_for_number(phone_number, "en"))
